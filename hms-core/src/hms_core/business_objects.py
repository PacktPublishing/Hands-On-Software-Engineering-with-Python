#!/usr/bin/env python
"""
Package-header for the hms_core namespace. 
Provides classes and functionality for SOME_PURPOSE
"""

#######################################
# Create an "__all__" list to support #
#   "from module import member" use   #
#######################################

__all__ = [
    # Constants
    # Exceptions
    # Functions
    # ABC "interface" classes
    # ABC abstract classes
    'BaseArtisan',
    'BaseCustomer',
    'BaseOrder',
    'BaseProduct',
    'HasProducts',
    # Concrete classes
    'Address',
    # Child packages and modules
]

#######################################
# Module metadata/dunder-names        #
#######################################

__author__ = 'Brian D. Allbee'
__copyright__ = 'Copyright 2018, all rights reserved'
__status__ = 'Development'

#######################################
# Standard library imports needed     #
#######################################

import abc
import re

from email.utils import parseaddr

#######################################
# Third-party imports needed          #
#######################################

#######################################
# Local imports needed                #
#######################################

#######################################
# Initialization needed before member #
#   definition can take place         #
#######################################

#######################################
# Module-level Constants              #
#######################################

EMAIL_CHECK = re.compile(
    r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
)
URL_CHECK = re.compile(
    r'(^https?://[A-Za-z0-9][-_A-Za-z0-9]*\.[A-Za-z0-9][-_A-Za-z0-9\.]*$)'
)

#######################################
# Custom Exceptions                   #
#######################################

#######################################
# Module functions                    #
#######################################

#######################################
# Out of normal position due to       #
# dependency on Address in            #
# BaseArtisan's address property      #
# annotations                         #
#######################################

