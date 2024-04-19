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
from swagger_client.models.identifiable import Identifiable  # noqa: F401,E501

class Submodel(Identifiable):
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
        'kind': 'ModellingKind',
        'semantic_id': 'Reference',
        'supplemental_semantic_ids': 'list[Reference]',
        'qualifiers': 'list[Qualifier]',
        'model_type': 'str',
        'embedded_data_specifications': 'list[EmbeddedDataSpecification]',
        'submodel_elements': 'list[SubmodelElementChoice]'
    }
    if hasattr(Identifiable, "swagger_types"):
        swagger_types.update(Identifiable.swagger_types)

    attribute_map = {
        'kind': 'kind',
        'semantic_id': 'semanticId',
        'supplemental_semantic_ids': 'supplementalSemanticIds',
        'qualifiers': 'qualifiers',
        'model_type': 'modelType',
        'embedded_data_specifications': 'embeddedDataSpecifications',
        'submodel_elements': 'submodelElements'
    }
    if hasattr(Identifiable, "attribute_map"):
        attribute_map.update(Identifiable.attribute_map)

    def __init__(self, kind=None, semantic_id=None, supplemental_semantic_ids=None, qualifiers=None, model_type=None, embedded_data_specifications=None, submodel_elements=None, *args, **kwargs):  # noqa: E501
        """Submodel - a model defined in Swagger"""  # noqa: E501
        self._kind = None
        self._semantic_id = None
        self._supplemental_semantic_ids = None
        self._qualifiers = None
        self._model_type = None
        self._embedded_data_specifications = None
        self._submodel_elements = None
        self.discriminator = None
        if kind is not None:
            self.kind = kind
        if semantic_id is not None:
            self.semantic_id = semantic_id
        if supplemental_semantic_ids is not None:
            self.supplemental_semantic_ids = supplemental_semantic_ids
        if qualifiers is not None:
            self.qualifiers = qualifiers
        self.model_type = model_type
        if embedded_data_specifications is not None:
            self.embedded_data_specifications = embedded_data_specifications
        if submodel_elements is not None:
            self.submodel_elements = submodel_elements
        Identifiable.__init__(self, *args, **kwargs)

    @property
    def kind(self):
        """Gets the kind of this Submodel.  # noqa: E501


        :return: The kind of this Submodel.  # noqa: E501
        :rtype: ModellingKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Submodel.


        :param kind: The kind of this Submodel.  # noqa: E501
        :type: ModellingKind
        """

        self._kind = kind

    @property
    def semantic_id(self):
        """Gets the semantic_id of this Submodel.  # noqa: E501


        :return: The semantic_id of this Submodel.  # noqa: E501
        :rtype: Reference
        """
        return self._semantic_id

    @semantic_id.setter
    def semantic_id(self, semantic_id):
        """Sets the semantic_id of this Submodel.


        :param semantic_id: The semantic_id of this Submodel.  # noqa: E501
        :type: Reference
        """

        self._semantic_id = semantic_id

    @property
    def supplemental_semantic_ids(self):
        """Gets the supplemental_semantic_ids of this Submodel.  # noqa: E501


        :return: The supplemental_semantic_ids of this Submodel.  # noqa: E501
        :rtype: list[Reference]
        """
        return self._supplemental_semantic_ids

    @supplemental_semantic_ids.setter
    def supplemental_semantic_ids(self, supplemental_semantic_ids):
        """Sets the supplemental_semantic_ids of this Submodel.


        :param supplemental_semantic_ids: The supplemental_semantic_ids of this Submodel.  # noqa: E501
        :type: list[Reference]
        """

        self._supplemental_semantic_ids = supplemental_semantic_ids

    @property
    def qualifiers(self):
        """Gets the qualifiers of this Submodel.  # noqa: E501


        :return: The qualifiers of this Submodel.  # noqa: E501
        :rtype: list[Qualifier]
        """
        return self._qualifiers

    @qualifiers.setter
    def qualifiers(self, qualifiers):
        """Sets the qualifiers of this Submodel.


        :param qualifiers: The qualifiers of this Submodel.  # noqa: E501
        :type: list[Qualifier]
        """

        self._qualifiers = qualifiers

    @property
    def model_type(self):
        """Gets the model_type of this Submodel.  # noqa: E501


        :return: The model_type of this Submodel.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this Submodel.


        :param model_type: The model_type of this Submodel.  # noqa: E501
        :type: str
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501

        self._model_type = model_type

    @property
    def embedded_data_specifications(self):
        """Gets the embedded_data_specifications of this Submodel.  # noqa: E501


        :return: The embedded_data_specifications of this Submodel.  # noqa: E501
        :rtype: list[EmbeddedDataSpecification]
        """
        return self._embedded_data_specifications

    @embedded_data_specifications.setter
    def embedded_data_specifications(self, embedded_data_specifications):
        """Sets the embedded_data_specifications of this Submodel.


        :param embedded_data_specifications: The embedded_data_specifications of this Submodel.  # noqa: E501
        :type: list[EmbeddedDataSpecification]
        """

        self._embedded_data_specifications = embedded_data_specifications

    @property
    def submodel_elements(self):
        """Gets the submodel_elements of this Submodel.  # noqa: E501


        :return: The submodel_elements of this Submodel.  # noqa: E501
        :rtype: list[SubmodelElementChoice]
        """
        return self._submodel_elements

    @submodel_elements.setter
    def submodel_elements(self, submodel_elements):
        """Sets the submodel_elements of this Submodel.


        :param submodel_elements: The submodel_elements of this Submodel.  # noqa: E501
        :type: list[SubmodelElementChoice]
        """

        self._submodel_elements = submodel_elements

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
        if issubclass(Submodel, dict):
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
        if not isinstance(other, Submodel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
