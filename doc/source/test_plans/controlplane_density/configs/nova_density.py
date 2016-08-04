# Copyright 2016: Mirantis Inc.
# All Rights Reserved.
#
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

from rally import consts
from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.cinder import utils as cinder_utils
from rally.plugins.openstack.scenarios.nova import utils
from rally.task import types
from rally.task import validation


class NovaDensityPlugin(utils.NovaScenario, cinder_utils.CinderScenario):
    """boot_attach_and_list_with_secgroups"""
    @types.convert(image={"type": "glance_image"},
                   flavor={"type": "nova_flavor"})
    @validation.image_valid_on_flavor("flavor", "image")
    @validation.required_parameters("security_group_count",
                                    "rules_per_security_group")
    @validation.required_contexts("network")
    @validation.required_services(consts.Service.NOVA)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["cinder", "nova"]})
    def boot_attach_and_list_with_secgroups(
            self, image, flavor,
            volume_size,
            security_group_count,
            rules_per_security_group,
            do_delete=False,
            detailed=True,
            boot_server_kwargs=None,
            create_volume_kwargs=None
    ):

        if boot_server_kwargs is None:
            boot_server_kwargs = {}
        if create_volume_kwargs is None:
            create_volume_kwargs = {}

        security_groups = self._create_security_groups(
            security_group_count)
        self._create_rules_for_security_group(security_groups,
                                              rules_per_security_group)

        secgroups_names = [sg.name for sg in security_groups]
        """boot server"""
        server = self._boot_server(image, flavor,
                                   security_groups=secgroups_names,
                                   **boot_server_kwargs)

        volume = self._create_volume(volume_size, **create_volume_kwargs)
        self._attach_volume(server, volume)

        self._list_security_groups()
        self._list_servers(detailed)

        if do_delete:
            self._detach_volume(server, volume)
            self._delete_server(server)
            self._delete_volume(volume)
            self._delete_security_groups(security_groups)

    """boot_and_list_with_secgroups"""
    @types.convert(image={"type": "glance_image"},
                   flavor={"type": "nova_flavor"})
    @validation.image_valid_on_flavor("flavor", "image")
    @validation.required_parameters("security_group_count",
                                    "rules_per_security_group")
    @validation.required_contexts("network")
    @validation.required_services(consts.Service.NOVA)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["nova"]})
    def boot_and_list_with_secgroups(
            self, image, flavor,
            security_group_count,
            rules_per_security_group,
            do_delete=False,
            detailed=True,
            boot_server_kwargs=None
    ):

        if boot_server_kwargs is None:
            boot_server_kwargs = {}

        security_groups = self._create_security_groups(
            security_group_count)
        self._create_rules_for_security_group(security_groups,
                                              rules_per_security_group)

        secgroups_names = [sg.name for sg in security_groups]
        """boot server"""
        server = self._boot_server(image, flavor,
                                   security_groups=secgroups_names,
                                   **boot_server_kwargs)

        self._list_security_groups()
        self._list_servers(detailed)

        if do_delete:
            self._delete_server(server)
            self._delete_security_groups(security_groups)

    """boot_attach_and_list"""
    @types.convert(image={"type": "glance_image"},
                   flavor={"type": "nova_flavor"})
    @validation.image_valid_on_flavor("flavor", "image")
    @validation.required_services(consts.Service.NOVA)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["cinder", "nova"]})
    def boot_attach_and_list(
            self, image, flavor,
            volume_size,
            do_delete=False,
            detailed=True,
            boot_server_kwargs=None,
            create_volume_kwargs=None
    ):

        if boot_server_kwargs is None:
            boot_server_kwargs = {}
        if create_volume_kwargs is None:
            create_volume_kwargs = {}

        """boot server"""
        server = self._boot_server(image, flavor,
                                   **boot_server_kwargs)

        volume = self._create_volume(volume_size, **create_volume_kwargs)
        self._attach_volume(server, volume)

        self._list_servers(detailed)

        if do_delete:
            self._detach_volume(server, volume)
            self._delete_server(server)
            self._delete_volume(volume)

    """boot_and_list"""
    @types.convert(image={"type": "glance_image"},
                   flavor={"type": "nova_flavor"})
    @validation.image_valid_on_flavor("flavor", "image")
    @validation.required_services(consts.Service.NOVA)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["nova"]})
    def boot_and_list(
            self, image, flavor,
            do_delete=False,
            detailed=True,
            boot_server_kwargs=None
    ):

        if boot_server_kwargs is None:
            boot_server_kwargs = {}

        """boot server"""
        server = self._boot_server(image, flavor,
                                   **boot_server_kwargs)

        self._list_servers(detailed)

        if do_delete:
            self._delete_server(server)
