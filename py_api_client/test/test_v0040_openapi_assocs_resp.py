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
from openapi_client.models.v0040_openapi_assocs_resp import V0040OpenapiAssocsResp  # noqa: E501
from openapi_client.rest import ApiException

class TestV0040OpenapiAssocsResp(unittest.TestCase):
    """V0040OpenapiAssocsResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V0040OpenapiAssocsResp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v0040_openapi_assocs_resp.V0040OpenapiAssocsResp()  # noqa: E501
        if include_optional :
            return V0040OpenapiAssocsResp(
                associations = [
                    openapi_client.models.v0/0/40_assoc.v0.0.40_assoc(
                        accounting = [
                            openapi_client.models.v0/0/40_accounting.v0.0.40_accounting(
                                allocated = openapi_client.models.v0_0_40_accounting_allocated.v0_0_40_accounting_allocated(
                                    seconds = 56, ), 
                                id = 56, 
                                start = 56, 
                                tres = openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                    type = '0', 
                                    name = '0', 
                                    id = 56, 
                                    count = 56, ), )
                            ], 
                        account = '0', 
                        cluster = '0', 
                        comment = '0', 
                        default = openapi_client.models.v0_0_40_assoc_default.v0_0_40_assoc_default(
                            qos = '0', ), 
                        flags = [
                            'DELETED'
                            ], 
                        max = openapi_client.models.v0_0_40_assoc_max.v0_0_40_assoc_max(
                            jobs = openapi_client.models.v0_0_40_assoc_max_jobs.v0_0_40_assoc_max_jobs(
                                per = openapi_client.models.v0_0_40_assoc_max_jobs_per.v0_0_40_assoc_max_jobs_per(
                                    count = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    accruing = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    submitted = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    wall_clock = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), ), 
                                active = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                    set = True, 
                                    infinite = True, 
                                    number = 56, ), 
                                accruing = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                    set = True, 
                                    infinite = True, 
                                    number = 56, ), 
                                total = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                    set = True, 
                                    infinite = True, 
                                    number = 56, ), ), 
                            tres = openapi_client.models.v0_0_40_assoc_max_tres.v0_0_40_assoc_max_tres(
                                group = openapi_client.models.v0_0_40_assoc_max_tres_group.v0_0_40_assoc_max_tres_group(
                                    minutes = [
                                        openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                            type = '0', 
                                            name = '0', 
                                            id = 56, )
                                        ], ), 
                                minutes = openapi_client.models.v0_0_40_assoc_max_tres_minutes.v0_0_40_assoc_max_tres_minutes(), ), 
                            per = openapi_client.models.v0_0_40_assoc_max_per.v0_0_40_assoc_max_per(
                                account = openapi_client.models.v0_0_40_assoc_max_per_account.v0_0_40_assoc_max_per_account(), ), ), 
                        id = openapi_client.models.v0/0/40_assoc_short.v0.0.40_assoc_short(
                            cluster = '0', 
                            partition = '0', 
                            user = '0', ), 
                        is_default = True, 
                        lineage = '0', 
                        min = openapi_client.models.v0_0_40_assoc_min.v0_0_40_assoc_min(
                            priority_threshold = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), ), 
                        parent_account = '0', 
                        partition = '0', 
                        priority = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        qos = [
                            '0'
                            ], 
                        shares_raw = 56, 
                        user = '0', )
                    ], 
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
            return V0040OpenapiAssocsResp(
                associations = [
                    openapi_client.models.v0/0/40_assoc.v0.0.40_assoc(
                        accounting = [
                            openapi_client.models.v0/0/40_accounting.v0.0.40_accounting(
                                allocated = openapi_client.models.v0_0_40_accounting_allocated.v0_0_40_accounting_allocated(
                                    seconds = 56, ), 
                                id = 56, 
                                start = 56, 
                                tres = openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                    type = '0', 
                                    name = '0', 
                                    id = 56, 
                                    count = 56, ), )
                            ], 
                        account = '0', 
                        cluster = '0', 
                        comment = '0', 
                        default = openapi_client.models.v0_0_40_assoc_default.v0_0_40_assoc_default(
                            qos = '0', ), 
                        flags = [
                            'DELETED'
                            ], 
                        max = openapi_client.models.v0_0_40_assoc_max.v0_0_40_assoc_max(
                            jobs = openapi_client.models.v0_0_40_assoc_max_jobs.v0_0_40_assoc_max_jobs(
                                per = openapi_client.models.v0_0_40_assoc_max_jobs_per.v0_0_40_assoc_max_jobs_per(
                                    count = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    accruing = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    submitted = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), 
                                    wall_clock = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                        set = True, 
                                        infinite = True, 
                                        number = 56, ), ), 
                                active = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                    set = True, 
                                    infinite = True, 
                                    number = 56, ), 
                                accruing = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                    set = True, 
                                    infinite = True, 
                                    number = 56, ), 
                                total = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                    set = True, 
                                    infinite = True, 
                                    number = 56, ), ), 
                            tres = openapi_client.models.v0_0_40_assoc_max_tres.v0_0_40_assoc_max_tres(
                                group = openapi_client.models.v0_0_40_assoc_max_tres_group.v0_0_40_assoc_max_tres_group(
                                    minutes = [
                                        openapi_client.models.v0/0/40_tres.v0.0.40_tres(
                                            type = '0', 
                                            name = '0', 
                                            id = 56, )
                                        ], ), 
                                minutes = openapi_client.models.v0_0_40_assoc_max_tres_minutes.v0_0_40_assoc_max_tres_minutes(), ), 
                            per = openapi_client.models.v0_0_40_assoc_max_per.v0_0_40_assoc_max_per(
                                account = openapi_client.models.v0_0_40_assoc_max_per_account.v0_0_40_assoc_max_per_account(), ), ), 
                        id = openapi_client.models.v0/0/40_assoc_short.v0.0.40_assoc_short(
                            cluster = '0', 
                            partition = '0', 
                            user = '0', ), 
                        is_default = True, 
                        lineage = '0', 
                        min = openapi_client.models.v0_0_40_assoc_min.v0_0_40_assoc_min(
                            priority_threshold = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), ), 
                        parent_account = '0', 
                        partition = '0', 
                        priority = openapi_client.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        qos = [
                            '0'
                            ], 
                        shares_raw = 56, 
                        user = '0', )
                    ],
        )

    def testV0040OpenapiAssocsResp(self):
        """Test V0040OpenapiAssocsResp"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
