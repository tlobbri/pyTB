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


class UserPasswordPolicy(object):
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
        'minimum_digits': 'int',
        'minimum_length': 'int',
        'minimum_lowercase_letters': 'int',
        'minimum_special_characters': 'int',
        'minimum_uppercase_letters': 'int',
        'password_expiration_period_days': 'int',
        'password_reuse_frequency_days': 'int'
    }

    attribute_map = {
        'minimum_digits': 'minimumDigits',
        'minimum_length': 'minimumLength',
        'minimum_lowercase_letters': 'minimumLowercaseLetters',
        'minimum_special_characters': 'minimumSpecialCharacters',
        'minimum_uppercase_letters': 'minimumUppercaseLetters',
        'password_expiration_period_days': 'passwordExpirationPeriodDays',
        'password_reuse_frequency_days': 'passwordReuseFrequencyDays'
    }

    def __init__(self, minimum_digits=None, minimum_length=None, minimum_lowercase_letters=None, minimum_special_characters=None, minimum_uppercase_letters=None, password_expiration_period_days=None, password_reuse_frequency_days=None):  # noqa: E501
        """UserPasswordPolicy - a model defined in Swagger"""  # noqa: E501
        self._minimum_digits = None
        self._minimum_length = None
        self._minimum_lowercase_letters = None
        self._minimum_special_characters = None
        self._minimum_uppercase_letters = None
        self._password_expiration_period_days = None
        self._password_reuse_frequency_days = None
        self.discriminator = None
        if minimum_digits is not None:
            self.minimum_digits = minimum_digits
        if minimum_length is not None:
            self.minimum_length = minimum_length
        if minimum_lowercase_letters is not None:
            self.minimum_lowercase_letters = minimum_lowercase_letters
        if minimum_special_characters is not None:
            self.minimum_special_characters = minimum_special_characters
        if minimum_uppercase_letters is not None:
            self.minimum_uppercase_letters = minimum_uppercase_letters
        if password_expiration_period_days is not None:
            self.password_expiration_period_days = password_expiration_period_days
        if password_reuse_frequency_days is not None:
            self.password_reuse_frequency_days = password_reuse_frequency_days

    @property
    def minimum_digits(self):
        """Gets the minimum_digits of this UserPasswordPolicy.  # noqa: E501


        :return: The minimum_digits of this UserPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._minimum_digits

    @minimum_digits.setter
    def minimum_digits(self, minimum_digits):
        """Sets the minimum_digits of this UserPasswordPolicy.


        :param minimum_digits: The minimum_digits of this UserPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._minimum_digits = minimum_digits

    @property
    def minimum_length(self):
        """Gets the minimum_length of this UserPasswordPolicy.  # noqa: E501


        :return: The minimum_length of this UserPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._minimum_length

    @minimum_length.setter
    def minimum_length(self, minimum_length):
        """Sets the minimum_length of this UserPasswordPolicy.


        :param minimum_length: The minimum_length of this UserPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._minimum_length = minimum_length

    @property
    def minimum_lowercase_letters(self):
        """Gets the minimum_lowercase_letters of this UserPasswordPolicy.  # noqa: E501


        :return: The minimum_lowercase_letters of this UserPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._minimum_lowercase_letters

    @minimum_lowercase_letters.setter
    def minimum_lowercase_letters(self, minimum_lowercase_letters):
        """Sets the minimum_lowercase_letters of this UserPasswordPolicy.


        :param minimum_lowercase_letters: The minimum_lowercase_letters of this UserPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._minimum_lowercase_letters = minimum_lowercase_letters

    @property
    def minimum_special_characters(self):
        """Gets the minimum_special_characters of this UserPasswordPolicy.  # noqa: E501


        :return: The minimum_special_characters of this UserPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._minimum_special_characters

    @minimum_special_characters.setter
    def minimum_special_characters(self, minimum_special_characters):
        """Sets the minimum_special_characters of this UserPasswordPolicy.


        :param minimum_special_characters: The minimum_special_characters of this UserPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._minimum_special_characters = minimum_special_characters

    @property
    def minimum_uppercase_letters(self):
        """Gets the minimum_uppercase_letters of this UserPasswordPolicy.  # noqa: E501


        :return: The minimum_uppercase_letters of this UserPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._minimum_uppercase_letters

    @minimum_uppercase_letters.setter
    def minimum_uppercase_letters(self, minimum_uppercase_letters):
        """Sets the minimum_uppercase_letters of this UserPasswordPolicy.


        :param minimum_uppercase_letters: The minimum_uppercase_letters of this UserPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._minimum_uppercase_letters = minimum_uppercase_letters

    @property
    def password_expiration_period_days(self):
        """Gets the password_expiration_period_days of this UserPasswordPolicy.  # noqa: E501


        :return: The password_expiration_period_days of this UserPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._password_expiration_period_days

    @password_expiration_period_days.setter
    def password_expiration_period_days(self, password_expiration_period_days):
        """Sets the password_expiration_period_days of this UserPasswordPolicy.


        :param password_expiration_period_days: The password_expiration_period_days of this UserPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._password_expiration_period_days = password_expiration_period_days

    @property
    def password_reuse_frequency_days(self):
        """Gets the password_reuse_frequency_days of this UserPasswordPolicy.  # noqa: E501


        :return: The password_reuse_frequency_days of this UserPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._password_reuse_frequency_days

    @password_reuse_frequency_days.setter
    def password_reuse_frequency_days(self, password_reuse_frequency_days):
        """Sets the password_reuse_frequency_days of this UserPasswordPolicy.


        :param password_reuse_frequency_days: The password_reuse_frequency_days of this UserPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._password_reuse_frequency_days = password_reuse_frequency_days

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
        if issubclass(UserPasswordPolicy, dict):
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
        if not isinstance(other, UserPasswordPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
