# coding: utf-8

"""
    Slurm REST API

    API to access and control Slurm  # noqa: E501

    The version of the OpenAPI document: Slurm-24.05.4&openapi/slurmctld&openapi/slurmdbd
    Contact: sales@schedmd.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class V0040JobSubmitReq(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'script': 'str',
        'jobs': 'list[V0040JobDescMsg]',
        'job': 'V0040JobDescMsg'
    }

    attribute_map = {
        'script': 'script',
        'jobs': 'jobs',
        'job': 'job'
    }

    def __init__(self, script=None, jobs=None, job=None, local_vars_configuration=None):  # noqa: E501
        """V0040JobSubmitReq - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._script = None
        self._jobs = None
        self._job = None
        self.discriminator = None

        if script is not None:
            self.script = script
        if jobs is not None:
            self.jobs = jobs
        if job is not None:
            self.job = job

    @property
    def script(self):
        """Gets the script of this V0040JobSubmitReq.  # noqa: E501

        Batch job script; must be specified in first component of jobs or in job if this field is not populated  # noqa: E501

        :return: The script of this V0040JobSubmitReq.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this V0040JobSubmitReq.

        Batch job script; must be specified in first component of jobs or in job if this field is not populated  # noqa: E501

        :param script: The script of this V0040JobSubmitReq.  # noqa: E501
        :type: str
        """

        self._script = script

    @property
    def jobs(self):
        """Gets the jobs of this V0040JobSubmitReq.  # noqa: E501


        :return: The jobs of this V0040JobSubmitReq.  # noqa: E501
        :rtype: list[V0040JobDescMsg]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this V0040JobSubmitReq.


        :param jobs: The jobs of this V0040JobSubmitReq.  # noqa: E501
        :type: list[V0040JobDescMsg]
        """

        self._jobs = jobs

    @property
    def job(self):
        """Gets the job of this V0040JobSubmitReq.  # noqa: E501


        :return: The job of this V0040JobSubmitReq.  # noqa: E501
        :rtype: V0040JobDescMsg
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this V0040JobSubmitReq.


        :param job: The job of this V0040JobSubmitReq.  # noqa: E501
        :type: V0040JobDescMsg
        """

        self._job = job

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V0040JobSubmitReq):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V0040JobSubmitReq):
            return True

        return self.to_dict() != other.to_dict()