# TODO: Consider whether Address needs some sort of validation 
#       mechanism that can leverage pycountry to assure that 
#       county/region combinations are kosher.
# TODO: Maybe we need some sort of export-mechanism? Or a 
#       label-ready output?
# TODO: Consider what can/should happen if a non-default property-
#       value is deleted in an instance. If a required value is 
#       deleted, the instance is no longer well-formed...
class Address:
    """
Represents a physical mailing-address/location
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    # - Default values for properties, used by deleter methods
    _building_address = None
    _city = None
    _country = None
    _region = None
    _postal_code = None
    _street_address = None

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_building_address(self) -> (str,None):
        return self._building_address

    def _get_city(self) -> str:
        return self._city

    def _get_country(self) -> (str,None):
        return self._country

    def _get_region(self) -> (str,None):
        return self._region

    def _get_postal_code(self) -> (str,None):
        return self._postal_code

    def _get_street_address(self) -> str:
        return self._street_address

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_building_address(self, value:(str,None)) -> None:
        if value != None:
            # - Type-check: If the value isn't None, then it has to 
            #   be a non-empty, single-line string without tabs
            if type(value) != str:
                raise TypeError(
                    '%s.building_address expects a single-line, '
                    'non-empty str value, with no whitespace '
                    'other than spaces or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - Value-check: no whitespace other than " "
            bad_chars = ('\n', '\r', '\t')
            is_valid = True
            for bad_char in bad_chars:
                if bad_char in value:
                    is_valid = False
                    break
            # - If it's empty or otherwise not valid, raise error
            if not value.strip() or not is_valid:
                raise ValueError(
                    '%s.building_address expects a single-line, '
                    'non-empty str value, with no whitespace '
                    'other than spaces or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - If this point is reached without error, then the 
            #   string-value is valid, so we can just exit the if
        self._building_address = value

    def _set_city(self, value:str) -> None:
        # - Type-check: This is a required str value
        if type(value) != str:
            raise TypeError(
                '%s.city expects a single-line, '
                'non-empty str value, with no whitespace '
                'other than spaces, but was passed '
                '"%s" (%s)' % 
                (
                    self.__class__.__name__, value, 
                    type(value).__name__
                )
            )
        # - Value-check: no whitespace other than " "
        bad_chars = ('\n', '\r', '\t')
        is_valid = True
        for bad_char in bad_chars:
            if bad_char in value:
                is_valid = False
                break
        # - If it's empty or otherwise not valid, raise error
        if not value.strip() or not is_valid:
            raise ValueError(
                '%s.city expects a single-line, '
                'non-empty str value, with no whitespace '
                'other than spaces, but was passed '
                '"%s" (%s)' % 
                (
                    self.__class__.__name__, value, 
                    type(value).__name__
                )
            )
        # - Everything checks out, so set the attribute
        self._city = value

    def _set_country(self, value:(str,None)) -> None:
        if value != None:
            # - Type-check: If the value isn't None, then it has to 
            #   be a non-empty, single-line string without tabs
            if type(value) != str:
                raise TypeError(
                    '%s.country expects a single-line, '
                    'non-empty str value, with no whitespace '
                    'other than spaces or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - Value-check: no whitespace other than " "
            bad_chars = ('\n', '\r', '\t')
            is_valid = True
            for bad_char in bad_chars:
                if bad_char in value:
                    is_valid = False
                    break
            # - If it's empty or otherwise not valid, raise error
            if not value.strip() or not is_valid:
                raise ValueError(
                    '%s.country expects a single-line, '
                    'non-empty str value, with no whitespace '
                    'other than spaces or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - If this point is reached without error, then the 
            #   string-value is valid, so we can just exit the if
        self._country = value

    def _set_region(self, value:(str,None)) -> None:
        if value != None:
            # - Type-check: If the value isn't None, then it has to 
            #   be a non-empty, single-line string without tabs
            if type(value) != str:
                raise TypeError(
                    '%s.region expects a single-line, '
                    'non-empty str value, with no whitespace '
                    'other than spaces or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - Value-check: no whitespace other than " "
            bad_chars = ('\n', '\r', '\t')
            is_valid = True
            for bad_char in bad_chars:
                if bad_char in value:
                    is_valid = False
                    break
            # - If it's empty or otherwise not valid, raise error
            if not value.strip() or not is_valid:
                raise ValueError(
                    '%s.region expects a single-line, '
                    'non-empty str value, with no whitespace '
                    'other than spaces or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - If this point is reached without error, then the 
            #   string-value is valid, so we can just exit the if
        self._region = value

    def _set_postal_code(self, value:(str,None)) -> None:
        if value != None:
            # - Type-check: If the value isn't None, then it has to 
            #   be a non-empty, single-line string without tabs
            if type(value) != str:
                raise TypeError(
                    '%s.postal_code expects a single-line, '
                    'non-empty str value, with no whitespace '
                    'other than spaces or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - Value-check: no whitespace other than " "
            bad_chars = ('\n', '\r', '\t')
            is_valid = True
            for bad_char in bad_chars:
                if bad_char in value:
                    is_valid = False
                    break
            # - If it's empty or otherwise not valid, raise error
            if not value.strip() or not is_valid:
                raise ValueError(
                    '%s.postal_code expects a single-line, '
                    'non-empty str value, with no whitespace '
                    'other than spaces or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - If this point is reached without error, then the 
            #   string-value is valid, so we can just exit the if
        self._postal_code = value

    def _set_street_address(self, value:str) -> None:
        # - Type-check: This is a required str value
        if type(value) != str:
            raise TypeError(
                '%s.street_address expects a single-line, '
                'non-empty str value, with no whitespace '
                'other than spaces, but was passed '
                '"%s" (%s)' % 
                (
                    self.__class__.__name__, value, 
                    type(value).__name__
                )
            )
        # - Value-check: no whitespace other than " "
        bad_chars = ('\n', '\r', '\t')
        is_valid = True
        for bad_char in bad_chars:
            if bad_char in value:
                is_valid = False
                break
        # - If it's empty or otherwise not valid, raise error
        if not value.strip() or not is_valid:
            raise ValueError(
                '%s.street_address expects a single-line, '
                'non-empty str value, with no whitespace '
                'other than spaces, but was passed '
                '"%s" (%s)' % 
                (
                    self.__class__.__name__, value, 
                    type(value).__name__
                )
            )
        # - Everything checks out, so set the attribute
        self._street_address = value

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_building_address(self) -> None:
        self._building_address = None

    def _del_city(self) -> None:
        self._city = None

    def _del_country(self) -> None:
        self._country = None

    def _del_region(self) -> None:
        self._region = None

    def _del_postal_code(self) -> None:
        self._postal_code = None

    def _del_street_address(self) -> None:
        self._street_address = None

    ###################################
    # Instance property definitions   #
    ###################################

    building_address = property(
        _get_building_address, _set_building_address, 
        _del_building_address, 
        'Gets, sets or deletes the building_address (str|None) '
        'of the instance'
    )
    city = property(
        _get_city, _set_city, _del_city, 
        'Gets, sets or deletes the city (str) of the instance'
    )
    country = property(
        _get_country, _set_country, _del_country, 
        'Gets, sets or deletes the country (str|None) of the '
        'instance'
    )
    region = property(
        _get_region, _set_region, _del_region, 
        'Gets, sets or deletes the region (str|None) of the '
        'instance'
    )
    postal_code = property(
        _get_postal_code, _set_postal_code, _del_postal_code, 
        'Gets, sets or deletes the postal_code (str|None) of '
        'the instance'
    )
    street_address = property(
        _get_street_address, _set_street_address, 
        _del_street_address, 
        'Gets, sets or deletes the street_address (str) of the '
        'instance'
    )

    ###################################
    # Object initialization           #
    ###################################

    def __init__(self, 
        street_address:(str,), city:(str,), 
        building_address:(str,None)=None, region:(str,None)=None, 
        postal_code:(str,None)=None, country:(str,None)=None
        ):
        """
Object initialization.

self .............. (Address instance, required) The instance to 
                    execute against
street_address .... (str, required) The base street-address of the 
                    location the instance represents
city .............. (str, required) The city portion of the street-
                    address that the instance represents
building_address .. (str, optional, defaults to None) The second 
                    line of the street address the instance represents, 
                    if applicable
region ............ (str, optional, defaults to None) The region 
                    (state, territory, etc.) portion of the street-
                    address that the instance represents
postal_code ....... (str, optional, defaults to None) The postal-code 
                    portion of the street-address that the instance 
                    represents
country ........... (str, optional, defaults to None) The country 
                    portion of the street-address that the instance 
                    represents
