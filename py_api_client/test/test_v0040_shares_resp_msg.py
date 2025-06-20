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
from openapi_client.models.v0040_shares_resp_msg import V0040SharesRespMsg  # noqa: E501
from openapi_client.rest import ApiException

class TestV0040SharesRespMsg(unittest.TestCase):
    """V0040SharesRespMsg unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V0040SharesRespMsg
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v0040_shares_resp_msg.V0040SharesRespMsg()  # noqa: E501
        if include_optional :
            return V0040SharesRespMsg(
                shares = [
                    openapi_client.models.v0/0/40_assoc_shares_obj_wrap.v0.0.40_assoc_shares_obj_wrap(
                        id = 56, 
                        cluster = '0', 
                        name = '0', 
                        parent = '0', 
                        partition = '0', 
                        shares_normalized = openapi_client.models.v0/0/40_float64_no_val.v0.0.40_float64_no_val(
                            set = True, 
                            infinite = True, 
                            number = 1.337, ), 
                        shares = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        tres = openapi_client.models.v0_0_40_assoc_shares_obj_wrap_tres.v0_0_40_assoc_shares_obj_wrap_tres(
                            run_seconds = [
                                openapi_client.models.v0/0/40_shares_uint64_tres.v0.0.40_shares_uint64_tres(
                                    name = '0', 
                                    value = openapi_client.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), )
                                ], 
                            group_minutes = [
                                openapi_client.models.v0/0/40_shares_uint64_tres.v0.0.40_shares_uint64_tres(
                                    name = '0', )
                                ], 
                            usage = [
                                openapi_client.models.v0/0/40_shares_float128_tres.v0.0.40_shares_float128_tres(
                                    name = '0', )
                                ], ), 
                        effective_usage = 1.337, 
                        usage_normalized = openapi_client.models.v0/0/40_float64_no_val.v0.0.40_float64_no_val(
                            set = True, 
                            infinite = True, 
                            number = 1.337, ), 
                        usage = 56, 
                        fairshare = openapi_client.models.v0_0_40_assoc_shares_obj_wrap_fairshare.v0_0_40_assoc_shares_obj_wrap_fairshare(
                            factor = 1.337, 
                            level = 1.337, ), 
                        type = [
                            'USER'
                            ], )
                    ], 
                total_shares = 56
            )
        else :
            return V0040SharesRespMsg(
        )

    def testV0040SharesRespMsg(self):
        """Test V0040SharesRespMsg"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
