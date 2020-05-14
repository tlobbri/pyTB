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


class AllowedPermissionsInfo(object):
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
        'allowed_for_group_owner_only_group_operations': 'list[str]',
        'allowed_for_group_owner_only_operations': 'list[str]',
        'allowed_for_group_role_operations': 'list[str]',
        'allowed_resources': 'list[str]',
        'operations_by_resource': 'dict(str, list[str])',
        'user_owner_id': 'EntityId',
        'user_permissions': 'MergedUserPermissions'
    }

    attribute_map = {
        'allowed_for_group_owner_only_group_operations': 'allowedForGroupOwnerOnlyGroupOperations',
        'allowed_for_group_owner_only_operations': 'allowedForGroupOwnerOnlyOperations',
        'allowed_for_group_role_operations': 'allowedForGroupRoleOperations',
        'allowed_resources': 'allowedResources',
        'operations_by_resource': 'operationsByResource',
        'user_owner_id': 'userOwnerId',
        'user_permissions': 'userPermissions'
    }

    def __init__(self, allowed_for_group_owner_only_group_operations=None, allowed_for_group_owner_only_operations=None, allowed_for_group_role_operations=None, allowed_resources=None, operations_by_resource=None, user_owner_id=None, user_permissions=None):  # noqa: E501
        """AllowedPermissionsInfo - a model defined in Swagger"""  # noqa: E501
        self._allowed_for_group_owner_only_group_operations = None
        self._allowed_for_group_owner_only_operations = None
        self._allowed_for_group_role_operations = None
        self._allowed_resources = None
        self._operations_by_resource = None
        self._user_owner_id = None
        self._user_permissions = None
        self.discriminator = None
        if allowed_for_group_owner_only_group_operations is not None:
            self.allowed_for_group_owner_only_group_operations = allowed_for_group_owner_only_group_operations
        if allowed_for_group_owner_only_operations is not None:
            self.allowed_for_group_owner_only_operations = allowed_for_group_owner_only_operations
        if allowed_for_group_role_operations is not None:
            self.allowed_for_group_role_operations = allowed_for_group_role_operations
        if allowed_resources is not None:
            self.allowed_resources = allowed_resources
        if operations_by_resource is not None:
            self.operations_by_resource = operations_by_resource
        if user_owner_id is not None:
            self.user_owner_id = user_owner_id
        if user_permissions is not None:
            self.user_permissions = user_permissions

    @property
    def allowed_for_group_owner_only_group_operations(self):
        """Gets the allowed_for_group_owner_only_group_operations of this AllowedPermissionsInfo.  # noqa: E501


        :return: The allowed_for_group_owner_only_group_operations of this AllowedPermissionsInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_for_group_owner_only_group_operations

    @allowed_for_group_owner_only_group_operations.setter
    def allowed_for_group_owner_only_group_operations(self, allowed_for_group_owner_only_group_operations):
        """Sets the allowed_for_group_owner_only_group_operations of this AllowedPermissionsInfo.


        :param allowed_for_group_owner_only_group_operations: The allowed_for_group_owner_only_group_operations of this AllowedPermissionsInfo.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ALL", "CREATE", "READ", "WRITE", "DELETE", "RPC_CALL", "READ_CREDENTIALS", "WRITE_CREDENTIALS", "READ_ATTRIBUTES", "WRITE_ATTRIBUTES", "READ_TELEMETRY", "WRITE_TELEMETRY", "ADD_TO_GROUP", "REMOVE_FROM_GROUP", "CHANGE_OWNER", "IMPERSONATE", "CLAIM_DEVICES"]  # noqa: E501
        if not set(allowed_for_group_owner_only_group_operations).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `allowed_for_group_owner_only_group_operations` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(allowed_for_group_owner_only_group_operations) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._allowed_for_group_owner_only_group_operations = allowed_for_group_owner_only_group_operations

    @property
    def allowed_for_group_owner_only_operations(self):
        """Gets the allowed_for_group_owner_only_operations of this AllowedPermissionsInfo.  # noqa: E501


        :return: The allowed_for_group_owner_only_operations of this AllowedPermissionsInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_for_group_owner_only_operations

    @allowed_for_group_owner_only_operations.setter
    def allowed_for_group_owner_only_operations(self, allowed_for_group_owner_only_operations):
        """Sets the allowed_for_group_owner_only_operations of this AllowedPermissionsInfo.


        :param allowed_for_group_owner_only_operations: The allowed_for_group_owner_only_operations of this AllowedPermissionsInfo.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ALL", "CREATE", "READ", "WRITE", "DELETE", "RPC_CALL", "READ_CREDENTIALS", "WRITE_CREDENTIALS", "READ_ATTRIBUTES", "WRITE_ATTRIBUTES", "READ_TELEMETRY", "WRITE_TELEMETRY", "ADD_TO_GROUP", "REMOVE_FROM_GROUP", "CHANGE_OWNER", "IMPERSONATE", "CLAIM_DEVICES"]  # noqa: E501
        if not set(allowed_for_group_owner_only_operations).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `allowed_for_group_owner_only_operations` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(allowed_for_group_owner_only_operations) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._allowed_for_group_owner_only_operations = allowed_for_group_owner_only_operations

    @property
    def allowed_for_group_role_operations(self):
        """Gets the allowed_for_group_role_operations of this AllowedPermissionsInfo.  # noqa: E501


        :return: The allowed_for_group_role_operations of this AllowedPermissionsInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_for_group_role_operations

    @allowed_for_group_role_operations.setter
    def allowed_for_group_role_operations(self, allowed_for_group_role_operations):
        """Sets the allowed_for_group_role_operations of this AllowedPermissionsInfo.


        :param allowed_for_group_role_operations: The allowed_for_group_role_operations of this AllowedPermissionsInfo.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ALL", "CREATE", "READ", "WRITE", "DELETE", "RPC_CALL", "READ_CREDENTIALS", "WRITE_CREDENTIALS", "READ_ATTRIBUTES", "WRITE_ATTRIBUTES", "READ_TELEMETRY", "WRITE_TELEMETRY", "ADD_TO_GROUP", "REMOVE_FROM_GROUP", "CHANGE_OWNER", "IMPERSONATE", "CLAIM_DEVICES"]  # noqa: E501
        if not set(allowed_for_group_role_operations).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `allowed_for_group_role_operations` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(allowed_for_group_role_operations) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._allowed_for_group_role_operations = allowed_for_group_role_operations

    @property
    def allowed_resources(self):
        """Gets the allowed_resources of this AllowedPermissionsInfo.  # noqa: E501


        :return: The allowed_resources of this AllowedPermissionsInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_resources

    @allowed_resources.setter
    def allowed_resources(self, allowed_resources):
        """Sets the allowed_resources of this AllowedPermissionsInfo.


        :param allowed_resources: The allowed_resources of this AllowedPermissionsInfo.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ALL", "PROFILE", "ADMIN_SETTINGS", "ALARM", "DEVICE", "ASSET", "CUSTOMER", "DASHBOARD", "ENTITY_VIEW", "TENANT", "RULE_CHAIN", "USER", "WIDGETS_BUNDLE", "WIDGET_TYPE", "CONVERTER", "INTEGRATION", "SCHEDULER_EVENT", "BLOB_ENTITY", "CUSTOMER_GROUP", "DEVICE_GROUP", "ASSET_GROUP", "USER_GROUP", "ENTITY_VIEW_GROUP", "DASHBOARD_GROUP", "ROLE", "GROUP_PERMISSION", "WHITE_LABELING", "AUDIT_LOG"]  # noqa: E501
        if not set(allowed_resources).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `allowed_resources` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(allowed_resources) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._allowed_resources = allowed_resources

    @property
    def operations_by_resource(self):
        """Gets the operations_by_resource of this AllowedPermissionsInfo.  # noqa: E501


        :return: The operations_by_resource of this AllowedPermissionsInfo.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._operations_by_resource

    @operations_by_resource.setter
    def operations_by_resource(self, operations_by_resource):
        """Sets the operations_by_resource of this AllowedPermissionsInfo.


        :param operations_by_resource: The operations_by_resource of this AllowedPermissionsInfo.  # noqa: E501
        :type: dict(str, list[str])
        """
        allowed_values = [ALL, CREATE, READ, WRITE, DELETE, RPC_CALL, READ_CREDENTIALS, WRITE_CREDENTIALS, READ_ATTRIBUTES, WRITE_ATTRIBUTES, READ_TELEMETRY, WRITE_TELEMETRY, ADD_TO_GROUP, REMOVE_FROM_GROUP, CHANGE_OWNER, IMPERSONATE, CLAIM_DEVICES]  # noqa: E501
        if not set(operations_by_resource.keys()).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid keys in `operations_by_resource` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(operations_by_resource.keys()) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._operations_by_resource = operations_by_resource

    @property
    def user_owner_id(self):
        """Gets the user_owner_id of this AllowedPermissionsInfo.  # noqa: E501


        :return: The user_owner_id of this AllowedPermissionsInfo.  # noqa: E501
        :rtype: EntityId
        """
        return self._user_owner_id

    @user_owner_id.setter
    def user_owner_id(self, user_owner_id):
        """Sets the user_owner_id of this AllowedPermissionsInfo.


        :param user_owner_id: The user_owner_id of this AllowedPermissionsInfo.  # noqa: E501
        :type: EntityId
        """

        self._user_owner_id = user_owner_id

    @property
    def user_permissions(self):
        """Gets the user_permissions of this AllowedPermissionsInfo.  # noqa: E501


        :return: The user_permissions of this AllowedPermissionsInfo.  # noqa: E501
        :rtype: MergedUserPermissions
        """
        return self._user_permissions

    @user_permissions.setter
    def user_permissions(self, user_permissions):
        """Sets the user_permissions of this AllowedPermissionsInfo.


        :param user_permissions: The user_permissions of this AllowedPermissionsInfo.  # noqa: E501
        :type: MergedUserPermissions
        """

        self._user_permissions = user_permissions

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
        if issubclass(AllowedPermissionsInfo, dict):
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
        if not isinstance(other, AllowedPermissionsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other