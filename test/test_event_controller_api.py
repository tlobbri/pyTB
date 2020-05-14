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
from api.event_controller_api import EventControllerApi  # noqa: E501
from pyTB.rest import ApiException


class TestEventControllerApi(unittest.TestCase):
    """EventControllerApi unit test stubs"""

    def setUp(self):
        self.api = api.event_controller_api.EventControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_events_using_get(self):
        """Test case for get_events_using_get

        getEvents  # noqa: E501
        """
        pass

    def test_get_events_using_get1(self):
        """Test case for get_events_using_get1

        getEvents  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
