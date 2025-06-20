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


class V0040PartitionInfo(object):
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
        'nodes': 'V0040PartitionInfoNodes',
        'accounts': 'V0040PartitionInfoAccounts',
        'groups': 'V0040PartitionInfoGroups',
        'qos': 'V0040PartitionInfoQos',
        'alternate': 'str',
        'tres': 'V0040PartitionInfoTres',
        'cluster': 'str',
        'cpus': 'V0040PartitionInfoCpus',
        'defaults': 'V0040PartitionInfoDefaults',
        'grace_time': 'int',
        'maximums': 'V0040PartitionInfoMaximums',
        'minimums': 'V0040PartitionInfoMinimums',
        'name': 'str',
        'node_sets': 'str',
        'priority': 'V0040PartitionInfoPriority',
        'timeouts': 'V0040PartitionInfoTimeouts',
        'partition': 'V0040PartitionInfoPartition',
        'suspend_time': 'V0040Uint32NoVal'
    }

    attribute_map = {
        'nodes': 'nodes',
        'accounts': 'accounts',
        'groups': 'groups',
        'qos': 'qos',
        'alternate': 'alternate',
        'tres': 'tres',
        'cluster': 'cluster',
        'cpus': 'cpus',
        'defaults': 'defaults',
        'grace_time': 'grace_time',
        'maximums': 'maximums',
        'minimums': 'minimums',
        'name': 'name',
        'node_sets': 'node_sets',
        'priority': 'priority',
        'timeouts': 'timeouts',
        'partition': 'partition',
        'suspend_time': 'suspend_time'
    }

    def __init__(self, nodes=None, accounts=None, groups=None, qos=None, alternate=None, tres=None, cluster=None, cpus=None, defaults=None, grace_time=None, maximums=None, minimums=None, name=None, node_sets=None, priority=None, timeouts=None, partition=None, suspend_time=None, local_vars_configuration=None):  # noqa: E501
        """V0040PartitionInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._nodes = None
        self._accounts = None
        self._groups = None
        self._qos = None
        self._alternate = None
        self._tres = None
        self._cluster = None
        self._cpus = None
        self._defaults = None
        self._grace_time = None
        self._maximums = None
        self._minimums = None
        self._name = None
        self._node_sets = None
        self._priority = None
        self._timeouts = None
        self._partition = None
        self._suspend_time = None
        self.discriminator = None

        if nodes is not None:
            self.nodes = nodes
        if accounts is not None:
            self.accounts = accounts
        if groups is not None:
            self.groups = groups
        if qos is not None:
            self.qos = qos
        if alternate is not None:
            self.alternate = alternate
        if tres is not None:
            self.tres = tres
        if cluster is not None:
            self.cluster = cluster
        if cpus is not None:
            self.cpus = cpus
        if defaults is not None:
            self.defaults = defaults
        if grace_time is not None:
            self.grace_time = grace_time
        if maximums is not None:
            self.maximums = maximums
        if minimums is not None:
            self.minimums = minimums
        if name is not None:
            self.name = name
        if node_sets is not None:
            self.node_sets = node_sets
        if priority is not None:
            self.priority = priority
        if timeouts is not None:
            self.timeouts = timeouts
        if partition is not None:
            self.partition = partition
        if suspend_time is not None:
            self.suspend_time = suspend_time

    @property
    def nodes(self):
        """Gets the nodes of this V0040PartitionInfo.  # noqa: E501


        :return: The nodes of this V0040PartitionInfo.  # noqa: E501
        :rtype: V0040PartitionInfoNodes
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this V0040PartitionInfo.


        :param nodes: The nodes of this V0040PartitionInfo.  # noqa: E501
        :type: V0040PartitionInfoNodes
        """

        self._nodes = nodes

    @property
    def accounts(self):
        """Gets the accounts of this V0040PartitionInfo.  # noqa: E501


        :return: The accounts of this V0040PartitionInfo.  # noqa: E501
        :rtype: V0040PartitionInfoAccounts
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this V0040PartitionInfo.


        :param accounts: The accounts of this V0040PartitionInfo.  # noqa: E501
        :type: V0040PartitionInfoAccounts
        """

        self._accounts = accounts

    @property
    def groups(self):
        """Gets the groups of this V0040PartitionInfo.  # noqa: E501


        :return: The groups of this V0040PartitionInfo.  # noqa: E501
        :rtype: V0040PartitionInfoGroups
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this V0040PartitionInfo.


        :param groups: The groups of this V0040PartitionInfo.  # noqa: E501
        :type: V0040PartitionInfoGroups
        """

        self._groups = groups

    @property
    def qos(self):
        """Gets the qos of this V0040PartitionInfo.  # noqa: E501


        :return: The qos of this V0040PartitionInfo.  # noqa: E501
        :rtype: V0040PartitionInfoQos
        """
        return self._qos

    @qos.setter
    def qos(self, qos):
        """Sets the qos of this V0040PartitionInfo.


        :param qos: The qos of this V0040PartitionInfo.  # noqa: E501
        :type: V0040PartitionInfoQos
        """

        self._qos = qos

    @property
    def alternate(self):
        """Gets the alternate of this V0040PartitionInfo.  # noqa: E501

        Alternate  # noqa: E501

        :return: The alternate of this V0040PartitionInfo.  # noqa: E501
        :rtype: str
        """
        return self._alternate

    @alternate.setter
    def alternate(self, alternate):
        """Sets the alternate of this V0040PartitionInfo.

        Alternate  # noqa: E501

        :param alternate: The alternate of this V0040PartitionInfo.  # noqa: E501
        :type: str
        """

        self._alternate = alternate

    @property
    def tres(self):
        """Gets the tres of this V0040PartitionInfo.  # noqa: E501


        :return: The tres of this V0040PartitionInfo.  # noqa: E501
        :rtype: V0040PartitionInfoTres
        """
        return self._tres

    @tres.setter
    def tres(self, tres):
        """Sets the tres of this V0040PartitionInfo.


        :param tres: The tres of this V0040PartitionInfo.  # noqa: E501
        :type: V0040PartitionInfoTres
        """

        self._tres = tres

    @property
    def cluster(self):
        """Gets the cluster of this V0040PartitionInfo.  # noqa: E501

        Cluster name  # noqa: E501

        :return: The cluster of this V0040PartitionInfo.  # noqa: E501
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this V0040PartitionInfo.

        Cluster name  # noqa: E501

        :param cluster: The cluster of this V0040PartitionInfo.  # noqa: E501
        :type: str
        """

        self._cluster = cluster

    @property
    def cpus(self):
        """Gets the cpus of this V0040PartitionInfo.  # noqa: E501


        :return: The cpus of this V0040PartitionInfo.  # noqa: E501
        :rtype: V0040PartitionInfoCpus
        """
        return self._cpus

    @cpus.setter
    def cpus(self, cpus):
        """Sets the cpus of this V0040PartitionInfo.


        :param cpus: The cpus of this V0040PartitionInfo.  # noqa: E501
        :type: V0040PartitionInfoCpus
        """

        self._cpus = cpus

    @property
    def defaults(self):
        """Gets the defaults of this V0040PartitionInfo.  # noqa: E501


        :return: The defaults of this V0040PartitionInfo.  # noqa: E501
        :rtype: V0040PartitionInfoDefaults
        """
        return self._defaults

    @defaults.setter
    def defaults(self, defaults):
        """Sets the defaults of this V0040PartitionInfo.


        :param defaults: The defaults of this V0040PartitionInfo.  # noqa: E501
        :type: V0040PartitionInfoDefaults
        """

        self._defaults = defaults

    @property
    def grace_time(self):
        """Gets the grace_time of this V0040PartitionInfo.  # noqa: E501

        GraceTime  # noqa: E501

        :return: The grace_time of this V0040PartitionInfo.  # noqa: E501
        :rtype: int
        """
        return self._grace_time

    @grace_time.setter
    def grace_time(self, grace_time):
        """Sets the grace_time of this V0040PartitionInfo.

        GraceTime  # noqa: E501

        :param grace_time: The grace_time of this V0040PartitionInfo.  # noqa: E501
        :type: int
        """

        self._grace_time = grace_time

    @property
    def maximums(self):
        """Gets the maximums of this V0040PartitionInfo.  # noqa: E501


        :return: The maximums of this V0040PartitionInfo.  # noqa: E501
        :rtype: V0040PartitionInfoMaximums
        """
        return self._maximums

    @maximums.setter
    def maximums(self, maximums):
        """Sets the maximums of this V0040PartitionInfo.


        :param maximums: The maximums of this V0040PartitionInfo.  # noqa: E501
        :type: V0040PartitionInfoMaximums
        """

        self._maximums = maximums

    @property
    def minimums(self):
        """Gets the minimums of this V0040PartitionInfo.  # noqa: E501


        :return: The minimums of this V0040PartitionInfo.  # noqa: E501
        :rtype: V0040PartitionInfoMinimums
        """
        return self._minimums

    @minimums.setter
    def minimums(self, minimums):
        """Sets the minimums of this V0040PartitionInfo.


        :param minimums: The minimums of this V0040PartitionInfo.  # noqa: E501
        :type: V0040PartitionInfoMinimums
        """

        self._minimums = minimums

    @property
    def name(self):
        """Gets the name of this V0040PartitionInfo.  # noqa: E501

        PartitionName  # noqa: E501

        :return: The name of this V0040PartitionInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V0040PartitionInfo.

        PartitionName  # noqa: E501

        :param name: The name of this V0040PartitionInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def node_sets(self):
        """Gets the node_sets of this V0040PartitionInfo.  # noqa: E501

        NodeSets  # noqa: E501

        :return: The node_sets of this V0040PartitionInfo.  # noqa: E501
        :rtype: str
        """
        return self._node_sets

    @node_sets.setter
    def node_sets(self, node_sets):
        """Sets the node_sets of this V0040PartitionInfo.

        NodeSets  # noqa: E501

        :param node_sets: The node_sets of this V0040PartitionInfo.  # noqa: E501
        :type: str
        """

        self._node_sets = node_sets

    @property
    def priority(self):
        """Gets the priority of this V0040PartitionInfo.  # noqa: E501


        :return: The priority of this V0040PartitionInfo.  # noqa: E501
        :rtype: V0040PartitionInfoPriority
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this V0040PartitionInfo.


        :param priority: The priority of this V0040PartitionInfo.  # noqa: E501
        :type: V0040PartitionInfoPriority
        """

        self._priority = priority

    @property
    def timeouts(self):
        """Gets the timeouts of this V0040PartitionInfo.  # noqa: E501


        :return: The timeouts of this V0040PartitionInfo.  # noqa: E501
        :rtype: V0040PartitionInfoTimeouts
        """
        return self._timeouts

    @timeouts.setter
    def timeouts(self, timeouts):
        """Sets the timeouts of this V0040PartitionInfo.


        :param timeouts: The timeouts of this V0040PartitionInfo.  # noqa: E501
        :type: V0040PartitionInfoTimeouts
        """

        self._timeouts = timeouts

    @property
    def partition(self):
        """Gets the partition of this V0040PartitionInfo.  # noqa: E501


        :return: The partition of this V0040PartitionInfo.  # noqa: E501
        :rtype: V0040PartitionInfoPartition
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this V0040PartitionInfo.


        :param partition: The partition of this V0040PartitionInfo.  # noqa: E501
        :type: V0040PartitionInfoPartition
        """

        self._partition = partition

    @property
    def suspend_time(self):
        """Gets the suspend_time of this V0040PartitionInfo.  # noqa: E501


        :return: The suspend_time of this V0040PartitionInfo.  # noqa: E501
        :rtype: V0040Uint32NoVal
        """
        return self._suspend_time

    @suspend_time.setter
    def suspend_time(self, suspend_time):
        """Sets the suspend_time of this V0040PartitionInfo.


        :param suspend_time: The suspend_time of this V0040PartitionInfo.  # noqa: E501
        :type: V0040Uint32NoVal
        """

        self._suspend_time = suspend_time

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
        if not isinstance(other, V0040PartitionInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V0040PartitionInfo):
            return True

        return self.to_dict() != other.to_dict()
