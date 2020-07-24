#!/usr/bin/env python

# Python unit-test-module template. Copy the template to a new
# unit-test-module location, and start replacing names as needed:
#
# hms_core  ==> The path/namespace of the parent of the module/package
#                  being tested in this file.
# data_storage   ==> The name of the module being tested
#
# Then remove this comment-block

"""
Defines unit-tests for the module at hms_core.data_storage.
"""

#######################################
# Any needed from __future__ imports  #
# Create an "__all__" list to support #
#   "from module import member" use   #
#######################################

__all__ = [
    # Test-case classes
    # Child test-modules
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

import json
import os
import sys
import unittest

from datetime import datetime
from uuid import uuid4, UUID

#######################################
# Third-party imports needed          #
#######################################

#######################################
# Local imports needed                #
#######################################

from idic.unit_testing import *

#######################################
# Initialization needed before member #
#   definition can take place         #
#######################################

#######################################
# Module-level Constants              #
#######################################

LocalSuite = unittest.TestSuite()

#######################################
# Import the module being tested      #
#######################################

import hms_core.data_storage as data_storage
from hms_core.data_storage import *

#######################################
# Test-value constants                #
#######################################

good_databases = [
    'my_database', None
]
bad_databases = [
    '', True, False, [], (), 1, 0
]

good_hosts = [
    'localhost', '127.0.0.1', 'mongodb.com', '54.175.147.155', None
]
bad_hosts = [
    '', True, False, [], (), 1, 0
]

good_passwords = [
    'some_password', 'Th!5*is*4P@s5w0rd', None
]
bad_passwords = [
    '', True, False, [], (), 1, 0
]

good_ports = [
    80, 1024, 65535, None
]
bad_ports = [
    '', True, False, [], (), -1, 65538, '12345'
]

good_users = [
    'some_user', None
]
bad_users = [
    '', True, False, [], (), 1, 0
]

good_oids = [
    # - actual UUID values
    uuid4(), str(uuid4()), 
    UUID('dc3a7fdf-2183-49cc-aa00-af9239950254'),
    UUID('ffffffff-ffff-ffff-ffff-ffffffffffff'),
    UUID('00000000-0000-0000-0000-000000000000'),
    # - strings
    'dc3a7fdf-2183-49cc-aa00-af9239950254',
    'ffffffff-ffff-ffff-ffff-ffffffffffff',
    '00000000-0000-0000-0000-000000000000',
    'dc3a7fdf218349ccaa00af9239950254',
    'ffffffffffffffffffffffffffffffff',
    '00000000000000000000000000000000',
]
bad_oids = [
    # - invalid types
    (1,2), tuple(), True, False, object(), 
    # - invalid values
    'true', '', '1911-01-01 12:34:56.123456'
]

good_datetimes = [
    # - actual datetime values
    datetime.now(), datetime.fromtimestamp(1234567890),
    datetime.now().timestamp(), 
    # - timestamp numbers
    1234567890, 1234567890.123456, 
    # - strings
    '2001-01-01 12:34:56', '3001-01-01 12:34:56', 
    '1911-01-01 12:34:56',
    # - datetimes outside the UNIX epoch, just in case
    datetime.strptime(
        '2001-01-01 12:34:56', HMSMongoDataObject._data_time_string
    ),
    datetime.strptime(
        '3001-01-01 12:34:56', HMSMongoDataObject._data_time_string
    ),
    datetime.strptime(
        '1911-01-01 12:34:56', HMSMongoDataObject._data_time_string
    ),
]
bad_datetimes = [
    # - invalid types
    (1,2), tuple(), True, False, object(), 
    # - invalid values
    'true', '', '1911-01-01 12:34:56.123456'
]

#######################################
# Code-coverage test-case and         #
# decorator-methods                   #
#######################################

class testdata_storageCodeCoverage(ModuleCoverageTest):
    _testNamespace = 'hms_core'
    _testModule = data_storage

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testdata_storageCodeCoverage
   )
)

#######################################
# Test-cases in the module            #
#######################################

