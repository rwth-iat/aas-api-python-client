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
from aas_python_http_client.models.event_element import EventElement  # noqa: F401,E501

class BasicEventElement(EventElement):
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
        'observed': 'Reference',
        'direction': 'Direction',
        'state': 'StateOfEvent',
        'message_topic': 'str',
        'message_broker': 'Reference',
        'last_update': 'str',
        'min_interval': 'str',
        'max_interval': 'str',
        'model_type': 'str'
    }
    if hasattr(EventElement, "swagger_types"):
        swagger_types.update(EventElement.swagger_types)

    attribute_map = {
        'observed': 'observed',
        'direction': 'direction',
        'state': 'state',
        'message_topic': 'messageTopic',
        'message_broker': 'messageBroker',
        'last_update': 'lastUpdate',
        'min_interval': 'minInterval',
        'max_interval': 'maxInterval',
        'model_type': 'modelType'
    }
    if hasattr(EventElement, "attribute_map"):
        attribute_map.update(EventElement.attribute_map)

    def __init__(self, observed=None, direction=None, state=None, message_topic=None, message_broker=None, last_update=None, min_interval=None, max_interval=None, model_type=None, *args, **kwargs):  # noqa: E501
        """BasicEventElement - a model defined in Swagger"""  # noqa: E501
        self._observed = None
        self._direction = None
        self._state = None
        self._message_topic = None
        self._message_broker = None
        self._last_update = None
        self._min_interval = None
        self._max_interval = None
        self._model_type = None
        self.discriminator = None
        self.observed = observed
        self.direction = direction
        self.state = state
        if message_topic is not None:
            self.message_topic = message_topic
        if message_broker is not None:
            self.message_broker = message_broker
        if last_update is not None:
            self.last_update = last_update
        if min_interval is not None:
            self.min_interval = min_interval
        if max_interval is not None:
            self.max_interval = max_interval
        if model_type is not None:
            self.model_type = model_type
        EventElement.__init__(self, *args, **kwargs)

    @property
    def observed(self):
        """Gets the observed of this BasicEventElement.  # noqa: E501


        :return: The observed of this BasicEventElement.  # noqa: E501
        :rtype: Reference
        """
        return self._observed

    @observed.setter
    def observed(self, observed):
        """Sets the observed of this BasicEventElement.


        :param observed: The observed of this BasicEventElement.  # noqa: E501
        :type: Reference
        """
        if observed is None:
            raise ValueError("Invalid value for `observed`, must not be `None`")  # noqa: E501

        self._observed = observed

    @property
    def direction(self):
        """Gets the direction of this BasicEventElement.  # noqa: E501


        :return: The direction of this BasicEventElement.  # noqa: E501
        :rtype: Direction
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this BasicEventElement.


        :param direction: The direction of this BasicEventElement.  # noqa: E501
        :type: Direction
        """
        if direction is None:
            raise ValueError("Invalid value for `direction`, must not be `None`")  # noqa: E501

        self._direction = direction

    @property
    def state(self):
        """Gets the state of this BasicEventElement.  # noqa: E501


        :return: The state of this BasicEventElement.  # noqa: E501
        :rtype: StateOfEvent
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BasicEventElement.


        :param state: The state of this BasicEventElement.  # noqa: E501
        :type: StateOfEvent
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def message_topic(self):
        """Gets the message_topic of this BasicEventElement.  # noqa: E501


        :return: The message_topic of this BasicEventElement.  # noqa: E501
        :rtype: str
        """
        return self._message_topic

    @message_topic.setter
    def message_topic(self, message_topic):
        """Sets the message_topic of this BasicEventElement.


        :param message_topic: The message_topic of this BasicEventElement.  # noqa: E501
        :type: str
        """

        self._message_topic = message_topic

    @property
    def message_broker(self):
        """Gets the message_broker of this BasicEventElement.  # noqa: E501


        :return: The message_broker of this BasicEventElement.  # noqa: E501
        :rtype: Reference
        """
        return self._message_broker

    @message_broker.setter
    def message_broker(self, message_broker):
        """Sets the message_broker of this BasicEventElement.


        :param message_broker: The message_broker of this BasicEventElement.  # noqa: E501
        :type: Reference
        """

        self._message_broker = message_broker

    @property
    def last_update(self):
        """Gets the last_update of this BasicEventElement.  # noqa: E501


        :return: The last_update of this BasicEventElement.  # noqa: E501
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this BasicEventElement.


        :param last_update: The last_update of this BasicEventElement.  # noqa: E501
        :type: str
        """

        self._last_update = last_update

    @property
    def min_interval(self):
        """Gets the min_interval of this BasicEventElement.  # noqa: E501


        :return: The min_interval of this BasicEventElement.  # noqa: E501
        :rtype: str
        """
        return self._min_interval

    @min_interval.setter
    def min_interval(self, min_interval):
        """Sets the min_interval of this BasicEventElement.


        :param min_interval: The min_interval of this BasicEventElement.  # noqa: E501
        :type: str
        """

        self._min_interval = min_interval

    @property
    def max_interval(self):
        """Gets the max_interval of this BasicEventElement.  # noqa: E501


        :return: The max_interval of this BasicEventElement.  # noqa: E501
        :rtype: str
        """
        return self._max_interval

    @max_interval.setter
    def max_interval(self, max_interval):
        """Sets the max_interval of this BasicEventElement.


        :param max_interval: The max_interval of this BasicEventElement.  # noqa: E501
        :type: str
        """

        self._max_interval = max_interval

    @property
    def model_type(self):
        """Gets the model_type of this BasicEventElement.  # noqa: E501


        :return: The model_type of this BasicEventElement.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this BasicEventElement.


        :param model_type: The model_type of this BasicEventElement.  # noqa: E501
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
        if issubclass(BasicEventElement, dict):
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
        if not isinstance(other, BasicEventElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
