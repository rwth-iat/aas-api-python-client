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

class ReferenceParent(object):
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
        'type': 'ReferenceTypes',
        'keys': 'list[Key]'
    }

    attribute_map = {
        'type': 'type',
        'keys': 'keys'
    }

    def __init__(self, type=None, keys=None):  # noqa: E501
        """ReferenceParent - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._keys = None
        self.discriminator = None
        self.type = type
        self.keys = keys

    @property
    def type(self):
        """Gets the type of this ReferenceParent.  # noqa: E501


        :return: The type of this ReferenceParent.  # noqa: E501
        :rtype: ReferenceTypes
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ReferenceParent.


        :param type: The type of this ReferenceParent.  # noqa: E501
        :type: ReferenceTypes
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def keys(self):
        """Gets the keys of this ReferenceParent.  # noqa: E501


        :return: The keys of this ReferenceParent.  # noqa: E501
        :rtype: list[Key]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this ReferenceParent.


        :param keys: The keys of this ReferenceParent.  # noqa: E501
        :type: list[Key]
        """
        if keys is None:
            raise ValueError("Invalid value for `keys`, must not be `None`")  # noqa: E501

        self._keys = keys

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
        if issubclass(ReferenceParent, dict):
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
        if not isinstance(other, ReferenceParent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
