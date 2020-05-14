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


class Alarm(object):
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
        'ack_ts': 'int',
        'clear_ts': 'int',
        'created_time': 'int',
        'details': 'str',
        'end_ts': 'int',
        'id': 'AlarmId',
        'name': 'str',
        'originator': 'EntityId',
        'propagate': 'bool',
        'propagate_relation_types': 'list[str]',
        'severity': 'str',
        'start_ts': 'int',
        'status': 'str',
        'tenant_id': 'TenantId',
        'type': 'str'
    }

    attribute_map = {
        'ack_ts': 'ackTs',
        'clear_ts': 'clearTs',
        'created_time': 'createdTime',
        'details': 'details',
        'end_ts': 'endTs',
        'id': 'id',
        'name': 'name',
        'originator': 'originator',
        'propagate': 'propagate',
        'propagate_relation_types': 'propagateRelationTypes',
        'severity': 'severity',
        'start_ts': 'startTs',
        'status': 'status',
        'tenant_id': 'tenantId',
        'type': 'type'
    }

    def __init__(self, ack_ts=None, clear_ts=None, created_time=None, details=None, end_ts=None, id=None, name=None, originator=None, propagate=None, propagate_relation_types=None, severity=None, start_ts=None, status=None, tenant_id=None, type=None):  # noqa: E501
        """Alarm - a model defined in Swagger"""  # noqa: E501
        self._ack_ts = None
        self._clear_ts = None
        self._created_time = None
        self._details = None
        self._end_ts = None
        self._id = None
        self._name = None
        self._originator = None
        self._propagate = None
        self._propagate_relation_types = None
        self._severity = None
        self._start_ts = None
        self._status = None
        self._tenant_id = None
        self._type = None
        self.discriminator = None
        if ack_ts is not None:
            self.ack_ts = ack_ts
        if clear_ts is not None:
            self.clear_ts = clear_ts
        if created_time is not None:
            self.created_time = created_time
        if details is not None:
            self.details = details
        if end_ts is not None:
            self.end_ts = end_ts
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if originator is not None:
            self.originator = originator
        if propagate is not None:
            self.propagate = propagate
        if propagate_relation_types is not None:
            self.propagate_relation_types = propagate_relation_types
        if severity is not None:
            self.severity = severity
        if start_ts is not None:
            self.start_ts = start_ts
        if status is not None:
            self.status = status
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if type is not None:
            self.type = type

    @property
    def ack_ts(self):
        """Gets the ack_ts of this Alarm.  # noqa: E501


        :return: The ack_ts of this Alarm.  # noqa: E501
        :rtype: int
        """
        return self._ack_ts

    @ack_ts.setter
    def ack_ts(self, ack_ts):
        """Sets the ack_ts of this Alarm.


        :param ack_ts: The ack_ts of this Alarm.  # noqa: E501
        :type: int
        """

        self._ack_ts = ack_ts

    @property
    def clear_ts(self):
        """Gets the clear_ts of this Alarm.  # noqa: E501


        :return: The clear_ts of this Alarm.  # noqa: E501
        :rtype: int
        """
        return self._clear_ts

    @clear_ts.setter
    def clear_ts(self, clear_ts):
        """Sets the clear_ts of this Alarm.


        :param clear_ts: The clear_ts of this Alarm.  # noqa: E501
        :type: int
        """

        self._clear_ts = clear_ts

    @property
    def created_time(self):
        """Gets the created_time of this Alarm.  # noqa: E501


        :return: The created_time of this Alarm.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Alarm.


        :param created_time: The created_time of this Alarm.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def details(self):
        """Gets the details of this Alarm.  # noqa: E501


        :return: The details of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Alarm.


        :param details: The details of this Alarm.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def end_ts(self):
        """Gets the end_ts of this Alarm.  # noqa: E501


        :return: The end_ts of this Alarm.  # noqa: E501
        :rtype: int
        """
        return self._end_ts

    @end_ts.setter
    def end_ts(self, end_ts):
        """Sets the end_ts of this Alarm.


        :param end_ts: The end_ts of this Alarm.  # noqa: E501
        :type: int
        """

        self._end_ts = end_ts

    @property
    def id(self):
        """Gets the id of this Alarm.  # noqa: E501


        :return: The id of this Alarm.  # noqa: E501
        :rtype: AlarmId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Alarm.


        :param id: The id of this Alarm.  # noqa: E501
        :type: AlarmId
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Alarm.  # noqa: E501


        :return: The name of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Alarm.


        :param name: The name of this Alarm.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def originator(self):
        """Gets the originator of this Alarm.  # noqa: E501


        :return: The originator of this Alarm.  # noqa: E501
        :rtype: EntityId
        """
        return self._originator

    @originator.setter
    def originator(self, originator):
        """Sets the originator of this Alarm.


        :param originator: The originator of this Alarm.  # noqa: E501
        :type: EntityId
        """

        self._originator = originator

    @property
    def propagate(self):
        """Gets the propagate of this Alarm.  # noqa: E501


        :return: The propagate of this Alarm.  # noqa: E501
        :rtype: bool
        """
        return self._propagate

    @propagate.setter
    def propagate(self, propagate):
        """Sets the propagate of this Alarm.


        :param propagate: The propagate of this Alarm.  # noqa: E501
        :type: bool
        """

        self._propagate = propagate

    @property
    def propagate_relation_types(self):
        """Gets the propagate_relation_types of this Alarm.  # noqa: E501


        :return: The propagate_relation_types of this Alarm.  # noqa: E501
        :rtype: list[str]
        """
        return self._propagate_relation_types

    @propagate_relation_types.setter
    def propagate_relation_types(self, propagate_relation_types):
        """Sets the propagate_relation_types of this Alarm.


        :param propagate_relation_types: The propagate_relation_types of this Alarm.  # noqa: E501
        :type: list[str]
        """

        self._propagate_relation_types = propagate_relation_types

    @property
    def severity(self):
        """Gets the severity of this Alarm.  # noqa: E501


        :return: The severity of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Alarm.


        :param severity: The severity of this Alarm.  # noqa: E501
        :type: str
        """
        allowed_values = ["CRITICAL", "MAJOR", "MINOR", "WARNING", "INDETERMINATE"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def start_ts(self):
        """Gets the start_ts of this Alarm.  # noqa: E501


        :return: The start_ts of this Alarm.  # noqa: E501
        :rtype: int
        """
        return self._start_ts

    @start_ts.setter
    def start_ts(self, start_ts):
        """Sets the start_ts of this Alarm.


        :param start_ts: The start_ts of this Alarm.  # noqa: E501
        :type: int
        """

        self._start_ts = start_ts

    @property
    def status(self):
        """Gets the status of this Alarm.  # noqa: E501


        :return: The status of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Alarm.


        :param status: The status of this Alarm.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE_UNACK", "ACTIVE_ACK", "CLEARED_UNACK", "CLEARED_ACK"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Alarm.  # noqa: E501


        :return: The tenant_id of this Alarm.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Alarm.


        :param tenant_id: The tenant_id of this Alarm.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def type(self):
        """Gets the type of this Alarm.  # noqa: E501


        :return: The type of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Alarm.


        :param type: The type of this Alarm.  # noqa: E501
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
        if issubclass(Alarm, dict):
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
        if not isinstance(other, Alarm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other