"""
        # - Call parent initializers if needed
        # - Set default instance property-values using _del_... methods
        self._del_building_address()
        self._del_city()
        self._del_country()
        self._del_postal_code()
        self._del_region()
        self._del_street_address()
        # - Set instance property-values from arguments using 
        #   _set_... methods
        self._set_street_address(street_address)
        self._set_city(city)
        if building_address:
            self._set_building_address(building_address)
        if region:
            self._set_region(region)
        if postal_code:
            self._set_postal_code(postal_code)
        if country:
            self._set_country(country)
        # - Perform any other initialization needed

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Instance methods                #
    ###################################

    def to_dict(self) -> (dict,):
        return {
            'street_address':self.street_address,
            'building_address':self.building_address,
            'city':self.city,
            'region':self.region,
            'postal_code':self.postal_code,
            'country':self.country
        }

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    @classmethod
    def standard_address(cls, 
            street_address:(str,), building_address:(str,None), 
            city:(str,), region:(str,None), postal_code:(str,None), 
            country:(str,None)
        ):
        return cls(
            street_address, city, building_address, 
            region, postal_code, country
        )

    ###################################
    # Static methods                  #
    ###################################

#######################################
# ABC "interface" classes             #
#######################################

# Out of normal alphabetical order because of dependencies in 
# method-annotations in BaseArtisan
class BaseProduct(metaclass=abc.ABCMeta):
    """TODO: Document the class.
Provides baseline functionality, interface requirements, and 
type-identity for objects that can REPRESENT_SOMETHING
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_available(self) -> (bool,):
        return self._available

    def _get_description(self) -> (str,None):
        return self._description

    def _get_dimensions(self) -> (str,None):
        return self._dimensions

    def _get_metadata(self) -> (dict,):
        return self._metadata

    def _get_name(self) -> (str,None):
        return self._name

    def _get_shipping_weight(self) -> (int,):
        return self._shipping_weight

    def _get_store_available(self) -> (bool,):
        return self._store_available

    def _get_summary(self) -> (str,None):
        return self._summary

