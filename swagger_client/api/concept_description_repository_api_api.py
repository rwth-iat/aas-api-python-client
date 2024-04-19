# coding: utf-8

"""
    DotAAS Part 2 | HTTP/REST | Entire API Collection

    All APIs of the Specification of the [Specification of the Asset Administration Shell: Part 2](http://industrialdigitaltwin.org/en/content-hub) in one collection. Please not that this API is not intended to generate productive code but only for overview purposes.   Publisher: Industrial Digital Twin Association (IDTA) 2023\"  # noqa: E501

    OpenAPI spec version: V3.0.1
    Contact: info@idtwin.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ConceptDescriptionRepositoryAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_concept_description_by_id(self, cd_identifier, **kwargs):  # noqa: E501
        """Deletes a Concept Description  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_concept_description_by_id(cd_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cd_identifier: The Concept Description’s unique id (UTF8-BASE64-URL-encoded) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_concept_description_by_id_with_http_info(cd_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_concept_description_by_id_with_http_info(cd_identifier, **kwargs)  # noqa: E501
            return data

    def delete_concept_description_by_id_with_http_info(self, cd_identifier, **kwargs):  # noqa: E501
        """Deletes a Concept Description  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_concept_description_by_id_with_http_info(cd_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cd_identifier: The Concept Description’s unique id (UTF8-BASE64-URL-encoded) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cd_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_concept_description_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cd_identifier' is set
        if ('cd_identifier' not in params or
                params['cd_identifier'] is None):
            raise ValueError("Missing the required parameter `cd_identifier` when calling `delete_concept_description_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cd_identifier' in params:
            path_params['cdIdentifier'] = params['cd_identifier']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/concept-descriptions/{cdIdentifier}', 'DELETE',
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

    def get_all_concept_descriptions(self, **kwargs):  # noqa: E501
        """Returns all Concept Descriptions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_concept_descriptions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id_short: The Concept Description’s IdShort
        :param str is_case_of: IsCaseOf reference (UTF8-BASE64-URL-encoded)
        :param str data_specification_ref: DataSpecification reference (UTF8-BASE64-URL-encoded)
        :param int limit: The maximum number of elements in the response array
        :param str cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
        :return: GetConceptDescriptionsResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_concept_descriptions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_concept_descriptions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_concept_descriptions_with_http_info(self, **kwargs):  # noqa: E501
        """Returns all Concept Descriptions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_concept_descriptions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id_short: The Concept Description’s IdShort
        :param str is_case_of: IsCaseOf reference (UTF8-BASE64-URL-encoded)
        :param str data_specification_ref: DataSpecification reference (UTF8-BASE64-URL-encoded)
        :param int limit: The maximum number of elements in the response array
        :param str cursor: A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue
        :return: GetConceptDescriptionsResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_short', 'is_case_of', 'data_specification_ref', 'limit', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_concept_descriptions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id_short' in params:
            query_params.append(('idShort', params['id_short']))  # noqa: E501
        if 'is_case_of' in params:
            query_params.append(('isCaseOf', params['is_case_of']))  # noqa: E501
        if 'data_specification_ref' in params:
            query_params.append(('dataSpecificationRef', params['data_specification_ref']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/concept-descriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetConceptDescriptionsResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_concept_description_by_id(self, cd_identifier, **kwargs):  # noqa: E501
        """Returns a specific Concept Description  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_concept_description_by_id(cd_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cd_identifier: The Concept Description’s unique id (UTF8-BASE64-URL-encoded) (required)
        :return: ConceptDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_concept_description_by_id_with_http_info(cd_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_concept_description_by_id_with_http_info(cd_identifier, **kwargs)  # noqa: E501
            return data

    def get_concept_description_by_id_with_http_info(self, cd_identifier, **kwargs):  # noqa: E501
        """Returns a specific Concept Description  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_concept_description_by_id_with_http_info(cd_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cd_identifier: The Concept Description’s unique id (UTF8-BASE64-URL-encoded) (required)
        :return: ConceptDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cd_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_concept_description_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cd_identifier' is set
        if ('cd_identifier' not in params or
                params['cd_identifier'] is None):
            raise ValueError("Missing the required parameter `cd_identifier` when calling `get_concept_description_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cd_identifier' in params:
            path_params['cdIdentifier'] = params['cd_identifier']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/concept-descriptions/{cdIdentifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConceptDescription',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_concept_description(self, body, **kwargs):  # noqa: E501
        """Creates a new Concept Description  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_concept_description(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConceptDescription body: Concept Description object (required)
        :return: ConceptDescription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_concept_description_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_concept_description_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_concept_description_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates a new Concept Description  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_concept_description_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConceptDescription body: Concept Description object (required)
        :return: ConceptDescription
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
                    " to method post_concept_description" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_concept_description`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/concept-descriptions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConceptDescription',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_concept_description_by_id(self, body, cd_identifier, **kwargs):  # noqa: E501
        """Updates an existing Concept Description  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_concept_description_by_id(body, cd_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConceptDescription body: Concept Description object (required)
        :param str cd_identifier: The Concept Description’s unique id (UTF8-BASE64-URL-encoded) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_concept_description_by_id_with_http_info(body, cd_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.put_concept_description_by_id_with_http_info(body, cd_identifier, **kwargs)  # noqa: E501
            return data

    def put_concept_description_by_id_with_http_info(self, body, cd_identifier, **kwargs):  # noqa: E501
        """Updates an existing Concept Description  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_concept_description_by_id_with_http_info(body, cd_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConceptDescription body: Concept Description object (required)
        :param str cd_identifier: The Concept Description’s unique id (UTF8-BASE64-URL-encoded) (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'cd_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_concept_description_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_concept_description_by_id`")  # noqa: E501
        # verify the required parameter 'cd_identifier' is set
        if ('cd_identifier' not in params or
                params['cd_identifier'] is None):
            raise ValueError("Missing the required parameter `cd_identifier` when calling `put_concept_description_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cd_identifier' in params:
            path_params['cdIdentifier'] = params['cd_identifier']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/concept-descriptions/{cdIdentifier}', 'PUT',
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
