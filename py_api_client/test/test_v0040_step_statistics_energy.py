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
from openapi_client.models.v0040_step_statistics_energy import V0040StepStatisticsEnergy  # noqa: E501
from openapi_client.rest import ApiException

class TestV0040StepStatisticsEnergy(unittest.TestCase):
    """V0040StepStatisticsEnergy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V0040StepStatisticsEnergy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v0040_step_statistics_energy.V0040StepStatisticsEnergy()  # noqa: E501
        if include_optional :
            return V0040StepStatisticsEnergy(
                consumed = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else :
            return V0040StepStatisticsEnergy(
        )

    def testV0040StepStatisticsEnergy(self):
        """Test V0040StepStatisticsEnergy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
