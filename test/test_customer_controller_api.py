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
from api.customer_controller_api import CustomerControllerApi  # noqa: E501
from pyTB.rest import ApiException


class TestCustomerControllerApi(unittest.TestCase):
    """CustomerControllerApi unit test stubs"""

    def setUp(self):
        self.api = api.customer_controller_api.CustomerControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_customer_using_delete(self):
        """Test case for delete_customer_using_delete

        deleteCustomer  # noqa: E501
        """
        pass

    def test_get_customer_by_id_using_get(self):
        """Test case for get_customer_by_id_using_get

        getCustomerById  # noqa: E501
        """
        pass

    def test_get_customer_title_by_id_using_get(self):
        """Test case for get_customer_title_by_id_using_get

        getCustomerTitleById  # noqa: E501
        """
        pass

    def test_get_customers_by_entity_group_id_using_get(self):
        """Test case for get_customers_by_entity_group_id_using_get

        getCustomersByEntityGroupId  # noqa: E501
        """
        pass

    def test_get_customers_by_ids_using_get(self):
        """Test case for get_customers_by_ids_using_get

        getCustomersByIds  # noqa: E501
        """
        pass

    def test_get_customers_using_get(self):
        """Test case for get_customers_using_get

        getCustomers  # noqa: E501
        """
        pass

    def test_get_short_customer_info_by_id_using_get(self):
        """Test case for get_short_customer_info_by_id_using_get

        getShortCustomerInfoById  # noqa: E501
        """
        pass

    def test_get_tenant_customer_using_get(self):
        """Test case for get_tenant_customer_using_get

        getTenantCustomer  # noqa: E501
        """
        pass

    def test_get_user_customers_using_get(self):
        """Test case for get_user_customers_using_get

        getUserCustomers  # noqa: E501
        """
        pass

    def test_save_customer_using_post(self):
        """Test case for save_customer_using_post

        saveCustomer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