@testdata_storageCodeCoverage.AddMethodTesting
@testdata_storageCodeCoverage.AddPropertyTesting
class testDatastoreConfig(unittest.TestCase):

    ###################################
    # Tests of class methods          #
    ###################################

    def test__init__(self):
        # Tests the __init__ method of the DatastoreConfig class
        for database in good_databases:
            for host in good_hosts:
                for password in good_passwords:
                    for port in good_ports:
                        for user in good_users:
                            config = {
                                'database':database,
                                'host':host,
                                'password':password,
                                'port':port,
                                'user':user,
                            }
                            test_object = DatastoreConfig(**config)
                            self.assertEqual(test_object.database, database)
                            self.assertEqual(test_object.host, host)
                            self.assertEqual(test_object.password, password)
                            self.assertEqual(test_object.port, port)
                            self.assertEqual(test_object.user, user)

    def test_del_database(self):
        # Tests the _del_database method of the DatastoreConfig class
        test_object = DatastoreConfig()
        expected = 'Some value'
        test_object._database = expected
        test_object._del_database()
        self.assertEqual(test_object.database, None)

    def test_del_host(self):
        # Tests the _del_host method of the DatastoreConfig class
        test_object = DatastoreConfig()
        expected = 'Some value'
        test_object._host = expected
        test_object._del_host()
        self.assertEqual(test_object.host, None)

    def test_del_password(self):
        # Tests the _del_password method of the DatastoreConfig class
        test_object = DatastoreConfig()
        expected = 'Some value'
        test_object._password = expected
        test_object._del_password()
        self.assertEqual(test_object.password, None)

    def test_del_port(self):
        # Tests the _del_port method of the DatastoreConfig class
        test_object = DatastoreConfig()
        expected = 'Some value'
        test_object._port = expected
        test_object._del_port()
        self.assertEqual(test_object.port, None)

    def test_del_user(self):
        # Tests the _del_user method of the DatastoreConfig class
        test_object = DatastoreConfig()
        expected = 'Some value'
        test_object._user = expected
        test_object._del_user()
        self.assertEqual(test_object.user, None)

    def test_get_database(self):
        # Tests the _get_database method of the DatastoreConfig class
        test_object = DatastoreConfig()
        expected = 'Some value'
        test_object._database = expected
        self.assertEqual(test_object._get_database(), expected)

    def test_get_host(self):
        # Tests the _get_host method of the DatastoreConfig class
        test_object = DatastoreConfig()
        expected = 'Some value'
        test_object._host = expected
        self.assertEqual(test_object._get_host(), expected)

    def test_get_password(self):
        # Tests the _get_password method of the DatastoreConfig class
        test_object = DatastoreConfig()
        expected = 'Some value'
        test_object._password = expected
        self.assertEqual(test_object._get_password(), expected)

    def test_get_port(self):
        # Tests the _get_port method of the DatastoreConfig class
        test_object = DatastoreConfig()
        expected = 'Some value'
        test_object._port = expected
        self.assertEqual(test_object._get_port(), expected)

    def test_get_user(self):
        # Tests the _get_user method of the DatastoreConfig class
        test_object = DatastoreConfig()
        expected = 'Some value'
        test_object._user = expected
        self.assertEqual(test_object._get_user(), expected)

    def test_set_database(self):
        # Tests the _set_database method of the DatastoreConfig class
        # - Test all permutations of "good" argument-values:
        test_object = DatastoreConfig()
        for expected in good_databases:
            if expected == None:
                # - None is valid during __init__, but not to the 
                #   setter-method, so skip it
                continue
            test_object._set_database(expected)
            self.assertEqual(test_object.database, expected)
        # - Test all permutations of each "bad" argument-values:
        for value in bad_databases + [None]:
            try:
                test_object._set_database(value)
                self.fail(
                    'DatastoreConfig.database should not accept '
                    '"%s" (%s) as a valid database value, but it was '
                    'allowed to be set' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                pass

    def test_set_host(self):
        # Tests the _set_host method of the DatastoreConfig class
        # - Test all permutations of "good" argument-values:
        test_object = DatastoreConfig()
        for expected in good_hosts:
            if expected == None:
                # - None is valid during __init__, but not to the 
                #   setter-method, so skip it
                continue
            test_object._set_host(expected)
            self.assertEqual(test_object.host, expected)
        # - Test all permutations of each "bad" argument-values:
        for value in bad_hosts + [None]:
            try:
                test_object._set_host(value)
                self.fail(
                    'DatastoreConfig.host should not accept '
                    '"%s" (%s) as a valid host value, but it was '
                    'allowed to be set' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                pass

    def test_set_password(self):
        # Tests the _set_password method of the DatastoreConfig class
        # - Test all permutations of "good" argument-values:
        test_object = DatastoreConfig()
        for expected in good_passwords:
            if expected == None:
                # - None is valid during __init__, but not to the 
                #   setter-method, so skip it
                continue
            test_object._set_password(expected)
            self.assertEqual(test_object.password, expected)
        # - Test all permutations of each "bad" argument-values:
        for value in bad_passwords + [None]:
            try:
                test_object._set_password(value)
                self.fail(
                    'DatastoreConfig.password should not accept '
                    '"%s" (%s) as a valid password value, but it was '
                    'allowed to be set' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                pass

    def test_set_port(self):
        # Tests the _set_port method of the DatastoreConfig class
        # - Test all permutations of "good" argument-values:
        test_object = DatastoreConfig()
        for expected in good_ports:
            if expected == None:
                # - None is valid during __init__, but not to the 
                #   setter-method, so skip it
                continue
            test_object._set_port(expected)
            self.assertEqual(test_object.port, expected)
        # - Test all permutations of each "bad" argument-values:
        for value in bad_ports + [None]:
            try:
                test_object._set_port(value)
                self.fail(
                    'DatastoreConfig.port should not accept '
                    '"%s" (%s) as a valid port value, but it was '
                    'allowed to be set' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                pass

    def test_set_user(self):
        # Tests the _set_user method of the DatastoreConfig class
        # - Test all permutations of "good" argument-values:
        test_object = DatastoreConfig()
        for expected in good_users:
            if expected == None:
                # - None is valid during __init__, but not to the 
                #   setter-method, so skip it
                continue
            test_object._set_user(expected)
            self.assertEqual(test_object.user, expected)
        # - Test all permutations of each "bad" argument-values:
        for value in bad_users + [None]:
            try:
                test_object._set_user(value)
                self.fail(
                    'DatastoreConfig.user should not accept '
                    '"%s" (%s) as a valid user value, but it was '
                    'allowed to be set' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                pass

    # - Noteworthy because files
    def testfrom_config(self):
        # Tests the from_config method of the DatastoreConfig class
        # - Test all permutations of "good" argument-values:
        config_file = '/tmp/datastore-test.json'
        for database in good_databases:
            for host in good_hosts:
                for password in good_passwords:
                    for port in good_ports:
                        for user in good_users:
                            config = {
                                'database':database,
                                'host':host,
                                'password':password,
                                'port':port,
                                'user':user,
                            }
                            fp = open('/tmp/datastore-test.json', 'w')
                            json.dump(config, fp)
                            fp.close()
                            test_object = DatastoreConfig.from_config(config_file)
                            self.assertEqual(test_object.database, database)
                            self.assertEqual(test_object.host, host)
                            self.assertEqual(test_object.password, password)
                            self.assertEqual(test_object.port, port)
                            self.assertEqual(test_object.user, user)
                            os.unlink(config_file)
        # - Test all permutations of each "bad" argument-value 
        #   set against "good" values for the other arguments:
        # - database
        host = good_hosts[0]
        password = good_passwords[0]
        port = good_ports[0]
        user = good_users[0]
        for database in bad_databases:
            config = {
                'database':database,
                'host':host,
                'password':password,
                'port':port,
                'user':user,
            }
            fp = open('/tmp/datastore-test.json', 'w')
            json.dump(config, fp)
            fp.close()
            try:
                test_object = DatastoreConfig.from_config(config_file)
                self.fail(
                    'DatastoreConfig.from_config should not '
                    'accept "%s" (%s) as a valid database config-'
                    'value, but it was allowed to create an '
                    'instance' % (database, type(database).__name__)
                )
            except (RuntimeError, TypeError, ValueError):
                pass
        # - host
        database = good_databases[0]
        password = good_passwords[0]
        port = good_ports[0]
        user = good_users[0]
        for host in bad_hosts:
            config = {
                'database':database,
                'host':host,
                'password':password,
                'port':port,
                'user':user,
            }
            fp = open('/tmp/datastore-test.json', 'w')
            json.dump(config, fp)
            fp.close()
            try:
                test_object = DatastoreConfig.from_config(config_file)
                self.fail(
                    'DatastoreConfig.from_config should not '
                    'accept "%s" (%s) as a valid host config-'
                    'value, but it was allowed to create an '
                    'instance' % (database, type(database).__name__)
                )
            except (RuntimeError, TypeError, ValueError):
                pass
        # - password
        database = good_databases[0]
        host = good_hosts[0]
        port = good_ports[0]
        user = good_users[0]
        for password in bad_passwords:
            config = {
                'database':database,
                'host':host,
                'password':password,
                'port':port,
                'user':user,
            }
            fp = open('/tmp/datastore-test.json', 'w')
            json.dump(config, fp)
            fp.close()
            try:
                test_object = DatastoreConfig.from_config(config_file)
                self.fail(
                    'DatastoreConfig.from_config should not '
                    'accept "%s" (%s) as a valid password config-'
                    'value, but it was allowed to create an '
                    'instance' % (database, type(database).__name__)
                )
            except (RuntimeError, TypeError, ValueError):
                pass
        # - port
        database = good_databases[0]
        host = good_hosts[0]
        password = good_passwords[0]
        user = good_users[0]
        for port in bad_ports:
            config = {
                'database':database,
                'host':host,
                'password':password,
                'port':port,
                'user':user,
            }
            fp = open('/tmp/datastore-test.json', 'w')
            json.dump(config, fp)
            fp.close()
            try:
                test_object = DatastoreConfig.from_config(config_file)
                self.fail(
                    'DatastoreConfig.from_config should not '
                    'accept "%s" (%s) as a valid port config-'
                    'value, but it was allowed to create an '
                    'instance' % (database, type(database).__name__)
                )
            except (RuntimeError, TypeError, ValueError):
                pass
        # - user
        database = good_databases[0]
        host = good_hosts[0]
        password = good_passwords[0]
        port = good_ports[0]
        for user in bad_users:
            config = {
                'database':database,
                'host':host,
                'password':password,
                'port':port,
                'user':user,
            }
            fp = open('/tmp/datastore-test.json', 'w')
            json.dump(config, fp)
            fp.close()
            try:
                test_object = DatastoreConfig.from_config(config_file)
                self.fail(
                    'DatastoreConfig.from_config should not '
                    'accept "%s" (%s) as a valid user config-'
                    'value, but it was allowed to create an '
                    'instance' % (database, type(database).__name__)
                )
            except (RuntimeError, TypeError, ValueError):
                pass
        os.unlink(config_file)

    ###################################
    # Tests of class properties       #
    ###################################

    def testdatabase(self):
        # Tests the database property of the DatastoreConfig class
        # - Assert that the getter is correct:
        self.assertEqual(
            DatastoreConfig.database.fget, 
            DatastoreConfig._get_database, 
            'DatastoreConfig.database is expected to use the '
            '_get_database method as its getter-method'
        )
        # - If database is not expected to be publicly settable,
        #   the second item here (DatastoreConfig._set_database) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            DatastoreConfig.database.fset, 
            DatastoreConfig._set_database, 
            'DatastoreConfig.database is expected to use the '
            '_set_database method as its setter-method'
        )
        # - If database is not expected to be publicly deletable,
        #   the second item here (DatastoreConfig._del_database) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            DatastoreConfig.database.fdel, 
            DatastoreConfig._del_database, 
            'DatastoreConfig.database is expected to use the '
            '_del_database method as its deleter-method'
        )

    def testhost(self):
        # Tests the host property of the DatastoreConfig class
        # - Assert that the getter is correct:
        self.assertEqual(
            DatastoreConfig.host.fget, 
            DatastoreConfig._get_host, 
            'DatastoreConfig.host is expected to use the '
            '_get_host method as its getter-method'
        )
        # - If host is not expected to be publicly settable,
        #   the second item here (DatastoreConfig._set_host) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            DatastoreConfig.host.fset, 
            DatastoreConfig._set_host, 
            'DatastoreConfig.host is expected to use the '
            '_set_host method as its setter-method'
        )
        # - If host is not expected to be publicly deletable,
        #   the second item here (DatastoreConfig._del_host) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            DatastoreConfig.host.fdel, 
            DatastoreConfig._del_host, 
            'DatastoreConfig.host is expected to use the '
            '_del_host method as its deleter-method'
        )

    def testpassword(self):
        # Tests the password property of the DatastoreConfig class
        # - Assert that the getter is correct:
        self.assertEqual(
            DatastoreConfig.password.fget, 
            DatastoreConfig._get_password, 
            'DatastoreConfig.password is expected to use the '
            '_get_password method as its getter-method'
        )
        # - If password is not expected to be publicly settable,
        #   the second item here (DatastoreConfig._set_password) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            DatastoreConfig.password.fset, 
            DatastoreConfig._set_password, 
            'DatastoreConfig.password is expected to use the '
            '_set_password method as its setter-method'
        )
        # - If password is not expected to be publicly deletable,
        #   the second item here (DatastoreConfig._del_password) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            DatastoreConfig.password.fdel, 
            DatastoreConfig._del_password, 
            'DatastoreConfig.password is expected to use the '
            '_del_password method as its deleter-method'
        )

    def testport(self):
        # Tests the port property of the DatastoreConfig class
        # - Assert that the getter is correct:
        self.assertEqual(
            DatastoreConfig.port.fget, 
            DatastoreConfig._get_port, 
            'DatastoreConfig.port is expected to use the '
            '_get_port method as its getter-method'
        )
        # - If port is not expected to be publicly settable,
        #   the second item here (DatastoreConfig._set_port) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            DatastoreConfig.port.fset, 
            DatastoreConfig._set_port, 
            'DatastoreConfig.port is expected to use the '
            '_set_port method as its setter-method'
        )
        # - If port is not expected to be publicly deletable,
        #   the second item here (DatastoreConfig._del_port) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            DatastoreConfig.port.fdel, 
            DatastoreConfig._del_port, 
            'DatastoreConfig.port is expected to use the '
            '_del_port method as its deleter-method'
        )

    def testuser(self):
        # Tests the user property of the DatastoreConfig class
        # - Assert that the getter is correct:
        self.assertEqual(
            DatastoreConfig.user.fget, 
            DatastoreConfig._get_user, 
            'DatastoreConfig.user is expected to use the '
            '_get_user method as its getter-method'
        )
        # - If user is not expected to be publicly settable,
        #   the second item here (DatastoreConfig._set_user) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            DatastoreConfig.user.fset, 
            DatastoreConfig._set_user, 
            'DatastoreConfig.user is expected to use the '
            '_set_user method as its setter-method'
        )
        # - If user is not expected to be publicly deletable,
        #   the second item here (DatastoreConfig._del_user) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            DatastoreConfig.user.fdel, 
            DatastoreConfig._del_user, 
            'DatastoreConfig.user is expected to use the '
            '_del_user method as its deleter-method'
        )

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testDatastoreConfig
    )
)

