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


class User(object):
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
        'authority': 'str',
        'created_time': 'int',
        'customer_id': 'CustomerId',
        'email': 'str',
        'first_name': 'str',
        'id': 'UserId',
        'last_name': 'str',
        'name': 'str',
        'owner_id': 'EntityId',
        'tenant_id': 'TenantId'
    }

    attribute_map = {
        'additional_info': 'additionalInfo',
        'authority': 'authority',
        'created_time': 'createdTime',
        'customer_id': 'customerId',
        'email': 'email',
        'first_name': 'firstName',
        'id': 'id',
        'last_name': 'lastName',
        'name': 'name',
        'owner_id': 'ownerId',
        'tenant_id': 'tenantId'
    }

    def __init__(self, additional_info=None, authority=None, created_time=None, customer_id=None, email=None, first_name=None, id=None, last_name=None, name=None, owner_id=None, tenant_id=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._additional_info = None
        self._authority = None
        self._created_time = None
        self._customer_id = None
        self._email = None
        self._first_name = None
        self._id = None
        self._last_name = None
        self._name = None
        self._owner_id = None
        self._tenant_id = None
        self.discriminator = None
        if additional_info is not None:
            self.additional_info = additional_info
        if authority is not None:
            self.authority = authority
        if created_time is not None:
            self.created_time = created_time
        if customer_id is not None:
            self.customer_id = customer_id
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if id is not None:
            self.id = id
        if last_name is not None:
            self.last_name = last_name
        if name is not None:
            self.name = name
        if owner_id is not None:
            self.owner_id = owner_id
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def additional_info(self):
        """Gets the additional_info of this User.  # noqa: E501


        :return: The additional_info of this User.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this User.


        :param additional_info: The additional_info of this User.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def authority(self):
        """Gets the authority of this User.  # noqa: E501


        :return: The authority of this User.  # noqa: E501
        :rtype: str
        """
        return self._authority

    @authority.setter
    def authority(self, authority):
        """Sets the authority of this User.


        :param authority: The authority of this User.  # noqa: E501
        :type: str
        """
        allowed_values = ["SYS_ADMIN", "TENANT_ADMIN", "CUSTOMER_USER", "REFRESH_TOKEN"]  # noqa: E501
        if authority not in allowed_values:
            raise ValueError(
                "Invalid value for `authority` ({0}), must be one of {1}"  # noqa: E501
                .format(authority, allowed_values)
            )

        self._authority = authority

    @property
    def created_time(self):
        """Gets the created_time of this User.  # noqa: E501


        :return: The created_time of this User.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this User.


        :param created_time: The created_time of this User.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def customer_id(self):
        """Gets the customer_id of this User.  # noqa: E501


        :return: The customer_id of this User.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this User.


        :param customer_id: The customer_id of this User.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501


        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.


        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501


        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.


        :param first_name: The first_name of this User.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: UserId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type: UserId
        """

        self._id = id

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501


        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.


        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501


        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.


        :param name: The name of this User.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner_id(self):
        """Gets the owner_id of this User.  # noqa: E501


        :return: The owner_id of this User.  # noqa: E501
        :rtype: EntityId
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this User.


        :param owner_id: The owner_id of this User.  # noqa: E501
        :type: EntityId
        """

        self._owner_id = owner_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this User.  # noqa: E501


        :return: The tenant_id of this User.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this User.


        :param tenant_id: The tenant_id of this User.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
