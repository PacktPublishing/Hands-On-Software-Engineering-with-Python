#!/usr/bin/env python
"""
TODO: Document the module.
Provides classes and functionality for SOME_PURPOSE
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
    'JSONFileDataObject',
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
import json
import os

from datetime import datetime
from uuid import UUID, uuid4

#######################################
# Third-party imports needed          #
#######################################

from hms_core.data_objects import BaseDataObject

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

class JSONFileDataObject(BaseDataObject, metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements, and 
type-identity for objects that can persist their state-data as 
JSON files in a local file-system file-cache
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    _file_store_dir = None
    _file_store_ready = False
    _loaded_objects = None

    ###################################
    # Property-getter methods         #
    ###################################

#     def _get_property_name(self) -> str:
#         return self._property_name

    ###################################
    # Property-setter methods         #
    ###################################

#     def _set_property_name(self, value:str) -> None:
#         # TODO: Type- and/or value-check the value argument of the 
#         #       setter-method, unless it's deemed unnecessary.
#         self._property_name = value

    ###################################
    # Property-deleter methods        #
    ###################################

#     def _del_property_name(self) -> None:
#         self._property_name = None

    ###################################
    # Instance property definitions   #
    ###################################

#     abstract_property = abc.abstractproperty()

#     property_name = property(
#         # TODO: Remove setter and deleter if access is not needed
#         _get_property_name, _set_property_name, _del_property_name, 
#         'Gets, sets or deletes the property_name (str) of the instance'
#     )

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

self .............. (JSONFileDataObject instance, required) The 
                    instance to execute against
oid ............... (UUID|str, optional, defaults to None) 
created ........... (datetime|str|float|int, optional, defaults to None) 
modified .......... (datetime|str|float|int, optional, defaults to None) 
is_active ......... (bool|int, optional, defaults to None) 
is_deleted ........ (bool|int, optional, defaults to None) 
is_dirty .......... (bool|int, optional, defaults to None) 
is_new ............ (bool|int, optional, defaults to None) 
"""
        # - When used by a subclass, require that subclass to 
        #   define a valid file-system path in its _file_store_dir 
        #   class-attribute - that's where the JSON files will live
        if self.__class__._file_store_dir == None:
            raise AttributeError(
                '%s has not defined a file-system location to '
                'store JSON data of its instances\' data. Please '
                'set %s._file_store_dir to a valid file-system '
                'path' % 
                (self.__class__.__name__, self.__class__.__name__)
            )
        if not self.__class__._file_store_ready:
            # - The first time the class is used, check the file-
            #   storage directory, and if everything checks out, 
            #   then re-set the flag that controls the checks.
            if not os.path.exists(self.__class__._file_store_dir):
                # - If the path-specification exists, try to 
                #   assure that the *path* exists, and create it 
                #   if it doesn't. If the path can't be created, 
                #   then that'll be an issue later too, so it'll 
                #   need to be dealt with.
                try:
                    os.makedirs(self.__class__._file_store_dir)
                except PermissionError:
                    raise PermissionError(
                        '%s cannot create the JSON data-store '
                        'directory (%s) because permission was '
                        'denied. Please check permissions on '
                        'that directory (or its parents, if it '
                        'hasn\'t been created yet) and try '
                        'again.' % 
                        (
                            self.__class__.__name__, 
                            self.__class__._file_store_dir
                        )
                    )
                # - Check to make sure that files can be 
                #   created there...
                try:
                    test_file = open(
                        '%s%stest-file.txt' % 
                        (self.__class__._file_store_dir, os.sep), 
                        'w'
                    )
                    test_file.write('test-file.txt')
                    test_file.close()
                except PermissionError:
                    raise PermissionError(
                        '%s cannot write files to the JSON data-'
                        'store directory (%s) because permission was '
                        'denied. Please check permissions on that '
                        'directory and try again.' % 
                        (
                            self.__class__.__name__, 
                            self.__class__._file_store_dir
                        )
                    )
                # - ... that files can be read from there...
                try:
                    test_file = open(
                        '%s%stest-file.txt' % 
                        (self.__class__._file_store_dir, os.sep), 
                        'r'
                    )
                    test_file.read()
                    test_file.close()
                except PermissionError:
                    raise PermissionError(
                        '%s cannot read files in the JSON data-'
                        'store directory (%s) because permission was '
                        'denied. Please check permissions on that '
                        'directory and try again.' % 
                        (
                            self.__class__.__name__, 
                            self.__class__._file_store_dir
                        )
                    )
                # - ... and deleted from there...
                try:
                    os.unlink(
                        '%s%stest-file.txt' % 
                        (self.__class__._file_store_dir, os.sep)
                    )
                except PermissionError:
                    raise PermissionError(
                        '%s cannot delete files in the JSON data-'
                        'store directory (%s) because permission was '
                        'denied. Please check permissions on that '
                        'directory and try again.' % 
                        (
                            self.__class__.__name__, 
                            self.__class__._file_store_dir
                        )
                    )
                # - If no errors were raised, then re-set the flag:
                self._file_store_ready = True
        # - Call parent initializers if needed
        BaseDataObject.__init__(
            self, oid, created, modified, is_active, is_deleted, 
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
    # Abstract methods                #
    ###################################

    ###################################
    # Instance methods                #
    ###################################

    def _create(self) -> None:
        """
Creates a new state-data record for the instance in the back-end 
data-store
"""
        # - Since all data-transactions for these objects involve 
        #   a file-write, we're just going to define this method 
        #   in order to meet the requirements of BaseDataObject, 
        #   make it raise an error, and override the save method 
        #   to perform the actual file-write.
        raise NotImplementedError(
            '%s._create is not implemented, because the save '
            'method handles all the data-writing needed for '
            'the class. Use save() instead.' % 
            self.__class__.__name__
        )

    def _update(self) -> None:
        """
Updates an existing state-data record for the instance in the 
back-end data-store
"""
        # - Since all data-transactions for these objects involve 
        #   a file-write, we're just going to define this method 
        #   in order to meet the requirements of BaseDataObject, 
        #   make it raise an error, and override the save method 
        #   to perform the actual file-write.
        raise NotImplementedError(
            '%s._update is not implemented, because the save '
            'method handles all the data-writing needed for '
            'the class. Use save() instead.' % 
            self.__class__.__name__
        )

    # NOTE: This can be used to illustrate unittest.skip
    def save(self):
        """
Saves the instance's state-data to the back-end data-store by 
creating it if the instance is new, or updating it if the 
instance is dirty
"""
        if self.is_new or self.is_dirty:
            # - Make sure objects are loaded:
            self.__class__._load_objects(self.__class__)
            # - Try to save the data:
            try:
                # - Open the file
                fp = open(
                    '%s%s%s-data%s%s.json' %
                    (
                        self.__class__._file_store_dir, os.sep, 
                        self.__class__.__name__, os.sep, 
                        self.oid
                    ), 'w'
                )
                # - Write the instance's data-dict to the file as JSON
                json.dump(self.to_data_dict(), fp, indent=4)
                # - re-set the new and dirty state-flags
                self._set_is_dirty(False)
                self._set_is_new(False)
                # - Update it in the loaded objects
                self.__class__._loaded_objects[self.oid] = self
            except PermissionError:
                # - Raise a more informative error
                raise PermissionError(
                    '%s could not save an object to the JSON data-'
                    'store directory (%s) because permission was '
                    'denied. Please check permissions on that '
                    'directory and try again.' % 
                    (
                        self.__class__.__name__, 
                        self.__class__._file_store_dir
                    )
                )
            # - Any other errors will just surface for the time being

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    def _load_objects(cls, force_load=False):
        """
Class-level helper-method that loads all of the objects in the 
local file-system data-store into memory so that they can be 
used more quickly afterwards.

Expected to be called by the get class-method to load objects 
for local retrieval, and other places as needed.

cls .......... (class, required) The class that the method is 
               bound to
force_load ... (bool, optional, defaults to False) If True, 
               forces the process to re-load data from scratch, 
               otherwise skips the load process if data already 
               exists.
"""
        if cls._loaded_objects == None or force_load:
            if not os.path.exists(cls._file_store_dir):
                # - If the path-specification exists, try to 
                #   assure that the *path* exists, and create it 
                #   if it doesn't. If the path can't be created, 
                #   then that'll be an issue later too, so it'll 
                #   need to be dealt with.
                try:
                    os.makedirs(cls._file_store_dir)
                except PermissionError:
                    raise PermissionError(
                        '%s cannot create the JSON data-store '
                        'directory (%s) because permission was '
                        'denied. Please check permissions on '
                        'that directory (or its parents, if it '
                        'hasn\'t been created yet) and try '
                        'again.' % 
                        (cls.__name__, cls._file_store_dir)
                    )
            class_files_path = '%s%s%s-data' % (
                cls._file_store_dir, os.sep, 
                cls.__name__
            )
            if not os.path.exists(class_files_path):
                try:
                    os.makedirs(class_files_path)
                except PermissionError:
                    raise PermissionError(
                        '%s cannot create the JSON data-store '
                        'directory (%s) because permission was '
                        'denied. Please check permissions on '
                        'that directory (or its parents, if it '
                        'hasn\'t been created yet) and try '
                        'again.' % 
                        (cls.__name__, class_files_path)
                    )
            # - Get a list of all the JSON files in the data-store 
            #   path
            files = [
                fname for fname in os.listdir(
                    '%s%s%s-data' % (
                        cls._file_store_dir, os.sep, 
                        cls.__name__
                    )
                ) if fname.endswith('.json')
            ]
            cls._loaded_objects = {}
            if files:
                for fname in files:
                    item_file = '%s%s%s-data%s%s' % (
                        cls._file_store_dir, os.sep, 
                        cls.__name__, os.sep, fname
                    )
                    try:
                        # - Read the JSON data
                        fp = open(item_file, 'r')
                        data_dict = json.load(fp)
                        fp.close()
                        # - Create an instance from that data
                        instance = cls.from_data_dict(data_dict)
                        # - Keep track of it by oid in the class
                        cls._loaded_objects[instance.oid] = instance
                    # - If permissions are a problem, raise an 
                    #   error with helpful information
                    except PermissionError as error:
                        raise PermissionError(
                            '%s could not load object-data from '
                            'the data-store file at %s because '
                            'permission was denied. Please check '
                            '(and, if needed, correct) the file- '
                            'and directory-permissions and try '
                            'again' % 
                            (cls.__name__, item_file)
                        )
                    # - If data-structure or -content is a problem, 
                    #   raise an error with helpful information
                    except (TypeError, ValueError) as error:
                        raise error.__class__(
                            '%s could not load object-data from '
                            'the data-store file at %s because '
                            'the data was corrupt or not what '
                            'was expected (%s: %s)' % 
                            (
                                cls.__name__, item_file, 
                                error.__class__.__name__, error
                            )
                        )
                    # - Other errors will simply surface, at 
                    #   least for now

    @classmethod
    def delete(cls, *oids):
        """
Performs an ACTUAL record deletion from the back-end data-store 
of all records whose unique identifiers have been provided
"""
        # - First, ensure that objects are loaded
        cls._load_objects(cls)
        # - For each oid specified, try to remove the file, handling 
        #   any errors raised in the process.
        failed_deletions = []
        for oid in oids:
            try:
                # - Try to delete the file first, so that deletion 
                #   failures won't leave the files but remove the 
                #   in-memory copies
                file_path = '%s%s%s-data%s%s.json' %(
                    cls._file_store_dir, os.sep, 
                    cls.__name__, os.sep, oid
                )
                # - Delete the file at file_path
                os.unlink(file_path)
                # - Remove the in-memory object-instance:
                del cls._loaded_objects[oid]
            except PermissionError:
                failed_deletions.append(file_path)
        if failed_deletions:
            # - Though we *are* raising an error here, *some* deletions 
            #   may have succeeded. If this error-message is displayed, 
            #   the user seeing it need only be concerned with the 
            #   items that failed, though...
            raise PermissionError(
                '%s.delete could not delete %d object-data %s '
                'because permission was denied. Please check the '
                'permissions on %s and try again' % 
                (
                    cls.__name__, len(failed_deletions), 
                    ('files' if len(failed_deletions) > 1 else 'file'), 
                    ', '.join(failed_deletions)
                )
            )

    @classmethod
    def get(cls, *oids, **criteria):
        """
Finds and returns all instances of the class from the back-end 
data-store whose oids are provided and/or that match the supplied 
criteria
"""
        # - First, ensure that objects are loaded
        cls._load_objects(cls)
        # - If oids have been specified, then the initial results are all 
        #   items in the in-memory store whose oids are in the supplied 
        #   oids-list
        if oids:
            oids = tuple(
                [str(o) for o in oids]
            )
            # - If no criteria were supplied, then oids are all we need 
            #   to match against:
            if not criteria:
                results = [
                    o for o in cls._loaded_objects.values()
                    if str(o.oid) in oids
                ]
            # - Otherwise, we *also* need to use matches to find items 
            #   that match the criteria
            else:
                results = [
                    o for o in cls._loaded_objects.values()
                    if str(o.oid) in oids
                    and o.matches(**criteria)
                ]
            # - In either case, we have a list of matching items, which 
            #   may be empty, so return it:
            return results
        # - If oids were NOT specified, then the results are all objects 
        #   in memory that match the criteria
        elif criteria:
            results = [
                o for o in cls._loaded_objects
                if o.matches(**criteria)
            ]
            return results
        # - If neither were specified, return all items available:
        else:
            return list(cls._loaded_objects.values())
    

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
