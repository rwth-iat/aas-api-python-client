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

import aas_api_python_client
from aas_api_python_client.api.submodel_repository_api_api import SubmodelRepositoryAPIApi  # noqa: E501
from aas_api_python_client.rest import ApiException


class TestSubmodelRepositoryAPIApi(unittest.TestCase):
    """SubmodelRepositoryAPIApi unit test stubs"""

    def setUp(self):
        self.api = SubmodelRepositoryAPIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_file_by_path_submodel_repo(self):
        """Test case for delete_file_by_path_submodel_repo

        Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy  # noqa: E501
        """
        pass

    def test_delete_submodel_by_id(self):
        """Test case for delete_submodel_by_id

        Deletes a Submodel  # noqa: E501
        """
        pass

    def test_delete_submodel_element_by_path_submodel_repo(self):
        """Test case for delete_submodel_element_by_path_submodel_repo

        Deletes a submodel element at a specified path within the submodel elements hierarchy  # noqa: E501
        """
        pass

    def test_get_all_submodel_elements_metadata_submodel_repository(self):
        """Test case for get_all_submodel_elements_metadata_submodel_repository

        Returns the metadata attributes of all submodel elements including their hierarchy  # noqa: E501
        """
        pass

    def test_get_all_submodel_elements_path_submodel_repo(self):
        """Test case for get_all_submodel_elements_path_submodel_repo

        Returns all submodel elements including their hierarchy in the Path notation  # noqa: E501
        """
        pass

    def test_get_all_submodel_elements_reference_submodel_repo(self):
        """Test case for get_all_submodel_elements_reference_submodel_repo

        Returns the References of all submodel elements  # noqa: E501
        """
        pass

    def test_get_all_submodel_elements_submodel_repository(self):
        """Test case for get_all_submodel_elements_submodel_repository

        Returns all submodel elements including their hierarchy  # noqa: E501
        """
        pass

    def test_get_all_submodel_elements_value_only_submodel_repo(self):
        """Test case for get_all_submodel_elements_value_only_submodel_repo

        Returns all submodel elements including their hierarchy in the ValueOnly representation  # noqa: E501
        """
        pass

    def test_get_all_submodels(self):
        """Test case for get_all_submodels

        Returns all Submodels  # noqa: E501
        """
        pass

    def test_get_all_submodels_metadata(self):
        """Test case for get_all_submodels_metadata

        Returns the metadata attributes of all Submodels  # noqa: E501
        """
        pass

    def test_get_all_submodels_path(self):
        """Test case for get_all_submodels_path

        Returns all Submodels in the Path notation  # noqa: E501
        """
        pass

    def test_get_all_submodels_reference(self):
        """Test case for get_all_submodels_reference

        Returns the References for all Submodels  # noqa: E501
        """
        pass

    def test_get_all_submodels_value_only(self):
        """Test case for get_all_submodels_value_only

        Returns all Submodels in their ValueOnly representation  # noqa: E501
        """
        pass

    def test_get_file_by_path_submodel_repo(self):
        """Test case for get_file_by_path_submodel_repo

        Downloads file content from a specific submodel element from the Submodel at a specified path  # noqa: E501
        """
        pass

    def test_get_operation_async_result_submodel_repo(self):
        """Test case for get_operation_async_result_submodel_repo

        Returns the Operation result of an asynchronous invoked Operation  # noqa: E501
        """
        pass

    def test_get_operation_async_result_value_only_submodel_repo(self):
        """Test case for get_operation_async_result_value_only_submodel_repo

        Returns the Operation result of an asynchronous invoked Operation  # noqa: E501
        """
        pass

    def test_get_operation_async_status_submodel_repo(self):
        """Test case for get_operation_async_status_submodel_repo

        Returns the Operation status of an asynchronous invoked Operation  # noqa: E501
        """
        pass

    def test_get_submodel_by_id(self):
        """Test case for get_submodel_by_id

        Returns a specific Submodel  # noqa: E501
        """
        pass

    def test_get_submodel_by_id_metadata(self):
        """Test case for get_submodel_by_id_metadata

        Returns the metadata attributes of a specific Submodel  # noqa: E501
        """
        pass

    def test_get_submodel_by_id_path(self):
        """Test case for get_submodel_by_id_path

        Returns a specific Submodel in the Path notation  # noqa: E501
        """
        pass

    def test_get_submodel_by_id_reference(self):
        """Test case for get_submodel_by_id_reference

        Returns the Reference of a specific Submodel  # noqa: E501
        """
        pass

    def test_get_submodel_by_id_value_only(self):
        """Test case for get_submodel_by_id_value_only

        Returns a specific Submodel in the ValueOnly representation  # noqa: E501
        """
        pass

    def test_get_submodel_element_by_path_metadata_submodel_repo(self):
        """Test case for get_submodel_element_by_path_metadata_submodel_repo

        Returns the matadata attributes of a specific submodel element from the Submodel at a specified path  # noqa: E501
        """
        pass

    def test_get_submodel_element_by_path_path_submodel_repo(self):
        """Test case for get_submodel_element_by_path_path_submodel_repo

        Returns a specific submodel element from the Submodel at a specified path in the Path notation  # noqa: E501
        """
        pass

    def test_get_submodel_element_by_path_reference_submodel_repo(self):
        """Test case for get_submodel_element_by_path_reference_submodel_repo

        Returns the Referene of a specific submodel element from the Submodel at a specified path  # noqa: E501
        """
        pass

    def test_get_submodel_element_by_path_submodel_repo(self):
        """Test case for get_submodel_element_by_path_submodel_repo

        Returns a specific submodel element from the Submodel at a specified path  # noqa: E501
        """
        pass

    def test_get_submodel_element_by_path_value_only_submodel_repo(self):
        """Test case for get_submodel_element_by_path_value_only_submodel_repo

        Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation  # noqa: E501
        """
        pass

    def test_invoke_operation_async_submodel_repo(self):
        """Test case for invoke_operation_async_submodel_repo

        Asynchronously invokes an Operation at a specified path  # noqa: E501
        """
        pass

    def test_invoke_operation_async_value_only_submodel_repo(self):
        """Test case for invoke_operation_async_value_only_submodel_repo

        Asynchronously invokes an Operation at a specified path  # noqa: E501
        """
        pass

    def test_invoke_operation_submodel_repo(self):
        """Test case for invoke_operation_submodel_repo

        Synchronously invokes an Operation at a specified path  # noqa: E501
        """
        pass

    def test_invoke_operation_value_only_submodel_repo(self):
        """Test case for invoke_operation_value_only_submodel_repo

        Synchronously invokes an Operation at a specified path  # noqa: E501
        """
        pass

    def test_patch_submodel_by_id(self):
        """Test case for patch_submodel_by_id

        Updates an existing Submodel  # noqa: E501
        """
        pass

    def test_patch_submodel_by_id_metadata(self):
        """Test case for patch_submodel_by_id_metadata

        Updates the metadata attributes of an existing Submodel  # noqa: E501
        """
        pass

    def test_patch_submodel_by_id_value_only(self):
        """Test case for patch_submodel_by_id_value_only

        Updates the values of an existing Submodel  # noqa: E501
        """
        pass

    def test_patch_submodel_element_by_path_metadata_submodel_repo(self):
        """Test case for patch_submodel_element_by_path_metadata_submodel_repo

        Updates the metadata attributes an existing SubmodelElement  # noqa: E501
        """
        pass

    def test_patch_submodel_element_by_path_submodel_repo(self):
        """Test case for patch_submodel_element_by_path_submodel_repo

        Updates an existing SubmodelElement  # noqa: E501
        """
        pass

    def test_patch_submodel_element_by_path_value_only_submodel_repo(self):
        """Test case for patch_submodel_element_by_path_value_only_submodel_repo

        Updates the value of an existing SubmodelElement  # noqa: E501
        """
        pass

    def test_post_submodel(self):
        """Test case for post_submodel

        Creates a new Submodel  # noqa: E501
        """
        pass

    def test_post_submodel_element_by_path_submodel_repo(self):
        """Test case for post_submodel_element_by_path_submodel_repo

        Creates a new submodel element at a specified path within submodel elements hierarchy  # noqa: E501
        """
        pass

    def test_post_submodel_element_submodel_repository(self):
        """Test case for post_submodel_element_submodel_repository

        Creates a new submodel element  # noqa: E501
        """
        pass

    def test_put_file_by_path_submodel_repo(self):
        """Test case for put_file_by_path_submodel_repo

        Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy  # noqa: E501
        """
        pass

    def test_put_submodel_by_id(self):
        """Test case for put_submodel_by_id

        Updates an existing Submodel  # noqa: E501
        """
        pass

    def test_put_submodel_element_by_path_submodel_repo(self):
        """Test case for put_submodel_element_by_path_submodel_repo

        Updates an existing submodel element at a specified path within submodel elements hierarchy  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()