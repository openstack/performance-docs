#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os_faults

from rally.common import logging
from rally import consts
from rally.task import hook

LOG = logging.getLogger(__name__)


@hook.configure(name="fault_injection")
class FaultInjectionHook(hook.Hook):
    """Performs fault injection."""

    CONFIG_SCHEMA = {
        "type": "object",
        "$schema": consts.JSON_SCHEMA,
        "properties": {
            "action": {"type": "string"},
        },
        "required": [
            "action",
        ],
        "additionalProperties": False,
    }

    def run(self):
        LOG.debug("Injecting fault: %s", self.config["action"])
        injector = os_faults.connect()

        try:
            os_faults.human_api(injector, self.config["action"])
            self.set_status(consts.HookStatus.SUCCESS)
        except Exception as e:
            self.set_status(consts.HookStatus.FAILED)
            self.set_error(exception_name=type(e),
                           description='Fault injection failure',
                           details=str(e))
