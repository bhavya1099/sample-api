# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CCListResponseSub(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, type: str=None, customer_id: float=None, amount: float=None, source_account_number: str=None, target_account_number: str=None, due_date: str=None, currency: str=None, status: str=None, id: str=None):  # noqa: E501
        """CCListResponseSub - a model defined in Swagger

        :param type: The type of this CCListResponseSub.  # noqa: E501
        :type type: str
        :param customer_id: The customer_id of this CCListResponseSub.  # noqa: E501
        :type customer_id: float
        :param amount: The amount of this CCListResponseSub.  # noqa: E501
        :type amount: float
        :param source_account_number: The source_account_number of this CCListResponseSub.  # noqa: E501
        :type source_account_number: str
        :param target_account_number: The target_account_number of this CCListResponseSub.  # noqa: E501
        :type target_account_number: str
        :param due_date: The due_date of this CCListResponseSub.  # noqa: E501
        :type due_date: str
        :param currency: The currency of this CCListResponseSub.  # noqa: E501
        :type currency: str
        :param status: The status of this CCListResponseSub.  # noqa: E501
        :type status: str
        :param id: The id of this CCListResponseSub.  # noqa: E501
        :type id: str
        """
        self.swagger_types = {
            'type': str,
            'customer_id': float,
            'amount': float,
            'source_account_number': str,
            'target_account_number': str,
            'due_date': str,
            'currency': str,
            'status': str,
            'id': str
        }

        self.attribute_map = {
            'type': 'Type',
            'customer_id': 'CustomerId',
            'amount': 'Amount',
            'source_account_number': 'SourceAccountNumber',
            'target_account_number': 'TargetAccountNumber',
            'due_date': 'DueDate',
            'currency': 'Currency',
            'status': 'Status',
            'id': 'id'
        }
        self._type = type
        self._customer_id = customer_id
        self._amount = amount
        self._source_account_number = source_account_number
        self._target_account_number = target_account_number
        self._due_date = due_date
        self._currency = currency
        self._status = status
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'CCListResponseSub':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CCListResponse_sub of this CCListResponseSub.  # noqa: E501
        :rtype: CCListResponseSub
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this CCListResponseSub.


        :return: The type of this CCListResponseSub.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this CCListResponseSub.


        :param type: The type of this CCListResponseSub.
        :type type: str
        """

        self._type = type

    @property
    def customer_id(self) -> float:
        """Gets the customer_id of this CCListResponseSub.


        :return: The customer_id of this CCListResponseSub.
        :rtype: float
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id: float):
        """Sets the customer_id of this CCListResponseSub.


        :param customer_id: The customer_id of this CCListResponseSub.
        :type customer_id: float
        """

        self._customer_id = customer_id

    @property
    def amount(self) -> float:
        """Gets the amount of this CCListResponseSub.


        :return: The amount of this CCListResponseSub.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        """Sets the amount of this CCListResponseSub.


        :param amount: The amount of this CCListResponseSub.
        :type amount: float
        """

        self._amount = amount

    @property
    def source_account_number(self) -> str:
        """Gets the source_account_number of this CCListResponseSub.


        :return: The source_account_number of this CCListResponseSub.
        :rtype: str
        """
        return self._source_account_number

    @source_account_number.setter
    def source_account_number(self, source_account_number: str):
        """Sets the source_account_number of this CCListResponseSub.


        :param source_account_number: The source_account_number of this CCListResponseSub.
        :type source_account_number: str
        """

        self._source_account_number = source_account_number

    @property
    def target_account_number(self) -> str:
        """Gets the target_account_number of this CCListResponseSub.


        :return: The target_account_number of this CCListResponseSub.
        :rtype: str
        """
        return self._target_account_number

    @target_account_number.setter
    def target_account_number(self, target_account_number: str):
        """Sets the target_account_number of this CCListResponseSub.


        :param target_account_number: The target_account_number of this CCListResponseSub.
        :type target_account_number: str
        """

        self._target_account_number = target_account_number

    @property
    def due_date(self) -> str:
        """Gets the due_date of this CCListResponseSub.


        :return: The due_date of this CCListResponseSub.
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date: str):
        """Sets the due_date of this CCListResponseSub.


        :param due_date: The due_date of this CCListResponseSub.
        :type due_date: str
        """

        self._due_date = due_date

    @property
    def currency(self) -> str:
        """Gets the currency of this CCListResponseSub.


        :return: The currency of this CCListResponseSub.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency: str):
        """Sets the currency of this CCListResponseSub.


        :param currency: The currency of this CCListResponseSub.
        :type currency: str
        """

        self._currency = currency

    @property
    def status(self) -> str:
        """Gets the status of this CCListResponseSub.


        :return: The status of this CCListResponseSub.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this CCListResponseSub.


        :param status: The status of this CCListResponseSub.
        :type status: str
        """

        self._status = status

    @property
    def id(self) -> str:
        """Gets the id of this CCListResponseSub.


        :return: The id of this CCListResponseSub.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this CCListResponseSub.


        :param id: The id of this CCListResponseSub.
        :type id: str
        """

        self._id = id
