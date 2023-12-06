# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.get_account_data_accounts_autopay import GetAccountDataAccountsAutopay  # noqa: F401,E501
from swagger_server.models.get_account_data_accounts_card_channel_info import GetAccountDataAccountsCardChannelInfo  # noqa: F401,E501
from swagger_server.models.get_account_data_accounts_card_restrictions import GetAccountDataAccountsCardRestrictions  # noqa: F401,E501
from swagger_server import util


class GetAccountDataAccountsCardDetails(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, card_name: str=None, card_number: str=None, card_status: str=None, card_image: str=None, card_type: str=None, exp_date: str=None, display_card_status: str=None, primary_card: str=None, card_channel_info: GetAccountDataAccountsCardChannelInfo=None, card_restrictions: GetAccountDataAccountsCardRestrictions=None, block_reason: str=None, name_on_card: str=None, card_network: str=None, autopay: GetAccountDataAccountsAutopay=None, due_amount: float=None, due_date: str=None, minimum_payment_due: float=None, partial_payment_paid: float=None):  # noqa: E501
        """GetAccountDataAccountsCardDetails - a model defined in Swagger

        :param card_name: The card_name of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type card_name: str
        :param card_number: The card_number of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type card_number: str
        :param card_status: The card_status of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type card_status: str
        :param card_image: The card_image of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type card_image: str
        :param card_type: The card_type of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type card_type: str
        :param exp_date: The exp_date of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type exp_date: str
        :param display_card_status: The display_card_status of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type display_card_status: str
        :param primary_card: The primary_card of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type primary_card: str
        :param card_channel_info: The card_channel_info of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type card_channel_info: GetAccountDataAccountsCardChannelInfo
        :param card_restrictions: The card_restrictions of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type card_restrictions: GetAccountDataAccountsCardRestrictions
        :param block_reason: The block_reason of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type block_reason: str
        :param name_on_card: The name_on_card of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type name_on_card: str
        :param card_network: The card_network of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type card_network: str
        :param autopay: The autopay of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type autopay: GetAccountDataAccountsAutopay
        :param due_amount: The due_amount of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type due_amount: float
        :param due_date: The due_date of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type due_date: str
        :param minimum_payment_due: The minimum_payment_due of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type minimum_payment_due: float
        :param partial_payment_paid: The partial_payment_paid of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :type partial_payment_paid: float
        """
        self.swagger_types = {
            'card_name': str,
            'card_number': str,
            'card_status': str,
            'card_image': str,
            'card_type': str,
            'exp_date': str,
            'display_card_status': str,
            'primary_card': str,
            'card_channel_info': GetAccountDataAccountsCardChannelInfo,
            'card_restrictions': GetAccountDataAccountsCardRestrictions,
            'block_reason': str,
            'name_on_card': str,
            'card_network': str,
            'autopay': GetAccountDataAccountsAutopay,
            'due_amount': float,
            'due_date': str,
            'minimum_payment_due': float,
            'partial_payment_paid': float
        }

        self.attribute_map = {
            'card_name': 'cardName',
            'card_number': 'cardNumber',
            'card_status': 'cardStatus',
            'card_image': 'cardImage',
            'card_type': 'cardType',
            'exp_date': 'expDate',
            'display_card_status': 'displayCardStatus',
            'primary_card': 'primaryCard',
            'card_channel_info': 'cardChannelInfo',
            'card_restrictions': 'cardRestrictions',
            'block_reason': 'blockReason',
            'name_on_card': 'nameOnCard',
            'card_network': 'cardNetwork',
            'autopay': 'autopay',
            'due_amount': 'dueAmount',
            'due_date': 'dueDate',
            'minimum_payment_due': 'minimumPaymentDue',
            'partial_payment_paid': 'partialPaymentPaid'
        }
        self._card_name = card_name
        self._card_number = card_number
        self._card_status = card_status
        self._card_image = card_image
        self._card_type = card_type
        self._exp_date = exp_date
        self._display_card_status = display_card_status
        self._primary_card = primary_card
        self._card_channel_info = card_channel_info
        self._card_restrictions = card_restrictions
        self._block_reason = block_reason
        self._name_on_card = name_on_card
        self._card_network = card_network
        self._autopay = autopay
        self._due_amount = due_amount
        self._due_date = due_date
        self._minimum_payment_due = minimum_payment_due
        self._partial_payment_paid = partial_payment_paid

    @classmethod
    def from_dict(cls, dikt) -> 'GetAccountDataAccountsCardDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The getAccountData_accounts_cardDetails of this GetAccountDataAccountsCardDetails.  # noqa: E501
        :rtype: GetAccountDataAccountsCardDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def card_name(self) -> str:
        """Gets the card_name of this GetAccountDataAccountsCardDetails.


        :return: The card_name of this GetAccountDataAccountsCardDetails.
        :rtype: str
        """
        return self._card_name

    @card_name.setter
    def card_name(self, card_name: str):
        """Sets the card_name of this GetAccountDataAccountsCardDetails.


        :param card_name: The card_name of this GetAccountDataAccountsCardDetails.
        :type card_name: str
        """

        self._card_name = card_name

    @property
    def card_number(self) -> str:
        """Gets the card_number of this GetAccountDataAccountsCardDetails.


        :return: The card_number of this GetAccountDataAccountsCardDetails.
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number: str):
        """Sets the card_number of this GetAccountDataAccountsCardDetails.


        :param card_number: The card_number of this GetAccountDataAccountsCardDetails.
        :type card_number: str
        """

        self._card_number = card_number

    @property
    def card_status(self) -> str:
        """Gets the card_status of this GetAccountDataAccountsCardDetails.


        :return: The card_status of this GetAccountDataAccountsCardDetails.
        :rtype: str
        """
        return self._card_status

    @card_status.setter
    def card_status(self, card_status: str):
        """Sets the card_status of this GetAccountDataAccountsCardDetails.


        :param card_status: The card_status of this GetAccountDataAccountsCardDetails.
        :type card_status: str
        """

        self._card_status = card_status

    @property
    def card_image(self) -> str:
        """Gets the card_image of this GetAccountDataAccountsCardDetails.


        :return: The card_image of this GetAccountDataAccountsCardDetails.
        :rtype: str
        """
        return self._card_image

    @card_image.setter
    def card_image(self, card_image: str):
        """Sets the card_image of this GetAccountDataAccountsCardDetails.


        :param card_image: The card_image of this GetAccountDataAccountsCardDetails.
        :type card_image: str
        """

        self._card_image = card_image

    @property
    def card_type(self) -> str:
        """Gets the card_type of this GetAccountDataAccountsCardDetails.


        :return: The card_type of this GetAccountDataAccountsCardDetails.
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type: str):
        """Sets the card_type of this GetAccountDataAccountsCardDetails.


        :param card_type: The card_type of this GetAccountDataAccountsCardDetails.
        :type card_type: str
        """

        self._card_type = card_type

    @property
    def exp_date(self) -> str:
        """Gets the exp_date of this GetAccountDataAccountsCardDetails.


        :return: The exp_date of this GetAccountDataAccountsCardDetails.
        :rtype: str
        """
        return self._exp_date

    @exp_date.setter
    def exp_date(self, exp_date: str):
        """Sets the exp_date of this GetAccountDataAccountsCardDetails.


        :param exp_date: The exp_date of this GetAccountDataAccountsCardDetails.
        :type exp_date: str
        """

        self._exp_date = exp_date

    @property
    def display_card_status(self) -> str:
        """Gets the display_card_status of this GetAccountDataAccountsCardDetails.


        :return: The display_card_status of this GetAccountDataAccountsCardDetails.
        :rtype: str
        """
        return self._display_card_status

    @display_card_status.setter
    def display_card_status(self, display_card_status: str):
        """Sets the display_card_status of this GetAccountDataAccountsCardDetails.


        :param display_card_status: The display_card_status of this GetAccountDataAccountsCardDetails.
        :type display_card_status: str
        """

        self._display_card_status = display_card_status

    @property
    def primary_card(self) -> str:
        """Gets the primary_card of this GetAccountDataAccountsCardDetails.


        :return: The primary_card of this GetAccountDataAccountsCardDetails.
        :rtype: str
        """
        return self._primary_card

    @primary_card.setter
    def primary_card(self, primary_card: str):
        """Sets the primary_card of this GetAccountDataAccountsCardDetails.


        :param primary_card: The primary_card of this GetAccountDataAccountsCardDetails.
        :type primary_card: str
        """

        self._primary_card = primary_card

    @property
    def card_channel_info(self) -> GetAccountDataAccountsCardChannelInfo:
        """Gets the card_channel_info of this GetAccountDataAccountsCardDetails.


        :return: The card_channel_info of this GetAccountDataAccountsCardDetails.
        :rtype: GetAccountDataAccountsCardChannelInfo
        """
        return self._card_channel_info

    @card_channel_info.setter
    def card_channel_info(self, card_channel_info: GetAccountDataAccountsCardChannelInfo):
        """Sets the card_channel_info of this GetAccountDataAccountsCardDetails.


        :param card_channel_info: The card_channel_info of this GetAccountDataAccountsCardDetails.
        :type card_channel_info: GetAccountDataAccountsCardChannelInfo
        """

        self._card_channel_info = card_channel_info

    @property
    def card_restrictions(self) -> GetAccountDataAccountsCardRestrictions:
        """Gets the card_restrictions of this GetAccountDataAccountsCardDetails.


        :return: The card_restrictions of this GetAccountDataAccountsCardDetails.
        :rtype: GetAccountDataAccountsCardRestrictions
        """
        return self._card_restrictions

    @card_restrictions.setter
    def card_restrictions(self, card_restrictions: GetAccountDataAccountsCardRestrictions):
        """Sets the card_restrictions of this GetAccountDataAccountsCardDetails.


        :param card_restrictions: The card_restrictions of this GetAccountDataAccountsCardDetails.
        :type card_restrictions: GetAccountDataAccountsCardRestrictions
        """

        self._card_restrictions = card_restrictions

    @property
    def block_reason(self) -> str:
        """Gets the block_reason of this GetAccountDataAccountsCardDetails.


        :return: The block_reason of this GetAccountDataAccountsCardDetails.
        :rtype: str
        """
        return self._block_reason

    @block_reason.setter
    def block_reason(self, block_reason: str):
        """Sets the block_reason of this GetAccountDataAccountsCardDetails.


        :param block_reason: The block_reason of this GetAccountDataAccountsCardDetails.
        :type block_reason: str
        """

        self._block_reason = block_reason

    @property
    def name_on_card(self) -> str:
        """Gets the name_on_card of this GetAccountDataAccountsCardDetails.


        :return: The name_on_card of this GetAccountDataAccountsCardDetails.
        :rtype: str
        """
        return self._name_on_card

    @name_on_card.setter
    def name_on_card(self, name_on_card: str):
        """Sets the name_on_card of this GetAccountDataAccountsCardDetails.


        :param name_on_card: The name_on_card of this GetAccountDataAccountsCardDetails.
        :type name_on_card: str
        """

        self._name_on_card = name_on_card

    @property
    def card_network(self) -> str:
        """Gets the card_network of this GetAccountDataAccountsCardDetails.


        :return: The card_network of this GetAccountDataAccountsCardDetails.
        :rtype: str
        """
        return self._card_network

    @card_network.setter
    def card_network(self, card_network: str):
        """Sets the card_network of this GetAccountDataAccountsCardDetails.


        :param card_network: The card_network of this GetAccountDataAccountsCardDetails.
        :type card_network: str
        """

        self._card_network = card_network

    @property
    def autopay(self) -> GetAccountDataAccountsAutopay:
        """Gets the autopay of this GetAccountDataAccountsCardDetails.


        :return: The autopay of this GetAccountDataAccountsCardDetails.
        :rtype: GetAccountDataAccountsAutopay
        """
        return self._autopay

    @autopay.setter
    def autopay(self, autopay: GetAccountDataAccountsAutopay):
        """Sets the autopay of this GetAccountDataAccountsCardDetails.


        :param autopay: The autopay of this GetAccountDataAccountsCardDetails.
        :type autopay: GetAccountDataAccountsAutopay
        """

        self._autopay = autopay

    @property
    def due_amount(self) -> float:
        """Gets the due_amount of this GetAccountDataAccountsCardDetails.


        :return: The due_amount of this GetAccountDataAccountsCardDetails.
        :rtype: float
        """
        return self._due_amount

    @due_amount.setter
    def due_amount(self, due_amount: float):
        """Sets the due_amount of this GetAccountDataAccountsCardDetails.


        :param due_amount: The due_amount of this GetAccountDataAccountsCardDetails.
        :type due_amount: float
        """

        self._due_amount = due_amount

    @property
    def due_date(self) -> str:
        """Gets the due_date of this GetAccountDataAccountsCardDetails.


        :return: The due_date of this GetAccountDataAccountsCardDetails.
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date: str):
        """Sets the due_date of this GetAccountDataAccountsCardDetails.


        :param due_date: The due_date of this GetAccountDataAccountsCardDetails.
        :type due_date: str
        """

        self._due_date = due_date

    @property
    def minimum_payment_due(self) -> float:
        """Gets the minimum_payment_due of this GetAccountDataAccountsCardDetails.


        :return: The minimum_payment_due of this GetAccountDataAccountsCardDetails.
        :rtype: float
        """
        return self._minimum_payment_due

    @minimum_payment_due.setter
    def minimum_payment_due(self, minimum_payment_due: float):
        """Sets the minimum_payment_due of this GetAccountDataAccountsCardDetails.


        :param minimum_payment_due: The minimum_payment_due of this GetAccountDataAccountsCardDetails.
        :type minimum_payment_due: float
        """

        self._minimum_payment_due = minimum_payment_due

    @property
    def partial_payment_paid(self) -> float:
        """Gets the partial_payment_paid of this GetAccountDataAccountsCardDetails.


        :return: The partial_payment_paid of this GetAccountDataAccountsCardDetails.
        :rtype: float
        """
        return self._partial_payment_paid

    @partial_payment_paid.setter
    def partial_payment_paid(self, partial_payment_paid: float):
        """Sets the partial_payment_paid of this GetAccountDataAccountsCardDetails.


        :param partial_payment_paid: The partial_payment_paid of this GetAccountDataAccountsCardDetails.
        :type partial_payment_paid: float
        """

        self._partial_payment_paid = partial_payment_paid
