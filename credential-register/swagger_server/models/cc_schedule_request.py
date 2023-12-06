# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CcScheduleRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, customer_id: float=None, status: str=None):  # noqa: E501
        """CcScheduleRequest - a model defined in Swagger

        :param customer_id: The customer_id of this CcScheduleRequest.  # noqa: E501
        :type customer_id: float
        :param status: The status of this CcScheduleRequest.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'customer_id': float,
            'status': str
        }

        self.attribute_map = {
            'customer_id': 'customerId',
            'status': 'status'
        }
        self._customer_id = customer_id
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'CcScheduleRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ccScheduleRequest of this CcScheduleRequest.  # noqa: E501
        :rtype: CcScheduleRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def customer_id(self) -> float:
        """Gets the customer_id of this CcScheduleRequest.


        :return: The customer_id of this CcScheduleRequest.
        :rtype: float
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id: float):
        """Sets the customer_id of this CcScheduleRequest.


        :param customer_id: The customer_id of this CcScheduleRequest.
        :type customer_id: float
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def status(self) -> str:
        """Gets the status of this CcScheduleRequest.


        :return: The status of this CcScheduleRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this CcScheduleRequest.


        :param status: The status of this CcScheduleRequest.
        :type status: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status
