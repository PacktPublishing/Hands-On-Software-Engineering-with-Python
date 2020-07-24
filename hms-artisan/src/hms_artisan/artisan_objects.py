#!/usr/bin/env python
"""
Provides classes and functionality that represent various 
business-objects as they exist in the context of the Artisan 
Application
"""

#######################################
# Any needed from __future__ imports  #
# Create an "__all__" list to support #
#   "from module import member" use   #
#######################################

__all__ = [
    # Constants
    # Exceptions
    # Functions
    # ABC "interface" classes
    # ABC abstract classes
    # Concrete classes
    'Artisan',
    'Order',
    'Product',
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

from datetime import datetime
from uuid import UUID

#######################################
# Third-party imports needed          #
#######################################

from hms_core.business_objects import Address, BaseArtisan, \
    BaseCustomer, BaseOrder, BaseProduct, HasProducts
from hms_core.data_objects import BaseDataObject
from hms_artisan.data_storage import JSONFileDataObject

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

#######################################
# Custom Exceptions                   #
#######################################

#######################################
# Module functions                    #
#######################################

#######################################
# ABC "interface" classes             #
#######################################

#######################################
# Abstract classes                    #
#######################################

#######################################
# Concrete classes                    #
#######################################

class Artisan(BaseArtisan, JSONFileDataObject, object):
    """
Represents an Artisan in the context of the Artisan Application
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    # TODO: Work out the configuration-based file-system path 
    #       for this attribute
    _file_store_dir = '/tmp/hms_data'

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_address(self, value:Address) -> None:
        # - Call the parent method
        result = BaseArtisan._set_address(self, value)
        self._set_is_dirty(True)
        return result

    def _set_company_name(self, value:str) -> None:
        # - Call the parent method
        result = BaseArtisan._set_company_name(self, value)
        self._set_is_dirty(True)
        return result

    def _set_contact_email(self, value:str) -> None:
        # - Call the parent method
        result = BaseArtisan._set_contact_email(self, value)
        self._set_is_dirty(True)
        return result

    def _set_contact_name(self, value:str) -> None:
        # - Call the parent method
        result = BaseArtisan._set_contact_name(self, value)
        self._set_is_dirty(True)
        return result

    def _set_website(self, value:(str,None)) -> None:
        # - Call the parent method
        result = BaseArtisan._set_website(self, value)
        self._set_is_dirty(True)
        return result

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_address(self) -> None:
        # - Call the parent method
        result = BaseArtisan._del_address(self)
        self._set_is_dirty(True)
        return result

    def _del_company_name(self) -> None:
        # - Call the parent method
        result = BaseArtisan._del_company_name(self)
        self._set_is_dirty(True)
        return result

    def _del_contact_email(self) -> None:
        # - Call the parent method
        result = BaseArtisan._del_contact_email(self)
        self._set_is_dirty(True)
        return result

    def _del_contact_name(self) -> None:
        # - Call the parent method
        result = BaseArtisan._del_contact_name(self)
        self._set_is_dirty(True)
        return result

    def _del_website(self) -> None:
        # - Call the parent method
        result = BaseArtisan._del_website(self)
        self._set_is_dirty(True)
        return result

    ###################################
    # Instance property definitions   #
    ###################################

    address = property(
        BaseArtisan._get_address, _set_address, _del_address, 
        'Gets, sets or deletes the physical address (Address) '
        'associated with the Artisan that the instance represents'
    )
    company_name = property(
        BaseArtisan._get_company_name, _set_company_name, 
        _del_company_name, 
        'Gets, sets or deletes the company name (str) associated '
        'with the Artisan that the instance represents'
    )
    contact_email = property(
        BaseArtisan._get_contact_email, _set_contact_email, 
        _del_contact_email, 
        'Gets, sets or deletes the email address (str) of the '
        'named contact associated with the Artisan that the '
        'instance represents'
    )
    contact_name = property(
        BaseArtisan._get_contact_name, _set_contact_name, 
        _del_contact_name, 
        'Gets, sets or deletes the name of the contact (str) '
        'associated with the Artisan that the instance represents'
    )
    website = property(
        BaseArtisan._get_website, _set_website, _del_website, 
        'Gets, sets or deletes the URL of the website (str) '
        'associated with the Artisan that the instance represents'
    )

    ###################################
    # Object initialization           #
    ###################################

    # TODO: Add and document arguments if/as needed
    def __init__(self,
        # - Required arguments from BaseArtisan
        contact_name:str, contact_email:str, address:Address, 
        # - Optional arguments from BaseArtisan
        company_name:str=None, website:(str,)=None, 
        # - Optional arguments from BaseDataObject/JSONFileDataObject
        oid:(UUID,str,None)=None, 
        created:(datetime,str,float,int,None)=None, 
        modified:(datetime,str,float,int,None)=None,
        is_active:(bool,int,None)=None, 
        is_deleted:(bool,int,None)=None,
        is_dirty:(bool,int,None)=None, 
        is_new:(bool,int,None)=None,
        # - the products arglist from BaseArtisan
        *products
    ):
        """
Object initialization.

self .............. (Artisan instance, required) The instance to 
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
website ........... (str, optional, defaults to None) The the URL of 
                    the website associated with the Artisan that the 
                    instance represents
oid ............... (UUID|str, optional, defaults to None) 
created ........... (datetime|str|float|int, optional, defaults to None) 
modified .......... (datetime|str|float|int, optional, defaults to None) 
is_active ......... (bool|int, optional, defaults to None) 
is_deleted ........ (bool|int, optional, defaults to None) 
is_dirty .......... (bool|int, optional, defaults to None) 
is_new ............ (bool|int, optional, defaults to None) 
products .......... (BaseProduct collection) The products associated 
                    with the Artisan that the instance represents
"""
        # - Call parent initializers if needed
        BaseArtisan.__init__(
            self, contact_name, contact_email, address, 
            company_name, website, *products
        )
        JSONFileDataObject.__init__(
            self, oid, created, modified, is_active, 
            is_deleted, is_dirty, is_new
        )
        # - Set default instance property-values using _del_... methods
        # - Set instance property-values from arguments using 
        #   _set_... methods
        # - Perform any other initialization needed
        self._set_is_dirty(False)

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Instance methods                #
    ###################################

    def add_product(self, product:BaseProduct) -> BaseProduct:
        return HasProducts.add_product(self, product)

    def matches(self, **criteria) -> (bool,):
        return BaseDataObject.matches(self, **criteria)

    def remove_product(self, product:BaseProduct) -> BaseProduct:
        return HasProducts.remove_product(self, product)

    def to_data_dict(self) -> (dict,):
        return {
            # Properties from BaseArtisan:
            'address':self.address.to_dict() if self.address else None,
            'company_name':self.company_name,
            'contact_email':self.contact_email,
            'contact_name':self.contact_name,
            'website':self.website, 
            # - Properties from BaseDataObject (through 
            #   JSONFileDataObject)
            'created':datetime.strftime(
                self.created, self.__class__._data_time_string
            ),
            'is_active':self.is_active,
            'is_deleted':self.is_deleted,
            'modified':datetime.strftime(
                self.modified, self.__class__._data_time_string
            ),
            'oid':str(self.oid),
        }

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    @classmethod
    def _load_objects(cls, force_load=False):
        return JSONFileDataObject._load_objects(cls, force_load)

    @classmethod
    def from_data_dict(cls, data_dict:(dict,)):
        if data_dict.get('address'):
            data_dict['address'] = Address.from_dict(
                data_dict['address']
            )
        return cls(**data_dict)

    @classmethod
    def sort(cls, objects:(list,tuple), sort_by:(str,)) -> (list,):
        """
Returns a list of the original objects supplied, sorted by the 
criteria provided
"""
        raise NotImplementedError()

    ###################################
    # Static methods                  #
    ###################################

# -  _load_objects, from_data_dict, matches, sort, to_data_dict

class Order(Address, JSONFileDataObject, object):
    """
Represents an Order in the context of the Artisan Application
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    # TODO: Work out the configuration-based file-system path 
    #       for this attribute
    _file_store_dir = '/tmp/hms_data'

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_items(self) -> dict:
        return dict(self._items)

    def _get_name(self) -> (str,None):
        return self._name

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_building_address(self, value:(str,None)) -> None:
        result = Address._set_building_address(self, value)
        self._set_is_dirty(True)
        return result

    def _set_city(self, value:str) -> None:
        result = Address._set_city(self, value)
        self._set_is_dirty(True)
        return result

    def _set_country(self, value:(str,None)) -> None:
        result = Address._set_country(self, value)
        self._set_is_dirty(True)
        return result

    def _set_items(self, value:(dict,)) -> None:
        if type(value) != dict:
            raise TypeError(
                '%s.items expects a dict of UUID keys and int-'
                'values, but was passed "%s" (%s)' % 
                (self.__class__.__name__, value,type(value).__name__)
            )
        self._del_items()
        for key in value:
            self.set_item_quantity(key, value[key])
        self._set_is_dirty(True)

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
        self._set_is_dirty(True)

    def _set_region(self, value:(str,None)) -> None:
        result = Address._set_region(self, value)
        self._set_is_dirty(True)
        return result

    def _set_postal_code(self, value:(str,None)) -> None:
        result = Address._set_postal_code(self, value)
        self._set_is_dirty(True)
        return result

    def _set_street_address(self, value:str) -> None:
        result = Address._set_street_address(self, value)
        self._set_is_dirty(True)
        return result

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_building_address(self) -> None:
        result = Address._del_building_address(self)
        self._set_is_dirty(True)
        return result

    def _del_city(self) -> None:
        result = Address._del_city(self)
        self._set_is_dirty(True)
        return result

    def _del_country(self) -> None:
        result = Address._del_country(self)
        self._set_is_dirty(True)
        return result

    def _del_items(self) -> None:
        self._items = {}
        self._set_is_dirty(True)

    def _del_name(self) -> None:
        self._name = None
        self._set_is_dirty(True)

    def _del_region(self) -> None:
        result = Address._del_region(self)
        self._set_is_dirty(True)
        return result

    def _del_postal_code(self) -> None:
        result = Address._del_postal_code(self)
        self._set_is_dirty(True)
        return result

    def _del_street_address(self) -> None:
        result = Address._del_street_address(self)
        self._set_is_dirty(True)
        return result

    ###################################
    # Instance property definitions   #
    ###################################

    building_address = property(
        Address._get_building_address, _set_building_address, 
        _del_building_address, 
        'Gets, sets or deletes the building_address (str|None) '
        'of the instance'
    )
    city = property(
        Address._get_city, _set_city, _del_city, 
        'Gets, sets or deletes the city (str) of the instance'
    )
    country = property(
        Address._get_country, _set_country, _del_country, 
        'Gets, sets or deletes the country (str|None) of the '
        'instance'
    )
    items = property(
        _get_items, None, None,
        'Gets the items associated with the order, a dict of OID '
        'keys with quantity values'
    )
    name = property(
        _get_name, _set_name, _del_name, 
        'Gets, sets or deletes the name associated with the order'
    )
    region = property(
        Address._get_region, _set_region, _del_region, 
        'Gets, sets or deletes the region (str|None) of the '
        'instance'
    )
    postal_code = property(
        Address._get_postal_code, _set_postal_code, _del_postal_code, 
        'Gets, sets or deletes the postal_code (str|None) of '
        'the instance'
    )
    street_address = property(
        Address._get_street_address, _set_street_address, 
        _del_street_address, 
        'Gets, sets or deletes the street_address (str) of the '
        'instance'
    )

    ###################################
    # Object initialization           #
    ###################################

    def __init__(self, 
        name:(str,),
        # - Required arguments from Address
        street_address:(str,), city:(str,), 
        # - Local optional arguments
        items:(dict,)={},
        # - Optional arguments from Address
        building_address:(str,None)=None, region:(str,None)=None, 
        postal_code:(str,None)=None, country:(str,None)=None,
        # - Optional arguments from BaseDataObject/JSONFileDataObject
        oid:(UUID,str,None)=None, 
        created:(datetime,str,float,int,None)=None, 
        modified:(datetime,str,float,int,None)=None,
        is_active:(bool,int,None)=None, 
        is_deleted:(bool,int,None)=None,
        is_dirty:(bool,int,None)=None, 
        is_new:(bool,int,None)=None,
    ):
        """
Object initialization.

self .............. (Order instance, required) The instance to 
                    execute against
name .............. (str, required) The name of the addressee
street_address .... (str, required) The base street-address of the 
                    location the instance represents
city .............. (str, required) The city portion of the street-
                    address that the instance represents
items ............. (dict, optional, defaults to {}) The dict of 
                    oids-to-quantities of products in the order
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
oid ............... (UUID|str, optional, defaults to None) 
created ........... (datetime|str|float|int, optional, defaults to None) 
modified .......... (datetime|str|float|int, optional, defaults to None) 
is_active ......... (bool|int, optional, defaults to None) 
is_deleted ........ (bool|int, optional, defaults to None) 
is_dirty .......... (bool|int, optional, defaults to None) 
is_new ............ (bool|int, optional, defaults to None) 
"""
        # - Call parent initializers if needed
        Address.__init__(
            self, street_address, city, building_address, region, 
            postal_code, country
        )
        JSONFileDataObject.__init__(
            self, oid, created, modified, is_active, 
            is_deleted, is_dirty, is_new
        )
        # - Set default instance property-values using _del_... methods
        self._del_items()
        self._del_name()
        # - Set instance property-values from arguments using 
        #   _set_... methods
        self._set_name(name)
        if items:
            self._set_items(items)
        # - Perform any other initialization needed
        self._set_is_dirty(False)

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Instance methods                #
    ###################################

    def matches(self, **criteria) -> (bool,):
        return BaseDataObject.matches(self, **criteria)

    def set_item_quantity(self, oid:(UUID,str), quantity:(int,)) -> None:
        if type(oid) not in (UUID, str):
            raise TypeError(
                '%s.set_item_quantity expects a UUID or string '
                'representation of one for its oid argument, but '
                'was passed "%s" (%s)' % 
                (self.__class__.__name__, oid, type(oid).__name__)
            )
        if type(oid) == str:
            try:
                oid = UUID(oid)
            except Exception as error:
                raise ValueError(
                    '%s.set_item_quantity expects a UUID or string '
                    'representation of one for its oid argument, but '
                    'was passed "%s" (%s) which could not be '
                    'converted into a UUID (%s: %s)' % 
                    (
                        self.__class__.__name__, oid, 
                        type(oid).__name__, error.__class__.__name__, 
                        error
                    )
                )
        if type(quantity) != int:
            raise TypeError(
                '%s.set_item_quantity expects non-negative int-value '
                'for its quantity argument, but was passed "%s" (%s)' 
                % (
                    self.__class__.__name__, quantity, 
                    type(quantity).__name__
                )
            )
        if quantity < 0:
            raise ValueError(
                '%s.set_item_quantity expects non-negative int-value '
                'for its quantity argument, but was passed "%s" (%s)' 
                % (
                    self.__class__.__name__, quantity, 
                    type(quantity).__name__
                )
            )
        if quantity != 0:
            self._items[oid] = quantity
        else:
            try:
                del self._items[oid]
            except KeyError:
                pass

    def to_data_dict(self) -> (dict,):
        return {
            # - Local properties
            'name':self.name,
            'street_address':self.street_address,
            'building_address':self.building_address,
            'city':self.city,
            'region':self.region,
            'postal_code':self.postal_code,
            'country':self.country,
            # - Generate a string:int dict from the UUID:int dict
            'items':dict(
                [
                    (str(key), int(self.items[key])) 
                    for key in self.items.keys()
                ]
            ),
            # - Properties from BaseDataObject (through 
            #   JSONFileDataObject)
            'created':datetime.strftime(
                self.created, self.__class__._data_time_string
            ),
            'is_active':self.is_active,
            'is_deleted':self.is_deleted,
            'modified':datetime.strftime(
                self.modified, self.__class__._data_time_string
            ),
            'oid':str(self.oid),
        }

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    @classmethod
    def _load_objects(cls, force_load=False):
        return JSONFileDataObject._load_objects(cls, force_load)

    @classmethod
    def from_data_dict(cls, data_dict:(dict,)):
        return cls(**data_dict)

    @classmethod
    def sort(cls, objects:(list,tuple), sort_by:(str,)) -> (list,):
        """
Returns a list of the original objects supplied, sorted by the 
criteria provided
"""
        raise NotImplementedError()

    @classmethod
    def standard_address(cls, 
            name:(str,), street_address:(str,), 
            building_address:(str,None), city:(str,), 
            region:(str,None), postal_code:(str,None), 
            country:(str,None)
        ):
        return cls(
            name=name, street_address=street_address, city=city,
            building_address=building_address, region=region, 
            postal_code=postal_code, country=country
        )

    ###################################
    # Static methods                  #
    ###################################

# - from_data_dict, matches, sort, to_data_dict

class Product(BaseProduct, JSONFileDataObject, object):
    """
Represents a Product in the context of the Artisan Application
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    # TODO: Work out the configuration-based file-system path 
    #       for this attribute
    _file_store_dir = '/tmp/hms_data'

    ###################################
    # Property-getter methods         #
    ###################################

#     def _get_property_name(self) -> str:
#         return self._property_name

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_available(self, value:(bool,int)):
        result = BaseProduct._set_available(self, value)
        self._set_is_dirty(True)
        return result

    def _set_description(self, value:str) -> None:
        result = BaseProduct._set_description(self, value)
        self._set_is_dirty(True)
        return result

    def _set_dimensions(self, value:str) -> None:
        result = BaseProduct._set_dimensions(self, value)
        self._set_is_dirty(True)
        return result

    def _set_metadata(self, value:(dict,)):
        result = BaseProduct._set_metadata(self, value)
        self._set_is_dirty(True)
        return result

    def _set_name(self, value:str) -> None:
        result = BaseProduct._set_name(self, value)
        self._set_is_dirty(True)
        return result

    def _set_shipping_weight(self, value:(int,float)):
        result = BaseProduct._set_shipping_weight(self, value)
        self._set_is_dirty(True)
        return result

    def _set_store_available(self, value:(bool,int)):
        result = BaseProduct._set_store_available(self, value)
        self._set_is_dirty(True)
        return result

    def _set_summary(self, value:str) -> None:
        result = BaseProduct._set_summary(self, value)
        self._set_is_dirty(True)
        return result

#     def _set_property_name(self, value:str) -> None:
#         # TODO: Type- and/or value-check the value argument of the 
#         #       setter-method, unless it's deemed unnecessary.
#         self._property_name = value

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_available(self) -> None:
        result = BaseProduct._del_available(self)
        self._set_is_dirty(True)
        return result

    def _del_description(self) -> None:
        result = BaseProduct._del_description(self)
        self._set_is_dirty(True)
        return result

    def _del_dimensions(self) -> None:
        result = BaseProduct._del_dimensions(self)
        self._set_is_dirty(True)
        return result

    def _del_metadata(self) -> None:
        result = BaseProduct._del_metadata(self)
        self._set_is_dirty(True)
        return result

    def _del_name(self) -> None:
        result = BaseProduct._del_name(self)
        self._set_is_dirty(True)
        return result

    def _del_shipping_weight(self) -> None:
        result = BaseProduct._del_shipping_weight(self)
        self._set_is_dirty(True)
        return result

    def _del_store_available(self) -> None:
        result = BaseProduct._del_store_available(self)
        self._set_is_dirty(True)
        return result

    def _del_summary(self) -> None:
        result = BaseProduct._del_summary(self)
        self._set_is_dirty(True)
        return result

#     def _del_property_name(self) -> None:
#         self._property_name = None

    ###################################
    # Instance property definitions   #
    ###################################

    available = property(
        BaseProduct._get_available, _set_available, _del_available, 
        'Gets sets or deletes the flag that indicates whether the '
        'artisan owner of the product that the instance represents '
        'is considered by them to be available'
    )
    description = property(
        BaseProduct._get_description, _set_description, _del_description, 
        'Gets, sets or deletes the description (str) associated '
        'with the Product that the instance represents'
    )
    dimensions = property(
        BaseProduct._get_dimensions, _set_dimensions, _del_dimensions, 
        'Gets, sets or deletes the company name (str) associated '
        'with the Artisan that the instance represents'
    )
    metadata = property(
        BaseProduct._get_metadata, None, None,
        'Gets metadata (dict) associated with the '
        'Product that the instance represents'
    )
    name = property(
        BaseProduct._get_name, _set_name, _del_name, 
        'Gets, sets or deletes the name (str) associated with the '
        'Product that the instance represents'
    )
    shipping_weight = property(
        BaseProduct._get_shipping_weight, _set_shipping_weight, 
        _del_shipping_weight, 
        'Gets, sets or deletes the shipping_weight (int) '
        'associated with the Product that the instance '
        'represents'
    )
    store_available = property(
        BaseProduct._get_store_available, _set_store_available, 
        _del_store_available, 
        'Gets sets or deletes the flag that indicates whether the '
        'central office considers the product that the instance '
        'represents available on the web-store'
    )
    summary = property(
        BaseProduct._get_summary, _set_summary, _del_summary, 
        'Gets, sets or deletes the summary (str) associated with the '
        'Product that the instance represents'
    )

    ###################################
    # Object initialization           #
    ###################################

    def __init__(self, 
        # - Required arguments from BaseProduct
        name:(str,), summary:(str,), available:(bool,), 
        store_available:(bool,), 
        # - Optional arguments from BaseProduct
        description:(str,None)=None, dimensions:(str,None)=None,
        metadata:(dict,)={}, shipping_weight:(int,)=0, 
        # - Optional arguments from BaseDataObject/JSONFileDataObject
        oid:(UUID,str,None)=None, 
        created:(datetime,str,float,int,None)=None, 
        modified:(datetime,str,float,int,None)=None,
        is_active:(bool,int,None)=None, 
        is_deleted:(bool,int,None)=None,
        is_dirty:(bool,int,None)=None, 
        is_new:(bool,int,None)=None,
    ):
        """
Object initialization.

self .............. (Product instance, required) The instance to 
                    execute against
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
oid ............... (UUID|str, optional, defaults to None) 
created ........... (datetime|str|float|int, optional, defaults to None) 
modified .......... (datetime|str|float|int, optional, defaults to None) 
is_active ......... (bool|int, optional, defaults to None) 
is_deleted ........ (bool|int, optional, defaults to None) 
is_dirty .......... (bool|int, optional, defaults to None) 
is_new ............ (bool|int, optional, defaults to None) 
products .......... (BaseProduct collection) The products associated 
                    with the Artisan that the instance represents
"""
        # - Call parent initializers if needed
        BaseProduct.__init__(
            self, name, summary, available, store_available, 
            description, dimensions, metadata, shipping_weight
        )
        JSONFileDataObject.__init__(
            self, oid, created, modified, is_active, 
            is_deleted, is_dirty, is_new
        )
        # - Set default instance property-values using _del_... methods
        # - Set instance property-values from arguments using 
        #   _set_... methods
        # - Perform any other initialization needed
        self._set_is_dirty(False)

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Instance methods                #
    ###################################

    def matches(self, **criteria) -> (bool,):
        return BaseDataObject.matches(self, **criteria)

    def to_data_dict(self) -> (dict,):
        return {
            # Properties from BaseProduct:
            'available':self.available,
            'description':self.description,
            'dimensions':self.dimensions,
            'metadata':self.metadata,
            'name':self.name,
            'shipping_weight':self.shipping_weight,
            'store_available':self.store_available,
            'summary':self.summary,
            # - Properties from BaseDataObject (through 
            #   JSONFileDataObject)
            'created':datetime.strftime(
                self.created, self.__class__._data_time_string
            ),
            'is_active':self.is_active,
            'is_deleted':self.is_deleted,
            'modified':datetime.strftime(
                self.modified, self.__class__._data_time_string
            ),
            'oid':str(self.oid),
        }

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    @classmethod
    def _load_objects(cls, force_load=False):
        return JSONFileDataObject._load_objects(cls, force_load)

    @classmethod
    def from_data_dict(cls, data_dict:(dict,)):
        return cls(**data_dict)

    @classmethod
    def sort(cls, objects:(list,tuple), sort_by:(str,)) -> (list,):
        """
Returns a list of the original objects supplied, sorted by the 
criteria provided
"""
        raise NotImplementedError()

    ###################################
    # Static methods                  #
    ###################################

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

    import json

    address = Address('12345 Main Street', 'City Name')
    a = Artisan('John Smith', 'j@smith.com', address)
    a.save()
#    print(json.dumps(a.to_data_dict(), indent=4, sort_keys=True))
#    artisans = Artisan.get()
#    print(artisans)
    
    o = Order('name', 'street address', 'city')
    o.save()

    p = Product('name', 'summary', True, True)
    p.save()
#    products = Product.get()
#    print(products)
