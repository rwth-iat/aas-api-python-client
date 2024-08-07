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
from aas_python_http_client.models.base_operation_result import BaseOperationResult  # noqa: F401,E501

class OperationResult(BaseOperationResult):
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
        'inoutput_arguments': 'list[OperationVariable]',
        'output_arguments': 'list[OperationVariable]'
    }
    if hasattr(BaseOperationResult, "swagger_types"):
        swagger_types.update(BaseOperationResult.swagger_types)

    attribute_map = {
        'inoutput_arguments': 'inoutputArguments',
        'output_arguments': 'outputArguments'
    }
    if hasattr(BaseOperationResult, "attribute_map"):
        attribute_map.update(BaseOperationResult.attribute_map)

    def __init__(self, inoutput_arguments=None, output_arguments=None, *args, **kwargs):  # noqa: E501
        """OperationResult - a model defined in Swagger"""  # noqa: E501
        self._inoutput_arguments = None
        self._output_arguments = None
        self.discriminator = None
        if inoutput_arguments is not None:
            self.inoutput_arguments = inoutput_arguments
        if output_arguments is not None:
            self.output_arguments = output_arguments
        BaseOperationResult.__init__(self, *args, **kwargs)

    @property
    def inoutput_arguments(self):
        """Gets the inoutput_arguments of this OperationResult.  # noqa: E501


        :return: The inoutput_arguments of this OperationResult.  # noqa: E501
        :rtype: list[OperationVariable]
        """
        return self._inoutput_arguments

    @inoutput_arguments.setter
    def inoutput_arguments(self, inoutput_arguments):
        """Sets the inoutput_arguments of this OperationResult.


        :param inoutput_arguments: The inoutput_arguments of this OperationResult.  # noqa: E501
        :type: list[OperationVariable]
        """

        self._inoutput_arguments = inoutput_arguments

    @property
    def output_arguments(self):
        """Gets the output_arguments of this OperationResult.  # noqa: E501


        :return: The output_arguments of this OperationResult.  # noqa: E501
        :rtype: list[OperationVariable]
        """
        return self._output_arguments

    @output_arguments.setter
    def output_arguments(self, output_arguments):
        """Sets the output_arguments of this OperationResult.


        :param output_arguments: The output_arguments of this OperationResult.  # noqa: E501
        :type: list[OperationVariable]
        """

        self._output_arguments = output_arguments

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
        if issubclass(OperationResult, dict):
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
        if not isinstance(other, OperationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