#     def _get_property_name(self) -> str:
#         return self._property_name

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_available(self, value:(bool,int)):
        if value not in (True, False, 1, 0):
            raise ValueError(
                '%s.available expects either a boolean value '
                '(True|False) or a direct int-value equivalent '
                '(1|0), but was passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        if value:
            self._available = True
        else:
            self._available = False

    def _set_description(self, value:str) -> None:
        if value != None:
            # - Type-check: If the value isn't None, then it has to 
            #   be a non-empty, single-line string without tabs
            if type(value) != str:
                raise TypeError(
                    '%s.description expects a single-line, non-'
                    'empty str value, or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - If it's empty or otherwise not valid, raise error
            if not value.strip():
                raise ValueError(
                    '%s.description expects a single-line, non-'
                    'empty str value, or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - If this point is reached without error, then the 
            #   string-value is valid, so we can just exit the if
        self._description = value

    def _set_dimensions(self, value:str) -> None:
        if value != None:
            # - Type-check: If the value isn't None, then it has to 
            #   be a non-empty, single-line string without tabs
            if type(value) != str:
                raise TypeError(
                    '%s.dimensions expects a single-line, '
                    'non-empty str value, with no whitespace '
                    'other than spaces or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - Value-check: no whitespace other than " "
            bad_chars = ('\n', '\r', '\t')
            is_valid = True
            for bad_char in bad_chars:
                if bad_char in value:
                    is_valid = False
                    break
            # - If it's empty or otherwise not valid, raise error
            if not value.strip() or not is_valid:
                raise ValueError(
                    '%s.dimensions expects a single-line, '
                    'non-empty str value, with no whitespace '
                    'other than spaces or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - If this point is reached without error, then the 
            #   string-value is valid, so we can just exit the if
        self._dimensions = value

    def _set_metadata(self, value:(dict,)):
        if type(value) != dict:
            raise TypeError(
                '%s.metadata expects a dictionary of metadata keys '
                '(strings) and values (also strings), but was passed '
                '"%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        badvalues = []
        # - First, we want to clear out any existing metadata values...
        self._del_metadata()
        if value: # Checking because value could be an empty dict: {}
            # - Then we populate the clean internal attribute 
            #   with metadata:
            for name in value:
                try:
                    # - Since set_metadata will do all the type- and 
                    #   value-checking we need, we'll just call that 
                    #   for each item handed off to us here...
                    self.set_metadata(name, value[name])
                except Exception:
                    # - If an error was raised,then we want to capture 
                    #   the key/value pair that caused it...
                    badvalues.append((name, value[name]))
            if badvalues:
                # - Oops... Something's not right...
                raise ValueError(
                    '%s.metadata expects a dictionary of metadata keys '
                    '(strings) and values, but was passed a dict with '
                    'values that aren\'t allowed: %s' % 
                    (self.__class__.__name__, str(badvalues))
                )
            # - If we reach this point, then all values were good, 
            #   *and* they've been populated, so we can just exit...

    def _set_name(self, value:str) -> None:
        # - Type-check: If the value isn't None, then it has to 
        #   be a non-empty, single-line string without tabs
        if type(value) != str:
            raise TypeError(
                '%s.name expects a single-line, '
                'non-empty str value, with no whitespace '
                'other than spaces or None, but was passed '
                '"%s" (%s)' % 
                (
                    self.__class__.__name__, value, 
                    type(value).__name__
                )
            )
        # - Value-check: no whitespace other than " "
        bad_chars = ('\n', '\r', '\t')
        is_valid = True
        for bad_char in bad_chars:
            if bad_char in value:
                is_valid = False
                break
        # - If it's empty or otherwise not valid, raise error
        if not value.strip() or not is_valid:
            raise ValueError(
                '%s.name expects a single-line, '
                'non-empty str value, with no whitespace '
                'other than spaces or None, but was passed '
                '"%s" (%s)' % 
                (
                    self.__class__.__name__, value, 
                    type(value).__name__
                )
            )
        # - If this point is reached without error, then the 
        #   string-value is valid, so we can just exit the if
        self._name = value

    def _set_shipping_weight(self, value:(int,float)):
        if type(value) not in (int, float):
            raise TypeError(
                '%s.shipping_weight expects a non-negative numeric '
                'value, but was passed "%s" (%s)' % 
                (
                    self.__class__.__name__, 
                    value, type(value).__name__
                )
            )
        if value < 0:
            raise ValueError(
                '%s.shipping_weight expects a non-negative numeric '
                'value, but was passed "%s" (%s)' % 
                (
                    self.__class__.__name__, 
                    value, type(value).__name__
                )
            )
        self._shipping_weight = value

    def _set_store_available(self, value:(bool,int)):
        if value not in (True, False, 1, 0):
            raise ValueError(
                '%s.store_available expects either a boolean value '
                '(True|False) or a direct int-value equivalent '
                '(1|0), but was passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        if value:
            self._store_available = True
        else:
            self._store_available = False

    def _set_summary(self, value:str) -> None:
        if value != None:
            # - Type-check: If the value isn't None, then it has to 
            #   be a non-empty, single-line string without tabs
            if type(value) != str:
                raise TypeError(
                    '%s.summary expects a single-line, '
                    'non-empty str value, with no whitespace '
                    'other than spaces or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - Value-check: no whitespace other than " "
            bad_chars = ('\n', '\r', '\t')
            is_valid = True
            for bad_char in bad_chars:
                if bad_char in value:
                    is_valid = False
                    break
            # - If it's empty or otherwise not valid, raise error
            if not value.strip() or not is_valid:
                raise ValueError(
                    '%s.summary expects a single-line, '
                    'non-empty str value, with no whitespace '
                    'other than spaces or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - If this point is reached without error, then the 
            #   string-value is valid, so we can just exit the if
        self._summary = value

#     def _set_property_name(self, value:str) -> None:
#         # TODO: Type- and/or value-check the value argument of the 
#         #       setter-method, unless it's deemed unnecessary.
#         self._property_name = value

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_available(self) -> None:
        self._available = False

    def _del_description(self) -> None:
        self._description = None

    def _del_dimensions(self) -> None:
        self._dimensions = None

    def _del_metadata(self) -> None:
        self._metadata = {}

    def _del_name(self) -> None:
        self._name = None

    def _del_shipping_weight(self) -> None:
        self._shipping_weight = 0

    def _del_store_available(self) -> None:
        self._store_available = False

    def _del_summary(self) -> None:
        self._summary = None

#     def _del_property_name(self) -> None:
#         self._property_name = None

    ###################################
    # Instance property definitions   #
    ###################################

    available = property(
        _get_available, _set_available, _del_available, 
        'Gets sets or deletes the flag that indicates whether the '
        'artisan owner of the product that the instance represents '
        'is considered by them to be available'
    )
    description = property(
        _get_description, _set_description, _del_description, 
        'Gets, sets or deletes the description (str) associated '
        'with the Product that the instance represents'
    )
    dimensions = property(
        _get_dimensions, _set_dimensions, _del_dimensions, 
        'Gets, sets or deletes the company name (str) associated '
        'with the Artisan that the instance represents'
    )
    metadata = property(
        _get_metadata, None, None,
        'Gets metadata (dict) associated with the '
        'Product that the instance represents'
    )
    name = property(
        _get_name, _set_name, _del_name, 
        'Gets, sets or deletes the name (str) associated with the '
        'Product that the instance represents'
    )
    shipping_weight = property(
        _get_shipping_weight, _set_shipping_weight, 
        _del_shipping_weight, 
        'Gets, sets or deletes the shipping_weight (int) '
        'associated with the Product that the instance '
        'represents'
    )
    store_available = property(
        _get_store_available, _set_store_available, _del_store_available, 
        'Gets sets or deletes the flag that indicates whether the '
        'central office considers the product that the instance '
        'represents available on the web-store'
    )
    summary = property(
        _get_summary, _set_summary, _del_summary, 
        'Gets, sets or deletes the summary (str) associated with the '
        'Product that the instance represents'
    )

    ###################################
    # Object initialization           #
    ###################################

    def __init__(self, 
        name:(str,), summary:(str,), available:(bool,), 
        store_available:(bool,), 
        # - Optional arguments:
        description:(str,None)=None, dimensions:(str,None)=None,
        metadata:(dict,)={}, shipping_weight:(int,)=0, 
    ):
        """
Object initialization.

self .............. (BaseProduct instance, required) The instance 
                    to execute against
name .............. (str, required) The name of the product
summary ........... (str, required) A one-line summary of the 
                    product
available ......... (bool, required) Flag indicating whether the 
                    product is considered available by the artisan 
                    who makes it
store_available ... (bool, required) Flag indicating whether the 
                    product is considered available on the web-
                    store by the central office
description ....... (str, optional, defaults to None) A detailed 
                    description of the product
dimensions ........ (str, optional, defaults to None) A measurement-
                    description of the product
metadata .......... (dict, optional, defaults to {}) A collection 
                    of metadata keys and values describing the 
                    product
shipping_weight ... (int, optional, defaults to 0) The shipping-
                    weight of the product
"""
        # TODO: We'll need to figure out what UNITS the shipping-
        #       weight is stored in...
        # - Call parent initializers if needed
        # - Set default instance property-values using _del_... methods
        self._del_available()
        self._del_description()
        self._del_dimensions()
        self._del_metadata()
        self._del_name()
        self._del_shipping_weight()
        self._del_store_available()
        self._del_summary()
        # - Set instance property-values from arguments using 
        #   _set_... methods
        self._set_available(available)
        self._set_name(name)
        self._set_store_available(store_available)
        self._set_summary(summary)
        if description:
            self._set_description(description)
        if dimensions:
            self._set_dimensions(dimensions)
        if metadata:
            self._set_metadata(metadata)
        if shipping_weight:
            self._set_shipping_weight(shipping_weight)
        # - Perform any other initialization needed

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Instance methods                #
    ###################################

    def set_metadata(self, key:(str,), value:(str,)):
        """
Sets the value of a specified metadata-key associated with the product 
that the instance represents.

self .............. (BaseProduct instance, required) The instance to 
                    execute against
key ............... (str, required) The metadata key to associate a 
                    value with
value ............. (str, required) The value to associate with the 
                    metadata key
"""
        if type(key) != str:
            raise TypeError(
                '%s.metadata expects a single-line, '
                'non-empty str key, with no whitespace '
                'other than spaces, but was passed "%s" (%s)' % 
                (
                    self.__class__.__name__, key, 
                    type(key).__name__
                )
            )
        # - Value-check of key: no whitespace other than " "
        bad_chars = ('\n', '\r', '\t')
        is_valid = True
        for bad_char in bad_chars:
            if bad_char in key:
                is_valid = False
                break
        # - If it's empty or otherwise not valid, raise error
        if not key.strip() or not is_valid:
            raise ValueError(
                '%s.metadata expects a single-line, '
                'non-empty str key, with no whitespace '
                'other than spaces, but was passed "%s" (%s)' % 
                (
                    self.__class__.__name__, key, 
                    type(key).__name__
                )
            )
        if type(value) != str:
            raise TypeError(
                '%s.metadata expects a single-line, '
                'non-empty str value, with no whitespace '
                'other than spaces, but was passed "%s" (%s)' % 
                (
                    self.__class__.__name__, value, 
                    type(value).__name__
                )
            )
        # - Value-check of value: no whitespace other than " "
        bad_chars = ('\n', '\r', '\t')
        is_valid = True
        for bad_char in bad_chars:
            if bad_char in value:
                is_valid = False
                break
        # - If it's empty or otherwise not valid, raise error
        if not value.strip() or not is_valid:
            raise ValueError(
                '%s.metadata expects a single-line, '
                'non-empty str value, with no whitespace '
                'other than spaces, but was passed "%s" (%s)' % 
                (
                    self.__class__.__name__, value, 
                    type(value).__name__
                )
            )
        self._metadata[key] = value

    def remove_metadata(self, key):
        """
Removes the specified metadata associated with the product that the 
instance represents, identified by the key

self .............. (BaseProduct instance, required) The instance to 
                    execute against
key ............... (str, required) The key that identifies the 
                    metadata value to remove
"""
        try:
            del self._metadata[key]
        except KeyError:
            pass

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    ###################################
    # Static methods                  #
    ###################################

class HasProducts(metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements, and 
type-identity for objects that can have a common products 
property whose membership is stored and handled in the same 
way.
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_products(self) -> (tuple,):
        return tuple(self._products)

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_products(self, value:(list, tuple)) -> None:
        # - Check first that the value is an iterable - list or 
        #   tuple, it doesn't really matter which, just so long 
        #   as it's a sequence-type collection of some kind.
        if type(value) not in (list, tuple):
            raise TypeError(
                '%s.products expects a list or tuple of BaseProduct '
                'objects, but was passed a %s instead' % 
                (self.__class__.__name__, type(value).__name__)
            )
        # - Start with a new, empty list
        new_items = []
        # - Iterate over the items in value, check each one, and 
        #   append them if they're OK
        bad_items = []
        for item in value:
            # - We're going to assume that all products will derive 
            #   from BaseProduct - That's why it's defined, after all
            if isinstance(item, BaseProduct):
                new_items.append(item)
            else:
                bad_items.append(item)
        # - If there are any bad items, then do NOT commit the 
        #   changes -- raise an error instead!
        if bad_items:
            raise TypeError(
                '%s.products expects a list or tuple of BaseProduct '
                'objects, but the value passed included %d items '
                'that are not of the right type: (%s)' % 
                (
                    self.__class__.__name__, len(bad_items), 
                    ', '.join([str(bi) for bi in bad_items])
                )
            )
        self._products = list(value)

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_products(self) -> None:
        self._products = []

    ###################################
    # Instance property definitions   #
    ###################################

    products = property(
         _get_products, None, None,
         'Gets the products (BaseProduct) of the instance'
    )

    ###################################
    # Object initialization           #
    ###################################

    def __init__(self, *products):
        """
Object initialization.

self .............. (BaseOrder instance, required) The instance to 
                    execute against
products .......... (list or tuple of BaseProduct instances) The 
                    products that were ordered
"""
        # - Call parent initializers if needed
        # - Set default instance property-values using _del_... methods
        self._del_products()
        # - Set instance property-values from arguments using 
        #   _set_... methods
        if products:
            self._set_products(products)
        # - Perform any other initialization needed

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Abstract methods                #
    ###################################

    @abc.abstractmethod
    def add_product(self, product:BaseProduct) -> BaseProduct:
        """
Adds a product to the instance's collection of products.

Returns the product added.

self ....... (HasProducts instance, required) The instance to 
             execute against
product ...  (BaseProduct, required) The product to add to the 
             instance's collection of products

Raises TypeError if the product specified is not a BaseProduct-
  derived instance

May be implemented in derived classes by simply calling
    return HasProducts.add_product(self, product)
"""
        # - Make sure the product passed in is a BaseProduct
        if not isinstance(product, BaseProduct):
            raise TypeError(
                '%s.add_product expects an instance of '
                'BaseProduct to be passed in its product '
                'argument, but "%s" (%s) was passed instead' % 
                (
                    self.__class__.__name__, product, 
                    type(product).__name__
                )
            )
        # - Append it to the internal _products list
        self._products.append(product)
        # - Return it
        return product

    @abc.abstractmethod
    def remove_product(self, product:BaseProduct) -> None:
        """
Removes a product from the instance's collection of products.

Returns the product removed.

self ....... (HasProducts instance, required) The instance to 
             execute against
product ...  (BaseProduct, required) The product to remove from 
             the instance's collection of products

Raises TypeError if the product specified is not a BaseProduct-
  derived instance
Raises ValueError if the product specified is not a member of the 
  instance's products collection

May be implemented in derived classes by simply calling
    return HasProducts.remove_product(self, product)
"""
        # - Make sure the product passed in is a BaseProduct.
        #   Technically this may not be necessary, since type 
        #   is enforced in add_product, but it does no harm to 
        #   re-check here...
        if not isinstance(product, BaseProduct):
            raise TypeError(
                '%s.add_product expects an instance of '
                'BaseProduct to be passed in its product '
                'argument, but "%s" (%s) was passed instead' % 
                (
                    self.__class__.__name__, value, 
                    type(value).__name__
                )
            )
        try:
            self._products.remove(product)
            return product
        except ValueError:
            raise ValueError(
                '%s.remove_product could not remove %s from its '
                'products collection because it was not a member '
                'of that collection' % 
                (self.__class__.__name__, product)
            )

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    ###################################
    # Static methods                  #
    ###################################

class BaseArtisan(HasProducts, metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements, and 
type-identity for objects that can represent an Artisan in 
the context of the HMS system.
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_address(self) -> (Address,):
        return self._address

    def _get_company_name(self) -> (str,None):
        return self._company_name

    def _get_contact_email(self) -> (str,None):
        return self._contact_email

    def _get_contact_name(self) -> (str,None):
        return self._contact_name

    def _get_website(self) -> (str,None):
        return self._website

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_address(self, value:Address) -> None:
        if not isinstance(value, Address):
            raise TypeError(
                '%s.address expects an Address object or an object '
                'derived from Address, but was passed "%s" (%s) '
                'instead, which is not.' %
                (self.__class__.__name__, value, type(value).__name__)
            )
        self._address = value

    def _set_company_name(self, value:str) -> None:
        if value != None:
            # - Type-check: If the value isn't None, then it has to 
            #   be a non-empty, single-line string without tabs
            if type(value) != str:
                raise TypeError(
                    '%s.company_name expects a single-line, '
                    'non-empty str value, with no whitespace '
                    'other than spaces or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - Value-check: no whitespace other than " "
            bad_chars = ('\n', '\r', '\t')
            is_valid = True
            for bad_char in bad_chars:
                if bad_char in value:
                    is_valid = False
                    break
            # - If it's empty or otherwise not valid, raise error
            if not value.strip() or not is_valid:
                raise ValueError(
                    '%s.company_name expects a single-line, '
                    'non-empty str value, with no whitespace '
                    'other than spaces or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - If this point is reached without error, then the 
            #   string-value is valid, so we can just exit the if
        self._company_name = value

    def _set_contact_email(self, value:str) -> None:
        # - Type-check: This is a required str value
        if type(value) != str:
            raise TypeError(
                '%s.contact_email expects a str value that is a '
                'well-formed email address, but was passed '
                '"%s" (%s)' % 
                (
                    self.__class__.__name__, value, 
                    type(value).__name__
                )
            )
        # - Since we know it's a string, we can start by parsing value 
        #   with email.utils.parseaddr, and using the second item of 
        #   that result to check for well-formed-ness
        check_value = parseaddr(value)[1]
        # - If value is not empty, then there was *something* that was
        #   recognized as being an email address
        valid = (check_value != '')
        if valid:
            # - Try removing an entire well-formed email address, as 
            #   defined by EMAIL_CHECK, from the value. If it works, 
            #   there will either be a remnant or not. If there is 
            #   a remnant, it's considered badly-formed.
            remnant = EMAIL_CHECK.sub('', check_value)
            if remnant != '' or not value:
                valid = False
        if not check_value or not valid:
            raise TypeError(
                '%s.contact_email expects a str value that is a '
                'well-formed email address, but was passed '
                '"%s" (%s)' % 
                (
                    self.__class__.__name__, value, 
                    type(value).__name__
                )
            )
        self._contact_email = value

    def _set_contact_name(self, value:str) -> None:
        # - Type-check: This is a required str value
        if type(value) != str:
            raise TypeError(
                '%s.contact_name expects a single-line, '
                'non-empty str value, with no whitespace '
                'other than spaces, but was passed '
                '"%s" (%s)' % 
                (
                    self.__class__.__name__, value, 
                    type(value).__name__
                )
            )
        # - Value-check: no whitespace other than " "
        bad_chars = ('\n', '\r', '\t')
        is_valid = True
        for bad_char in bad_chars:
            if bad_char in value:
                is_valid = False
                break
        # - If it's empty or otherwise not valid, raise error
        if not value.strip() or not is_valid:
            raise ValueError(
                '%s.contact_name expects a single-line, '
                'non-empty str value, with no whitespace '
                'other than spaces, but was passed '
                '"%s" (%s)' % 
                (
                    self.__class__.__name__, value, 
                    type(value).__name__
                )
            )
        # - Everything checks out, so set the attribute
        self._contact_name = value

    def _set_website(self, value:(str,None)) -> None:
        # - Type-check: This is an optional required str value
        if value != None:
            if type(value) != str:
                raise TypeError(
                    '%s.website expects a str value that is a '
                    'well-formed URL, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            remnant = URL_CHECK.sub('', value)
            if remnant != '' or not value:
                raise TypeError(
                    '%s.website expects a str value that is a '
                    'well-formed URL, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
        self._website = value

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_address(self) -> None:
        self._address = None

    def _del_company_name(self) -> None:
        self._company_name = None

    def _del_contact_email(self) -> None:
        self._contact_email = None

    def _del_contact_name(self) -> None:
        self._contact_name = None

    def _del_website(self) -> None:
        self._website = None

    ###################################
    # Instance property definitions   #
    ###################################

    address = property(
        _get_address, _set_address, _del_address, 
        'Gets, sets or deletes the physical address (Address) '
        'associated with the Artisan that the instance represents'
    )
    company_name = property(
        _get_company_name, _set_company_name, _del_company_name, 
        'Gets, sets or deletes the company name (str) associated '
        'with the Artisan that the instance represents'
    )
    contact_email = property(
        _get_contact_email, _set_contact_email, _del_contact_email, 
        'Gets, sets or deletes the email address (str) of the '
        'named contact associated with the Artisan that the '
        'instance represents'
    )
    contact_name = property(
        _get_contact_name, _set_contact_name, _del_contact_name, 
        'Gets, sets or deletes the name of the contact (str) '
        'associated with the Artisan that the instance represents'
    )
    website = property(
        _get_website, _set_website, _del_website, 
        'Gets, sets or deletes the URL of the website (str) '
        'associated with the Artisan that the instance represents'
    )

    ###################################
    # Object initialization           #
    ###################################

    def __init__(self, 
        contact_name:str, contact_email:str, 
        address:Address, company_name:str=None, 
        website:(str,)=None, 
        *products
        ):
        """
Object initialization.

self .............. (BaseArtisan instance, required) The instance to 
                    execute against
contact_name ...... (str, required) The name of the primary contact 
                    for the Artisan that the instance represents
contact_email ..... (str [email address], required) The email address 
                    of the primary contact for the Artisan that the 
                    instance represents
address ........... (Address, required) The mailing/shipping address 
                    for the Artisan that the instance represents
company_name ...... (str, optional, defaults to None) The company-
                    name for the Artisan that the instance represents
products .......... (BaseProduct collection) The products associated 
                    with the Artisan that the instance represents
"""
        # - Call parent initializers if needed
        HasProducts.__init__(self, *products)
        # - Set default instance property-values using _del_... methods
        self._del_address()
        self._del_company_name()
        self._del_contact_email()
        self._del_contact_name()
        self._del_website()
        # - Set instance property-values from arguments using 
        #   _set_... methods
        self._set_contact_name(contact_name)
        self._set_contact_email(contact_email)
        self._set_address(address)
        if company_name:
            self._set_company_name(company_name)
        if website:
            self._set_website(website)
        # - Perform any other initialization needed

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Abstract methods                #
    ###################################

    ###################################
    # Instance methods                #
    ###################################

#     def instance_method(self, arg:str, *args, **kwargs):
#         """TODO: Document method
# DOES_WHATEVER
# 
# self .............. (BaseArtisan instance, required) The 
#                     instance to execute against
# arg ............... (str, required) The string argument
# *args ............. (object*, optional) The arglist
# **kwargs .......... (dict, optional) keyword-args, accepts:
#  - kwd_arg ........ (type, optional, defaults to SOMETHING) The SOMETHING 
#                     to apply
# """
#         pass

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    ###################################
    # Static methods                  #
    ###################################

class BaseCustomer(metaclass=abc.ABCMeta):
    """TODO: Document the class.
Provides baseline functionality, interface requirements, and 
type-identity for objects that can REPRESENT_SOMETHING
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_billing_address(self) -> (Address,):
        return self._billing_address

    def _get_shipping_address(self) -> (Address,):
        return self._shipping_address

    def _get_name(self) -> (str,None):
        return self._name

    ###################################
    # Property-setter methods         #
    ###################################

#     def _set_property_name(self, value:str) -> None:
#         # TODO: Type- and/or value-check the value argument of the 
#         #       setter-method, unless it's deemed unnecessary.
#         self._property_name = value

    def _set_billing_address(self, value:Address) -> None:
        if not isinstance(value, Address):
            raise TypeError(
                '%s.billing_address expects an Address object or '
                'an object derived from Address, but was passed '
                '"%s" (%s) instead, which is not.' %
                (self.__class__.__name__, value, type(value).__name__)
            )
        self._billing_address = value

    def _set_shipping_address(self, value:Address) -> None:
        if not isinstance(value, Address):
            raise TypeError(
                '%s.shipping_address expects an Address object or '
                'an object derived from Address, but was passed '
                '"%s" (%s) instead, which is not.' %
                (self.__class__.__name__, value, type(value).__name__)
            )
        self._shipping_address = value

    def _set_name(self, value:str) -> None:
        if value != None:
            # - Type-check: If the value isn't None, then it has to 
            #   be a non-empty, single-line string without tabs
            if type(value) != str:
                raise TypeError(
                    '%s.name expects a single-line, '
                    'non-empty str value, with no whitespace '
                    'other than spaces or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - Value-check: no whitespace other than " "
            bad_chars = ('\n', '\r', '\t')
            is_valid = True
            for bad_char in bad_chars:
                if bad_char in value:
                    is_valid = False
                    break
            # - If it's empty or otherwise not valid, raise error
            if not value.strip() or not is_valid:
                raise ValueError(
                    '%s.name expects a single-line, '
                    'non-empty str value, with no whitespace '
                    'other than spaces or None, but was passed '
                    '"%s" (%s)' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
            # - If this point is reached without error, then the 
            #   string-value is valid, so we can just exit the if
        self._name = value

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_billing_address(self) -> None:
        self._billing_address = None

    def _del_shipping_address(self) -> None:
        self._shipping_address = None

    def _del_name(self) -> None:
        self._name = None

    ###################################
    # Instance property definitions   #
    ###################################

    billing_address = property(
        _get_billing_address, _set_billing_address, 
        _del_billing_address, 
        'Gets, sets or deletes the billing-address of the customer '
        'that the instance represents'
    )
    name = property(
        _get_name, _set_name, _del_name, 
        'Gets, sets or deletes the billing-address of the customer '
        'that the instance represents'
    )
    shipping_address = property(
        _get_shipping_address, _set_shipping_address, 
        _del_shipping_address, 
        'Gets, sets or deletes the shipping-address of the customer '
        'that the instance represents'
    )

    ###################################
    # Object initialization           #
    ###################################

    def __init__(self, 
        name:(str,), billing_address:(Address,), 
        shipping_address:(Address,None)=None
    ):
        """
Object initialization.

self .............. (BaseCustomer instance, required) The instance to 
                    execute against
name .............. (str, required) The name of the customer.
billing_address ... (Address, required) The billing address of the 
                    customer
shipping_address .. (Address, optional, defaults to None) The shipping 
                    address of the customer.
"""
        # - Prevent a direct instantiation of this class - it's 
        #   intended to be abstract, even though it has no 
        #   explicitly-abstract members:
        if self.__class__ == BaseCustomer:
            raise NotImplementedError(
                'BaseCustomer is intended to be an abstract class, '
                'even though it does not have any explicitly '
                'abstract members, and should not be instantiated.'
            )
        # - Call parent initializers if needed
        # - Set default instance property-values using _del_... methods
        self._del_billing_address()
        self._del_name()
        self._del_shipping_address()
        # - Set instance property-values from arguments using 
        #   _set_... methods
        self._set_name(name)
        self._set_billing_address(billing_address)
        if shipping_address:
            self._set_shipping_address(shipping_address)
        # - Perform any other initialization needed

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Abstract methods                #
    ###################################

#     @abc.abstractmethod
#     def instance_method(self, arg:str, *args, **kwargs):
#         """TODO: Document method
# DOES_WHATEVER
# 
# self .............. (BaseCustomer instance, required) The 
#                     instance to execute against
# arg ............... (str, required) The string argument
# *args ............. (object*, optional) The arglist
# **kwargs .......... (dict, optional) keyword-args, accepts:
#  - kwd_arg ........ (type, optional, defaults to SOMETHING) The SOMETHING 
#                     to apply
# """
#         pass

    ###################################
    # Instance methods                #
    ###################################

#     def instance_method(self, arg:str, *args, **kwargs):
#         """TODO: Document method
# DOES_WHATEVER
# 
# self .............. (BaseCustomer instance, required) The 
#                     instance to execute against
# arg ............... (str, required) The string argument
# *args ............. (object*, optional) The arglist
# **kwargs .......... (dict, optional) keyword-args, accepts:
#  - kwd_arg ........ (type, optional, defaults to SOMETHING) The SOMETHING 
#                     to apply
# """
#         pass

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    ###################################
    # Static methods                  #
    ###################################

class BaseOrder(HasProducts, metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements, and 
type-identity for objects that represent a customer's order of 
one-to-many products
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_customer(self) -> (BaseCustomer,):
        return self._customer

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_customer(self, value:BaseCustomer) -> None:
        if not isinstance(value, BaseCustomer):
            raise TypeError(
                '%s.address expects a BaseCustomer object or an '
                'object derived from BaseCustomer, but was passed '
                '"%s" (%s) instead, which is not.' %
                (value, type(value).__name__)
            )
        self._customer = value

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_customer(self) -> None:
        self._customer = None

    ###################################
    # Instance property definitions   #
    ###################################

    customer = property(
        _get_customer, None, None, 
        'Gets the customer (BaseCustomer) of the instance'
    )

    ###################################
    # Object initialization           #
    ###################################

    def __init__(self, customer:(BaseCustomer,), *products):
        """
Object initialization.

self .............. (BaseOrder instance, required) The instance to 
                    execute against
customer .......... (BaseCustomer, required) The customer that placed 
                    the order
products .......... (list or tuple of BaseProduct instances) The 
                    products that were ordered
"""
        # - Call parent initializers if needed
        HasProducts.__init__(self, *products)
        # - Set default instance property-values using _del_... methods
        self._del_customer()
        # - Set instance property-values from arguments using 
        #   _set_... methods
        self._set_customer(customer)
        # - Perform any other initialization needed

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Abstract methods                #
    ###################################

    ###################################
    # Instance methods                #
    ###################################

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    ###################################
    # Static methods                  #
    ###################################

#######################################
# Concrete classes                    #
#######################################


#######################################
# Initialization needed after member  #
#   definition is complete            #
#######################################

#######################################
# Imports needed after member         #
#   definition (to resolve circular   #
#   dependencies - avoid if at all    #
#   possible                          #
#######################################

#######################################
# Code to execute if the module is    #
#   called directly                   #
#######################################

if __name__ == '__main__':
    pass

