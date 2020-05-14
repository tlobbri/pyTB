# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import pyTB
from api.device_api_controller_api import DeviceApiControllerApi  # noqa: E501
from pyTB.rest import ApiException


class TestDeviceApiControllerApi(unittest.TestCase):
    """DeviceApiControllerApi unit test stubs"""

    def setUp(self):
        self.api = api.device_api_controller_api.DeviceApiControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_claim_device_using_post(self):
        """Test case for claim_device_using_post

        claimDevice  # noqa: E501
        """
        pass

    def test_get_device_attributes_using_get(self):
        """Test case for get_device_attributes_using_get

        getDeviceAttributes  # noqa: E501
        """
        pass

    def test_post_device_attributes_using_post(self):
        """Test case for post_device_attributes_using_post

        postDeviceAttributes  # noqa: E501
        """
        pass

    def test_post_rpc_request_using_post(self):
        """Test case for post_rpc_request_using_post

        postRpcRequest  # noqa: E501
        """
        pass

    def test_post_telemetry_using_post(self):
        """Test case for post_telemetry_using_post

        postTelemetry  # noqa: E501
        """
        pass

    def test_reply_to_command_using_post(self):
        """Test case for reply_to_command_using_post

        replyToCommand  # noqa: E501
        """
        pass

    def test_subscribe_to_attributes_using_get(self):
        """Test case for subscribe_to_attributes_using_get

        subscribeToAttributes  # noqa: E501
        """
        pass

    def test_subscribe_to_commands_using_get(self):
        """Test case for subscribe_to_commands_using_get

        subscribeToCommands  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
