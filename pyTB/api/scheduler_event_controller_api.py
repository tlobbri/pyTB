# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pyTB.api_client import ApiClient


class SchedulerEventControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_scheduler_event_using_delete(self, scheduler_event_id, **kwargs):  # noqa: E501
        """deleteSchedulerEvent  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_scheduler_event_using_delete(scheduler_event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scheduler_event_id: schedulerEventId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_scheduler_event_using_delete_with_http_info(scheduler_event_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_scheduler_event_using_delete_with_http_info(scheduler_event_id, **kwargs)  # noqa: E501
            return data

    def delete_scheduler_event_using_delete_with_http_info(self, scheduler_event_id, **kwargs):  # noqa: E501
        """deleteSchedulerEvent  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_scheduler_event_using_delete_with_http_info(scheduler_event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scheduler_event_id: schedulerEventId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scheduler_event_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_scheduler_event_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scheduler_event_id' is set
        if ('scheduler_event_id' not in params or
                params['scheduler_event_id'] is None):
            raise ValueError("Missing the required parameter `scheduler_event_id` when calling `delete_scheduler_event_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scheduler_event_id' in params:
            path_params['schedulerEventId'] = params['scheduler_event_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/schedulerEvent/{schedulerEventId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_scheduler_event_by_id_using_get(self, scheduler_event_id, **kwargs):  # noqa: E501
        """getSchedulerEventById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scheduler_event_by_id_using_get(scheduler_event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scheduler_event_id: schedulerEventId (required)
        :return: SchedulerEvent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_scheduler_event_by_id_using_get_with_http_info(scheduler_event_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_scheduler_event_by_id_using_get_with_http_info(scheduler_event_id, **kwargs)  # noqa: E501
            return data

    def get_scheduler_event_by_id_using_get_with_http_info(self, scheduler_event_id, **kwargs):  # noqa: E501
        """getSchedulerEventById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scheduler_event_by_id_using_get_with_http_info(scheduler_event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scheduler_event_id: schedulerEventId (required)
        :return: SchedulerEvent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scheduler_event_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scheduler_event_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scheduler_event_id' is set
        if ('scheduler_event_id' not in params or
                params['scheduler_event_id'] is None):
            raise ValueError("Missing the required parameter `scheduler_event_id` when calling `get_scheduler_event_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scheduler_event_id' in params:
            path_params['schedulerEventId'] = params['scheduler_event_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/schedulerEvent/{schedulerEventId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SchedulerEvent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_scheduler_event_info_by_id_using_get(self, scheduler_event_id, **kwargs):  # noqa: E501
        """getSchedulerEventInfoById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scheduler_event_info_by_id_using_get(scheduler_event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scheduler_event_id: schedulerEventId (required)
        :return: SchedulerEventInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_scheduler_event_info_by_id_using_get_with_http_info(scheduler_event_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_scheduler_event_info_by_id_using_get_with_http_info(scheduler_event_id, **kwargs)  # noqa: E501
            return data

    def get_scheduler_event_info_by_id_using_get_with_http_info(self, scheduler_event_id, **kwargs):  # noqa: E501
        """getSchedulerEventInfoById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scheduler_event_info_by_id_using_get_with_http_info(scheduler_event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scheduler_event_id: schedulerEventId (required)
        :return: SchedulerEventInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scheduler_event_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scheduler_event_info_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scheduler_event_id' is set
        if ('scheduler_event_id' not in params or
                params['scheduler_event_id'] is None):
            raise ValueError("Missing the required parameter `scheduler_event_id` when calling `get_scheduler_event_info_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scheduler_event_id' in params:
            path_params['schedulerEventId'] = params['scheduler_event_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/schedulerEvent/info/{schedulerEventId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SchedulerEventInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_scheduler_events_by_ids_using_get(self, scheduler_event_ids, **kwargs):  # noqa: E501
        """getSchedulerEventsByIds  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scheduler_events_by_ids_using_get(scheduler_event_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scheduler_event_ids: schedulerEventIds (required)
        :return: list[SchedulerEventInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_scheduler_events_by_ids_using_get_with_http_info(scheduler_event_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.get_scheduler_events_by_ids_using_get_with_http_info(scheduler_event_ids, **kwargs)  # noqa: E501
            return data

    def get_scheduler_events_by_ids_using_get_with_http_info(self, scheduler_event_ids, **kwargs):  # noqa: E501
        """getSchedulerEventsByIds  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scheduler_events_by_ids_using_get_with_http_info(scheduler_event_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scheduler_event_ids: schedulerEventIds (required)
        :return: list[SchedulerEventInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scheduler_event_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scheduler_events_by_ids_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scheduler_event_ids' is set
        if ('scheduler_event_ids' not in params or
                params['scheduler_event_ids'] is None):
            raise ValueError("Missing the required parameter `scheduler_event_ids` when calling `get_scheduler_events_by_ids_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scheduler_event_ids' in params:
            query_params.append(('schedulerEventIds', params['scheduler_event_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/schedulerEvents{?schedulerEventIds}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SchedulerEventInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_scheduler_events_using_get(self, **kwargs):  # noqa: E501
        """getSchedulerEvents  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scheduler_events_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: type
        :return: list[SchedulerEventInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_scheduler_events_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_scheduler_events_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_scheduler_events_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """getSchedulerEvents  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scheduler_events_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: type
        :return: list[SchedulerEventInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scheduler_events_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/schedulerEvents{?type}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SchedulerEventInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_scheduler_event_using_post(self, body, **kwargs):  # noqa: E501
        """saveSchedulerEvent  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_scheduler_event_using_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SchedulerEvent body: schedulerEvent (required)
        :return: SchedulerEvent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_scheduler_event_using_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.save_scheduler_event_using_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def save_scheduler_event_using_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """saveSchedulerEvent  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_scheduler_event_using_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SchedulerEvent body: schedulerEvent (required)
        :return: SchedulerEvent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_scheduler_event_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `save_scheduler_event_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/schedulerEvent', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SchedulerEvent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
