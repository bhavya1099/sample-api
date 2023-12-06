# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class LocateProfileResponseCardDetails(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, card_number: str=None, expiry_date: str=None, cvv: str=None, pin: str=None):  # noqa: E501
        """LocateProfileResponseCardDetails - a model defined in Swagger

        :param card_number: The card_number of this LocateProfileResponseCardDetails.  # noqa: E501
        :type card_number: str
        :param expiry_date: The expiry_date of this LocateProfileResponseCardDetails.  # noqa: E501
        :type expiry_date: str
        :param cvv: The cvv of this LocateProfileResponseCardDetails.  # noqa: E501
        :type cvv: str
        :param pin: The pin of this LocateProfileResponseCardDetails.  # noqa: E501
        :type pin: str
        """
        self.swagger_types = {
            'card_number': str,
            'expiry_date': str,
            'cvv': str,
            'pin': str
        }

        self.attribute_map = {
            'card_number': 'cardNumber',
            'expiry_date': 'expiryDate',
            'cvv': 'cvv',
            'pin': 'pin'
        }
        self._card_number = card_number
        self._expiry_date = expiry_date
        self._cvv = cvv
        self._pin = pin

    @classmethod
    def from_dict(cls, dikt) -> 'LocateProfileResponseCardDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The locateProfileResponse_cardDetails of this LocateProfileResponseCardDetails.  # noqa: E501
        :rtype: LocateProfileResponseCardDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def card_number(self) -> str:
        """Gets the card_number of this LocateProfileResponseCardDetails.


        :return: The card_number of this LocateProfileResponseCardDetails.
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number: str):
        """Sets the card_number of this LocateProfileResponseCardDetails.


        :param card_number: The card_number of this LocateProfileResponseCardDetails.
        :type card_number: str
        """

        self._card_number = card_number

    @property
    def expiry_date(self) -> str:
        """Gets the expiry_date of this LocateProfileResponseCardDetails.


        :return: The expiry_date of this LocateProfileResponseCardDetails.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date: str):
        """Sets the expiry_date of this LocateProfileResponseCardDetails.


        :param expiry_date: The expiry_date of this LocateProfileResponseCardDetails.
        :type expiry_date: str
        """

        self._expiry_date = expiry_date

    @property
    def cvv(self) -> str:
        """Gets the cvv of this LocateProfileResponseCardDetails.


        :return: The cvv of this LocateProfileResponseCardDetails.
        :rtype: str
        """
        return self._cvv

    @cvv.setter
    def cvv(self, cvv: str):
        """Sets the cvv of this LocateProfileResponseCardDetails.


        :param cvv: The cvv of this LocateProfileResponseCardDetails.
        :type cvv: str
        """

        self._cvv = cvv

    @property
    def pin(self) -> str:
        """Gets the pin of this LocateProfileResponseCardDetails.


        :return: The pin of this LocateProfileResponseCardDetails.
        :rtype: str
        """
        return self._pin

    @pin.setter
    def pin(self, pin: str):
        """Sets the pin of this LocateProfileResponseCardDetails.


        :param pin: The pin of this LocateProfileResponseCardDetails.
        :type pin: str
        """

        self._pin = pin
