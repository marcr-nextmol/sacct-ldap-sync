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


class V0040AssocRecSet(object):
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
        'comment': 'str',
        'defaultqos': 'str',
        'grpjobs': 'V0040Uint32NoVal',
        'grpjobsaccrue': 'V0040Uint32NoVal',
        'grpsubmitjobs': 'V0040Uint32NoVal',
        'grptres': 'list[V0040Tres]',
        'grptresmins': 'list[V0040Tres]',
        'grptresrunmins': 'list[V0040Tres]',
        'grpwall': 'V0040Uint32NoVal',
        'maxjobs': 'V0040Uint32NoVal',
        'maxjobsaccrue': 'V0040Uint32NoVal',
        'maxsubmitjobs': 'V0040Uint32NoVal',
        'maxtresminsperjob': 'list[V0040Tres]',
        'maxtresrunmins': 'list[V0040Tres]',
        'maxtresperjob': 'list[V0040Tres]',
        'maxtrespernode': 'list[V0040Tres]',
        'maxwalldurationperjob': 'V0040Uint32NoVal',
        'minpriothresh': 'V0040Uint32NoVal',
        'parent': 'str',
        'priority': 'V0040Uint32NoVal',
        'qoslevel': 'list[str]',
        'fairshare': 'int'
    }

    attribute_map = {
        'comment': 'comment',
        'defaultqos': 'defaultqos',
        'grpjobs': 'grpjobs',
        'grpjobsaccrue': 'grpjobsaccrue',
        'grpsubmitjobs': 'grpsubmitjobs',
        'grptres': 'grptres',
        'grptresmins': 'grptresmins',
        'grptresrunmins': 'grptresrunmins',
        'grpwall': 'grpwall',
        'maxjobs': 'maxjobs',
        'maxjobsaccrue': 'maxjobsaccrue',
        'maxsubmitjobs': 'maxsubmitjobs',
        'maxtresminsperjob': 'maxtresminsperjob',
        'maxtresrunmins': 'maxtresrunmins',
        'maxtresperjob': 'maxtresperjob',
        'maxtrespernode': 'maxtrespernode',
        'maxwalldurationperjob': 'maxwalldurationperjob',
        'minpriothresh': 'minpriothresh',
        'parent': 'parent',
        'priority': 'priority',
        'qoslevel': 'qoslevel',
        'fairshare': 'fairshare'
    }

    def __init__(self, comment=None, defaultqos=None, grpjobs=None, grpjobsaccrue=None, grpsubmitjobs=None, grptres=None, grptresmins=None, grptresrunmins=None, grpwall=None, maxjobs=None, maxjobsaccrue=None, maxsubmitjobs=None, maxtresminsperjob=None, maxtresrunmins=None, maxtresperjob=None, maxtrespernode=None, maxwalldurationperjob=None, minpriothresh=None, parent=None, priority=None, qoslevel=None, fairshare=None, local_vars_configuration=None):  # noqa: E501
        """V0040AssocRecSet - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._comment = None
        self._defaultqos = None
        self._grpjobs = None
        self._grpjobsaccrue = None
        self._grpsubmitjobs = None
        self._grptres = None
        self._grptresmins = None
        self._grptresrunmins = None
        self._grpwall = None
        self._maxjobs = None
        self._maxjobsaccrue = None
        self._maxsubmitjobs = None
        self._maxtresminsperjob = None
        self._maxtresrunmins = None
        self._maxtresperjob = None
        self._maxtrespernode = None
        self._maxwalldurationperjob = None
        self._minpriothresh = None
        self._parent = None
        self._priority = None
        self._qoslevel = None
        self._fairshare = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if defaultqos is not None:
            self.defaultqos = defaultqos
        if grpjobs is not None:
            self.grpjobs = grpjobs
        if grpjobsaccrue is not None:
            self.grpjobsaccrue = grpjobsaccrue
        if grpsubmitjobs is not None:
            self.grpsubmitjobs = grpsubmitjobs
        if grptres is not None:
            self.grptres = grptres
        if grptresmins is not None:
            self.grptresmins = grptresmins
        if grptresrunmins is not None:
            self.grptresrunmins = grptresrunmins
        if grpwall is not None:
            self.grpwall = grpwall
        if maxjobs is not None:
            self.maxjobs = maxjobs
        if maxjobsaccrue is not None:
            self.maxjobsaccrue = maxjobsaccrue
        if maxsubmitjobs is not None:
            self.maxsubmitjobs = maxsubmitjobs
        if maxtresminsperjob is not None:
            self.maxtresminsperjob = maxtresminsperjob
        if maxtresrunmins is not None:
            self.maxtresrunmins = maxtresrunmins
        if maxtresperjob is not None:
            self.maxtresperjob = maxtresperjob
        if maxtrespernode is not None:
            self.maxtrespernode = maxtrespernode
        if maxwalldurationperjob is not None:
            self.maxwalldurationperjob = maxwalldurationperjob
        if minpriothresh is not None:
            self.minpriothresh = minpriothresh
        if parent is not None:
            self.parent = parent
        if priority is not None:
            self.priority = priority
        if qoslevel is not None:
            self.qoslevel = qoslevel
        if fairshare is not None:
            self.fairshare = fairshare

    @property
    def comment(self):
        """Gets the comment of this V0040AssocRecSet.  # noqa: E501

        Arbitrary comment  # noqa: E501

        :return: The comment of this V0040AssocRecSet.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this V0040AssocRecSet.

        Arbitrary comment  # noqa: E501

        :param comment: The comment of this V0040AssocRecSet.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def defaultqos(self):
        """Gets the defaultqos of this V0040AssocRecSet.  # noqa: E501

        Default QOS  # noqa: E501

        :return: The defaultqos of this V0040AssocRecSet.  # noqa: E501
        :rtype: str
        """
        return self._defaultqos

    @defaultqos.setter
    def defaultqos(self, defaultqos):
        """Sets the defaultqos of this V0040AssocRecSet.

        Default QOS  # noqa: E501

        :param defaultqos: The defaultqos of this V0040AssocRecSet.  # noqa: E501
        :type: str
        """

        self._defaultqos = defaultqos

    @property
    def grpjobs(self):
        """Gets the grpjobs of this V0040AssocRecSet.  # noqa: E501


        :return: The grpjobs of this V0040AssocRecSet.  # noqa: E501
        :rtype: V0040Uint32NoVal
        """
        return self._grpjobs

    @grpjobs.setter
    def grpjobs(self, grpjobs):
        """Sets the grpjobs of this V0040AssocRecSet.


        :param grpjobs: The grpjobs of this V0040AssocRecSet.  # noqa: E501
        :type: V0040Uint32NoVal
        """

        self._grpjobs = grpjobs

    @property
    def grpjobsaccrue(self):
        """Gets the grpjobsaccrue of this V0040AssocRecSet.  # noqa: E501


        :return: The grpjobsaccrue of this V0040AssocRecSet.  # noqa: E501
        :rtype: V0040Uint32NoVal
        """
        return self._grpjobsaccrue

    @grpjobsaccrue.setter
    def grpjobsaccrue(self, grpjobsaccrue):
        """Sets the grpjobsaccrue of this V0040AssocRecSet.


        :param grpjobsaccrue: The grpjobsaccrue of this V0040AssocRecSet.  # noqa: E501
        :type: V0040Uint32NoVal
        """

        self._grpjobsaccrue = grpjobsaccrue

    @property
    def grpsubmitjobs(self):
        """Gets the grpsubmitjobs of this V0040AssocRecSet.  # noqa: E501


        :return: The grpsubmitjobs of this V0040AssocRecSet.  # noqa: E501
        :rtype: V0040Uint32NoVal
        """
        return self._grpsubmitjobs

    @grpsubmitjobs.setter
    def grpsubmitjobs(self, grpsubmitjobs):
        """Sets the grpsubmitjobs of this V0040AssocRecSet.


        :param grpsubmitjobs: The grpsubmitjobs of this V0040AssocRecSet.  # noqa: E501
        :type: V0040Uint32NoVal
        """

        self._grpsubmitjobs = grpsubmitjobs

    @property
    def grptres(self):
        """Gets the grptres of this V0040AssocRecSet.  # noqa: E501


        :return: The grptres of this V0040AssocRecSet.  # noqa: E501
        :rtype: list[V0040Tres]
        """
        return self._grptres

    @grptres.setter
    def grptres(self, grptres):
        """Sets the grptres of this V0040AssocRecSet.


        :param grptres: The grptres of this V0040AssocRecSet.  # noqa: E501
        :type: list[V0040Tres]
        """

        self._grptres = grptres

    @property
    def grptresmins(self):
        """Gets the grptresmins of this V0040AssocRecSet.  # noqa: E501


        :return: The grptresmins of this V0040AssocRecSet.  # noqa: E501
        :rtype: list[V0040Tres]
        """
        return self._grptresmins

    @grptresmins.setter
    def grptresmins(self, grptresmins):
        """Sets the grptresmins of this V0040AssocRecSet.


        :param grptresmins: The grptresmins of this V0040AssocRecSet.  # noqa: E501
        :type: list[V0040Tres]
        """

        self._grptresmins = grptresmins

    @property
    def grptresrunmins(self):
        """Gets the grptresrunmins of this V0040AssocRecSet.  # noqa: E501


        :return: The grptresrunmins of this V0040AssocRecSet.  # noqa: E501
        :rtype: list[V0040Tres]
        """
        return self._grptresrunmins

    @grptresrunmins.setter
    def grptresrunmins(self, grptresrunmins):
        """Sets the grptresrunmins of this V0040AssocRecSet.


        :param grptresrunmins: The grptresrunmins of this V0040AssocRecSet.  # noqa: E501
        :type: list[V0040Tres]
        """

        self._grptresrunmins = grptresrunmins

    @property
    def grpwall(self):
        """Gets the grpwall of this V0040AssocRecSet.  # noqa: E501


        :return: The grpwall of this V0040AssocRecSet.  # noqa: E501
        :rtype: V0040Uint32NoVal
        """
        return self._grpwall

    @grpwall.setter
    def grpwall(self, grpwall):
        """Sets the grpwall of this V0040AssocRecSet.


        :param grpwall: The grpwall of this V0040AssocRecSet.  # noqa: E501
        :type: V0040Uint32NoVal
        """

        self._grpwall = grpwall

    @property
    def maxjobs(self):
        """Gets the maxjobs of this V0040AssocRecSet.  # noqa: E501


        :return: The maxjobs of this V0040AssocRecSet.  # noqa: E501
        :rtype: V0040Uint32NoVal
        """
        return self._maxjobs

    @maxjobs.setter
    def maxjobs(self, maxjobs):
        """Sets the maxjobs of this V0040AssocRecSet.


        :param maxjobs: The maxjobs of this V0040AssocRecSet.  # noqa: E501
        :type: V0040Uint32NoVal
        """

        self._maxjobs = maxjobs

    @property
    def maxjobsaccrue(self):
        """Gets the maxjobsaccrue of this V0040AssocRecSet.  # noqa: E501


        :return: The maxjobsaccrue of this V0040AssocRecSet.  # noqa: E501
        :rtype: V0040Uint32NoVal
        """
        return self._maxjobsaccrue

    @maxjobsaccrue.setter
    def maxjobsaccrue(self, maxjobsaccrue):
        """Sets the maxjobsaccrue of this V0040AssocRecSet.


        :param maxjobsaccrue: The maxjobsaccrue of this V0040AssocRecSet.  # noqa: E501
        :type: V0040Uint32NoVal
        """

        self._maxjobsaccrue = maxjobsaccrue

    @property
    def maxsubmitjobs(self):
        """Gets the maxsubmitjobs of this V0040AssocRecSet.  # noqa: E501


        :return: The maxsubmitjobs of this V0040AssocRecSet.  # noqa: E501
        :rtype: V0040Uint32NoVal
        """
        return self._maxsubmitjobs

    @maxsubmitjobs.setter
    def maxsubmitjobs(self, maxsubmitjobs):
        """Sets the maxsubmitjobs of this V0040AssocRecSet.


        :param maxsubmitjobs: The maxsubmitjobs of this V0040AssocRecSet.  # noqa: E501
        :type: V0040Uint32NoVal
        """

        self._maxsubmitjobs = maxsubmitjobs

    @property
    def maxtresminsperjob(self):
        """Gets the maxtresminsperjob of this V0040AssocRecSet.  # noqa: E501


        :return: The maxtresminsperjob of this V0040AssocRecSet.  # noqa: E501
        :rtype: list[V0040Tres]
        """
        return self._maxtresminsperjob

    @maxtresminsperjob.setter
    def maxtresminsperjob(self, maxtresminsperjob):
        """Sets the maxtresminsperjob of this V0040AssocRecSet.


        :param maxtresminsperjob: The maxtresminsperjob of this V0040AssocRecSet.  # noqa: E501
        :type: list[V0040Tres]
        """

        self._maxtresminsperjob = maxtresminsperjob

    @property
    def maxtresrunmins(self):
        """Gets the maxtresrunmins of this V0040AssocRecSet.  # noqa: E501


        :return: The maxtresrunmins of this V0040AssocRecSet.  # noqa: E501
        :rtype: list[V0040Tres]
        """
        return self._maxtresrunmins

    @maxtresrunmins.setter
    def maxtresrunmins(self, maxtresrunmins):
        """Sets the maxtresrunmins of this V0040AssocRecSet.


        :param maxtresrunmins: The maxtresrunmins of this V0040AssocRecSet.  # noqa: E501
        :type: list[V0040Tres]
        """

        self._maxtresrunmins = maxtresrunmins

    @property
    def maxtresperjob(self):
        """Gets the maxtresperjob of this V0040AssocRecSet.  # noqa: E501


        :return: The maxtresperjob of this V0040AssocRecSet.  # noqa: E501
        :rtype: list[V0040Tres]
        """
        return self._maxtresperjob

    @maxtresperjob.setter
    def maxtresperjob(self, maxtresperjob):
        """Sets the maxtresperjob of this V0040AssocRecSet.


        :param maxtresperjob: The maxtresperjob of this V0040AssocRecSet.  # noqa: E501
        :type: list[V0040Tres]
        """

        self._maxtresperjob = maxtresperjob

    @property
    def maxtrespernode(self):
        """Gets the maxtrespernode of this V0040AssocRecSet.  # noqa: E501


        :return: The maxtrespernode of this V0040AssocRecSet.  # noqa: E501
        :rtype: list[V0040Tres]
        """
        return self._maxtrespernode

    @maxtrespernode.setter
    def maxtrespernode(self, maxtrespernode):
        """Sets the maxtrespernode of this V0040AssocRecSet.


        :param maxtrespernode: The maxtrespernode of this V0040AssocRecSet.  # noqa: E501
        :type: list[V0040Tres]
        """

        self._maxtrespernode = maxtrespernode

    @property
    def maxwalldurationperjob(self):
        """Gets the maxwalldurationperjob of this V0040AssocRecSet.  # noqa: E501


        :return: The maxwalldurationperjob of this V0040AssocRecSet.  # noqa: E501
        :rtype: V0040Uint32NoVal
        """
        return self._maxwalldurationperjob

    @maxwalldurationperjob.setter
    def maxwalldurationperjob(self, maxwalldurationperjob):
        """Sets the maxwalldurationperjob of this V0040AssocRecSet.


        :param maxwalldurationperjob: The maxwalldurationperjob of this V0040AssocRecSet.  # noqa: E501
        :type: V0040Uint32NoVal
        """

        self._maxwalldurationperjob = maxwalldurationperjob

    @property
    def minpriothresh(self):
        """Gets the minpriothresh of this V0040AssocRecSet.  # noqa: E501


        :return: The minpriothresh of this V0040AssocRecSet.  # noqa: E501
        :rtype: V0040Uint32NoVal
        """
        return self._minpriothresh

    @minpriothresh.setter
    def minpriothresh(self, minpriothresh):
        """Sets the minpriothresh of this V0040AssocRecSet.


        :param minpriothresh: The minpriothresh of this V0040AssocRecSet.  # noqa: E501
        :type: V0040Uint32NoVal
        """

        self._minpriothresh = minpriothresh

    @property
    def parent(self):
        """Gets the parent of this V0040AssocRecSet.  # noqa: E501

        Name of parent account  # noqa: E501

        :return: The parent of this V0040AssocRecSet.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this V0040AssocRecSet.

        Name of parent account  # noqa: E501

        :param parent: The parent of this V0040AssocRecSet.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def priority(self):
        """Gets the priority of this V0040AssocRecSet.  # noqa: E501


        :return: The priority of this V0040AssocRecSet.  # noqa: E501
        :rtype: V0040Uint32NoVal
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this V0040AssocRecSet.


        :param priority: The priority of this V0040AssocRecSet.  # noqa: E501
        :type: V0040Uint32NoVal
        """

        self._priority = priority

    @property
    def qoslevel(self):
        """Gets the qoslevel of this V0040AssocRecSet.  # noqa: E501

        List of QOS names  # noqa: E501

        :return: The qoslevel of this V0040AssocRecSet.  # noqa: E501
        :rtype: list[str]
        """
        return self._qoslevel

    @qoslevel.setter
    def qoslevel(self, qoslevel):
        """Sets the qoslevel of this V0040AssocRecSet.

        List of QOS names  # noqa: E501

        :param qoslevel: The qoslevel of this V0040AssocRecSet.  # noqa: E501
        :type: list[str]
        """

        self._qoslevel = qoslevel

    @property
    def fairshare(self):
        """Gets the fairshare of this V0040AssocRecSet.  # noqa: E501

        Allocated shares used for fairshare calculation  # noqa: E501

        :return: The fairshare of this V0040AssocRecSet.  # noqa: E501
        :rtype: int
        """
        return self._fairshare

    @fairshare.setter
    def fairshare(self, fairshare):
        """Sets the fairshare of this V0040AssocRecSet.

        Allocated shares used for fairshare calculation  # noqa: E501

        :param fairshare: The fairshare of this V0040AssocRecSet.  # noqa: E501
        :type: int
        """

        self._fairshare = fairshare

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
        if not isinstance(other, V0040AssocRecSet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V0040AssocRecSet):
            return True

        return self.to_dict() != other.to_dict()
