#!/usr/bin/env python
"""
Provides classes and functionality that represent business objects 
in the context of teh central office applications and services, with 
state-data persistence to and from a MongoDB database.
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
from hms_core.data_storage import DatastoreConfig, HMSMongoDataObject

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

class Artisan(BaseArtisan, HMSMongoDataObject):
    """
Represents an Artisan in the context of the central office 
applications and services
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    _data_dict_keys = (
        'contact_name', 'contact_email', 'address', 'company_name', 
        'website', 'oid', 'created', 'modified', 'is_active', 
        'is_deleted', 'products'
    )

    ###################################
    # Property-getter methods         #
    ###################################

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
        contact_name:str, contact_email:str, 
        address:Address, company_name:str=None, 
        website:(str,)=None, 
        # - Arguments from HMSMongoDataObject
        oid:(UUID,str,None)=None, 
        created:(datetime,str,float,int,None)=None, 
        modified:(datetime,str,float,int,None)=None,
        is_active:(bool,int,None)=None, 
        is_deleted:(bool,int,None)=None,
        is_dirty:(bool,int,None)=None, 
        is_new:(bool,int,None)=None,
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
oid ............... (UUID|str, optional, defaults to None) The unique 
                    identifier of the object's state-data record in the 
                    back-end data-store
created ........... (datetime|str|float|int, optional, defaults to None) 
                    The date/time that the object was created
modified .......... (datetime|str|float|int, optional, defaults to None) 
                    The date/time that the object was last modified
is_active ......... (bool|int, optional, defaults to None) A flag 
                    indicating that the object is active
is_deleted ........ (bool|int, optional, defaults to None) A flag 
                    indicating that the object should be considered 
                    deleted (and may be in the near future)
is_dirty .......... (bool|int, optional, defaults to None) A flag 
                    indicating that the object's data needs to be 
                    updated in the back-end data-store
is_new ............ (bool|int, optional, defaults to None) A flag 
                    indicating that the object's data needs to be 
                    created in the back-end data-store
products .......... (BaseProduct collection) The products associated 
                    with the Artisan that the instance represents
"""
        # - Call parent initializers if needed
        BaseArtisan.__init__(self, 
            contact_name, contact_email, address, company_name, website
        )
        HMSMongoDataObject.__init__(self, 
            oid, created, modified, is_active, is_deleted, 
            is_dirty, is_new
        )
        if products:
            BaseArtisan._set_products(*products)
        # - Perform any other initialization needed

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Instance methods                #
    ###################################

    def add_product(self, product:BaseProduct) -> BaseProduct:
        return HasProducts.add_product(self, product)

    def matches(self, **criteria) -> (bool,):
        return HMSMongoDataObject.matches(self, **criteria)

    def remove_product(self, product:BaseProduct) -> None:
        return HasProducts.remove_product(self, product)

    def to_data_dict(self):
        return {
            # - BaseArtisan-derived items
            'address':self.address.to_dict() if self.address else None,
            'company_name':self.company_name,
            'contact_email':self.contact_email,
            'contact_name':self.contact_name,
            'website':self.website, 
            # - BaseDataObject-derived items
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
    def from_data_dict(cls, data_dict):
        # - This has to be overridden because we have to pre-process 
        #   incoming address and (maybe, eventually?) product-list 
        #   values...
        if data_dict.get('address'):
            data_dict['address'] = Address.from_dict(data_dict['address'])
        ####### NOTE: Changes made here, for whatever reason might 
        #       arise, may also need to be made in 
        #       HMSMongoDataObject.from_data_dict – it's the same 
        ####### process!
        # - Assure that we have the collection of keys that are 
        #   allowed for the class!
        if cls._data_dict_keys == None:
            from inspect import getfullargspec
            argspec = getfullargspec(cls.__init__)
            init_args = argspec.args
            try:
                init_args.remove('self')
            except:
                pass
            try:
                init_args.remove('cls')
            except:
                pass
            print(argspec)
            if argspec.varargs:
                init_args.append(argspec.varargs)
            if argspec.varkw:
                init_args.append(argspec.varkw)
            raise AttributeError(
                '%s.from_data_dict cannot be used because the %s '
                'class has not specified what data-store keys are '
                'allowed to be used to create new instances from '
                'retrieved data. Set %s._data_dict_keys to a list '
                'or tuple of argument-names present in %s.__init__ '
                '(%s)' % 
                (
                    cls.__name__, cls.__name__, cls.__name__, 
                    cls.__name__, "'" + "', '".join(init_args) + "'"
                )
            )
        # - Remove any keys that aren't listed in the class' 
        #   initialization arguments:
        data_dict = dict(
            [
                (key, data_dict[key]) for key in data_dict.keys() 
                if key in cls._data_dict_keys
            ]
        )
        # - Then create and return an instance of the class
        return cls(**data_dict)

    @classmethod
    def sort(cls, objects:(list,tuple), sort_by:(str,)) -> (list,):
        return BaseDataObject.sort(cls, objects, sort_by)

    ###################################
    # Static methods                  #
    ###################################

class Product(BaseProduct, HMSMongoDataObject):
    """
