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
from openapi_client.models.v0040_kill_jobs_msg import V0040KillJobsMsg  # noqa: E501
from openapi_client.rest import ApiException

class TestV0040KillJobsMsg(unittest.TestCase):
    """V0040KillJobsMsg unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V0040KillJobsMsg
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v0040_kill_jobs_msg.V0040KillJobsMsg()  # noqa: E501
        if include_optional :
            return V0040KillJobsMsg(
                account = '0', 
                flags = [
                    'BATCH_JOB'
                    ], 
                job_name = '0', 
                jobs = [
                    '0'
                    ], 
                partition = '0', 
                qos = '0', 
                reservation = '0', 
                signal = '0', 
                job_state = [
                    'PENDING'
                    ], 
                user_id = '0', 
                user_name = '0', 
                wckey = '0', 
                nodes = [
                    '0'
                    ]
            )
        else :
            return V0040KillJobsMsg(
        )

    def testV0040KillJobsMsg(self):
        """Test V0040KillJobsMsg"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
