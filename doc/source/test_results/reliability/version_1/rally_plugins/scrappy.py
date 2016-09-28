# Copyright 2014: Mirantis Inc.
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


"""
Rully scrappy plugin
This is pluging was designed for OpenStack
reliability testing.
"""

from rally.common.i18n import _
from rally import consts
from rally.task import sla
import os
from rally.common import logging
from rally.common import streaming_algorithms as streaming


LOG = logging.getLogger(__name__)

class MttrCalculation():
    def __init__(self):
        self.min_timestamp = streaming.MinComputation()
        self.max_timestamp = streaming.MaxComputation()
        self.mttr = 0
        self.last_error_duration = 0
        self.last_iteration = None

    def add(self, iteration):
        if iteration["error"]:
            # Store duration of last error iteration
            if self.max_timestamp.result() < iteration["timestamp"]:
                self.last_error_duration = iteration["duration"]

            self.min_timestamp.add(iteration["timestamp"])
            self.max_timestamp.add(iteration["timestamp"])
            LOG.info("TIMESTAMP: %s" % iteration["timestamp"])

        self.last_iteration = iteration

    def result(self):
        self.mttr = round(self.max_timestamp.result() -
                          self.min_timestamp.result() +
                          self.last_error_duration, 2)
        # SLA Context don't have information about iterations count,
        # so assume that if last iteration completed with error,
        # that cluster was not auto-healed
        if self.last_iteration["error"]:
            self.mttr = "Inf."
        return(self.mttr)


@sla.configure(name="scrappy")
class Scrappy(sla.SLA):
    """Scrappy events."""
    CONFIG_SCHEMA = {
        "type": "object",
        "$schema": consts.JSON_SCHEMA,
        "properties": {
            "on_iter": {"type": "number"},
            "execute": {"type": "string"},
            "cycle": {"type": "number"}
        }
    }

    def __init__(self, criterion_value):
        super(Scrappy, self).__init__(criterion_value)
        self.on_iter = self.criterion_value.get("on_iter", None)
        self.execute = self.criterion_value.get("execute", None)
        self.cycle = self.criterion_value.get("cycle", 0)
        self.errors = 0
        self.total = 0
        self.error_rate = 0.0
        self.mttr = MttrCalculation()

    def add_iteration(self, iteration):
        self.total += 1
        if iteration["error"]:
            self.errors += 1

        self.mttr.add(iteration)

        """Start iteration event"""
        if self.on_iter == self.total:
            LOG.info("Scrappy testing cycle: ITER: %s" % self.cycle)
            LOG.info("Scrappy executing: %s" % self.on_iter)
            os.system(self.execute)

        self.error_rate = self.errors * 100.0 / self.total
        self.success = self.error_rate <= 5
        return self.success

    def merge(self, other):
        self.total += other.total
        self.errors += other.errors
        if self.total:
            self.error_rate = self.errors * 100.0 / self.total
        self.success = self.error_rate <= 5
        return self.success

    def details(self):
        return (_("Scrappy failure rate %.2f%% MTTR %s seconds - %s") %
                (self.error_rate, self.mttr.result(), self.status()))