Represents a Product in the context of the central office 
applications and services
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    _data_dict_keys = [
        'name', 'summary', 'available', 'store_available', 
        'description', 'dimensions', 'metadata', 'shipping_weight', 
        'oid', 'created', 'modified', 'is_active', 'is_deleted'
    ]

    ###################################
    # Property-getter methods         #
    ###################################

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
        # - Arguments from HMSMongoDataObject
        name:(str,), summary:(str,), available:(bool,), 
        store_available:(bool,), 
        # - Optional arguments:
        description:(str,None)=None, dimensions:(str,None)=None,
        metadata:(dict,)={}, shipping_weight:(int,)=0, 
        # - Arguments from HMSMongoDataObject
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
oid ............... (UUID|str, optional, defaults to None) The unique 
                    identifier of the object's state-data record in the 
                    back-end data-store
created ........... (datetime|str|float|int, optional, defaults to None) 
                    The date/time that the object was created
modified .......... (datetime|str|float|int, optional, defaults to None) 
                    The date/time that the object was last modified
is_active ......... (bool|int, optional, defaults to None) A flag 
                    indicating that the object is active
is_deleted ........ (bool|int, optional, defaults to None) A flag 
                    indicating that the object should be considered 
                    deleted (and may be in the near future)
is_dirty .......... (bool|int, optional, defaults to None) A flag 
                    indicating that the object's data needs to be 
                    updated in the back-end data-store
is_new ............ (bool|int, optional, defaults to None) A flag 
                    indicating that the object's data needs to be 
                    created in the back-end data-store
"""
        # - Call parent initializers if needed
        BaseProduct.__init__(
            self, name, summary, available, store_available, 
            description, dimensions, metadata, shipping_weight
        )
        HMSMongoDataObject.__init__(self, 
            oid, created, modified, is_active, is_deleted, 
            is_dirty, is_new
        )
        # - Set default instance property-values using _del_... methods
        # - Set instance property-values from arguments using 
        #   _set_... methods
        # - Perform any other initialization needed

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Instance methods                #
    ###################################

    def matches(self, **criteria) -> (bool,):
        return HMSMongoDataObject.matches(self, **criteria)

    def to_data_dict(self):
        return {
            # - BaseProduct-derived items
            'available':self.available,
            'description':self.description,
            'dimensions':self.dimensions,
            'metadata':self.metadata,
            'name':self.name,
            'shipping_weight':self.shipping_weight,
            'store_available':self.store_available,
            'summary':self.summary,
            # - BaseDataObject-derived items
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
    def sort(cls, objects:(list,tuple), sort_by:(str,)) -> (list,):
        return BaseDataObject.sort(cls, objects, sort_by)

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

    config = DatastoreConfig(
        database='delete_me_later',
    )

    HMSMongoDataObject.configure(config)

