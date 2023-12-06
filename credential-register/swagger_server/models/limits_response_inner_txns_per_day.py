# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class LimitsResponseInnerTxnsPerDay(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, available: float=None, maximum: float=None, usedup: float=None, amountperday: float=None):  # noqa: E501
        """LimitsResponseInnerTxnsPerDay - a model defined in Swagger

        :param available: The available of this LimitsResponseInnerTxnsPerDay.  # noqa: E501
        :type available: float
        :param maximum: The maximum of this LimitsResponseInnerTxnsPerDay.  # noqa: E501
        :type maximum: float
        :param usedup: The usedup of this LimitsResponseInnerTxnsPerDay.  # noqa: E501
        :type usedup: float
        :param amountperday: The amountperday of this LimitsResponseInnerTxnsPerDay.  # noqa: E501
        :type amountperday: float
        """
        self.swagger_types = {
            'available': float,
            'maximum': float,
            'usedup': float,
            'amountperday': float
        }

        self.attribute_map = {
            'available': 'available',
            'maximum': 'maximum',
            'usedup': 'usedup',
            'amountperday': 'amountperday'
        }
        self._available = available
        self._maximum = maximum
        self._usedup = usedup
        self._amountperday = amountperday

    @classmethod
    def from_dict(cls, dikt) -> 'LimitsResponseInnerTxnsPerDay':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The limitsResponse_inner_txnsPerDay of this LimitsResponseInnerTxnsPerDay.  # noqa: E501
        :rtype: LimitsResponseInnerTxnsPerDay
        """
        return util.deserialize_model(dikt, cls)

    @property
    def available(self) -> float:
        """Gets the available of this LimitsResponseInnerTxnsPerDay.


        :return: The available of this LimitsResponseInnerTxnsPerDay.
        :rtype: float
        """
        return self._available

    @available.setter
    def available(self, available: float):
        """Sets the available of this LimitsResponseInnerTxnsPerDay.


        :param available: The available of this LimitsResponseInnerTxnsPerDay.
        :type available: float
        """

        self._available = available

    @property
    def maximum(self) -> float:
        """Gets the maximum of this LimitsResponseInnerTxnsPerDay.


        :return: The maximum of this LimitsResponseInnerTxnsPerDay.
        :rtype: float
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum: float):
        """Sets the maximum of this LimitsResponseInnerTxnsPerDay.


        :param maximum: The maximum of this LimitsResponseInnerTxnsPerDay.
        :type maximum: float
        """

        self._maximum = maximum

    @property
    def usedup(self) -> float:
        """Gets the usedup of this LimitsResponseInnerTxnsPerDay.


        :return: The usedup of this LimitsResponseInnerTxnsPerDay.
        :rtype: float
        """
        return self._usedup

    @usedup.setter
    def usedup(self, usedup: float):
        """Sets the usedup of this LimitsResponseInnerTxnsPerDay.


        :param usedup: The usedup of this LimitsResponseInnerTxnsPerDay.
        :type usedup: float
        """

        self._usedup = usedup

    @property
    def amountperday(self) -> float:
        """Gets the amountperday of this LimitsResponseInnerTxnsPerDay.


        :return: The amountperday of this LimitsResponseInnerTxnsPerDay.
        :rtype: float
        """
        return self._amountperday

    @amountperday.setter
    def amountperday(self, amountperday: float):
        """Sets the amountperday of this LimitsResponseInnerTxnsPerDay.


        :param amountperday: The amountperday of this LimitsResponseInnerTxnsPerDay.
        :type amountperday: float
        """

        self._amountperday = amountperday
