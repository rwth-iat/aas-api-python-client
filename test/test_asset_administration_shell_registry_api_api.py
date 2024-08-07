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

import aas_python_http_client
from aas_python_http_client.api.asset_administration_shell_registry_api_api import AssetAdministrationShellRegistryAPIApi  # noqa: E501
from aas_python_http_client.rest import ApiException


class TestAssetAdministrationShellRegistryAPIApi(unittest.TestCase):
    """AssetAdministrationShellRegistryAPIApi unit test stubs"""

    def setUp(self):
        self.api = AssetAdministrationShellRegistryAPIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_asset_administration_shell_descriptor_by_id(self):
        """Test case for delete_asset_administration_shell_descriptor_by_id

        Deletes an Asset Administration Shell Descriptor, i.e. de-registers an AAS  # noqa: E501
        """
        pass

    def test_delete_submodel_descriptor_by_id_through_superpath(self):
        """Test case for delete_submodel_descriptor_by_id_through_superpath

        Deletes a Submodel Descriptor, i.e. de-registers a submodel  # noqa: E501
        """
        pass

    def test_get_all_asset_administration_shell_descriptors(self):
        """Test case for get_all_asset_administration_shell_descriptors

        Returns all Asset Administration Shell Descriptors  # noqa: E501
        """
        pass

    def test_get_all_submodel_descriptors_through_superpath(self):
        """Test case for get_all_submodel_descriptors_through_superpath

        Returns all Submodel Descriptors  # noqa: E501
        """
        pass

    def test_get_asset_administration_shell_descriptor_by_id(self):
        """Test case for get_asset_administration_shell_descriptor_by_id

        Returns a specific Asset Administration Shell Descriptor  # noqa: E501
        """
        pass

    def test_get_submodel_descriptor_by_id_through_superpath(self):
        """Test case for get_submodel_descriptor_by_id_through_superpath

        Returns a specific Submodel Descriptor  # noqa: E501
        """
        pass

    def test_post_asset_administration_shell_descriptor(self):
        """Test case for post_asset_administration_shell_descriptor

        Creates a new Asset Administration Shell Descriptor, i.e. registers an AAS  # noqa: E501
        """
        pass

    def test_post_submodel_descriptor_through_superpath(self):
        """Test case for post_submodel_descriptor_through_superpath

        Creates a new Submodel Descriptor, i.e. registers a submodel  # noqa: E501
        """
        pass

    def test_put_asset_administration_shell_descriptor_by_id(self):
        """Test case for put_asset_administration_shell_descriptor_by_id

        Updates an existing Asset Administration Shell Descriptor  # noqa: E501
        """
        pass

    def test_put_submodel_descriptor_by_id_through_superpath(self):
        """Test case for put_submodel_descriptor_by_id_through_superpath

        Updates an existing Submodel Descriptor  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
