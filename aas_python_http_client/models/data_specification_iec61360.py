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
from aas_python_http_client.models.data_specification_content import DataSpecificationContent  # noqa: F401,E501

class DataSpecificationIec61360(DataSpecificationContent):
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
        'preferred_name': 'list[LangStringPreferredNameTypeIec61360]',
        'short_name': 'list[LangStringShortNameTypeIec61360]',
        'unit': 'str',
        'unit_id': 'Reference',
        'source_of_definition': 'str',
        'symbol': 'str',
        'data_type': 'DataTypeIec61360',
        'definition': 'list[LangStringDefinitionTypeIec61360]',
        'value_format': 'str',
        'value_list': 'ValueList',
        'value': 'str',
        'level_type': 'LevelType',
        'model_type': 'str'
    }
    if hasattr(DataSpecificationContent, "swagger_types"):
        swagger_types.update(DataSpecificationContent.swagger_types)

    attribute_map = {
        'preferred_name': 'preferredName',
        'short_name': 'shortName',
        'unit': 'unit',
        'unit_id': 'unitId',
        'source_of_definition': 'sourceOfDefinition',
        'symbol': 'symbol',
        'data_type': 'dataType',
        'definition': 'definition',
        'value_format': 'valueFormat',
        'value_list': 'valueList',
        'value': 'value',
        'level_type': 'levelType',
        'model_type': 'modelType'
    }
    if hasattr(DataSpecificationContent, "attribute_map"):
        attribute_map.update(DataSpecificationContent.attribute_map)

    def __init__(self, preferred_name=None, short_name=None, unit=None, unit_id=None, source_of_definition=None, symbol=None, data_type=None, definition=None, value_format=None, value_list=None, value=None, level_type=None, model_type=None, *args, **kwargs):  # noqa: E501
        """DataSpecificationIec61360 - a model defined in Swagger"""  # noqa: E501
        self._preferred_name = None
        self._short_name = None
        self._unit = None
        self._unit_id = None
        self._source_of_definition = None
        self._symbol = None
        self._data_type = None
        self._definition = None
        self._value_format = None
        self._value_list = None
        self._value = None
        self._level_type = None
        self._model_type = None
        self.discriminator = None
        self.preferred_name = preferred_name
        if short_name is not None:
            self.short_name = short_name
        if unit is not None:
            self.unit = unit
        if unit_id is not None:
            self.unit_id = unit_id
        if source_of_definition is not None:
            self.source_of_definition = source_of_definition
        if symbol is not None:
            self.symbol = symbol
        if data_type is not None:
            self.data_type = data_type
        if definition is not None:
            self.definition = definition
        if value_format is not None:
            self.value_format = value_format
        if value_list is not None:
            self.value_list = value_list
        if value is not None:
            self.value = value
        if level_type is not None:
            self.level_type = level_type
        if model_type is not None:
            self.model_type = model_type
        DataSpecificationContent.__init__(self, *args, **kwargs)

    @property
    def preferred_name(self):
        """Gets the preferred_name of this DataSpecificationIec61360.  # noqa: E501


        :return: The preferred_name of this DataSpecificationIec61360.  # noqa: E501
        :rtype: list[LangStringPreferredNameTypeIec61360]
        """
        return self._preferred_name

    @preferred_name.setter
    def preferred_name(self, preferred_name):
        """Sets the preferred_name of this DataSpecificationIec61360.


        :param preferred_name: The preferred_name of this DataSpecificationIec61360.  # noqa: E501
        :type: list[LangStringPreferredNameTypeIec61360]
        """
        if preferred_name is None:
            raise ValueError("Invalid value for `preferred_name`, must not be `None`")  # noqa: E501

        self._preferred_name = preferred_name

    @property
    def short_name(self):
        """Gets the short_name of this DataSpecificationIec61360.  # noqa: E501


        :return: The short_name of this DataSpecificationIec61360.  # noqa: E501
        :rtype: list[LangStringShortNameTypeIec61360]
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this DataSpecificationIec61360.


        :param short_name: The short_name of this DataSpecificationIec61360.  # noqa: E501
        :type: list[LangStringShortNameTypeIec61360]
        """

        self._short_name = short_name

    @property
    def unit(self):
        """Gets the unit of this DataSpecificationIec61360.  # noqa: E501


        :return: The unit of this DataSpecificationIec61360.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this DataSpecificationIec61360.


        :param unit: The unit of this DataSpecificationIec61360.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def unit_id(self):
        """Gets the unit_id of this DataSpecificationIec61360.  # noqa: E501


        :return: The unit_id of this DataSpecificationIec61360.  # noqa: E501
        :rtype: Reference
        """
        return self._unit_id

    @unit_id.setter
    def unit_id(self, unit_id):
        """Sets the unit_id of this DataSpecificationIec61360.


        :param unit_id: The unit_id of this DataSpecificationIec61360.  # noqa: E501
        :type: Reference
        """

        self._unit_id = unit_id

    @property
    def source_of_definition(self):
        """Gets the source_of_definition of this DataSpecificationIec61360.  # noqa: E501


        :return: The source_of_definition of this DataSpecificationIec61360.  # noqa: E501
        :rtype: str
        """
        return self._source_of_definition

    @source_of_definition.setter
    def source_of_definition(self, source_of_definition):
        """Sets the source_of_definition of this DataSpecificationIec61360.


        :param source_of_definition: The source_of_definition of this DataSpecificationIec61360.  # noqa: E501
        :type: str
        """

        self._source_of_definition = source_of_definition

    @property
    def symbol(self):
        """Gets the symbol of this DataSpecificationIec61360.  # noqa: E501


        :return: The symbol of this DataSpecificationIec61360.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this DataSpecificationIec61360.


        :param symbol: The symbol of this DataSpecificationIec61360.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def data_type(self):
        """Gets the data_type of this DataSpecificationIec61360.  # noqa: E501


        :return: The data_type of this DataSpecificationIec61360.  # noqa: E501
        :rtype: DataTypeIec61360
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this DataSpecificationIec61360.


        :param data_type: The data_type of this DataSpecificationIec61360.  # noqa: E501
        :type: DataTypeIec61360
        """

        self._data_type = data_type

    @property
    def definition(self):
        """Gets the definition of this DataSpecificationIec61360.  # noqa: E501


        :return: The definition of this DataSpecificationIec61360.  # noqa: E501
        :rtype: list[LangStringDefinitionTypeIec61360]
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this DataSpecificationIec61360.


        :param definition: The definition of this DataSpecificationIec61360.  # noqa: E501
        :type: list[LangStringDefinitionTypeIec61360]
        """

        self._definition = definition

    @property
    def value_format(self):
        """Gets the value_format of this DataSpecificationIec61360.  # noqa: E501


        :return: The value_format of this DataSpecificationIec61360.  # noqa: E501
        :rtype: str
        """
        return self._value_format

    @value_format.setter
    def value_format(self, value_format):
        """Sets the value_format of this DataSpecificationIec61360.


        :param value_format: The value_format of this DataSpecificationIec61360.  # noqa: E501
        :type: str
        """

        self._value_format = value_format

    @property
    def value_list(self):
        """Gets the value_list of this DataSpecificationIec61360.  # noqa: E501


        :return: The value_list of this DataSpecificationIec61360.  # noqa: E501
        :rtype: ValueList
        """
        return self._value_list

    @value_list.setter
    def value_list(self, value_list):
        """Sets the value_list of this DataSpecificationIec61360.


        :param value_list: The value_list of this DataSpecificationIec61360.  # noqa: E501
        :type: ValueList
        """

        self._value_list = value_list

    @property
    def value(self):
        """Gets the value of this DataSpecificationIec61360.  # noqa: E501


        :return: The value of this DataSpecificationIec61360.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DataSpecificationIec61360.


        :param value: The value of this DataSpecificationIec61360.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def level_type(self):
        """Gets the level_type of this DataSpecificationIec61360.  # noqa: E501


        :return: The level_type of this DataSpecificationIec61360.  # noqa: E501
        :rtype: LevelType
        """
        return self._level_type

    @level_type.setter
    def level_type(self, level_type):
        """Sets the level_type of this DataSpecificationIec61360.


        :param level_type: The level_type of this DataSpecificationIec61360.  # noqa: E501
        :type: LevelType
        """

        self._level_type = level_type

    @property
    def model_type(self):
        """Gets the model_type of this DataSpecificationIec61360.  # noqa: E501


        :return: The model_type of this DataSpecificationIec61360.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this DataSpecificationIec61360.


        :param model_type: The model_type of this DataSpecificationIec61360.  # noqa: E501
        :type: str
        """

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
        if issubclass(DataSpecificationIec61360, dict):
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
        if not isinstance(other, DataSpecificationIec61360):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
