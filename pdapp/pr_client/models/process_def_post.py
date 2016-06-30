# coding: utf-8

"""
    Process Registry API

    Register processes with the Process Registry API.

    OpenAPI spec version: 0.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class ProcessDefPost(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ProcessDefPost - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'appliance': 'str',
            'archive_url': 'str',
            'adapters': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'appliance': 'appliance',
            'archive_url': 'archive_url',
            'adapters': 'adapters'
        }

        self._name = None
        self._appliance = None
        self._archive_url = None
        self._adapters = None

    @property
    def name(self):
        """
        Gets the name of this ProcessDefPost.
        Name given to the process

        :return: The name of this ProcessDefPost.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProcessDefPost.
        Name given to the process

        :param name: The name of this ProcessDefPost.
        :type: str
        """
        
        self._name = name

    @property
    def appliance(self):
        """
        Gets the appliance of this ProcessDefPost.
        Name of the appliance on which the process must be run

        :return: The appliance of this ProcessDefPost.
        :rtype: str
        """
        return self._appliance

    @appliance.setter
    def appliance(self, appliance):
        """
        Sets the appliance of this ProcessDefPost.
        Name of the appliance on which the process must be run

        :param appliance: The appliance of this ProcessDefPost.
        :type: str
        """
        
        self._appliance = appliance

    @property
    def archive_url(self):
        """
        Gets the archive_url of this ProcessDefPost.
        URL of the archive to download and extract on the worker before starting the job

        :return: The archive_url of this ProcessDefPost.
        :rtype: str
        """
        return self._archive_url

    @archive_url.setter
    def archive_url(self, archive_url):
        """
        Sets the archive_url of this ProcessDefPost.
        URL of the archive to download and extract on the worker before starting the job

        :param archive_url: The archive_url of this ProcessDefPost.
        :type: str
        """
        
        self._archive_url = archive_url

    @property
    def adapters(self):
        """
        Gets the adapters of this ProcessDefPost.
        JSON-formatted string containing all the information required to start the process

        :return: The adapters of this ProcessDefPost.
        :rtype: str
        """
        return self._adapters

    @adapters.setter
    def adapters(self, adapters):
        """
        Sets the adapters of this ProcessDefPost.
        JSON-formatted string containing all the information required to start the process

        :param adapters: The adapters of this ProcessDefPost.
        :type: str
        """
        
        self._adapters = adapters

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
