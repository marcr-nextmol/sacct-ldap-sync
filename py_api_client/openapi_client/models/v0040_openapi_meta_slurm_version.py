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


class V0040OpenapiMetaSlurmVersion(object):
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
        'major': 'str',
        'micro': 'str',
        'minor': 'str'
    }

    attribute_map = {
        'major': 'major',
        'micro': 'micro',
        'minor': 'minor'
    }

    def __init__(self, major=None, micro=None, minor=None, local_vars_configuration=None):  # noqa: E501
        """V0040OpenapiMetaSlurmVersion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._major = None
        self._micro = None
        self._minor = None
        self.discriminator = None

        if major is not None:
            self.major = major
        if micro is not None:
            self.micro = micro
        if minor is not None:
            self.minor = minor

    @property
    def major(self):
        """Gets the major of this V0040OpenapiMetaSlurmVersion.  # noqa: E501

        Slurm release major version  # noqa: E501

        :return: The major of this V0040OpenapiMetaSlurmVersion.  # noqa: E501
        :rtype: str
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this V0040OpenapiMetaSlurmVersion.

        Slurm release major version  # noqa: E501

        :param major: The major of this V0040OpenapiMetaSlurmVersion.  # noqa: E501
        :type: str
        """

        self._major = major

    @property
    def micro(self):
        """Gets the micro of this V0040OpenapiMetaSlurmVersion.  # noqa: E501

        Slurm release micro version  # noqa: E501

        :return: The micro of this V0040OpenapiMetaSlurmVersion.  # noqa: E501
        :rtype: str
        """
        return self._micro

    @micro.setter
    def micro(self, micro):
        """Sets the micro of this V0040OpenapiMetaSlurmVersion.

        Slurm release micro version  # noqa: E501

        :param micro: The micro of this V0040OpenapiMetaSlurmVersion.  # noqa: E501
        :type: str
        """

        self._micro = micro

    @property
    def minor(self):
        """Gets the minor of this V0040OpenapiMetaSlurmVersion.  # noqa: E501

        Slurm release minor version  # noqa: E501

        :return: The minor of this V0040OpenapiMetaSlurmVersion.  # noqa: E501
        :rtype: str
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this V0040OpenapiMetaSlurmVersion.

        Slurm release minor version  # noqa: E501

        :param minor: The minor of this V0040OpenapiMetaSlurmVersion.  # noqa: E501
        :type: str
        """

        self._minor = minor

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
        if not isinstance(other, V0040OpenapiMetaSlurmVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V0040OpenapiMetaSlurmVersion):
            return True

        return self.to_dict() != other.to_dict()
