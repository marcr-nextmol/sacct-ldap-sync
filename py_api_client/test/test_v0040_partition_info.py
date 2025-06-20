# coding: utf-8

"""
    Slurm REST API

    API to access and control Slurm  # noqa: E501

    The version of the OpenAPI document: Slurm-24.05.4&openapi/slurmctld&openapi/slurmdbd
    Contact: sales@schedmd.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.v0040_partition_info import V0040PartitionInfo  # noqa: E501
from openapi_client.rest import ApiException

class TestV0040PartitionInfo(unittest.TestCase):
    """V0040PartitionInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V0040PartitionInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v0040_partition_info.V0040PartitionInfo()  # noqa: E501
        if include_optional :
            return V0040PartitionInfo(
                nodes = openapi_client.models.v0_0_40_partition_info_nodes.v0_0_40_partition_info_nodes(
                    allowed_allocation = '0', 
                    configured = '0', 
                    total = 56, ), 
                accounts = openapi_client.models.v0_0_40_partition_info_accounts.v0_0_40_partition_info_accounts(
                    allowed = '0', 
                    deny = '0', ), 
                groups = openapi_client.models.v0_0_40_partition_info_groups.v0_0_40_partition_info_groups(
                    allowed = '0', ), 
                qos = openapi_client.models.v0_0_40_partition_info_qos.v0_0_40_partition_info_qos(
                    allowed = '0', 
                    deny = '0', 
                    assigned = '0', ), 
                alternate = '0', 
                tres = openapi_client.models.v0_0_40_partition_info_tres.v0_0_40_partition_info_tres(
                    billing_weights = '0', 
                    configured = '0', ), 
                cluster = '0', 
                cpus = openapi_client.models.v0_0_40_partition_info_cpus.v0_0_40_partition_info_cpus(
                    task_binding = 56, 
                    total = 56, ), 
                defaults = openapi_client.models.v0_0_40_partition_info_defaults.v0_0_40_partition_info_defaults(
                    memory_per_cpu = 56, 
                    partition_memory_per_cpu = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    partition_memory_per_node = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    time = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    job = '0', ), 
                grace_time = 56, 
                maximums = openapi_client.models.v0_0_40_partition_info_maximums.v0_0_40_partition_info_maximums(
                    cpus_per_node = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    cpus_per_socket = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    memory_per_cpu = 56, 
                    partition_memory_per_cpu = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    partition_memory_per_node = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    nodes = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    shares = 56, 
                    oversubscribe = openapi_client.models.v0_0_40_partition_info_maximums_oversubscribe.v0_0_40_partition_info_maximums_oversubscribe(
                        jobs = 56, 
                        flags = [
                            'force'
                            ], ), 
                    time = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    over_time_limit = openapi_client.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ), 
                minimums = openapi_client.models.v0_0_40_partition_info_minimums.v0_0_40_partition_info_minimums(
                    nodes = 56, ), 
                name = '0', 
                node_sets = '0', 
                priority = openapi_client.models.v0_0_40_partition_info_priority.v0_0_40_partition_info_priority(
                    job_factor = 56, 
                    tier = 56, ), 
                timeouts = openapi_client.models.v0_0_40_partition_info_timeouts.v0_0_40_partition_info_timeouts(
                    resume = openapi_client.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    suspend = openapi_client.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ), 
                partition = openapi_client.models.v0_0_40_partition_info_partition.v0_0_40_partition_info_partition(
                    state = [
                        'INACTIVE'
                        ], ), 
                suspend_time = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else :
            return V0040PartitionInfo(
        )

    def testV0040PartitionInfo(self):
        """Test V0040PartitionInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
