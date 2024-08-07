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
from aas_python_http_client.models.result import Result  # noqa: F401,E501

class BaseOperationResult(Result):
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
        'execution_state': 'ExecutionState',
        'success': 'bool'
    }
    if hasattr(Result, "swagger_types"):
        swagger_types.update(Result.swagger_types)

    attribute_map = {
        'execution_state': 'executionState',
        'success': 'success'
    }
    if hasattr(Result, "attribute_map"):
        attribute_map.update(Result.attribute_map)

    def __init__(self, execution_state=None, success=None, *args, **kwargs):  # noqa: E501
        """BaseOperationResult - a model defined in Swagger"""  # noqa: E501
        self._execution_state = None
        self._success = None
        self.discriminator = None
        if execution_state is not None:
            self.execution_state = execution_state
        if success is not None:
            self.success = success
        Result.__init__(self, *args, **kwargs)

    @property
    def execution_state(self):
        """Gets the execution_state of this BaseOperationResult.  # noqa: E501


        :return: The execution_state of this BaseOperationResult.  # noqa: E501
        :rtype: ExecutionState
        """
        return self._execution_state

    @execution_state.setter
    def execution_state(self, execution_state):
        """Sets the execution_state of this BaseOperationResult.


        :param execution_state: The execution_state of this BaseOperationResult.  # noqa: E501
        :type: ExecutionState
        """

        self._execution_state = execution_state

    @property
    def success(self):
        """Gets the success of this BaseOperationResult.  # noqa: E501


        :return: The success of this BaseOperationResult.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this BaseOperationResult.


        :param success: The success of this BaseOperationResult.  # noqa: E501
        :type: bool
        """

        self._success = success

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
        if issubclass(BaseOperationResult, dict):
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
        if not isinstance(other, BaseOperationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
