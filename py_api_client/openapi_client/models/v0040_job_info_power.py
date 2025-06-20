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


class V0040JobInfoPower(object):
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
        'flags': 'list[object]'
    }

    attribute_map = {
        'flags': 'flags'
    }

    def __init__(self, flags=None, local_vars_configuration=None):  # noqa: E501
        """V0040JobInfoPower - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._flags = None
        self.discriminator = None

        if flags is not None:
            self.flags = flags

    @property
    def flags(self):
        """Gets the flags of this V0040JobInfoPower.  # noqa: E501

        removed field  # noqa: E501

        :return: The flags of this V0040JobInfoPower.  # noqa: E501
        :rtype: list[object]
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this V0040JobInfoPower.

        removed field  # noqa: E501

        :param flags: The flags of this V0040JobInfoPower.  # noqa: E501
        :type: list[object]
        """

        self._flags = flags

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
        if not isinstance(other, V0040JobInfoPower):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V0040JobInfoPower):
            return True

        return self.to_dict() != other.to_dict()
