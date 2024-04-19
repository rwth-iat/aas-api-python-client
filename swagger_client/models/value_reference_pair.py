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

class ValueReferencePair(object):
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
        'value': 'str',
        'value_id': 'Reference'
    }

    attribute_map = {
        'value': 'value',
        'value_id': 'valueId'
    }

    def __init__(self, value=None, value_id=None):  # noqa: E501
        """ValueReferencePair - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._value_id = None
        self.discriminator = None
        self.value = value
        self.value_id = value_id

    @property
    def value(self):
        """Gets the value of this ValueReferencePair.  # noqa: E501


        :return: The value of this ValueReferencePair.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ValueReferencePair.


        :param value: The value of this ValueReferencePair.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def value_id(self):
        """Gets the value_id of this ValueReferencePair.  # noqa: E501


        :return: The value_id of this ValueReferencePair.  # noqa: E501
        :rtype: Reference
        """
        return self._value_id

    @value_id.setter
    def value_id(self, value_id):
        """Sets the value_id of this ValueReferencePair.


        :param value_id: The value_id of this ValueReferencePair.  # noqa: E501
        :type: Reference
        """
        if value_id is None:
            raise ValueError("Invalid value for `value_id`, must not be `None`")  # noqa: E501

        self._value_id = value_id

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
        if issubclass(ValueReferencePair, dict):
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
        if not isinstance(other, ValueReferencePair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
