# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.get_customer_data_personal_banker import GetCustomerDataPersonalBanker  # noqa: F401,E501
from swagger_server.models.locate_profile_response_card_details import LocateProfileResponseCardDetails  # noqa: F401,E501
from swagger_server.models.locate_profile_response_multi_accounts import LocateProfileResponseMultiAccounts  # noqa: F401,E501
from swagger_server.models.locate_profile_response_personal_questions import LocateProfileResponsePersonalQuestions  # noqa: F401,E501
from swagger_server.models.locate_profile_response_warning_codes import LocateProfileResponseWarningCodes  # noqa: F401,E501
from swagger_server import util


class LocateProfileResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, account_number: str=None, card_details: LocateProfileResponseCardDetails=None, personal_questions: LocateProfileResponsePersonalQuestions=None, ss_number: float=None, ssn_short: float=None, alternate_phone_number: float=None, customer_id: str=None, email: str=None, identification_number: str=None, identification_type: str=None, image: str=None, is_alternate_mobile_number: bool=None, is_primary_mobile_number: bool=None, location: str=None, name: str=None, personal_banker: GetCustomerDataPersonalBanker=None, phone: float=None, security_questions: List[str]=None, segment_id: float=None, multi_accounts: List[LocateProfileResponseMultiAccounts]=None, warning_codes: List[LocateProfileResponseWarningCodes]=None):  # noqa: E501
        """LocateProfileResponse - a model defined in Swagger

        :param account_number: The account_number of this LocateProfileResponse.  # noqa: E501
        :type account_number: str
        :param card_details: The card_details of this LocateProfileResponse.  # noqa: E501
        :type card_details: LocateProfileResponseCardDetails
        :param personal_questions: The personal_questions of this LocateProfileResponse.  # noqa: E501
        :type personal_questions: LocateProfileResponsePersonalQuestions
        :param ss_number: The ss_number of this LocateProfileResponse.  # noqa: E501
        :type ss_number: float
        :param ssn_short: The ssn_short of this LocateProfileResponse.  # noqa: E501
        :type ssn_short: float
        :param alternate_phone_number: The alternate_phone_number of this LocateProfileResponse.  # noqa: E501
        :type alternate_phone_number: float
        :param customer_id: The customer_id of this LocateProfileResponse.  # noqa: E501
        :type customer_id: str
        :param email: The email of this LocateProfileResponse.  # noqa: E501
        :type email: str
        :param identification_number: The identification_number of this LocateProfileResponse.  # noqa: E501
        :type identification_number: str
        :param identification_type: The identification_type of this LocateProfileResponse.  # noqa: E501
        :type identification_type: str
        :param image: The image of this LocateProfileResponse.  # noqa: E501
        :type image: str
        :param is_alternate_mobile_number: The is_alternate_mobile_number of this LocateProfileResponse.  # noqa: E501
        :type is_alternate_mobile_number: bool
        :param is_primary_mobile_number: The is_primary_mobile_number of this LocateProfileResponse.  # noqa: E501
        :type is_primary_mobile_number: bool
        :param location: The location of this LocateProfileResponse.  # noqa: E501
        :type location: str
        :param name: The name of this LocateProfileResponse.  # noqa: E501
        :type name: str
        :param personal_banker: The personal_banker of this LocateProfileResponse.  # noqa: E501
        :type personal_banker: GetCustomerDataPersonalBanker
        :param phone: The phone of this LocateProfileResponse.  # noqa: E501
        :type phone: float
        :param security_questions: The security_questions of this LocateProfileResponse.  # noqa: E501
        :type security_questions: List[str]
        :param segment_id: The segment_id of this LocateProfileResponse.  # noqa: E501
        :type segment_id: float
        :param multi_accounts: The multi_accounts of this LocateProfileResponse.  # noqa: E501
        :type multi_accounts: List[LocateProfileResponseMultiAccounts]
        :param warning_codes: The warning_codes of this LocateProfileResponse.  # noqa: E501
        :type warning_codes: List[LocateProfileResponseWarningCodes]
        """
        self.swagger_types = {
            'account_number': str,
            'card_details': LocateProfileResponseCardDetails,
            'personal_questions': LocateProfileResponsePersonalQuestions,
            'ss_number': float,
            'ssn_short': float,
            'alternate_phone_number': float,
            'customer_id': str,
            'email': str,
            'identification_number': str,
            'identification_type': str,
            'image': str,
            'is_alternate_mobile_number': bool,
            'is_primary_mobile_number': bool,
            'location': str,
            'name': str,
            'personal_banker': GetCustomerDataPersonalBanker,
            'phone': float,
            'security_questions': List[str],
            'segment_id': float,
            'multi_accounts': List[LocateProfileResponseMultiAccounts],
            'warning_codes': List[LocateProfileResponseWarningCodes]
        }

        self.attribute_map = {
            'account_number': 'accountNumber',
            'card_details': 'cardDetails',
            'personal_questions': 'personalQuestions',
            'ss_number': 'ssNumber',
            'ssn_short': 'ssnShort',
            'alternate_phone_number': 'alternatePhoneNumber',
            'customer_id': 'customerId',
            'email': 'email',
            'identification_number': 'identificationNumber',
            'identification_type': 'identificationType',
            'image': 'image',
            'is_alternate_mobile_number': 'isAlternateMobileNumber',
            'is_primary_mobile_number': 'isPrimaryMobileNumber',
            'location': 'location',
            'name': 'name',
            'personal_banker': 'personalBanker',
            'phone': 'phone',
            'security_questions': 'securityQuestions',
            'segment_id': 'segmentId',
            'multi_accounts': 'multiAccounts',
            'warning_codes': 'warningCodes'
        }
        self._account_number = account_number
        self._card_details = card_details
        self._personal_questions = personal_questions
        self._ss_number = ss_number
        self._ssn_short = ssn_short
        self._alternate_phone_number = alternate_phone_number
        self._customer_id = customer_id
        self._email = email
        self._identification_number = identification_number
        self._identification_type = identification_type
        self._image = image
        self._is_alternate_mobile_number = is_alternate_mobile_number
        self._is_primary_mobile_number = is_primary_mobile_number
        self._location = location
        self._name = name
        self._personal_banker = personal_banker
        self._phone = phone
        self._security_questions = security_questions
        self._segment_id = segment_id
        self._multi_accounts = multi_accounts
        self._warning_codes = warning_codes

    @classmethod
    def from_dict(cls, dikt) -> 'LocateProfileResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The locateProfileResponse of this LocateProfileResponse.  # noqa: E501
        :rtype: LocateProfileResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_number(self) -> str:
        """Gets the account_number of this LocateProfileResponse.


        :return: The account_number of this LocateProfileResponse.
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number: str):
        """Sets the account_number of this LocateProfileResponse.


        :param account_number: The account_number of this LocateProfileResponse.
        :type account_number: str
        """

        self._account_number = account_number

    @property
    def card_details(self) -> LocateProfileResponseCardDetails:
        """Gets the card_details of this LocateProfileResponse.


        :return: The card_details of this LocateProfileResponse.
        :rtype: LocateProfileResponseCardDetails
        """
        return self._card_details

    @card_details.setter
    def card_details(self, card_details: LocateProfileResponseCardDetails):
        """Sets the card_details of this LocateProfileResponse.


        :param card_details: The card_details of this LocateProfileResponse.
        :type card_details: LocateProfileResponseCardDetails
        """

        self._card_details = card_details

    @property
    def personal_questions(self) -> LocateProfileResponsePersonalQuestions:
        """Gets the personal_questions of this LocateProfileResponse.


        :return: The personal_questions of this LocateProfileResponse.
        :rtype: LocateProfileResponsePersonalQuestions
        """
        return self._personal_questions

    @personal_questions.setter
    def personal_questions(self, personal_questions: LocateProfileResponsePersonalQuestions):
        """Sets the personal_questions of this LocateProfileResponse.


        :param personal_questions: The personal_questions of this LocateProfileResponse.
        :type personal_questions: LocateProfileResponsePersonalQuestions
        """

        self._personal_questions = personal_questions

    @property
    def ss_number(self) -> float:
        """Gets the ss_number of this LocateProfileResponse.


        :return: The ss_number of this LocateProfileResponse.
        :rtype: float
        """
        return self._ss_number

    @ss_number.setter
    def ss_number(self, ss_number: float):
        """Sets the ss_number of this LocateProfileResponse.


        :param ss_number: The ss_number of this LocateProfileResponse.
        :type ss_number: float
        """

        self._ss_number = ss_number

    @property
    def ssn_short(self) -> float:
        """Gets the ssn_short of this LocateProfileResponse.


        :return: The ssn_short of this LocateProfileResponse.
        :rtype: float
        """
        return self._ssn_short

    @ssn_short.setter
    def ssn_short(self, ssn_short: float):
        """Sets the ssn_short of this LocateProfileResponse.


        :param ssn_short: The ssn_short of this LocateProfileResponse.
        :type ssn_short: float
        """

        self._ssn_short = ssn_short

    @property
    def alternate_phone_number(self) -> float:
        """Gets the alternate_phone_number of this LocateProfileResponse.


        :return: The alternate_phone_number of this LocateProfileResponse.
        :rtype: float
        """
        return self._alternate_phone_number

    @alternate_phone_number.setter
    def alternate_phone_number(self, alternate_phone_number: float):
        """Sets the alternate_phone_number of this LocateProfileResponse.


        :param alternate_phone_number: The alternate_phone_number of this LocateProfileResponse.
        :type alternate_phone_number: float
        """

        self._alternate_phone_number = alternate_phone_number

    @property
    def customer_id(self) -> str:
        """Gets the customer_id of this LocateProfileResponse.


        :return: The customer_id of this LocateProfileResponse.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id: str):
        """Sets the customer_id of this LocateProfileResponse.


        :param customer_id: The customer_id of this LocateProfileResponse.
        :type customer_id: str
        """

        self._customer_id = customer_id

    @property
    def email(self) -> str:
        """Gets the email of this LocateProfileResponse.


        :return: The email of this LocateProfileResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this LocateProfileResponse.


        :param email: The email of this LocateProfileResponse.
        :type email: str
        """

        self._email = email

    @property
    def identification_number(self) -> str:
        """Gets the identification_number of this LocateProfileResponse.


        :return: The identification_number of this LocateProfileResponse.
        :rtype: str
        """
        return self._identification_number

    @identification_number.setter
    def identification_number(self, identification_number: str):
        """Sets the identification_number of this LocateProfileResponse.


        :param identification_number: The identification_number of this LocateProfileResponse.
        :type identification_number: str
        """

        self._identification_number = identification_number

    @property
    def identification_type(self) -> str:
        """Gets the identification_type of this LocateProfileResponse.


        :return: The identification_type of this LocateProfileResponse.
        :rtype: str
        """
        return self._identification_type

    @identification_type.setter
    def identification_type(self, identification_type: str):
        """Sets the identification_type of this LocateProfileResponse.


        :param identification_type: The identification_type of this LocateProfileResponse.
        :type identification_type: str
        """

        self._identification_type = identification_type

    @property
    def image(self) -> str:
        """Gets the image of this LocateProfileResponse.


        :return: The image of this LocateProfileResponse.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image: str):
        """Sets the image of this LocateProfileResponse.


        :param image: The image of this LocateProfileResponse.
        :type image: str
        """

        self._image = image

    @property
    def is_alternate_mobile_number(self) -> bool:
        """Gets the is_alternate_mobile_number of this LocateProfileResponse.


        :return: The is_alternate_mobile_number of this LocateProfileResponse.
        :rtype: bool
        """
        return self._is_alternate_mobile_number

    @is_alternate_mobile_number.setter
    def is_alternate_mobile_number(self, is_alternate_mobile_number: bool):
        """Sets the is_alternate_mobile_number of this LocateProfileResponse.


        :param is_alternate_mobile_number: The is_alternate_mobile_number of this LocateProfileResponse.
        :type is_alternate_mobile_number: bool
        """

        self._is_alternate_mobile_number = is_alternate_mobile_number

    @property
    def is_primary_mobile_number(self) -> bool:
        """Gets the is_primary_mobile_number of this LocateProfileResponse.


        :return: The is_primary_mobile_number of this LocateProfileResponse.
        :rtype: bool
        """
        return self._is_primary_mobile_number

    @is_primary_mobile_number.setter
    def is_primary_mobile_number(self, is_primary_mobile_number: bool):
        """Sets the is_primary_mobile_number of this LocateProfileResponse.


        :param is_primary_mobile_number: The is_primary_mobile_number of this LocateProfileResponse.
        :type is_primary_mobile_number: bool
        """

        self._is_primary_mobile_number = is_primary_mobile_number

    @property
    def location(self) -> str:
        """Gets the location of this LocateProfileResponse.


        :return: The location of this LocateProfileResponse.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """Sets the location of this LocateProfileResponse.


        :param location: The location of this LocateProfileResponse.
        :type location: str
        """

        self._location = location

    @property
    def name(self) -> str:
        """Gets the name of this LocateProfileResponse.


        :return: The name of this LocateProfileResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this LocateProfileResponse.


        :param name: The name of this LocateProfileResponse.
        :type name: str
        """

        self._name = name

    @property
    def personal_banker(self) -> GetCustomerDataPersonalBanker:
        """Gets the personal_banker of this LocateProfileResponse.


        :return: The personal_banker of this LocateProfileResponse.
        :rtype: GetCustomerDataPersonalBanker
        """
        return self._personal_banker

    @personal_banker.setter
    def personal_banker(self, personal_banker: GetCustomerDataPersonalBanker):
        """Sets the personal_banker of this LocateProfileResponse.


        :param personal_banker: The personal_banker of this LocateProfileResponse.
        :type personal_banker: GetCustomerDataPersonalBanker
        """

        self._personal_banker = personal_banker

    @property
    def phone(self) -> float:
        """Gets the phone of this LocateProfileResponse.


        :return: The phone of this LocateProfileResponse.
        :rtype: float
        """
        return self._phone

    @phone.setter
    def phone(self, phone: float):
        """Sets the phone of this LocateProfileResponse.


        :param phone: The phone of this LocateProfileResponse.
        :type phone: float
        """

        self._phone = phone

    @property
    def security_questions(self) -> List[str]:
        """Gets the security_questions of this LocateProfileResponse.


        :return: The security_questions of this LocateProfileResponse.
        :rtype: List[str]
        """
        return self._security_questions

    @security_questions.setter
    def security_questions(self, security_questions: List[str]):
        """Sets the security_questions of this LocateProfileResponse.


        :param security_questions: The security_questions of this LocateProfileResponse.
        :type security_questions: List[str]
        """

        self._security_questions = security_questions

    @property
    def segment_id(self) -> float:
        """Gets the segment_id of this LocateProfileResponse.


        :return: The segment_id of this LocateProfileResponse.
        :rtype: float
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id: float):
        """Sets the segment_id of this LocateProfileResponse.


        :param segment_id: The segment_id of this LocateProfileResponse.
        :type segment_id: float
        """

        self._segment_id = segment_id

    @property
    def multi_accounts(self) -> List[LocateProfileResponseMultiAccounts]:
        """Gets the multi_accounts of this LocateProfileResponse.


        :return: The multi_accounts of this LocateProfileResponse.
        :rtype: List[LocateProfileResponseMultiAccounts]
        """
        return self._multi_accounts

    @multi_accounts.setter
    def multi_accounts(self, multi_accounts: List[LocateProfileResponseMultiAccounts]):
        """Sets the multi_accounts of this LocateProfileResponse.


        :param multi_accounts: The multi_accounts of this LocateProfileResponse.
        :type multi_accounts: List[LocateProfileResponseMultiAccounts]
        """

        self._multi_accounts = multi_accounts

    @property
    def warning_codes(self) -> List[LocateProfileResponseWarningCodes]:
        """Gets the warning_codes of this LocateProfileResponse.


        :return: The warning_codes of this LocateProfileResponse.
        :rtype: List[LocateProfileResponseWarningCodes]
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, warning_codes: List[LocateProfileResponseWarningCodes]):
        """Sets the warning_codes of this LocateProfileResponse.


        :param warning_codes: The warning_codes of this LocateProfileResponse.
        :type warning_codes: List[LocateProfileResponseWarningCodes]
        """

        self._warning_codes = warning_codes
