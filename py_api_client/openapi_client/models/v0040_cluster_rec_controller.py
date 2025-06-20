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


class V0040ClusterRecController(object):
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
        'host': 'str',
        'port': 'int'
    }

    attribute_map = {
        'host': 'host',
        'port': 'port'
    }

    def __init__(self, host=None, port=None, local_vars_configuration=None):  # noqa: E501
        """V0040ClusterRecController - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._host = None
        self._port = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if port is not None:
            self.port = port

    @property
    def host(self):
        """Gets the host of this V0040ClusterRecController.  # noqa: E501

        ControlHost  # noqa: E501

        :return: The host of this V0040ClusterRecController.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this V0040ClusterRecController.

        ControlHost  # noqa: E501

        :param host: The host of this V0040ClusterRecController.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """Gets the port of this V0040ClusterRecController.  # noqa: E501

        ControlPort  # noqa: E501

        :return: The port of this V0040ClusterRecController.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this V0040ClusterRecController.

        ControlPort  # noqa: E501

        :param port: The port of this V0040ClusterRecController.  # noqa: E501
        :type: int
        """

        self._port = port

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
        if not isinstance(other, V0040ClusterRecController):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V0040ClusterRecController):
            return True

        return self.to_dict() != other.to_dict()
