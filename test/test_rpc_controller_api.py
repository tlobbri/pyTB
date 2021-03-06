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
from api.rpc_controller_api import RpcControllerApi  # noqa: E501
from pyTB.rest import ApiException


class TestRpcControllerApi(unittest.TestCase):
    """RpcControllerApi unit test stubs"""

    def setUp(self):
        self.api = api.rpc_controller_api.RpcControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_handle_one_way_device_rpc_request_using_post(self):
        """Test case for handle_one_way_device_rpc_request_using_post

        handleOneWayDeviceRPCRequest  # noqa: E501
        """
        pass

    def test_handle_two_way_device_rpc_request_using_post(self):
        """Test case for handle_two_way_device_rpc_request_using_post

        handleTwoWayDeviceRPCRequest  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
