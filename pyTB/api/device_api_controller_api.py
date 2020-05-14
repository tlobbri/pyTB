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


class DeviceApiControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def claim_device_using_post(self, device_token, **kwargs):  # noqa: E501
        """claimDevice  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.claim_device_using_post(device_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_token: deviceToken (required)
        :param str body: json
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.claim_device_using_post_with_http_info(device_token, **kwargs)  # noqa: E501
        else:
            (data) = self.claim_device_using_post_with_http_info(device_token, **kwargs)  # noqa: E501
            return data

    def claim_device_using_post_with_http_info(self, device_token, **kwargs):  # noqa: E501
        """claimDevice  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.claim_device_using_post_with_http_info(device_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_token: deviceToken (required)
        :param str body: json
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_token', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method claim_device_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_token' is set
        if ('device_token' not in params or
                params['device_token'] is None):
            raise ValueError("Missing the required parameter `device_token` when calling `claim_device_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_token' in params:
            path_params['deviceToken'] = params['device_token']  # noqa: E501

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
            '/api/v1/{deviceToken}/claim', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_device_attributes_using_get(self, device_token, **kwargs):  # noqa: E501
        """getDeviceAttributes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_attributes_using_get(device_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_token: deviceToken (required)
        :param str client_keys: clientKeys
        :param str shared_keys: sharedKeys
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_device_attributes_using_get_with_http_info(device_token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_device_attributes_using_get_with_http_info(device_token, **kwargs)  # noqa: E501
            return data

    def get_device_attributes_using_get_with_http_info(self, device_token, **kwargs):  # noqa: E501
        """getDeviceAttributes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_attributes_using_get_with_http_info(device_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_token: deviceToken (required)
        :param str client_keys: clientKeys
        :param str shared_keys: sharedKeys
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_token', 'client_keys', 'shared_keys']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_device_attributes_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_token' is set
        if ('device_token' not in params or
                params['device_token'] is None):
            raise ValueError("Missing the required parameter `device_token` when calling `get_device_attributes_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_token' in params:
            path_params['deviceToken'] = params['device_token']  # noqa: E501

        query_params = []
        if 'client_keys' in params:
            query_params.append(('clientKeys', params['client_keys']))  # noqa: E501
        if 'shared_keys' in params:
            query_params.append(('sharedKeys', params['shared_keys']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/{deviceToken}/attributes{?clientKeys,sharedKeys}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_device_attributes_using_post(self, body, device_token, **kwargs):  # noqa: E501
        """postDeviceAttributes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_device_attributes_using_post(body, device_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: json (required)
        :param str device_token: deviceToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_device_attributes_using_post_with_http_info(body, device_token, **kwargs)  # noqa: E501
        else:
            (data) = self.post_device_attributes_using_post_with_http_info(body, device_token, **kwargs)  # noqa: E501
            return data

    def post_device_attributes_using_post_with_http_info(self, body, device_token, **kwargs):  # noqa: E501
        """postDeviceAttributes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_device_attributes_using_post_with_http_info(body, device_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: json (required)
        :param str device_token: deviceToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'device_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_device_attributes_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_device_attributes_using_post`")  # noqa: E501
        # verify the required parameter 'device_token' is set
        if ('device_token' not in params or
                params['device_token'] is None):
            raise ValueError("Missing the required parameter `device_token` when calling `post_device_attributes_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_token' in params:
            path_params['deviceToken'] = params['device_token']  # noqa: E501

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
            '/api/v1/{deviceToken}/attributes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_rpc_request_using_post(self, body, device_token, **kwargs):  # noqa: E501
        """postRpcRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_rpc_request_using_post(body, device_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: json (required)
        :param str device_token: deviceToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_rpc_request_using_post_with_http_info(body, device_token, **kwargs)  # noqa: E501
        else:
            (data) = self.post_rpc_request_using_post_with_http_info(body, device_token, **kwargs)  # noqa: E501
            return data

    def post_rpc_request_using_post_with_http_info(self, body, device_token, **kwargs):  # noqa: E501
        """postRpcRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_rpc_request_using_post_with_http_info(body, device_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: json (required)
        :param str device_token: deviceToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'device_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_rpc_request_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_rpc_request_using_post`")  # noqa: E501
        # verify the required parameter 'device_token' is set
        if ('device_token' not in params or
                params['device_token'] is None):
            raise ValueError("Missing the required parameter `device_token` when calling `post_rpc_request_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_token' in params:
            path_params['deviceToken'] = params['device_token']  # noqa: E501

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
            '/api/v1/{deviceToken}/rpc', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_telemetry_using_post(self, body, device_token, **kwargs):  # noqa: E501
        """postTelemetry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_telemetry_using_post(body, device_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: json (required)
        :param str device_token: deviceToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_telemetry_using_post_with_http_info(body, device_token, **kwargs)  # noqa: E501
        else:
            (data) = self.post_telemetry_using_post_with_http_info(body, device_token, **kwargs)  # noqa: E501
            return data

    def post_telemetry_using_post_with_http_info(self, body, device_token, **kwargs):  # noqa: E501
        """postTelemetry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_telemetry_using_post_with_http_info(body, device_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: json (required)
        :param str device_token: deviceToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'device_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_telemetry_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_telemetry_using_post`")  # noqa: E501
        # verify the required parameter 'device_token' is set
        if ('device_token' not in params or
                params['device_token'] is None):
            raise ValueError("Missing the required parameter `device_token` when calling `post_telemetry_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_token' in params:
            path_params['deviceToken'] = params['device_token']  # noqa: E501

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
            '/api/v1/{deviceToken}/telemetry', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reply_to_command_using_post(self, body, device_token, request_id, **kwargs):  # noqa: E501
        """replyToCommand  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reply_to_command_using_post(body, device_token, request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: json (required)
        :param str device_token: deviceToken (required)
        :param int request_id: requestId (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reply_to_command_using_post_with_http_info(body, device_token, request_id, **kwargs)  # noqa: E501
        else:
            (data) = self.reply_to_command_using_post_with_http_info(body, device_token, request_id, **kwargs)  # noqa: E501
            return data

    def reply_to_command_using_post_with_http_info(self, body, device_token, request_id, **kwargs):  # noqa: E501
        """replyToCommand  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reply_to_command_using_post_with_http_info(body, device_token, request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: json (required)
        :param str device_token: deviceToken (required)
        :param int request_id: requestId (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'device_token', 'request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reply_to_command_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `reply_to_command_using_post`")  # noqa: E501
        # verify the required parameter 'device_token' is set
        if ('device_token' not in params or
                params['device_token'] is None):
            raise ValueError("Missing the required parameter `device_token` when calling `reply_to_command_using_post`")  # noqa: E501
        # verify the required parameter 'request_id' is set
        if ('request_id' not in params or
                params['request_id'] is None):
            raise ValueError("Missing the required parameter `request_id` when calling `reply_to_command_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_token' in params:
            path_params['deviceToken'] = params['device_token']  # noqa: E501
        if 'request_id' in params:
            path_params['requestId'] = params['request_id']  # noqa: E501

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
            '/api/v1/{deviceToken}/rpc/{requestId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def subscribe_to_attributes_using_get(self, device_token, **kwargs):  # noqa: E501
        """subscribeToAttributes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subscribe_to_attributes_using_get(device_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_token: deviceToken (required)
        :param int timeout: timeout
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.subscribe_to_attributes_using_get_with_http_info(device_token, **kwargs)  # noqa: E501
        else:
            (data) = self.subscribe_to_attributes_using_get_with_http_info(device_token, **kwargs)  # noqa: E501
            return data

    def subscribe_to_attributes_using_get_with_http_info(self, device_token, **kwargs):  # noqa: E501
        """subscribeToAttributes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subscribe_to_attributes_using_get_with_http_info(device_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_token: deviceToken (required)
        :param int timeout: timeout
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_token', 'timeout']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscribe_to_attributes_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_token' is set
        if ('device_token' not in params or
                params['device_token'] is None):
            raise ValueError("Missing the required parameter `device_token` when calling `subscribe_to_attributes_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_token' in params:
            path_params['deviceToken'] = params['device_token']  # noqa: E501

        query_params = []
        if 'timeout' in params:
            query_params.append(('timeout', params['timeout']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/{deviceToken}/attributes/updates{?timeout}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def subscribe_to_commands_using_get(self, device_token, **kwargs):  # noqa: E501
        """subscribeToCommands  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subscribe_to_commands_using_get(device_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_token: deviceToken (required)
        :param int timeout: timeout
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.subscribe_to_commands_using_get_with_http_info(device_token, **kwargs)  # noqa: E501
        else:
            (data) = self.subscribe_to_commands_using_get_with_http_info(device_token, **kwargs)  # noqa: E501
            return data

    def subscribe_to_commands_using_get_with_http_info(self, device_token, **kwargs):  # noqa: E501
        """subscribeToCommands  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.subscribe_to_commands_using_get_with_http_info(device_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_token: deviceToken (required)
        :param int timeout: timeout
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_token', 'timeout']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscribe_to_commands_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_token' is set
        if ('device_token' not in params or
                params['device_token'] is None):
            raise ValueError("Missing the required parameter `device_token` when calling `subscribe_to_commands_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_token' in params:
            path_params['deviceToken'] = params['device_token']  # noqa: E501

        query_params = []
        if 'timeout' in params:
            query_params.append(('timeout', params['timeout']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/{deviceToken}/rpc{?timeout}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)