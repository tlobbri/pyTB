# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class RuleChainConnectionInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'additional_info': 'str',
        'from_index': 'int',
        'target_rule_chain_id': 'RuleChainId',
        'type': 'str'
    }

    attribute_map = {
        'additional_info': 'additionalInfo',
        'from_index': 'fromIndex',
        'target_rule_chain_id': 'targetRuleChainId',
        'type': 'type'
    }

    def __init__(self, additional_info=None, from_index=None, target_rule_chain_id=None, type=None):  # noqa: E501
        """RuleChainConnectionInfo - a model defined in Swagger"""  # noqa: E501
        self._additional_info = None
        self._from_index = None
        self._target_rule_chain_id = None
        self._type = None
        self.discriminator = None
        if additional_info is not None:
            self.additional_info = additional_info
        if from_index is not None:
            self.from_index = from_index
        if target_rule_chain_id is not None:
            self.target_rule_chain_id = target_rule_chain_id
        if type is not None:
            self.type = type

    @property
    def additional_info(self):
        """Gets the additional_info of this RuleChainConnectionInfo.  # noqa: E501


        :return: The additional_info of this RuleChainConnectionInfo.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this RuleChainConnectionInfo.


        :param additional_info: The additional_info of this RuleChainConnectionInfo.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def from_index(self):
        """Gets the from_index of this RuleChainConnectionInfo.  # noqa: E501


        :return: The from_index of this RuleChainConnectionInfo.  # noqa: E501
        :rtype: int
        """
        return self._from_index

    @from_index.setter
    def from_index(self, from_index):
        """Sets the from_index of this RuleChainConnectionInfo.


        :param from_index: The from_index of this RuleChainConnectionInfo.  # noqa: E501
        :type: int
        """

        self._from_index = from_index

    @property
    def target_rule_chain_id(self):
        """Gets the target_rule_chain_id of this RuleChainConnectionInfo.  # noqa: E501


        :return: The target_rule_chain_id of this RuleChainConnectionInfo.  # noqa: E501
        :rtype: RuleChainId
        """
        return self._target_rule_chain_id

    @target_rule_chain_id.setter
    def target_rule_chain_id(self, target_rule_chain_id):
        """Sets the target_rule_chain_id of this RuleChainConnectionInfo.


        :param target_rule_chain_id: The target_rule_chain_id of this RuleChainConnectionInfo.  # noqa: E501
        :type: RuleChainId
        """

        self._target_rule_chain_id = target_rule_chain_id

    @property
    def type(self):
        """Gets the type of this RuleChainConnectionInfo.  # noqa: E501


        :return: The type of this RuleChainConnectionInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RuleChainConnectionInfo.


        :param type: The type of this RuleChainConnectionInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(RuleChainConnectionInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RuleChainConnectionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
