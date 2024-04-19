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

class Qualifiable(object):
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
        'qualifiers': 'list[Qualifier]',
        'model_type': 'ModelType'
    }

    attribute_map = {
        'qualifiers': 'qualifiers',
        'model_type': 'modelType'
    }

    def __init__(self, qualifiers=None, model_type=None):  # noqa: E501
        """Qualifiable - a model defined in Swagger"""  # noqa: E501
        self._qualifiers = None
        self._model_type = None
        self.discriminator = None
        if qualifiers is not None:
            self.qualifiers = qualifiers
        self.model_type = model_type

    @property
    def qualifiers(self):
        """Gets the qualifiers of this Qualifiable.  # noqa: E501


        :return: The qualifiers of this Qualifiable.  # noqa: E501
        :rtype: list[Qualifier]
        """
        return self._qualifiers

    @qualifiers.setter
    def qualifiers(self, qualifiers):
        """Sets the qualifiers of this Qualifiable.


        :param qualifiers: The qualifiers of this Qualifiable.  # noqa: E501
        :type: list[Qualifier]
        """

        self._qualifiers = qualifiers

    @property
    def model_type(self):
        """Gets the model_type of this Qualifiable.  # noqa: E501


        :return: The model_type of this Qualifiable.  # noqa: E501
        :rtype: ModelType
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this Qualifiable.


        :param model_type: The model_type of this Qualifiable.  # noqa: E501
        :type: ModelType
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501

        self._model_type = model_type

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
        if issubclass(Qualifiable, dict):
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
        if not isinstance(other, Qualifiable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
