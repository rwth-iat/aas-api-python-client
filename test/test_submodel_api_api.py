# coding: utf-8

"""
    DotAAS Part 2 | HTTP/REST | Entire API Collection

    All APIs of the Specification of the [Specification of the Asset Administration Shell: Part 2](http://industrialdigitaltwin.org/en/content-hub) in one collection. Please not that this API is not intended to generate productive code but only for overview purposes.   Publisher: Industrial Digital Twin Association (IDTA) 2023\"  # noqa: E501

    OpenAPI spec version: V3.0.1
    Contact: info@idtwin.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.submodel_api_api import SubmodelAPIApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSubmodelAPIApi(unittest.TestCase):
    """SubmodelAPIApi unit test stubs"""

    def setUp(self):
        self.api = SubmodelAPIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_file_by_path(self):
        """Test case for delete_file_by_path

        Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy  # noqa: E501
        """
        pass

    def test_delete_submodel_element_by_path(self):
        """Test case for delete_submodel_element_by_path

        Deletes a submodel element at a specified path within the submodel elements hierarchy  # noqa: E501
        """
        pass

    def test_get_all_submodel_elements(self):
        """Test case for get_all_submodel_elements

        Returns all submodel elements including their hierarchy  # noqa: E501
        """
        pass

    def test_get_all_submodel_elements_metadata(self):
        """Test case for get_all_submodel_elements_metadata

        Returns the metadata attributes of all submodel elements including their hierarchy  # noqa: E501
        """
        pass

    def test_get_all_submodel_elements_path(self):
        """Test case for get_all_submodel_elements_path

        Returns all submodel elements including their hierarchy in the Path notation  # noqa: E501
        """
        pass

    def test_get_all_submodel_elements_reference(self):
        """Test case for get_all_submodel_elements_reference

        Returns the References of all submodel elements  # noqa: E501
        """
        pass

    def test_get_all_submodel_elements_value_only(self):
        """Test case for get_all_submodel_elements_value_only

        Returns all submodel elements including their hierarchy in the ValueOnly representation  # noqa: E501
        """
        pass

    def test_get_file_by_path(self):
        """Test case for get_file_by_path

        Downloads file content from a specific submodel element from the Submodel at a specified path  # noqa: E501
        """
        pass

    def test_get_operation_async_result(self):
        """Test case for get_operation_async_result

        Returns the Operation result of an asynchronous invoked Operation  # noqa: E501
        """
        pass

    def test_get_operation_async_result_value_only(self):
        """Test case for get_operation_async_result_value_only

        Returns the value of the Operation result of an asynchronous invoked Operation  # noqa: E501
        """
        pass

    def test_get_operation_async_status(self):
        """Test case for get_operation_async_status

        Returns the Operation status of an asynchronous invoked Operation  # noqa: E501
        """
        pass

    def test_get_submodel(self):
        """Test case for get_submodel

        Returns the Submodel  # noqa: E501
        """
        pass

    def test_get_submodel_element_by_path(self):
        """Test case for get_submodel_element_by_path

        Returns a specific submodel element from the Submodel at a specified path  # noqa: E501
        """
        pass

    def test_get_submodel_element_by_path_metadata(self):
        """Test case for get_submodel_element_by_path_metadata

        Returns the matadata attributes of a specific submodel element from the Submodel at a specified path  # noqa: E501
        """
        pass

    def test_get_submodel_element_by_path_path(self):
        """Test case for get_submodel_element_by_path_path

        Returns a specific submodel element from the Submodel at a specified path in the Path notation  # noqa: E501
        """
        pass

    def test_get_submodel_element_by_path_reference(self):
        """Test case for get_submodel_element_by_path_reference

        Returns the Referene of a specific submodel element from the Submodel at a specified path  # noqa: E501
        """
        pass

    def test_get_submodel_element_by_path_value_only(self):
        """Test case for get_submodel_element_by_path_value_only

        Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation  # noqa: E501
        """
        pass

    def test_get_submodel_metadata(self):
        """Test case for get_submodel_metadata

        Returns the metadata attributes of a specific Submodel  # noqa: E501
        """
        pass

    def test_get_submodel_path(self):
        """Test case for get_submodel_path

        Returns the Submodel in the Path notation  # noqa: E501
        """
        pass

    def test_get_submodel_reference(self):
        """Test case for get_submodel_reference

        Returns the Reference of the Submodel  # noqa: E501
        """
        pass

    def test_get_submodel_value_only(self):
        """Test case for get_submodel_value_only

        Returns the Submodel in the ValueOnly representation  # noqa: E501
        """
        pass

    def test_invoke_operation(self):
        """Test case for invoke_operation

        Synchronously invokes an Operation at a specified path  # noqa: E501
        """
        pass

    def test_invoke_operation_async(self):
        """Test case for invoke_operation_async

        Asynchronously invokes an Operation at a specified path  # noqa: E501
        """
        pass

    def test_invoke_operation_async_value_only(self):
        """Test case for invoke_operation_async_value_only

        Asynchronously invokes an Operation at a specified path  # noqa: E501
        """
        pass

    def test_invoke_operation_sync_value_only(self):
        """Test case for invoke_operation_sync_value_only

        Synchronously invokes an Operation at a specified path  # noqa: E501
        """
        pass

    def test_patch_submodel(self):
        """Test case for patch_submodel

        Updates the Submodel  # noqa: E501
        """
        pass

    def test_patch_submodel_element_by_path(self):
        """Test case for patch_submodel_element_by_path

        Updates an existing SubmodelElement  # noqa: E501
        """
        pass

    def test_patch_submodel_element_by_path_metadata(self):
        """Test case for patch_submodel_element_by_path_metadata

        Updates the metadata attributes an existing SubmodelElement  # noqa: E501
        """
        pass

    def test_patch_submodel_element_by_path_value_only(self):
        """Test case for patch_submodel_element_by_path_value_only

        Updates the value of an existing SubmodelElement  # noqa: E501
        """
        pass

    def test_patch_submodel_metadata(self):
        """Test case for patch_submodel_metadata

        Updates the metadata attributes of the Submodel  # noqa: E501
        """
        pass

    def test_patch_submodel_value_only(self):
        """Test case for patch_submodel_value_only

        Updates the values of the Submodel  # noqa: E501
        """
        pass

    def test_post_submodel_element(self):
        """Test case for post_submodel_element

        Creates a new submodel element  # noqa: E501
        """
        pass

    def test_post_submodel_element_by_path(self):
        """Test case for post_submodel_element_by_path

        Creates a new submodel element at a specified path within submodel elements hierarchy  # noqa: E501
        """
        pass

    def test_put_file_by_path(self):
        """Test case for put_file_by_path

        Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy  # noqa: E501
        """
        pass

    def test_put_submodel(self):
        """Test case for put_submodel

        Updates the Submodel  # noqa: E501
        """
        pass

    def test_put_submodel_element_by_path(self):
        """Test case for put_submodel_element_by_path

        Updates an existing submodel element at a specified path within submodel elements hierarchy  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
