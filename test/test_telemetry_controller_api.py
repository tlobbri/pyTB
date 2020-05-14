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
from api.telemetry_controller_api import TelemetryControllerApi  # noqa: E501
from pyTB.rest import ApiException


class TestTelemetryControllerApi(unittest.TestCase):
    """TelemetryControllerApi unit test stubs"""

    def setUp(self):
        self.api = api.telemetry_controller_api.TelemetryControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_entity_attributes_using_delete(self):
        """Test case for delete_entity_attributes_using_delete

        deleteEntityAttributes  # noqa: E501
        """
        pass

    def test_delete_entity_attributes_using_delete1(self):
        """Test case for delete_entity_attributes_using_delete1

        deleteEntityAttributes  # noqa: E501
        """
        pass

    def test_delete_entity_timeseries_using_delete(self):
        """Test case for delete_entity_timeseries_using_delete

        deleteEntityTimeseries  # noqa: E501
        """
        pass

    def test_get_attribute_keys_by_scope_using_get(self):
        """Test case for get_attribute_keys_by_scope_using_get

        getAttributeKeysByScope  # noqa: E501
        """
        pass

    def test_get_attribute_keys_using_get(self):
        """Test case for get_attribute_keys_using_get

        getAttributeKeys  # noqa: E501
        """
        pass

    def test_get_attributes_by_scope_using_get(self):
        """Test case for get_attributes_by_scope_using_get

        getAttributesByScope  # noqa: E501
        """
        pass

    def test_get_attributes_using_get(self):
        """Test case for get_attributes_using_get

        getAttributes  # noqa: E501
        """
        pass

    def test_get_latest_timeseries_using_get(self):
        """Test case for get_latest_timeseries_using_get

        getLatestTimeseries  # noqa: E501
        """
        pass

    def test_get_timeseries_keys_using_get(self):
        """Test case for get_timeseries_keys_using_get

        getTimeseriesKeys  # noqa: E501
        """
        pass

    def test_get_timeseries_using_get(self):
        """Test case for get_timeseries_using_get

        getTimeseries  # noqa: E501
        """
        pass

    def test_save_device_attributes_using_post(self):
        """Test case for save_device_attributes_using_post

        saveDeviceAttributes  # noqa: E501
        """
        pass

    def test_save_entity_attributes_v1_using_post(self):
        """Test case for save_entity_attributes_v1_using_post

        saveEntityAttributesV1  # noqa: E501
        """
        pass

    def test_save_entity_attributes_v2_using_post(self):
        """Test case for save_entity_attributes_v2_using_post

        saveEntityAttributesV2  # noqa: E501
        """
        pass

    def test_save_entity_telemetry_using_post(self):
        """Test case for save_entity_telemetry_using_post

        saveEntityTelemetry  # noqa: E501
        """
        pass

    def test_save_entity_telemetry_with_ttl_using_post(self):
        """Test case for save_entity_telemetry_with_ttl_using_post

        saveEntityTelemetryWithTTL  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