class HMSMongoDataObjectDerived(HMSMongoDataObject):

    _data_dict_keys = (
        'name', 'description', 'cost', 'oid', 'created', 'modified', 
        'is_active', 'is_deleted'
    )

    def __init__(self, name=None, description=None, cost=0, 
        oid=None, created=None, modified=None, is_active=None, 
        is_deleted=None, is_dirty=None, is_new=None
    ):
        HMSMongoDataObject.__init__(
            self, oid, created, modified, is_active, is_deleted, 
            is_dirty, is_new
        )
        self.name = name
        self.description = description
        self.cost = cost

    def __str__(self):
        return '<%s oid: %s>' % (self.__class__.__name__, self.oid)

    def matches(self, **criteria):
        return HMSMongoDataObject.matches(self, **criteria)

    def to_data_dict(self):
        return {
            # - "local" properties
            'name':self.name,
            'description':self.description,
            'cost':self.cost,
            # - standard items from HMSMongoDataObject/BaseDataObject
            'created':self.created.strftime(self.__class__._data_time_string),
            'is_active':self.is_active,
            'is_deleted':self.is_deleted,
            'modified':self.modified.strftime(self.__class__._data_time_string),
            'oid':str(self.oid),
        }

    @classmethod
    def sort(cls, objects, sorty_by):
        pass

