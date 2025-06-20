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

import openapi_client
from openapi_client.api.slurm_api import SlurmApi  # noqa: E501
from openapi_client.rest import ApiException


class TestSlurmApi(unittest.TestCase):
    """SlurmApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.slurm_api.SlurmApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_slurm_v0040_delete_job(self):
        """Test case for slurm_v0040_delete_job

        cancel or signal job  # noqa: E501
        """
        pass

    def test_slurm_v0040_delete_jobs(self):
        """Test case for slurm_v0040_delete_jobs

        send signal to list of jobs  # noqa: E501
        """
        pass

    def test_slurm_v0040_delete_node(self):
        """Test case for slurm_v0040_delete_node

        delete node  # noqa: E501
        """
        pass

    def test_slurm_v0040_get_diag(self):
        """Test case for slurm_v0040_get_diag

        get diagnostics  # noqa: E501
        """
        pass

    def test_slurm_v0040_get_job(self):
        """Test case for slurm_v0040_get_job

        get job info  # noqa: E501
        """
        pass

    def test_slurm_v0040_get_jobs(self):
        """Test case for slurm_v0040_get_jobs

        get list of jobs  # noqa: E501
        """
        pass

    def test_slurm_v0040_get_jobs_state(self):
        """Test case for slurm_v0040_get_jobs_state

        get list of job states  # noqa: E501
        """
        pass

    def test_slurm_v0040_get_licenses(self):
        """Test case for slurm_v0040_get_licenses

        get all Slurm tracked license info  # noqa: E501
        """
        pass

    def test_slurm_v0040_get_node(self):
        """Test case for slurm_v0040_get_node

        get node info  # noqa: E501
        """
        pass

    def test_slurm_v0040_get_nodes(self):
        """Test case for slurm_v0040_get_nodes

        get node(s) info  # noqa: E501
        """
        pass

    def test_slurm_v0040_get_partition(self):
        """Test case for slurm_v0040_get_partition

        get partition info  # noqa: E501
        """
        pass

    def test_slurm_v0040_get_partitions(self):
        """Test case for slurm_v0040_get_partitions

        get all partition info  # noqa: E501
        """
        pass

    def test_slurm_v0040_get_ping(self):
        """Test case for slurm_v0040_get_ping

        ping test  # noqa: E501
        """
        pass

    def test_slurm_v0040_get_reconfigure(self):
        """Test case for slurm_v0040_get_reconfigure

        request slurmctld reconfigure  # noqa: E501
        """
        pass

    def test_slurm_v0040_get_reservation(self):
        """Test case for slurm_v0040_get_reservation

        get reservation info  # noqa: E501
        """
        pass

    def test_slurm_v0040_get_reservations(self):
        """Test case for slurm_v0040_get_reservations

        get all reservation info  # noqa: E501
        """
        pass

    def test_slurm_v0040_get_shares(self):
        """Test case for slurm_v0040_get_shares

        get fairshare info  # noqa: E501
        """
        pass

    def test_slurm_v0040_post_job(self):
        """Test case for slurm_v0040_post_job

        update job  # noqa: E501
        """
        pass

    def test_slurm_v0040_post_job_submit(self):
        """Test case for slurm_v0040_post_job_submit

        submit new job  # noqa: E501
        """
        pass

    def test_slurm_v0040_post_node(self):
        """Test case for slurm_v0040_post_node

        update node properties  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
