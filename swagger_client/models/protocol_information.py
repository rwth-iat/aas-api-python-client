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

class ProtocolInformation(object):
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
        'href': 'str',
        'endpoint_protocol': 'str',
        'endpoint_protocol_version': 'list[str]',
        'subprotocol': 'str',
        'subprotocol_body': 'str',
        'subprotocol_body_encoding': 'str',
        'security_attributes': 'list[ProtocolInformationSecurityAttributes]'
    }

    attribute_map = {
        'href': 'href',
        'endpoint_protocol': 'endpointProtocol',
        'endpoint_protocol_version': 'endpointProtocolVersion',
        'subprotocol': 'subprotocol',
        'subprotocol_body': 'subprotocolBody',
        'subprotocol_body_encoding': 'subprotocolBodyEncoding',
        'security_attributes': 'securityAttributes'
    }

    def __init__(self, href=None, endpoint_protocol=None, endpoint_protocol_version=None, subprotocol=None, subprotocol_body=None, subprotocol_body_encoding=None, security_attributes=None):  # noqa: E501
        """ProtocolInformation - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._endpoint_protocol = None
        self._endpoint_protocol_version = None
        self._subprotocol = None
        self._subprotocol_body = None
        self._subprotocol_body_encoding = None
        self._security_attributes = None
        self.discriminator = None
        self.href = href
        if endpoint_protocol is not None:
            self.endpoint_protocol = endpoint_protocol
        if endpoint_protocol_version is not None:
            self.endpoint_protocol_version = endpoint_protocol_version
        if subprotocol is not None:
            self.subprotocol = subprotocol
        if subprotocol_body is not None:
            self.subprotocol_body = subprotocol_body
        if subprotocol_body_encoding is not None:
            self.subprotocol_body_encoding = subprotocol_body_encoding
        if security_attributes is not None:
            self.security_attributes = security_attributes

    @property
    def href(self):
        """Gets the href of this ProtocolInformation.  # noqa: E501


        :return: The href of this ProtocolInformation.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ProtocolInformation.


        :param href: The href of this ProtocolInformation.  # noqa: E501
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def endpoint_protocol(self):
        """Gets the endpoint_protocol of this ProtocolInformation.  # noqa: E501


        :return: The endpoint_protocol of this ProtocolInformation.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_protocol

    @endpoint_protocol.setter
    def endpoint_protocol(self, endpoint_protocol):
        """Sets the endpoint_protocol of this ProtocolInformation.


        :param endpoint_protocol: The endpoint_protocol of this ProtocolInformation.  # noqa: E501
        :type: str
        """

        self._endpoint_protocol = endpoint_protocol

    @property
    def endpoint_protocol_version(self):
        """Gets the endpoint_protocol_version of this ProtocolInformation.  # noqa: E501


        :return: The endpoint_protocol_version of this ProtocolInformation.  # noqa: E501
        :rtype: list[str]
        """
        return self._endpoint_protocol_version

    @endpoint_protocol_version.setter
    def endpoint_protocol_version(self, endpoint_protocol_version):
        """Sets the endpoint_protocol_version of this ProtocolInformation.


        :param endpoint_protocol_version: The endpoint_protocol_version of this ProtocolInformation.  # noqa: E501
        :type: list[str]
        """

        self._endpoint_protocol_version = endpoint_protocol_version

    @property
    def subprotocol(self):
        """Gets the subprotocol of this ProtocolInformation.  # noqa: E501


        :return: The subprotocol of this ProtocolInformation.  # noqa: E501
        :rtype: str
        """
        return self._subprotocol

    @subprotocol.setter
    def subprotocol(self, subprotocol):
        """Sets the subprotocol of this ProtocolInformation.


        :param subprotocol: The subprotocol of this ProtocolInformation.  # noqa: E501
        :type: str
        """

        self._subprotocol = subprotocol

    @property
    def subprotocol_body(self):
        """Gets the subprotocol_body of this ProtocolInformation.  # noqa: E501


        :return: The subprotocol_body of this ProtocolInformation.  # noqa: E501
        :rtype: str
        """
        return self._subprotocol_body

    @subprotocol_body.setter
    def subprotocol_body(self, subprotocol_body):
        """Sets the subprotocol_body of this ProtocolInformation.


        :param subprotocol_body: The subprotocol_body of this ProtocolInformation.  # noqa: E501
        :type: str
        """

        self._subprotocol_body = subprotocol_body

    @property
    def subprotocol_body_encoding(self):
        """Gets the subprotocol_body_encoding of this ProtocolInformation.  # noqa: E501


        :return: The subprotocol_body_encoding of this ProtocolInformation.  # noqa: E501
        :rtype: str
        """
        return self._subprotocol_body_encoding

    @subprotocol_body_encoding.setter
    def subprotocol_body_encoding(self, subprotocol_body_encoding):
        """Sets the subprotocol_body_encoding of this ProtocolInformation.


        :param subprotocol_body_encoding: The subprotocol_body_encoding of this ProtocolInformation.  # noqa: E501
        :type: str
        """

        self._subprotocol_body_encoding = subprotocol_body_encoding

    @property
    def security_attributes(self):
        """Gets the security_attributes of this ProtocolInformation.  # noqa: E501


        :return: The security_attributes of this ProtocolInformation.  # noqa: E501
        :rtype: list[ProtocolInformationSecurityAttributes]
        """
        return self._security_attributes

    @security_attributes.setter
    def security_attributes(self, security_attributes):
        """Sets the security_attributes of this ProtocolInformation.


        :param security_attributes: The security_attributes of this ProtocolInformation.  # noqa: E501
        :type: list[ProtocolInformationSecurityAttributes]
        """

        self._security_attributes = security_attributes

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
        if issubclass(ProtocolInformation, dict):
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
        if not isinstance(other, ProtocolInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