@testdata_storageCodeCoverage.AddMethodTesting
@testdata_storageCodeCoverage.AddPropertyTesting
class testHMSMongoDataObject(unittest.TestCase):

    config = DatastoreConfig(
        database='test_data_storage'
    )

    def setUp(self):
        # - Since we need a database to test certain methods, 
        #   create one here
        HMSMongoDataObject.configure(self.__class__.config)

    def tearDown(self):
        # - delete the database after we're done with it, so that we 
        #   don't have data persisting that could bollix up subsequent 
        #   test-runs
        from pymongo import MongoClient
        client = MongoClient()
        client.drop_database(self.__class__.config.database)

    ###################################
    # Tests of class methods          #
    ###################################

    def test__init__(self):
        # Tests the __init__ method of the BaseDataObject class
        # - All we need to do here is prove that the various 
        #   setter- and deleter-method calls are operating as 
        #   expected.
        # - deleters first
        test_object = HMSMongoDataObjectDerived()
        self.assertEquals(test_object._created, None)
        self.assertEquals(test_object._is_active, True)
        self.assertEquals(test_object._is_deleted, False)
        self.assertEquals(test_object._is_dirty, False)
        self.assertEquals(test_object._is_new, True)
        self.assertEquals(test_object._modified, None)
        self.assertEquals(test_object._oid, None)
        # - setters
        oid = uuid4()
        created = good_datetimes[0]
        modified = good_datetimes[1]
        is_active = False
        is_deleted = True
        is_dirty = True
        is_new = False
        test_object = HMSMongoDataObjectDerived(
            'name', 'name', 12, 
            oid, created, modified, is_active, is_deleted, 
            is_dirty, is_new
        )
        self.assertEquals(test_object.oid, oid)
        self.assertEquals(test_object.created, created)
        self.assertEquals(test_object.is_active, is_active)
        self.assertEquals(test_object.is_deleted, is_deleted)
        self.assertEquals(test_object.is_dirty, is_dirty)
        self.assertEquals(test_object.is_new, is_new)
        self.assertEquals(test_object.modified, modified)

    def test_create(self):
        # Tests the _create method of the HMSMongoDataObject class
        test_object = HMSMongoDataObjectDerived()
        try:
            test_object._create()
            self.fail(
                'HMSMongoDataObject-derived classes are expected '
                'to raise NotImplementedError when _create is '
                'called'
            )
        except NotImplementedError:
            pass

    @unittest.skip(
        'Tested in test_get_collection'
    )
    def test_del_collection(self):
        # Tests the _del_collection method of the HMSMongoDataObject class
        self.fail('test_del_collection is not implemented')

    @unittest.skip(
        'Tested in test_get_connection'
    )
    def test_del_connection(self):
        # Tests the _del_connection method of the HMSMongoDataObject class
        self.fail('test_del_connection is not implemented')

    @unittest.skip(
        'Tested in test_get_database'
    )
    def test_del_database(self):
        # Tests the _del_database method of the HMSMongoDataObject class
        self.fail('test_del_database is not implemented')

    def test_get_collection(self):
        # Tests the _get_collection method of the HMSMongoDataObject class
        # - Test that lazy instantiation on a new instance returns the 
        #   class-attribute value (_collection)
        test_object =  HMSMongoDataObjectDerived()
        self.assertEqual(
            test_object._get_collection(), 
            HMSMongoDataObjectDerived._collection
        )
        # - Test that deleting the current collection and re-aquiring it 
        #   works as expected
        test_object._del_collection()
        self.assertEqual(
            test_object._get_collection(), 
            HMSMongoDataObjectDerived._collection
        )
        # - There may be more to test later, but this suffices for now...

    @unittest.skip(
        'The fact that the configuration works in setUp is sufficient'
    )
    def test_get_configuration(self):
        # Tests the _get_configuration method of the HMSMongoDataObject class
        # - Test all permutations of "good" argument-values:
        # - Test all permutations of each "bad" argument-value 
        #   set against "good" values for the other arguments:
        self.fail('test_get_configuration is not yet implemented')

    def test_get_connection(self):
        # Tests the _get_connection method of the HMSMongoDataObject class
        # - Test that lazy instantiation on a new instance returns the 
        #   class-attribute value (_connection)
        test_object =  HMSMongoDataObjectDerived()
        self.assertEqual(
            test_object._get_connection(), 
            HMSMongoDataObjectDerived._connection
        )
        # - Test that deleting the current connection and re-aquiring it 
        #   works as expected
        test_object._del_connection()
        self.assertEqual(
            test_object._get_connection(), 
            HMSMongoDataObjectDerived._connection
        )
        # - There may be more to test later, but this suffices for now...

    def test_get_database(self):
        # Tests the _get_database method of the HMSMongoDataObject class
        # - Test that lazy instantiation on a new instance returns the 
        #   class-attribute value (_database)
        test_object =  HMSMongoDataObjectDerived()
        self.assertEqual(
            test_object._get_database(), 
            HMSMongoDataObjectDerived._database
        )
        # - Test that deleting the current database and re-aquiring it 
        #   works as expected
        test_object._del_database()
        self.assertEqual(
            test_object._get_database(), 
            HMSMongoDataObjectDerived._database
        )
        # - There may be more to test later, but this suffices for now...

    def test_update(self):
        # Tests the _update method of the HMSMongoDataObject class
        test_object = HMSMongoDataObjectDerived()
        try:
            test_object._update()
            self.fail(
                'HMSMongoDataObject-derived classes are expected '
                'to raise NotImplementedError when _update is '
                'called'
            )
        except NotImplementedError:
            pass

    @unittest.skip(
        'The fact that the configuration works in setUp is sufficient'
    )
    def testconfigure(self):
        # Tests the configure method of the HMSMongoDataObject class
        self.fail('testconfigure is not yet implemented')

    def testdelete(self):
        # Tests the delete method of the HMSMongoDataObject class
        # - In order to really test get, we need some objects to test 
        #   against, so create a couple dozen:
        names = ['Alice', 'Bob', 'Carl', 'Doug']
        costs = [1, 2, 3]
        descriptions = [None, 'Description']
        all_oids = []
        for name in names:
            for description in descriptions:
                for cost in costs:
                    item = HMSMongoDataObjectDerived(
                        name=name, description=description, cost=cost
                    )
                    item.save()
                    all_oids.append(item.oid)
        # - Delete varying-sized sets of items by oid, and verify that 
        #   the deleted oids are gone afterwards...
        while all_oids:
            try:
                oids = all_oids[len(all_oids)/2:]
                all_oids = [o for o in all_oids if o not in oids]
            except:
                oids = all_oids
                all_oids = []
            HMSMongoDataObjectDerived.delete(*oids)
            items = HMSMongoDataObjectDerived.get(*oids)
            self.assertEqual(len(items), 0)
        # - Verify that *no* items exist after they've all been deleted
        items = HMSMongoDataObjectDerived.get()
        self.assertEqual(items, [])

    # - Noteworthy because to_data_dict and __init__ are 
    #   implementation-specific.
    def testfrom_data_dict(self):
        # Tests the from_data_dict method of the HMSMongoDataObject class
        names = ['Alice', 'Bob', 'Carl', 'Doug']
        costs = [1, 2, 3]
        descriptions = [None, 'Description']
        for name in names:
            for description in descriptions:
                for cost in costs:
                    data_dict = {
                        'description':description,
                        'name':name,
                        'cost':cost,
                    }
                    test_object = HMSMongoDataObjectDerived.from_data_dict(data_dict)
                    self.assertEqual(test_object.description, description)
                    self.assertEqual(test_object.name, name)
                    self.assertEqual(test_object.cost, cost)

    # - Noteworthy because _data_dict_keys attribute
    def testget(self):
        # Tests the get method of the HMSMongoDataObject class
        # - In order to really test get, we need some objects to test 
        #   against, so create a couple dozen:
        names = ['Alice', 'Bob', 'Carl', 'Doug']
        costs = [1, 2, 3]
        descriptions = [None, 'Description']
        for name in names:
            for description in descriptions:
                for cost in costs:
                    HMSMongoDataObjectDerived(
                        name=name, description=description, cost=cost
                    ).save()
        # - Now we should be able to try various permutations of get 
        #   and get verifiable results. These tests will fail if the 
        #   _data_dict_keys class-attribute isn't accurate...
        for name in names:
            criteria = {
                'name':name,
            }
            items = HMSMongoDataObjectDerived.get(**criteria)
            actual = len(items)
            expected = len(costs) * len(descriptions)
            self.assertEqual(actual, expected, 
                'Expected %d items returned (all matching name="%s"), '
                'but %d were returned' % 
                (expected, name, actual)
            )
            for item in items:
                self.assertEqual(item.name, name)
            for cost in costs:
                criteria = {
                    'name':name,
                    'cost':cost,
                }
                items = HMSMongoDataObjectDerived.get(**criteria)
                actual = len(items)
                expected = len(descriptions)
                self.assertEqual(actual, expected, 
                    'Expected %d items returned (all matching '
                    'name="%s" and cost=%d), but %d were returned' % 
                    (expected, name, cost, actual)
                )
                for item in items:
                    self.assertEqual(item.name, name)
                    self.assertEqual(item.cost, cost)

    # - Noteworthy because trust
    def testget_mongo_collection(self):
        # Tests the get_mongo_collection method of the 
        # HMSMongoDataObject class
        # - Ultimately, what we need to prove here is that the method 
        #   returns a Collection, and that the collection is named as 
        #   expected.
        from pymongo.collection import Collection
        actual = HMSMongoDataObjectDerived.get_mongo_collection()
        self.assertEqual(actual.__class__, Collection)
        # - This is not optimal, maybe, but 
        #   HMSMongoDataObjectDerived.__class__ returns 'ABCMeta' 
        #   rather than 'HMSMongoDataObjectDerived' for some reason...?
        #   Bug? Can't find any documented reason why this should 
        #   be the case...
        self.assertEqual(actual.name, 'HMSMongoDataObjectDerived')

    # - Noteworthy because save/get rather than save/pymongo-query.
    #   another option would be to do a "real" pymongo query, but that 
    #   test-code would look like the code in get anyway...?
    def testsave(self):
        # Tests the save method of the HMSMongoDataObject class
        # - Testing save without using get is somewhat cumbersome, and 
        #   perhaps too simple...?
        test_object = HMSMongoDataObjectDerived()
        test_object.save()
        expected = test_object.to_data_dict()
        results = HMSMongoDataObjectDerived.get(str(test_object.oid))
        actual = results[0].to_data_dict()
        self.assertEqual(actual, expected)

    ###################################
    # Tests of class properties       #
    ###################################

    def testcollection(self):
        # Tests the collection property of the HMSMongoDataObject class
        # - Assert that the getter is correct:
        self.assertEqual(
            HMSMongoDataObject.collection.fget, 
            HMSMongoDataObject._get_collection, 
            'HMSMongoDataObject.collection is expected to use the '
            '_get_collection method as its getter-method'
        )
        # - If collection is not expected to be publicly settable,
        #   the second item here (HMSMongoDataObject._set_collection) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            HMSMongoDataObject.collection.fset, 
            None, 
            'HMSMongoDataObject.collection is expected to use the '
            '_set_collection method as its setter-method'
        )
        # - If collection is not expected to be publicly deletable,
        #   the second item here (HMSMongoDataObject._del_collection) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            HMSMongoDataObject.collection.fdel, 
            HMSMongoDataObject._del_collection, 
            'HMSMongoDataObject.collection is expected to use the '
            '_del_collection method as its deleter-method'
        )

    def testconfiguration(self):
        # Tests the configuration property of the HMSMongoDataObject class
        # - Assert that the getter is correct:
        self.assertEqual(
            HMSMongoDataObject.configuration.fget, 
            HMSMongoDataObject._get_configuration, 
            'HMSMongoDataObject.configuration is expected to use the '
            '_get_configuration method as its getter-method'
        )
        # - If configuration is not expected to be publicly settable,
        #   the second item here (HMSMongoDataObject._set_configuration) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            HMSMongoDataObject.configuration.fset, 
            None, 
            'HMSMongoDataObject.configuration is expected to use the '
            '_set_configuration method as its setter-method'
        )
        # - If configuration is not expected to be publicly deletable,
        #   the second item here (HMSMongoDataObject._del_configuration) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            HMSMongoDataObject.configuration.fdel, 
            None, 
            'HMSMongoDataObject.configuration is expected to use the '
            '_del_configuration method as its deleter-method'
        )

    def testconnection(self):
        # Tests the connection property of the HMSMongoDataObject class
        # - Assert that the getter is correct:
        self.assertEqual(
            HMSMongoDataObject.connection.fget, 
            HMSMongoDataObject._get_connection, 
            'HMSMongoDataObject.connection is expected to use the '
            '_get_connection method as its getter-method'
        )
        # - If connection is not expected to be publicly settable,
        #   the second item here (HMSMongoDataObject._set_connection) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            HMSMongoDataObject.connection.fset, 
            None, 
            'HMSMongoDataObject.connection is expected to use the '
            '_set_connection method as its setter-method'
        )
        # - If connection is not expected to be publicly deletable,
        #   the second item here (HMSMongoDataObject._del_connection) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            HMSMongoDataObject.connection.fdel, 
            HMSMongoDataObject._del_connection, 
            'HMSMongoDataObject.connection is expected to use the '
            '_del_connection method as its deleter-method'
        )

    def testdatabase(self):
        # Tests the database property of the HMSMongoDataObject class
        # - Assert that the getter is correct:
        self.assertEqual(
            HMSMongoDataObject.database.fget, 
            HMSMongoDataObject._get_database, 
            'HMSMongoDataObject.database is expected to use the '
            '_get_database method as its getter-method'
        )
        # - If database is not expected to be publicly settable,
        #   the second item here (HMSMongoDataObject._set_database) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            HMSMongoDataObject.database.fset, 
            None, 
            'HMSMongoDataObject.database is expected to use the '
            '_set_database method as its setter-method'
        )
        # - If database is not expected to be publicly deletable,
        #   the second item here (HMSMongoDataObject._del_database) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            HMSMongoDataObject.database.fdel, 
            HMSMongoDataObject._del_database, 
            'HMSMongoDataObject.database is expected to use the '
            '_del_database method as its deleter-method'
        )

