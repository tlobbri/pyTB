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
from api.component_descriptor_controller_api import ComponentDescriptorControllerApi  # noqa: E501
from pyTB.rest import ApiException


class TestComponentDescriptorControllerApi(unittest.TestCase):
    """ComponentDescriptorControllerApi unit test stubs"""

    def setUp(self):
        self.api = api.component_descriptor_controller_api.ComponentDescriptorControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_component_descriptor_by_clazz_using_get(self):
        """Test case for get_component_descriptor_by_clazz_using_get

        getComponentDescriptorByClazz  # noqa: E501
        """
        pass

    def test_get_component_descriptors_by_type_using_get(self):
        """Test case for get_component_descriptors_by_type_using_get

        getComponentDescriptorsByType  # noqa: E501
        """
        pass

    def test_get_component_descriptors_by_types_using_get(self):
        """Test case for get_component_descriptors_by_types_using_get

        getComponentDescriptorsByTypes  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
