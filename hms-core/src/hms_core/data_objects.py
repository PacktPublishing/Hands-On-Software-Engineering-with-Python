#!/usr/bin/env python
"""
Provides classes and functionality to help streamline the process of 
creating classes whose instances can persist their state-data in any 
of several back-end data-stores.
"""

# Adapted from concepts in Brian Allbee's original Python-code blog, 
# My Brain on Python, at
# https://my-brain-on-python.blogspot.com/

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
    'BaseDataObject',
    # Concrete classes
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
import inspect

from datetime import datetime
from uuid import UUID, uuid3, uuid4

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

#######################################
# Custom Exceptions                   #
#######################################

#######################################
# Module functions                    #
#######################################

#######################################
# ABC "interface" classes             #
#######################################

class BaseDataObject(metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements, and 
type-identity for objects that can persist their state-data in 
any of several back-end data-stores.
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    _data_time_string = '%Y-%m-%d %H:%M:%S'

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_created(self) -> datetime:
        if self._created == None:
            self.created = datetime.now()
        return self._created

    def _get_is_active(self) -> (bool,):
        return self._is_active

    def _get_is_deleted(self) -> (bool,):
        return self._is_deleted

    def _get_is_dirty(self) -> (bool,):
        return self._is_dirty

    def _get_is_new(self) -> (bool,):
        return self._is_new

    def _get_modified(self) -> datetime:
        if self._modified == None:
            self.modified = datetime.now()
        return self._modified

    def _get_oid(self) -> UUID:
        if self._oid == None:
            self._oid = uuid4()
        return self._oid

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_created(self, value:(datetime,str,float,int)):
        if type(value) not in (datetime,str,float,int):
            raise TypeError(
                '%s.created expects a datetime value, a numeric '
                'value (float or int) that can be converted to '
                'one, or a string value of the format "%s" that '
                'can be parsed into one, but was passed '
                '"%s" (%s)' % 
                (
                    self.__class__.__name__, 
                    value, self.__class__._data_time_string, 
                    type(value).__name__, 
                )
            )
        elif type(value) in (int, float):
            # - A numeric value was passed, so create a new 
            #   value from it
            try:
                value = datetime.fromtimestamp(value)
            except Exception as error:
                raise ValueError(
                    '%s.created could not create a valid datetime '
                    'object from the value provided, "%s" (%s) due '
                    'to an error - %s: %s' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__, 
                        error.__class__.__name__, error
                    )
                )
        elif type(value) == str:
            # - A string value was passed, so create a new value 
            #   by parsing it with the standard format
            try:
                value = datetime.strptime(
                    value, self.__class__._data_time_string
                )
            except Exception as error:
                raise ValueError(
                    '%s.created could not parse a valid datetime '
                    'object using "%s" from the value provided, '
                    '"%s" (%s) due to an error - %s: %s' % 
                    (
                        self.__class__.__name__, 
                        self.__class__._data_time_string, 
                        value, type(value).__name__, 
                        error.__class__.__name__, error
                    )
                )
        # - If this point is reached without error,then we have a 
        #   well-formed datetime object, so store it
        self._created = value
        

    def _set_is_active(self, value:(bool,int)):
        if value not in (True, False, 1, 0):
            raise ValueError(
                '%s.is_active expects either a boolean value '
                '(True|False) or a direct int-value equivalent '
                '(1|0), but was passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        if value:
            self._is_active = True
        else:
            self._is_active = False

    def _set_is_deleted(self, value:(bool,int)):
        if value not in (True, False, 1, 0):
            raise ValueError(
                '%s.is_deleted expects either a boolean value '
                '(True|False) or a direct int-value equivalent '
                '(1|0), but was passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        if value:
            self._is_deleted = True
        else:
            self._is_deleted = False

    def _set_is_dirty(self, value:(bool,int)):
        if value not in (True, False, 1, 0):
            raise ValueError(
                '%s.is_dirty expects either a boolean value '
                '(True|False) or a direct int-value equivalent '
                '(1|0), but was passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        if value:
            self._is_dirty = True
        else:
            self._is_dirty = False

    def _set_is_new(self, value:(bool,int)):
        if value not in (True, False, 1, 0):
            raise ValueError(
                '%s.is_new expects either a boolean value '
                '(True|False) or a direct int-value equivalent '
                '(1|0), but was passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        if value:
            self._is_new = True
        else:
            self._is_new = False

    def _set_modified(self, value:(datetime,str,float,int)):
        if type(value) not in (datetime,str,float,int):
            raise TypeError(
                '%s.modified expects a datetime value, a numeric '
                'value (float or int) that can be converted to '
                'one, or a string value of the format "%s" that '
                'can be parsed into one, but was passed '
                '"%s" (%s)' % 
                (
                    self.__class__.__name__, 
                    value, self.__class__._data_time_string, 
                    type(value).__name__, 
                )
            )
        elif type(value) in (int, float):
            # - A numeric value was passed, so create a new 
            #   value from it
            try:
                value = datetime.fromtimestamp(value)
            except Exception as error:
                raise ValueError(
                    '%s.modified could not create a valid datetime '
                    'object from the value provided, "%s" (%s) due '
                    'to an error - %s: %s' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__, 
                        error.__class__.__name__, error
                    )
                )
        elif type(value) == str:
            # - A string value was passed, so create a new value 
            #   by parsing it with the standard format
            try:
                value = datetime.strptime(
                    value, self.__class__._data_time_string
                )
            except Exception as error:
                raise ValueError(
                    '%s.modified could not parse a valid datetime '
                    'object using "%s" from the value provided, '
                    '"%s" (%s) due to an error - %s: %s' % 
                    (
                        self.__class__.__name__, 
                        self.__class__._data_time_string, 
                        value, type(value).__name__, 
                        error.__class__.__name__, error
                    )
                )
        # - If this point is reached without error,then we have a 
        #   well-formed datetime object, so store it
        self._modified = value

    def _set_oid(self, value:(UUID,str)):
        if type(value) not in (UUID,str):
            raise TypeError(
                '%s.oid expects a UUID value, or string '
                'representation of one, but was passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        if type(value) == str:
            try:
                value = UUID(value)
            except Exception as error:
                raise ValueError(
                    '%s.oid could not create a valid UUID from '
                    'the provided string "%s" because of an error '
                    '%s: %s' % 
                    (
                        self.__class__.__name__, value, 
                        error.__class__.__name__, error
                    )
                )
        self._oid = value

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_created(self) -> None:
        self._created = None

    def _del_is_active(self) -> None:
        self._is_active = True

    def _del_is_deleted(self) -> None:
        self._is_deleted = False

    def _del_is_dirty(self) -> None:
        self._is_dirty = False

    def _del_is_new(self) -> None:
        self._is_new = True

    def _del_modified(self) -> None:
        self._modified = None

    def _del_oid(self) -> None:
        self._oid = None

    ###################################
    # Instance property definitions   #
    ###################################

    created = property(
        _get_created, _set_created, _del_created, 
        'Gets, sets or deletes the date-time that the state-data '
        'record of the instance was created'
    )
    is_active = property(
        _get_is_active, _set_is_active, _del_is_active, 
        'Gets sets or deletes the flag that indicates whether '
        'the instance is considered active/available'
    )
    is_deleted = property(
        _get_is_deleted, _set_is_deleted, _del_is_deleted, 
        'Gets sets or deletes the flag that indicates whether '
        'the instance is considered to be "deleted," and thus '
        'not generally available'
    )
    is_dirty = property(
        _get_is_dirty, _set_is_dirty, _del_is_dirty, 
        'Gets sets or deletes the flag that indicates whether '
        'the instance\'s state-data has been changed such that '
        'its record needs to be updated'
    )
    is_new = property(
        _get_is_new, _set_is_new, _del_is_new, 
        'Gets sets or deletes the flag that indicates whether '
        'the instance needs to have a state-data record created'
    )
    modified = property(
        _get_modified, _set_modified, _del_modified, 
        'Gets, sets or deletes the date-time that the state-data '
        'record of the instance was last modified'
    )
    oid = property(
        _get_oid, _set_oid, _del_oid, 
        'Gets, sets or deletes the unique identifier of the '
        'instance\'s state-data record in the back-end data-store'
    )

    ###################################
    # Object initialization           #
    ###################################

    def __init__(self, 
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

self .............. (BaseDataObject instance, required) The instance to 
                    execute against
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
        # - Set default instance property-values using _del_... methods
        self._del_created()
        self._del_is_active()
        self._del_is_deleted()
        self._del_is_dirty()
        self._del_is_new()
        self._del_modified()
        self._del_oid()
        # - Set instance property-values from arguments using 
        #   _set_... methods
        if oid != None:
            self._set_oid(oid)
        if created != None:
            self._set_created(created)
        if modified != None:
            self._set_modified(modified)
        if is_active != None:
            self._set_is_active(is_active)
        if is_deleted != None:
            self._set_is_deleted(is_deleted)
        if is_dirty != None:
            self._set_is_dirty(is_dirty)
        if is_new != None:
            self._set_is_new(is_new)
        # - Perform any other initialization needed

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Abstract methods                #
    ###################################

    @abc.abstractmethod
    def _create(self) -> None:
        """
Creates a new state-data record for the instance in the back-end 
data-store
"""
        raise NotImplementedError(
            '%s has not implemented _create, as required by '
            'BaseDataObject' % (self.__class__.__name__)
        )

    @abc.abstractmethod
    def to_data_dict(self) -> (dict,):
        """
Returns a dictionary representation of the instance which can 
be used to generate data-store records, or for criteria-matching 
with the matches method.
"""
        raise NotImplementedError(
            '%s has not implemented _create, as required by '
            'BaseDataObject' % (self.__class__.__name__)
        )

    @abc.abstractmethod
    def _update(self) -> None:
        """
Updates an existing state-data record for the instance in the 
back-end data-store
"""
        raise NotImplementedError(
            '%s has not implemented _update, as required by '
            'BaseDataObject' % (self.__class__.__name__)
        )

    ###################################
    # Instance methods                #
    ###################################

    @abc.abstractmethod
    def matches(self, **criteria) -> (bool,):
        """
Compares the supplied criteria with the state-data values of 
the instance, and returns True if all instance properties 
specified in the criteria exist and equal the values supplied.
"""
        # - First, if criteria is empty, we can save some time 
        #   and simply return True - If no criteria are specified, 
        #   then the object is considered to match the criteria.
        if not criteria:
            return True
        # - Next, we need to check to see if all the criteria 
        #   specified even exist in the instance:
        data_dict = self.to_data_dict()
        data_keys = set(data_dict.keys())
        criteria_keys = set(criteria.keys())
        # - If all criteria_keys exist in data_keys, then the 
        #   intersection of the two will equal criteria_keys. 
        #   If that's not the case, at least one key-value won't 
        #   match (because it doesn't exist), so return False
        if criteria_keys.intersection(data_keys) != criteria_keys:
            return False
        # - Next, we need to verify that values match for all 
        #   specified criteria
        return all(
            [
                (data_dict[key] == criteria[key]) 
                for key in criteria_keys
            ]
        )

    def save(self):
        """
Saves the instance's state-data to the back-end data-store by 
creating it if the instance is new, or updating it if the 
instance is dirty
"""
        if self.is_new:
            self._create()
            self._set_is_new = False
            self._set_is_dirty = False
        elif self.is_dirty:
            self._update()
            self._set_is_dirty = False
            self._set_is_new = False

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    @abc.abstractclassmethod
    def delete(cls, *oids):
        """
Performs an ACTUAL record deletion from the back-end data-store 
of all records whose unique identifiers have been provided
"""
        raise NotImplementedError(
            '%s.delete (a class method) has not been implemented, '
            'as required by BaseDataObject' % (cls.__name__)
        )

    @abc.abstractclassmethod
    def from_data_dict(cls, data_dict:(dict,)):
        """
Creates and returns an instance of the class whose state-data has 
been populate with values from the provided data_dict
"""
        raise NotImplementedError(
            '%s.from_data_dict (a class method) has not been '
            'implemented, as required by BaseDataObject' % 
            (cls.__name__)
        )

    @abc.abstractclassmethod
    def get(cls, *oids, **criteria):
        """
Finds and returns all instances of the class from the back-end 
data-store whose oids are provided and/or that match the supplied 
criteria
"""
        raise NotImplementedError(
            '%s.get (a class method) has not been implemented, '
            'as required by BaseDataObject' % (cls.__name__)
        )

    @abc.abstractclassmethod
    def sort(cls, objects:(list,tuple), sort_by:(str,)) -> (list,):
        """
Returns a list of the original objects supplied, sorted by the 
criteria provided
"""
        raise NotImplementedError(
            '%s.sort (a class method) has not been implemented, '
            'as required by BaseDataObject' % (cls.__name__)
        )

    ###################################
    # Static methods                  #
    ###################################

#######################################
# Abstract classes                    #
#######################################

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
