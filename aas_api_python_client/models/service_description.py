# coding: utf-8

"""
    DotAAS Part 2 | HTTP/REST | Entire API Collection

    All APIs of the Specification of the [Specification of the Asset Administration Shell: Part 2](http://industrialdigitaltwin.org/en/content-hub) in one collection. Please not that this API is not intended to generate productive code but only for overview purposes.   Publisher: Industrial Digital Twin Association (IDTA) 2023\"  # noqa: E501

    OpenAPI spec version: V3.0.1
    Contact: info@idtwin.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ServiceDescription(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'profiles': 'list[str]'
    }

    attribute_map = {
        'profiles': 'profiles'
    }

    def __init__(self, profiles=None):  # noqa: E501
        """ServiceDescription - a model defined in Swagger"""  # noqa: E501
        self._profiles = None
        self.discriminator = None
        if profiles is not None:
            self.profiles = profiles

    @property
    def profiles(self):
        """Gets the profiles of this ServiceDescription.  # noqa: E501


        :return: The profiles of this ServiceDescription.  # noqa: E501
        :rtype: list[str]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """Sets the profiles of this ServiceDescription.


        :param profiles: The profiles of this ServiceDescription.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["https://admin-shell.io/aas/API/3/0/AssetAdministrationShellServiceSpecification/SSP-001", "https://admin-shell.io/aas/API/3/0/AssetAdministrationShellServiceSpecification/SSP-002", "https://admin-shell.io/aas/API/3/0/SubmodelServiceSpecification/SSP-001", "https://admin-shell.io/aas/API/3/0/SubmodelServiceSpecification/SSP-002", "https://admin-shell.io/aas/API/3/0/SubmodelServiceSpecification/SSP-003", "https://admin-shell.io/aas/API/3/0/AasxFileServerServiceSpecification/SSP-001", "https://admin-shell.io/aas/API/3/0/AssetAdministrationShellRegistryServiceSpecification/SSP-001", "https://admin-shell.io/aas/API/3/0/AssetAdministrationShellRegistryServiceSpecification/SSP-002", "https://admin-shell.io/aas/API/3/0/SubmodelRegistryServiceSpecification/SSP-001", "https://admin-shell.io/aas/API/3/0/SubmodelRegistryServiceSpecification/SSP-002", "https://admin-shell.io/aas/API/3/0/DiscoveryServiceSpecification/SSP-001", "https://admin-shell.io/aas/API/3/0/AssetAdministrationShellRepositoryServiceSpecification/SSP-001", "https://admin-shell.io/aas/API/3/0/AssetAdministrationShellRepositoryServiceSpecification/SSP-002", "https://admin-shell.io/aas/API/3/0/SubmodelRepositoryServiceSpecification/SSP-001", "https://admin-shell.io/aas/API/3/0/SubmodelRepositoryServiceSpecification/SSP-002", "https://admin-shell.io/aas/API/3/0/SubmodelRepositoryServiceSpecification/SSP-003", "https://admin-shell.io/aas/API/3/0/SubmodelRepositoryServiceSpecification/SSP-004", "https://admin-shell.io/aas/API/3/0/ConceptDescriptionServiceSpecification/SSP-001"]  # noqa: E501
        if not set(profiles).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `profiles` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(profiles) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._profiles = profiles

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ServiceDescription, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServiceDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
