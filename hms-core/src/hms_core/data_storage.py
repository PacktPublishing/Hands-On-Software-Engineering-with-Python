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
    'HMSMongoDataObject',
    # Concrete classes
    'DatastoreConfig',
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
import pymongo

from datetime import datetime
from uuid import UUID

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
# Concrete classes for dependencies   #
# in ABCs below                       #
#######################################

class DatastoreConfig:
    """
Represents a set of credentials for connecting to a back-end 
database engine that requires host, port, database, user, and 
password values.
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_database(self) -> str:
        return self._database

    def _get_host(self) -> str:
        return self._host

    def _get_password(self) -> str:
        return self._password

    def _get_port(self) -> int:
        return self._port

    def _get_user(self) -> str:
        return self._user

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_database(self, value:str) -> None:
        if type(value) != str:
            raise TypeError(
                '%s.database expects a non-empty, single-line string '
                'value with no whitespace other than spaces, but was '
                'passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        if not value.strip() or '\n' in value or '\t' in value \
            or '\r' in value:
            raise ValueError(
                '%s.database expects a non-empty, single-line string '
                'value with no whitespace other than spaces, but was '
                'passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        self._database = value

    def _set_host(self, value:str) -> None:
        if type(value) != str:
            raise TypeError(
                '%s.host expects a non-empty, single-line string '
                'value with no whitespace other than spaces, but '
                'was passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        if not value.strip() or '\n' in value or '\t' in value \
            or '\r' in value:
            raise ValueError(
                '%s.host expects a non-empty, single-line string '
                'value with no whitespace other than spaces, but '
                'was passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        self._host = value

    def _set_password(self, value:str) -> None:
        if type(value) != str:
            raise TypeError(
                '%s.password expects a non-empty, single-line string '
                'value with no whitespace other than spaces, but was '
                'passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        if not value.strip() or '\n' in value or '\t' in value \
            or '\r' in value:
            raise ValueError(
                '%s.password expects a non-empty, single-line string '
                'value with no whitespace other than spaces, but was '
                'passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        self._password = value

    def _set_port(self, value:int) -> None:
        if type(value) != int:
            raise TypeError(
                '%s.port expects an int value from 0 through 65535, '
                'inclusive, but was passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        if value < 0 or value > 65535:
            raise ValueError(
                '%s.port expects an int value from 0 through 65535, '
                'inclusive, but was passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        self._port = value

    def _set_user(self, value:str) -> None:
        if type(value) != str:
            raise TypeError(
                '%s.user expects a non-empty, single-line string '
                'value with no whitespace other than spaces, but '
                'was passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        if not value.strip() or '\n' in value or '\t' in value \
            or '\r' in value:
            raise ValueError(
                '%s.user expects a non-empty, single-line string '
                'value with no whitespace other than spaces, but '
                'was passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        self._user = value

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_database(self) -> None:
        self._database = None

    def _del_host(self) -> None:
        self._host = None

    def _del_password(self) -> None:
        self._password = None

    def _del_port(self) -> None:
        self._port = None

    def _del_user(self) -> None:
        self._user = None

    ###################################
    # Instance property definitions   #
    ###################################

    database=property(
        _get_database, _set_database, _del_database, 
        'Gets, sets or deletes the name of the database that '
        'instance-data will be persisted in'
    )
    host=property(
        _get_host, _set_host, _del_host, 
        'Gets, sets or deletes the host-name of the MongoDB service '
        'that instance-data will be persisted in'
    )
    password=property(
        _get_password, _set_password, _del_password, 
        'Gets, sets or deletes the password that will be used to '
        'connect to the MongoDB service that instance-data will be persisted in'
    )
    port=property(
        _get_port, _set_port, _del_port, 
        'Gets, sets or deletes the TCP/IP port of the MongoDB service '
        'that instance-data will be persisted in'
    )
    user=property(
        _get_user, _set_user, _del_user, 
        'Gets, sets or deletes the user-name that will be used to '
        'connect to the MongoDB service that instance-data will be persisted in'
    )

    ###################################
    # Object initialization           #
    ###################################

    def __init__(self, 
        host=None, port=None, database=None, user=None, password=None
    ):
        """
