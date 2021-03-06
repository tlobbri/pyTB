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
from api.scheduler_event_controller_api import SchedulerEventControllerApi  # noqa: E501
from pyTB.rest import ApiException


class TestSchedulerEventControllerApi(unittest.TestCase):
    """SchedulerEventControllerApi unit test stubs"""

    def setUp(self):
        self.api = api.scheduler_event_controller_api.SchedulerEventControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_scheduler_event_using_delete(self):
        """Test case for delete_scheduler_event_using_delete

        deleteSchedulerEvent  # noqa: E501
        """
        pass

    def test_get_scheduler_event_by_id_using_get(self):
        """Test case for get_scheduler_event_by_id_using_get

        getSchedulerEventById  # noqa: E501
        """
        pass

    def test_get_scheduler_event_info_by_id_using_get(self):
        """Test case for get_scheduler_event_info_by_id_using_get

        getSchedulerEventInfoById  # noqa: E501
        """
        pass

    def test_get_scheduler_events_by_ids_using_get(self):
        """Test case for get_scheduler_events_by_ids_using_get

        getSchedulerEventsByIds  # noqa: E501
        """
        pass

    def test_get_scheduler_events_using_get(self):
        """Test case for get_scheduler_events_using_get

        getSchedulerEvents  # noqa: E501
        """
        pass

    def test_save_scheduler_event_using_post(self):
        """Test case for save_scheduler_event_using_post

        saveSchedulerEvent  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
