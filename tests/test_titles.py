# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import glob
import re

import docutils.core
import testtools


OPTIONAL_SECTIONS = ("Upper level additional section",)
OPTIONAL_SUBSECTIONS = ("Some additional section",)
OPTIONAL_SUBSUBSECTIONS = ("Parameters", "Some additional section",)
OPTIONAL_FIELDS = ("Conventions",)


class TestTitles(testtools.TestCase):
    def _get_title(self, section_tree, depth=1):
        section = {
            "subtitles": [],
        }
        for node in section_tree:
            if node.tagname == "title":
                section["name"] = node.rawsource
            elif node.tagname == "section":
                subsection = self._get_title(node, depth+1)
                if depth < 2:
                    if subsection["subtitles"]:
                        section["subtitles"].append(subsection)
                    else:
                        section["subtitles"].append(subsection["name"])
                elif depth == 2:
                    section["subtitles"].append(subsection["name"])
        return section

    def _get_titles(self, test_plan):
        titles = {}
        for node in test_plan:
            if node.tagname == "section":
                section = self._get_title(node)
                titles[section["name"]] = section["subtitles"]
        return titles

    @staticmethod
    def _get_docinfo(test_plan):
        fields = []
        for node in test_plan:
            if node.tagname == "field_list":
                for field in node:
                    for f_opt in field:
                        if f_opt.tagname == "field_name":
                            fields.append(f_opt.rawsource)

            if node.tagname == "docinfo":
                for info in node:
                    fields.append(info.tagname)

            if node.tagname == "topic":
                fields.append("abstract")

        return fields

    def _check_fields(self, tmpl, test_plan):
        tmpl_fields = self._get_docinfo(tmpl)
        test_plan_fields = self._get_docinfo(test_plan)

        missing_fields = [f for f in tmpl_fields
                          if f not in test_plan_fields and
                          f not in OPTIONAL_FIELDS]

        if len(missing_fields) > 0:
            self.fail("While checking '%s':\n  %s"
                      % (test_plan[0].rawsource,
                         "Missing fields: %s" % missing_fields))

    def _check_titles(self, filename, expect, actual):
        missing_sections = [x for x in expect.keys() if (
            x not in actual.keys()) and (x not in OPTIONAL_SECTIONS)]

        msgs = []
        if len(missing_sections) > 0:
            msgs.append("Missing sections: %s" % missing_sections)

        for section in expect.keys():
            missing_subsections = [x for x in expect[section]
                                   if x not in actual.get(section, {}) and
                                   (x not in OPTIONAL_SUBSECTIONS)]
            extra_subsections = [x for x in actual.get(section, {})
                                 if x not in expect[section]]

            for ex_s in extra_subsections:
                s_name = (ex_s if type(ex_s) is str or
                                  type(ex_s) is unicode else ex_s["name"])
                if s_name.startswith("Test Case"):
                    new_missing_subsections = []
                    for m_s in missing_subsections:
                        m_s_name = (m_s if type(m_s) is str or
                                           type(m_s) is unicode
                                    else m_s["name"])
                        if not m_s_name.startswith("Test Case"):
                            new_missing_subsections.append(m_s)
                    missing_subsections = new_missing_subsections
                    break

            if len(missing_subsections) > 0:
                msgs.append("Section '%s' is missing subsections: %s"
                            % (section, missing_subsections))

            for subsection in expect[section]:
                if type(subsection) is dict:
                    missing_subsubsections = []
                    actual_section = actual.get(section, {})
                    matching_actual_subsections = [
                        s for s in actual_section
                        if type(s) is dict and (
                            s["name"] == subsection["name"] or
                            (s["name"].startswith("Test Case") and
                             subsection["name"].startswith("Test Case")))
                        ]
                    for actual_subsection in matching_actual_subsections:
                        for x in subsection["subtitles"]:
                            if (x not in actual_subsection["subtitles"] and
                                    x not in OPTIONAL_SUBSUBSECTIONS):
                                missing_subsubsections.append(x)
                        if len(missing_subsubsections) > 0:
                            msgs.append("Subsection '%s' is missing "
                                        "subsubsections: %s"
                                        % (actual_subsection,
                                           missing_subsubsections))

        if len(msgs) > 0:
            self.fail("While checking '%s':\n  %s"
                      % (filename, "\n  ".join(msgs)))

    def _check_lines_wrapping(self, tpl, raw):
        code_block = False
        for i, line in enumerate(raw.split("\n")):
            # NOTE(ndipanov): Allow code block lines to be longer than 79 ch
            if code_block:
                if not line or line.startswith(" "):
                    continue
                else:
                    code_block = False
            if "::" in line:
                code_block = True
            if "http://" in line or "https://" in line:
                continue
            # Allow lines which do not contain any whitespace
            if re.match("\s*[^\s]+$", line):
                continue
            self.assertTrue(
                len(line) < 80,
                msg="%s:%d: Line limited to a maximum of 79 characters." %
                (tpl, i + 1))

    def _check_no_cr(self, tpl, raw):
        matches = re.findall("\r", raw)
        self.assertEqual(
            len(matches), 0,
            "Found %s literal carriage returns in file %s" %
            (len(matches), tpl))

    def _check_trailing_spaces(self, tpl, raw):
        for i, line in enumerate(raw.split("\n")):
            trailing_spaces = re.findall("\s+$", line)
            self.assertEqual(
                len(trailing_spaces), 0,
                "Found trailing spaces on line %s of %s" % (i + 1, tpl))

    def test_template(self):
        with open("doc/source/test_plans/template.rst") as f:
            template = f.read()
        test_plan_tmpl = docutils.core.publish_doctree(template)
        template_titles = self._get_titles(test_plan_tmpl)

        files = glob.glob("doc/source/test_plans/*/*.rst")

        for filename in files:
            with open(filename) as f:
                data = f.read()

            test_plan = docutils.core.publish_doctree(data)
            self._check_titles(filename,
                               template_titles,
                               self._get_titles(test_plan))
            self._check_fields(test_plan_tmpl, test_plan)
            self._check_lines_wrapping(filename, data)
            self._check_no_cr(filename, data)
            self._check_trailing_spaces(filename, data)