Object initialization.

self .............. (DatastoreConfig instance, required) The instance 
                    to execute against
host .............. (str, optional, defaults to None) the host-name 
                    (FQDN, machine network-name or IP address) where 
                    the database that the instance will use to persist 
                    state-data resides
port .............. (int [0..65535], optional, defaults to None) the 
                    TCP/IP port on the host that the database 
                    connection will use
database .......... (str, optional, defaults to None) the name of 
                    the database that the instance will use to persist 
                    state-data
user .............. (str, optional, defaults to None) the user-name 
                    used to connect to the database that the instance 
                    will use to persist state-data
password .......... (str, optional, defaults to None) the password 
                    used to connect to the database that the instance 
                    will use to persist state-data
"""
        # - Call parent initializers if needed
        # - Set default instance property-values using _del_... methods
        self._del_database()
        self._del_host()
        self._del_password()
        self._del_port()
        self._del_user()
        # - Set instance property-values from arguments using 
        #   _set_... methods
        if host != None:
            self._set_host(host)
        if port != None:
            self._set_port(port)
        if database != None:
            self._set_database(database)
        if user != None:
            self._set_user(user)
        if password != None:
            self._set_password(password)
        # - Perform any other initialization needed

    ###################################
    # Object deletion                 #
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

    @classmethod
    def from_config(cls, config_file:(str,)):
        # - Use an explicit try/except instead of with ... as ...
        try:
            fp = open(config_file, 'r')
            config_data = fp.read()
            fp.close()
        except (IOError, PermissionError) as error:
            raise error.__class__(
                '%s could not read the config-file at %s due to '
                'an error (%s): %s' % 
                (
                    self.__class__.__name__, config_file, 
                    error.__class__.__name__, error
                )
            )
        # - For now, we'll assume that config-data is in JSON, though 
        #   other formats might be better later on (YAML, for instance)
        load_successful = False
        try:
            parameters = json.loads(config_data)
            load_successful = True
        except Exception as error:
            pass
        # - YAML can go here
        # - .ini-file format here, maybe?
        if load_successful:
            try:
                return cls(**parameters)
            except Exception as error:
                raise RuntimeError(
                    '%s could not load configuration-data from %s '
                    'due to an %s: %s' % 
                    (
                        cls.__name__, config_file, 
                        error.__class__.__name__, error
                    )
                )
        else:
            raise RuntimeError(
                '%s did not recognize the format of the config-file '
                'at %s' % (cls.__name__, config_file)
            )

    ###################################
    # Static methods                  #
    ###################################

#######################################
# ABC "interface" classes             #
#######################################

#######################################
# Abstract classes                    #
#######################################

class HMSMongoDataObject(BaseDataObject, metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements, and 
type-identity for objects that can persist their state-data to 
a MongoDB-based back-end data-store.
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    # - Keeps track of the global configuration for data-access
    _configuration = None
    # - Keeps track of the keys allowed for object-creation from 
    #   retrieved data
    _data_dict_keys = None
    # - Allows the default mongo-collection name (the __name__ 
    #   of the class) to be overridden. This should not be changed 
    #   lightly, since data saved to the old collection-name will 
    #   no longer be available!
    _mongo_collection = None

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_collection(self) -> pymongo.collection.Collection:
        try:
            return self.__class__._collection
        except AttributeError:
            # - If the class specifies a collection-name, then use that 
            #   as the collection...
            if self.__class__._mongo_collection:
                self.__class__._collection = self.database[
                    self.__class__._mongo_collection
                ]
            # - Otherwise, use the class-name
            else:
                self.__class__._collection = self.database[
                    self.__class__.__name__
                ]
            return self.__class__._collection

    def _get_configuration(self) -> DatastoreConfig:
        return HMSMongoDataObject._configuration

    def _get_connection(self) -> pymongo.MongoClient:
        try:
            return self.__class__._connection
        except AttributeError:
            # - Build the connection-parameters we need:
            conn_config = []
            # - host
            if self.configuration.host:
                conn_config.append(self.configuration.host)
                # - port. Ports don't make any sense without a 
                #   host, though, so host has to be defined first...
                if self.configuration.port:
                    conn_config.append(self.configuration.port)
            # - Create the connection
            self.__class__._connection = pymongo.MongoClient(*conn_config)
            return self.__class__._connection

    def _get_database(self) -> pymongo.database.Database:
        try:
            return self.__class__._database
        except AttributeError:
            self.__class__._database = self.connection[
                self.configuration.database
            ]
            return self.__class__._database

    ###################################
    # Property-setter methods         #
    ###################################

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_collection(self) -> None:
        # - If the collection is deleted, then the database needs 
        #   to be as well:
        self._del_database()
        try:
            del self._collection
        except AttributeError:
            # - It may already not exist
            pass

    def _del_connection(self) -> None:
        # - If the connection is deleted, then the collection and 
        #   database need to be as well:
        self._del_collection()
        self._del_database()
        try:
            del self.__class__._connection
        except AttributeError:
            # - It may already not exist
            pass

    def _del_database(self) -> None:
        try:
            del self.__class__._database
        except AttributeError:
            # - It may already not exist
            pass

    ###################################
    # Instance property definitions   #
    ###################################

    collection = property(
        _get_collection, None, _del_collection, 
        'Gets or deletes the MongoDB collection that instance '
        'state-data is stored in'
    )
    connection = property(
        _get_connection, None, _del_connection, 
        'Gets or deletes the database-connection that the instance '
        'will use to manage its persistent state-data'
    )
    database = property(
        _get_database, None, _del_database, 
        'Gets or deletes the MongoDB database that instance '
        'state-data is stored in'
    )
    configuration = property(
        _get_configuration, None, None, 
        'Gets, sets or deletes the configuration-data '
        '(DatastoreConfig) of the instance, from HMSMongoDataObject'
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

self .............. (HMSMongoDataObject instance, required) The 
                    instance to execute against
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
        BaseDataObject.__init__(self, 
            oid, created, modified, is_active, is_deleted, 
            is_dirty, is_new
        )
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
# self .............. (HMSMongoDataObject instance, required) The 
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

    def save(self):
        # TODO: For the time being, we're going to assume that save 
        #       operations don't need to care about whether the 
        #       object's data is new or dirty, that we wouldn't be 
        #       calling save unless we already knew that to be the 
        #       case. If that changes, we'll want to check is_dirty 
        #       and is_new, as shown below, *and* make sure that 
        #       they get modified accordingly.
#        if self._is_new or self._is_dirty:
        # - Make sure to update the modified time-stamp!
        self.modified = datetime.now()
        data_dict = self.to_data_dict()
        data_dict['_id'] = self.oid
        self.collection.insert_one(data_dict)
        self._set_is_dirty(False)
        self._set_is_new(False)

#     def instance_method(self, arg:str, *args, **kwargs):
#         """TODO: Document method
# DOES_WHATEVER
# 
# self .............. (HMSMongoDataObject instance, required) The 
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

    @classmethod
    def configure(cls, configuration:(DatastoreConfig)):
        """
Sets configuration values across all classes derived from 
HMSMongoDataObject.
"""
        if cls != HMSMongoDataObject:
            raise RuntimeError(
                '%s.configure will alter *all* MongoDB configuration, '
                'not just the configuration for %s. Please use '
                'HMSMongoDataObject.configure instead.' % 
                (cls.__name__, cls.__name__)
            )
        if not isinstance(configuration, DatastoreConfig):
            raise TypeError(
                '%s.configure expects an instance of '
                'DatastoreConfig, but was passed "%s" (%s)' % 
                (
                    cls.__name__, configuration, 
                    type(configuration).__name__
                )
            )
        HMSMongoDataObject._configuration = configuration

    @classmethod
    def delete(cls, *oids):
        """
Performs an ACTUAL record deletion from the back-end data-store 
of all records whose unique identifiers have been provided
"""
        # - First, we need the collection that we're working with:
        collection = cls.get_mongo_collection()
        if oids:
            for oid in oids:
                collection.remove({'oid':str(oid)})

    @classmethod
    def from_data_dict(cls, data_dict):
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
                if data_dict
                and key in cls._data_dict_keys
            ]
        )
        # - Then create and return an instance of the class
        return cls(**data_dict)

    @classmethod
    def get(cls, *oids, **criteria) -> list:
        # - First, we need the collection that we're working with:
        collection = cls.get_mongo_collection()
        # - The first pass of the process retrieves documents based 
        #   on oids or criteria.
        # - We also need to keep track of whether or not to do a 
        #   matches call on the results after the initial data-
        #   retrieval:
        post_filter = False
        if oids:
            # - oid-based requests should usually be a fairly short 
            #   list, so finding individual items and appending them 
            #   should be OK, performance-wise.
            data_dicts = [
                collection.find_one({'oid':oid})
                for oid in oids
            ]
            # - If this becomes an issue later, consider changing 
            #   it to a variant of 
            #   collection.find({'oid':{'$in':oids}})
            #   (the oids argument-list may need pre-processing first)
            if criteria:
                post_filter = True
        elif criteria:
            # - criteria-based items can do a find based on all criteria 
            #   straight away
            data_dicts = [
                item for item in collection.find(criteria)
            ]
        else:
            # - If there are no oids specified, and no criteria, 
            #   the implication is that we want *all* object-records 
            #   to be returned...
            # - First, we need the results
            data_dicts = [
                item for item in collection.find()
            ]
        # - At this point, we have data_dict values that should be 
        #   able to create instances, so create them.
        results = [
            cls.from_data_dict(data_dict) 
            for data_dict in data_dicts
            if data_dict
        ]
        # - If post_filter has been set to True, then the request 
        #   was for items by oid *and* that have certain criteria
        if post_filter:
            results = [
                obj for obj in results if obj.matches(**criteria)
            ]
        return results

    @classmethod
    def get_mongo_collection(cls) -> pymongo.collection.Collection:
        """
Helper class-method that retrieves the relevant MongoDB collection for 
data-access to state-data records for the class.
"""
        # - If the collection has already been created, then 
        #   return it, otherwise create it then return it
        try:
            return cls._collection
        except AttributeError:
            pass
        if not cls._configuration:
            raise RuntimeError(
                '%s must be configured before the '
                'use of %s.get will work. Call HMSMongoDataObject.'
                'configure with a DatastoreConfig object to resolve '
                'this issue' % (cls.__name__, cls.__name__)
            )
        # - With configuration established, we can create the 
        #   connection, database and collection objects we need 
        #   in order to execute the request:
        # - Build the connection-parameters we need:
        conn_config = []
        # - host
        if cls._configuration.host:
            conn_config.append(cls.configuration.host)
            # - port. Ports don't make any sense without a 
            #   host, though, so host has to be defined first...
            if cls._configuration.port:
                conn_config.append(cls.configuration.port)
        # - Create the connection
        cls._connection = pymongo.MongoClient(*conn_config)
        # - Create the database
        cls._database = cls._connection[cls._configuration.database]
        # - and the collection
        if cls._mongo_collection:
            cls._collection = cls._database[cls._mongo_collection]
        # - Otherwise, use the class-name
        else:
            cls._collection = cls._database[cls.__name__]
        return cls._collection

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

