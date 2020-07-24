#!/usr/bin/env python

"""
Defines unit-tests for the module at hms_artisan.data_storage.
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

import os
import sys
import unittest

from datetime import datetime
from uuid import UUID, uuid4

import os
from shutil import rmtree

from hms_core.data_objects import BaseDataObject

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

import hms_artisan.data_storage as data_storage
from hms_artisan.data_storage import *

#######################################
# Constants for test-methods          #
#######################################

GoodDateTimes = [
    # - actual datetime values
    datetime.now(), datetime.fromtimestamp(1234567890),
    datetime.now().timestamp(), 
    # - timestamp numbers
    1234567890, 1234567890.123456, 
    # - strings
    '2001-01-01 12:34:56', '3001-01-01 12:34:56', 
    '1911-01-01 12:34:56',
    # - A parsed datetime
    datetime.strptime(
        '2001-01-01 12:34:56', JSONFileDataObject._data_time_string
    ),
    # - datetimes outside the UNIX epoch, just in case
    datetime.strptime(
        '3001-01-01 12:34:56', JSONFileDataObject._data_time_string
    ),
    datetime.strptime(
        '1911-01-01 12:34:56', JSONFileDataObject._data_time_string
    ),
]

#######################################
# Code-coverage test-case and         #
# decorator-methods                   #
#######################################

class testdata_storageCodeCoverage(ModuleCoverageTest):
    _testNamespace = 'hms_artisan'
    _testModule = data_storage

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testdata_storageCodeCoverage
   )
)

#######################################
# Test-cases in the module            #
#######################################

class JSONFileDataObjectDerived(JSONFileDataObject):
    _file_store_dir = '/tmp/hms_artisan_test'

    def matches(self, **criteria) -> (bool,):
        return JSONFileDataObject.matches(self, **criteria)

    def to_data_dict(self):
        return {
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

    @classmethod
    def from_data_dict(cls, data_dict:(dict,)):
        return cls(**data_dict)

    @classmethod
    def sort(cls, objects, sort_by):
        pass

class NoFileStoreDir(JSONFileDataObject):

    def matches(self, **criteria) -> (bool,):
        return JSONFileDataObject.matches(self, **criteria)

    def to_data_dict(self):
        return {
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

    @classmethod
    def from_data_dict(cls, data_dict:(dict,)):
        return cls(**data_dict)

    @classmethod
    def sort(cls, objects, sort_by):
        pass

@testdata_storageCodeCoverage.AddMethodTesting
@testdata_storageCodeCoverage.AddPropertyTesting
class testJSONFileDataObject(unittest.TestCase):

    ###################################
    # Tests of class methods          #
    ###################################

    def test__init__(self):
        # Tests the __init__ method of the JSONFileDataObject class
        # - All we need to do here is prove that the various 
        #   setter- and deleter-method calls are operating as 
        #   expected -- same as BaseDataObject
        # - deleters first
        test_object = JSONFileDataObjectDerived()
        self.assertEquals(test_object._created, None)
        self.assertEquals(test_object._is_active, True)
        self.assertEquals(test_object._is_deleted, False)
        self.assertEquals(test_object._is_dirty, False)
        self.assertEquals(test_object._is_new, True)
        self.assertEquals(test_object._modified, None)
        self.assertEquals(test_object._oid, None)
        # - setters
        oid = uuid4()
        created = GoodDateTimes[0]
        modified = GoodDateTimes[1]
        is_active = False
        is_deleted = True
        is_dirty = True
        is_new = False
        test_object = JSONFileDataObjectDerived(
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
        # Tests the _create method of the JSONFileDataObject class
        test_object = JSONFileDataObjectDerived()
        try:
            test_object._create()
            self.fail(
                'JSONFileDataObject is not expected to raise '
                'NotImplementedError on a call to _create'
            )
        except NotImplementedError:
            pass
        except Exception as error:
            self.fail(
                'JSONFileDataObject is not expected to raise '
                'NotImplementedError on a call to _create, but %s '
                'was raised instead:\n - %s' %
                (error.__class__.__name__, error)
            )

    @unittest.skip(
        'Since the file-load process provided by _load_objects is '
        'used by mahy of the CRUD operations, it is tested  as part of '
        'testCRUDOperations'
    )
    def test_load_objects(self):
        # Tests the _load_objects method of the JSONFileDataObject class
        self.fail('test_load_objects is not yet implemented')

    def test_update(self):
        # Tests the _update method of the JSONFileDataObject class
        test_object = JSONFileDataObjectDerived()
        try:
            test_object._update()
            self.fail(
                'JSONFileDataObject is not expected to raise '
                'NotImplementedError on a call to _update'
            )
        except NotImplementedError:
            pass
        except Exception as error:
            self.fail(
                'JSONFileDataObject is not expected to raise '
                'NotImplementedError on a call to _update, but %s '
                'was raised instead:\n - %s' %
                (error.__class__.__name__, error)
            )

    @unittest.skip(
        'Since deleting a data-file is part of the CRUD operations, '
        'it is tested as part of testCRUDOperations'
    )
    def testdelete(self):
        # Tests the delete method of the JSONFileDataObject class
        self.fail('testdelete is not yet implemented')

    @unittest.skip(
        'Since reading data-files is part of the CRUD operations, '
        'it is tested as part of testCRUDOperations'
    )
    def testget(self):
        # Tests the get method of the JSONFileDataObject class
        self.fail('testget is not yet implemented')

    @unittest.skip(
        'Since creating a data-file is part of the CRUD operations, '
        'it is tested as part of testCRUDOperations'
    )
    def testsave(self):
        # Tests the save method of the JSONFileDataObject class
        self.fail('testsave is not yet implemented')

    def testCRUDOperations(self):
        # - First, assure that the class-level data-object collection 
        #   (in JSONFileDataObjectDerived._loaded_objects) is None, 
        #   and that the file-repository does not exist.
        JSONFileDataObjectDerived._loaded_objects = None
        if os.path.exists(JSONFileDataObjectDerived._file_store_dir):
            rmtree(JSONFileDataObjectDerived._file_store_dir)
        # - Next, create an item and save it
        first_object = JSONFileDataObjectDerived()
        first_object.save()
        # - Verify that the file exists where we're expecting it
        self.assertTrue(
            os.path.exists(
                '/tmp/hms_artisan_test/JSONFileDataObjectDerived-'
                'data/%s.json' % first_object.oid
            )
        )
        # - and that it exists in the in-memory cache
        self.assertNotEqual(
            JSONFileDataObjectDerived._loaded_objects.get(
                first_object.oid
            ), None
        )
        # - Verify that the item can be retrieved, and has the same 
        #   data
        first_object_get = JSONFileDataObjectDerived.get()[0]
        self.assertTrue(
            first_object.matches(**first_object_get.to_data_dict())
        )
        self.assertEqual(
            first_object.is_dirty, first_object_get.is_dirty
        )
        self.assertEqual(
            first_object.is_new, first_object_get.is_new
        )
        # - Create and save two more items
        second_object = JSONFileDataObjectDerived()
        second_object.save()
        third_object = JSONFileDataObjectDerived()
        third_object.save()
        # - Verify that all three items can be retrieved, and that 
        #   they are the expected objects, at least by their oids: 
        #   Those, as part of the file-names, *will* be unique and 
        #   distinct...
        all_objects = JSONFileDataObjectDerived.get()
        expected = set(
            [o.oid for o in [first_object, second_object, third_object]]
        )
        actual = set([o.oid for o in all_objects])
        self.assertEqual(expected, actual)
        # - Verify that the file for the second item exists, so the 
        #   verification later of its deletion is a valid test
        self.assertTrue(
            os.path.exists(
                '/tmp/hms_artisan_test/JSONFileDataObjectDerived-'
                'data/%s.json' % second_object.oid
            )
        )
        # - Delete the second item
        JSONFileDataObjectDerived.delete(second_object.oid)
        # - Verify that the item has been removed from the loaded-
        #   object store and from the file-system
        self.assertEqual(
            JSONFileDataObjectDerived._loaded_objects.get(second_object.oid), 
            None
        )
        self.assertFalse(
            os.path.exists(
                '/tmp/hms_artisan_test/JSONFileDataObjectDerived-'
                'data/%s.json' % second_object.oid
            )
        )
        # - Update the last object created, and save it
        third_object._set_is_active(False)
        third_object._set_is_deleted(True)
        third_object.save()
        # - Read the updated object and verify that the changes made 
        #   were saved to the file.
        third_object_get = JSONFileDataObjectDerived.get(third_object.oid)[0]
        self.assertEqual(
            third_object.to_data_dict(),
            third_object_get.to_data_dict()
        )
        self.assertTrue(
            third_object.matches(**third_object_get.to_data_dict())
        )
        self.assertEqual(
            third_object.is_dirty, third_object_get.is_dirty
        )
        self.assertEqual(
            third_object.is_new, third_object_get.is_new
        )
        # - Since other test-methods down the line might need to start 
        #   with empty object- and file-sets, re-clear them both
        JSONFileDataObjectDerived._loaded_objects = None
        if os.path.exists(JSONFileDataObjectDerived._file_store_dir):
            rmtree(JSONFileDataObjectDerived._file_store_dir)

    ###################################
    # Tests of class properties       #
    ###################################

    def test_file_store_dir(self):
        self.assertEqual(
            JSONFileDataObject._file_store_dir, None, 
            'JSONFileDataObject._file_store_dir is expected to provide '
            'a None default value that must be overridden by derived '
            'classes, but it is set to "%s" (%s)' % 
            (
                JSONFileDataObject._file_store_dir, 
                type(JSONFileDataObject._file_store_dir).__name__
            )
        )
        try:
            test_object = NoFileStoreDir()
            self.fail(
                'Classes derived from JSONFileDataObject are expected '
                'to define a _file_store_dir class-attribute, or cause '
                'instantiation of objects from classes that don\'t '
                'have one defined to fail with an AttributeError'
            )
        except AttributeError:
            pass

#    def testproperty_name(self):
#        # Tests the property_name property of the JSONFileDataObject class
#        # - Assert that the getter is correct:
#        self.assertEqual(
#            JSONFileDataObject.property_name.fget, 
#            JSONFileDataObject._get_property_name, 
#            'JSONFileDataObject.property_name is expected to use the '
#            '_get_property_name method as its getter-method'
#        )
#        # - If property_name is not expected to be publicly settable,
#        #   the second item here (JSONFileDataObject._set_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the setter is correct:
#        self.assertEqual(
#            JSONFileDataObject.property_name.fset, 
#            JSONFileDataObject._set_property_name, 
#            'JSONFileDataObject.property_name is expected to use the '
#            '_set_property_name method as its setter-method'
#        )
#        # - If property_name is not expected to be publicly deletable,
#        #   the second item here (JSONFileDataObject._del_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the deleter is correct:
#        self.assertEqual(
#            JSONFileDataObject.property_name.fdel, 
#            JSONFileDataObject._del_property_name, 
#            'JSONFileDataObject.property_name is expected to use the '
#            '_del_property_name method as its deleter-method'
#        )

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testJSONFileDataObject
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
        SaveTestReport(results, 'hms_artisan.data_storage',
            'hms_artisan.data_storage.test-results')
