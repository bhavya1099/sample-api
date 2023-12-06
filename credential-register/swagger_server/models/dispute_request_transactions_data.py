# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DisputeRequestTransactionsData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, transaction_id: float=None, reason_code: str=None):  # noqa: E501
        """DisputeRequestTransactionsData - a model defined in Swagger

        :param transaction_id: The transaction_id of this DisputeRequestTransactionsData.  # noqa: E501
        :type transaction_id: float
        :param reason_code: The reason_code of this DisputeRequestTransactionsData.  # noqa: E501
        :type reason_code: str
        """
        self.swagger_types = {
            'transaction_id': float,
            'reason_code': str
        }

        self.attribute_map = {
            'transaction_id': 'transactionId',
            'reason_code': 'reasonCode'
        }
        self._transaction_id = transaction_id
        self._reason_code = reason_code

    @classmethod
    def from_dict(cls, dikt) -> 'DisputeRequestTransactionsData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The disputeRequest_transactionsData of this DisputeRequestTransactionsData.  # noqa: E501
        :rtype: DisputeRequestTransactionsData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def transaction_id(self) -> float:
        """Gets the transaction_id of this DisputeRequestTransactionsData.


        :return: The transaction_id of this DisputeRequestTransactionsData.
        :rtype: float
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id: float):
        """Sets the transaction_id of this DisputeRequestTransactionsData.


        :param transaction_id: The transaction_id of this DisputeRequestTransactionsData.
        :type transaction_id: float
        """
        if transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def reason_code(self) -> str:
        """Gets the reason_code of this DisputeRequestTransactionsData.

        CHRG-AMNT-MORE - expectedAmount, CHRG-MULTPLE-TIME - duplicateTxnId, CANCL-PURCH & CANCL-REC-CHRG - cancelledAt CANCl-RECV-GD-SERV - purchasedAt & cancelledAt, INDESC-GD-SERV - customerDescription, UIDENTF-CHRG - NA  codes requires the corresponding fields mapped to it  # noqa: E501

        :return: The reason_code of this DisputeRequestTransactionsData.
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code: str):
        """Sets the reason_code of this DisputeRequestTransactionsData.

        CHRG-AMNT-MORE - expectedAmount, CHRG-MULTPLE-TIME - duplicateTxnId, CANCL-PURCH & CANCL-REC-CHRG - cancelledAt CANCl-RECV-GD-SERV - purchasedAt & cancelledAt, INDESC-GD-SERV - customerDescription, UIDENTF-CHRG - NA  codes requires the corresponding fields mapped to it  # noqa: E501

        :param reason_code: The reason_code of this DisputeRequestTransactionsData.
        :type reason_code: str
        """
        if reason_code is None:
            raise ValueError("Invalid value for `reason_code`, must not be `None`")  # noqa: E501

        self._reason_code = reason_code
