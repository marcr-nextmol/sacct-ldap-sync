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
from openapi_client.models.v0040_openapi_job_submit_response import V0040OpenapiJobSubmitResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestV0040OpenapiJobSubmitResponse(unittest.TestCase):
    """V0040OpenapiJobSubmitResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V0040OpenapiJobSubmitResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v0040_openapi_job_submit_response.V0040OpenapiJobSubmitResponse()  # noqa: E501
        if include_optional :
            return V0040OpenapiJobSubmitResponse(
                result = openapi_client.models.v0/0/40_job_submit_response_msg.v0.0.40_job_submit_response_msg(
                    job_id = 56, 
                    step_id = '0', 
                    error_code = 56, 
                    error = '0', 
                    job_submit_user_msg = '0', ), 
                job_id = 56, 
                step_id = '0', 
                job_submit_user_msg = '0', 
                meta = openapi_client.models.v0/0/40_openapi_meta.v0.0.40_openapi_meta(
                    plugin = openapi_client.models.v0_0_40_openapi_meta_plugin.v0_0_40_openapi_meta_plugin(
                        type = '0', 
                        name = '0', 
                        data_parser = '0', 
                        accounting_storage = '0', ), 
                    client = openapi_client.models.v0_0_40_openapi_meta_client.v0_0_40_openapi_meta_client(
                        source = '0', 
                        user = '0', 
                        group = '0', ), 
                    command = [
                        '0'
                        ], 
                    slurm = openapi_client.models.v0_0_40_openapi_meta_slurm.v0_0_40_openapi_meta_slurm(
                        version = openapi_client.models.v0_0_40_openapi_meta_slurm_version.v0_0_40_openapi_meta_slurm_version(
                            major = '0', 
                            micro = '0', 
                            minor = '0', ), 
                        release = '0', 
                        cluster = '0', ), ), 
                errors = [
                    openapi_client.models.v0/0/40_openapi_error.v0.0.40_openapi_error(
                        description = '0', 
                        error_number = 56, 
                        error = '0', 
                        source = '0', )
                    ], 
                warnings = [
                    openapi_client.models.v0/0/40_openapi_warning.v0.0.40_openapi_warning(
                        description = '0', 
                        source = '0', )
                    ]
            )
        else :
            return V0040OpenapiJobSubmitResponse(
        )

    def testV0040OpenapiJobSubmitResponse(self):
        """Test V0040OpenapiJobSubmitResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
