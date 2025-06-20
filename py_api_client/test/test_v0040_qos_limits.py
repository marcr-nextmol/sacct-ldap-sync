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
from openapi_client.models.v0040_qos_limits import V0040QosLimits  # noqa: E501
from openapi_client.rest import ApiException

class TestV0040QosLimits(unittest.TestCase):
    """V0040QosLimits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V0040QosLimits
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v0040_qos_limits.V0040QosLimits()  # noqa: E501
        if include_optional :
            return V0040QosLimits(
                grace_time = 56, 
                max = openapi_client.models.v0_0_40_qos_limits_max.v0_0_40_qos_limits_max(
                    active_jobs = openapi_client.models.v0_0_40_qos_limits_max_active_jobs.v0_0_40_qos_limits_max_active_jobs(
                        accruing = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        count = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), ), 
                    tres = openapi_client.models.v0_0_40_qos_limits_max_tres.v0_0_40_qos_limits_max_tres(
                        total = [
                            openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                type = '0', 
                                name = '0', 
                                id = 56, )
                            ], 
                        minutes = openapi_client.models.v0_0_40_qos_limits_max_tres_minutes.v0_0_40_qos_limits_max_tres_minutes(
                            per = openapi_client.models.v0_0_40_qos_limits_max_tres_minutes_per.v0_0_40_qos_limits_max_tres_minutes_per(
                                qos = [
                                    openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                        type = '0', 
                                        name = '0', 
                                        id = 56, )
                                    ], 
                                job = [
                                    openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                        type = '0', 
                                        name = '0', 
                                        id = 56, )
                                    ], 
                                account = [
                                    openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                        type = '0', 
                                        name = '0', 
                                        id = 56, )
                                    ], 
                                user = [
                                    openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                        type = '0', 
                                        name = '0', 
                                        id = 56, )
                                    ], ), ), 
                        per = openapi_client.models.v0_0_40_qos_limits_max_tres_per.v0_0_40_qos_limits_max_tres_per(
                            account = [
                                openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                    type = '0', 
                                    name = '0', 
                                    id = 56, )
                                ], 
                            job = [
                                openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                    type = '0', 
                                    name = '0', 
                                    id = 56, )
                                ], 
                            node = [
                                openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                    type = '0', 
                                    name = '0', 
                                    id = 56, )
                                ], 
                            user = [
                                openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                    type = '0', 
                                    name = '0', 
                                    id = 56, )
                                ], ), ), 
                    wall_clock = openapi_client.models.v0_0_40_qos_limits_max_wall_clock.v0_0_40_qos_limits_max_wall_clock(), 
                    jobs = openapi_client.models.v0_0_40_qos_limits_max_jobs.v0_0_40_qos_limits_max_jobs(), 
                    accruing = openapi_client.models.v0_0_40_qos_limits_max_jobs_active_jobs.v0_0_40_qos_limits_max_jobs_active_jobs(), ), 
                factor = openapi_client.models.v0/0/40_float64_no_val.v0.0.40_float64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 1.337, ), 
                min = openapi_client.models.v0_0_40_qos_limits_min.v0_0_40_qos_limits_min(
                    priority_threshold = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    tres = openapi_client.models.v0_0_40_qos_limits_min_tres.v0_0_40_qos_limits_min_tres(
                        per = openapi_client.models.v0_0_40_qos_limits_min_tres_per.v0_0_40_qos_limits_min_tres_per(
                            job = [
                                openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                    type = '0', 
                                    name = '0', 
                                    id = 56, 
                                    count = 56, )
                                ], ), ), )
            )
        else :
            return V0040QosLimits(
        )

    def testV0040QosLimits(self):
        """Test V0040QosLimits"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
