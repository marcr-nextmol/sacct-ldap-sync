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


class V0040License(object):
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
        'license_name': 'str',
        'total': 'int',
        'used': 'int',
        'free': 'int',
        'remote': 'bool',
        'reserved': 'int',
        'last_consumed': 'int',
        'last_deficit': 'int',
        'last_update': 'int'
    }

    attribute_map = {
        'license_name': 'LicenseName',
        'total': 'Total',
        'used': 'Used',
        'free': 'Free',
        'remote': 'Remote',
        'reserved': 'Reserved',
        'last_consumed': 'LastConsumed',
        'last_deficit': 'LastDeficit',
        'last_update': 'LastUpdate'
    }

    def __init__(self, license_name=None, total=None, used=None, free=None, remote=None, reserved=None, last_consumed=None, last_deficit=None, last_update=None, local_vars_configuration=None):  # noqa: E501
        """V0040License - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._license_name = None
        self._total = None
        self._used = None
        self._free = None
        self._remote = None
        self._reserved = None
        self._last_consumed = None
        self._last_deficit = None
        self._last_update = None
        self.discriminator = None

        if license_name is not None:
            self.license_name = license_name
        if total is not None:
            self.total = total
        if used is not None:
            self.used = used
        if free is not None:
            self.free = free
        if remote is not None:
            self.remote = remote
        if reserved is not None:
            self.reserved = reserved
        if last_consumed is not None:
            self.last_consumed = last_consumed
        if last_deficit is not None:
            self.last_deficit = last_deficit
        if last_update is not None:
            self.last_update = last_update

    @property
    def license_name(self):
        """Gets the license_name of this V0040License.  # noqa: E501

        Name of the license  # noqa: E501

        :return: The license_name of this V0040License.  # noqa: E501
        :rtype: str
        """
        return self._license_name

    @license_name.setter
    def license_name(self, license_name):
        """Sets the license_name of this V0040License.

        Name of the license  # noqa: E501

        :param license_name: The license_name of this V0040License.  # noqa: E501
        :type: str
        """

        self._license_name = license_name

    @property
    def total(self):
        """Gets the total of this V0040License.  # noqa: E501

        Total number of licenses present  # noqa: E501

        :return: The total of this V0040License.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this V0040License.

        Total number of licenses present  # noqa: E501

        :param total: The total of this V0040License.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def used(self):
        """Gets the used of this V0040License.  # noqa: E501

        Number of licenses in use  # noqa: E501

        :return: The used of this V0040License.  # noqa: E501
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this V0040License.

        Number of licenses in use  # noqa: E501

        :param used: The used of this V0040License.  # noqa: E501
        :type: int
        """

        self._used = used

    @property
    def free(self):
        """Gets the free of this V0040License.  # noqa: E501

        Number of licenses currently available  # noqa: E501

        :return: The free of this V0040License.  # noqa: E501
        :rtype: int
        """
        return self._free

    @free.setter
    def free(self, free):
        """Sets the free of this V0040License.

        Number of licenses currently available  # noqa: E501

        :param free: The free of this V0040License.  # noqa: E501
        :type: int
        """

        self._free = free

    @property
    def remote(self):
        """Gets the remote of this V0040License.  # noqa: E501

        Indicates whether licenses are served by the database  # noqa: E501

        :return: The remote of this V0040License.  # noqa: E501
        :rtype: bool
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this V0040License.

        Indicates whether licenses are served by the database  # noqa: E501

        :param remote: The remote of this V0040License.  # noqa: E501
        :type: bool
        """

        self._remote = remote

    @property
    def reserved(self):
        """Gets the reserved of this V0040License.  # noqa: E501

        Number of licenses reserved  # noqa: E501

        :return: The reserved of this V0040License.  # noqa: E501
        :rtype: int
        """
        return self._reserved

    @reserved.setter
    def reserved(self, reserved):
        """Sets the reserved of this V0040License.

        Number of licenses reserved  # noqa: E501

        :param reserved: The reserved of this V0040License.  # noqa: E501
        :type: int
        """

        self._reserved = reserved

    @property
    def last_consumed(self):
        """Gets the last_consumed of this V0040License.  # noqa: E501

        Last known number of licenses that were consumed in the license manager (Remote Only)  # noqa: E501

        :return: The last_consumed of this V0040License.  # noqa: E501
        :rtype: int
        """
        return self._last_consumed

    @last_consumed.setter
    def last_consumed(self, last_consumed):
        """Sets the last_consumed of this V0040License.

        Last known number of licenses that were consumed in the license manager (Remote Only)  # noqa: E501

        :param last_consumed: The last_consumed of this V0040License.  # noqa: E501
        :type: int
        """

        self._last_consumed = last_consumed

    @property
    def last_deficit(self):
        """Gets the last_deficit of this V0040License.  # noqa: E501

        Number of \"missing licenses\" from the cluster's perspective  # noqa: E501

        :return: The last_deficit of this V0040License.  # noqa: E501
        :rtype: int
        """
        return self._last_deficit

    @last_deficit.setter
    def last_deficit(self, last_deficit):
        """Sets the last_deficit of this V0040License.

        Number of \"missing licenses\" from the cluster's perspective  # noqa: E501

        :param last_deficit: The last_deficit of this V0040License.  # noqa: E501
        :type: int
        """

        self._last_deficit = last_deficit

    @property
    def last_update(self):
        """Gets the last_update of this V0040License.  # noqa: E501

        When the license information was last updated (UNIX Timestamp)  # noqa: E501

        :return: The last_update of this V0040License.  # noqa: E501
        :rtype: int
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this V0040License.

        When the license information was last updated (UNIX Timestamp)  # noqa: E501

        :param last_update: The last_update of this V0040License.  # noqa: E501
        :type: int
        """

        self._last_update = last_update

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
        if not isinstance(other, V0040License):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V0040License):
            return True

        return self.to_dict() != other.to_dict()
