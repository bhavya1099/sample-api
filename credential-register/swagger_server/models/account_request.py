# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AccountRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, customer_id: float=None):  # noqa: E501
        """AccountRequest - a model defined in Swagger

        :param customer_id: The customer_id of this AccountRequest.  # noqa: E501
        :type customer_id: float
        """
        self.swagger_types = {
            'customer_id': float
        }

        self.attribute_map = {
            'customer_id': 'customerId'
        }
        self._customer_id = customer_id

    @classmethod
    def from_dict(cls, dikt) -> 'AccountRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The accountRequest of this AccountRequest.  # noqa: E501
        :rtype: AccountRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def customer_id(self) -> float:
        """Gets the customer_id of this AccountRequest.


        :return: The customer_id of this AccountRequest.
        :rtype: float
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id: float):
        """Sets the customer_id of this AccountRequest.


        :param customer_id: The customer_id of this AccountRequest.
        :type customer_id: float
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id