#    def testproperty_name(self):
#        # Tests the property_name property of the HMSMongoDataObject class
#        # - Assert that the getter is correct:
#        self.assertEqual(
#            HMSMongoDataObject.property_name.fget, 
#            HMSMongoDataObject._get_property_name, 
#            'HMSMongoDataObject.property_name is expected to use the '
#            '_get_property_name method as its getter-method'
#        )
#        # - If property_name is not expected to be publicly settable,
#        #   the second item here (HMSMongoDataObject._set_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the setter is correct:
#        self.assertEqual(
#            HMSMongoDataObject.property_name.fset, 
#            HMSMongoDataObject._set_property_name, 
#            'HMSMongoDataObject.property_name is expected to use the '
#            '_set_property_name method as its setter-method'
#        )
#        # - If property_name is not expected to be publicly deletable,
#        #   the second item here (HMSMongoDataObject._del_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the deleter is correct:
#        self.assertEqual(
#            HMSMongoDataObject.property_name.fdel, 
#            HMSMongoDataObject._del_property_name, 
#            'HMSMongoDataObject.property_name is expected to use the '
#            '_del_property_name method as its deleter-method'
#        )

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testHMSMongoDataObject
    )
)

#######################################
# Child-module test-cases to execute  #
#######################################

# import child_module
# LocalSuite.addTests(child_module.LocalSuite._tests)

#######################################
# Imports to resolve circular         #
# dependencies. Avoid if possible.    #
#######################################

#######################################
# Initialization that needs to        #
# happen after member definition.     #
#######################################

#######################################
# Code to execute if file is called   #
# or run directly.                    #
#######################################

if __name__ == '__main__':
    import time
    results = unittest.TestResult()
    testStartTime = time.time()
    LocalSuite.run(results)
    results.runTime = time.time() - testStartTime
    PrintTestResults(results)
    if not results.errors and not results.failures:
        SaveTestReport(results, 'hms_core.data_storage',
            'hms_core.data_storage.test-results')
