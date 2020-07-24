#!/usr/bin/env python

"""
Defines unit-tests for the module at hms_core.data_objects.
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

import hms_core.data_objects as data_objects
from hms_core.data_objects import *

#######################################
# Constants for test-methods          #
#######################################

GoodBooleanOrIntEquivalents = [
    True, False, 1, 0
]
BadBooleanOrIntEquivalents = [
    'true', '', (1,2), tuple()
]

GoodDateTimes = [
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
        '2001-01-01 12:34:56', BaseDataObject._data_time_string
    ),
    datetime.strptime(
        '3001-01-01 12:34:56', BaseDataObject._data_time_string
    ),
    datetime.strptime(
        '1911-01-01 12:34:56', BaseDataObject._data_time_string
    ),
]
BadDateTimes = [
    # - invalid types
    (1,2), tuple(), True, False, object(), 
    # - invalid values
    'true', '', '1911-01-01 12:34:56.123456'
]

GoodOIDs = [
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
BadOIDs = [
    # - invalid types
    (1,2), tuple(), True, False, object(), 
    # - invalid values
    'true', '', '1911-01-01 12:34:56.123456'
]

#######################################
# Code-coverage test-case and         #
# decorator-methods                   #
#######################################

class testdata_objectsCodeCoverage(ModuleCoverageTest):
    _testNamespace = 'hms_core'
    _testModule = data_objects

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testdata_objectsCodeCoverage
   )
)

#######################################
# Test-cases in the module            #
#######################################

class BaseDataObjectDerived(BaseDataObject):
    def __init__(self, 
        oid=None, created=None, modified=None, is_active=None, 
        is_deleted=None, is_dirty=None, is_new=None
    ):
        BaseDataObject.__init__(
            self, oid, created, modified, is_active, is_deleted, 
            is_dirty, is_new
        )
    def _create(self):
        return BaseDataObject._create(self)
    def _update(self):
        return BaseDataObject._update(self)
    def matches(self, **criteria):
        return BaseDataObject.matches(self, **criteria)
    def to_data_dict(self):
        return BaseDataObject.to_data_dict(self)
    @classmethod
    def delete(cls, *oids):
        pass
    @classmethod
    def from_data_dict(cls, data_dict):
        pass
    @classmethod
    def get(cls, *oids, **criteria):
        pass
    @classmethod
    def sort(cls, objects, sort_by):
        pass

@testdata_objectsCodeCoverage.AddMethodTesting
@testdata_objectsCodeCoverage.AddPropertyTesting
class testBaseDataObject(unittest.TestCase):

    ###################################
    # Tests of class methods          #
    ###################################

    def test__init__(self):
        # Tests the __init__ method of the BaseDataObject class
        # - All we need to do here is prove that the various 
        #   setter- and deleter-method calls are operating as 
        #   expected.
        # - deleters first
        test_object = BaseDataObjectDerived()
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
        test_object = BaseDataObjectDerived(
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

    def test_del_created(self):
        # Tests the _del_created method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        test_object._created = 'unexpected value'
        test_object._del_created()
        self.assertEquals(
            test_object._created, None,
            'BaseDataObject._del_created should leave None in the '
            'underlying storage attribute, but "%s" (%s) was '
            'found instead' % 
            (
                test_object._created, 
                type(test_object._created).__name__
            )
        )

    def test_del_is_active(self):
        # Tests the _del_is_active method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        test_object._is_active = 'unexpected value'
        test_object._del_is_active()
        self.assertEquals(
            test_object._is_active, True,
            'BaseDataObject._del_is_active should leave None in the '
            'underlying storage attribute, but "%s" (%s) was '
            'found instead' % 
            (
                test_object._is_active, 
                type(test_object._is_active).__name__
            )
        )

    def test_del_is_deleted(self):
        # Tests the _del_is_deleted method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        test_object._is_deleted = 'unexpected value'
        test_object._del_is_deleted()
        self.assertEquals(
            test_object._is_deleted, False,
            'BaseDataObject._del_is_deleted should leave None in the '
            'underlying storage attribute, but "%s" (%s) was '
            'found instead' % 
            (
                test_object._is_deleted, 
                type(test_object._is_deleted).__name__
            )
        )

    def test_del_is_dirty(self):
        # Tests the _del_is_dirty method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        test_object._is_dirty = 'unexpected value'
        test_object._del_is_dirty()
        self.assertEquals(
            test_object._is_dirty, False,
            'BaseDataObject._del_is_dirty should leave None in the '
            'underlying storage attribute, but "%s" (%s) was '
            'found instead' % 
            (
                test_object._is_dirty, 
                type(test_object._is_dirty).__name__
            )
        )

    def test_del_is_new(self):
        # Tests the _del_is_new method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        test_object._is_new = 'unexpected value'
        test_object._del_is_new()
        self.assertEquals(
            test_object._is_new, True,
            'BaseDataObject._del_is_new should leave None in the '
            'underlying storage attribute, but "%s" (%s) was '
            'found instead' % 
            (test_object._is_new, type(test_object._is_new).__name__)
        )

    def test_del_modified(self):
        # Tests the _del_modified method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        test_object._modified = 'unexpected value'
        test_object._del_modified()
        self.assertEquals(
            test_object._modified, None,
            'BaseDataObject._del_modified should leave None in the '
            'underlying storage attribute, but "%s" (%s) was '
            'found instead' % 
            (
                test_object._modified, 
                type(test_object._modified).__name__
            )
        )

    def test_del_oid(self):
        # Tests the _del_oid method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        test_object._oid = 'unexpected value'
        test_object._del_oid()
        self.assertEquals(
            test_object._oid, None,
            'BaseDataObject._del_oid should leave None in the '
            'underlying storage attribute, but "%s" (%s) was '
            'found instead' % 
            (test_object._oid, type(test_object._oid).__name__)
        )

    def test_get_created(self):
        # Tests the _get_created method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        expected = 'expected value'
        test_object._created = expected
        actual = test_object.created
        self.assertEquals(actual, expected, 
            '_get_created was expected to return "%s" (%s), but '
            'returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__
            )
        )
        test_object._created = None
        self.assertEqual(type(test_object._get_created()), datetime, 
            'BaseDataObject._get_created should return a '
            'datetime value if it\'s retrieved from an instance '
            'with an underlying None value'
        )

    def test_get_is_active(self):
        # Tests the _get_is_active method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        expected = 'expected value'
        test_object._is_active = expected
        actual = test_object.is_active
        self.assertEquals(actual, expected, 
            '_get_is_active was expected to return "%s" (%s), but '
            'returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__
            )
        )

    def test_get_is_deleted(self):
        # Tests the _get_is_deleted method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        expected = 'expected value'
        test_object._is_deleted = expected
        actual = test_object.is_deleted
        self.assertEquals(actual, expected, 
            '_get_is_deleted was expected to return "%s" (%s), but '
            'returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__
            )
        )

    def test_get_is_dirty(self):
        # Tests the _get_is_dirty method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        expected = 'expected value'
        test_object._is_dirty = expected
        actual = test_object.is_dirty
        self.assertEquals(actual, expected, 
            '_get_is_dirty was expected to return "%s" (%s), but '
            'returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__
            )
        )

    def test_get_is_new(self):
        # Tests the _get_is_new method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        expected = 'expected value'
        test_object._is_new = expected
        actual = test_object.is_new
        self.assertEquals(actual, expected, 
            '_get_is_new was expected to return "%s" (%s), but '
            'returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__
            )
        )

    def test_get_modified(self):
        # Tests the _get_modified method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        expected = 'expected value'
        test_object._modified = expected
        actual = test_object.modified
        self.assertEquals(actual, expected, 
            '_get_modified was expected to return "%s" (%s), but '
            'returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__
            )
        )
        test_object._modified = None
        self.assertEqual(type(test_object._get_modified()), datetime, 
            'BaseDataObject._get_modified should return a '
            'datetime value if it\'s retrieved from an instance '
            'with an underlying None value'
        )

    def test_get_oid(self):
        # Tests the _get_oid method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        expected = 'expected value'
        test_object._oid = expected
        actual = test_object.oid
        self.assertEquals(actual, expected, 
            '_get_oid was expected to return "%s" (%s), but '
            'returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__
            )
        )
        test_object._oid = None
        self.assertEqual(type(test_object._get_oid()), UUID, 
            'BaseDataObject._get_oid should return a UUID value '
            'if it\'s retrieved from an instance with an '
            'underlying None value'
        )

    def test_set_created(self):
        # Tests the _set_created method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        # - Test all "good" values
        for created in GoodDateTimes:
            if type(created) == datetime:
                expected = created
            elif type(created) in (int, float):
                expected = datetime.fromtimestamp(created)
            elif type(created) == str:
                expected = datetime.strptime(
                    created, BaseDataObject._data_time_string
                )
            test_object._set_created(created)
            actual = test_object.created
            self.assertEqual(
                actual, expected, 
                'Setting created to "%s" (%s) should return '
                '"%s" (%s) through the property, but "%s" (%s) '
                'was returned instead' % 
                (
                    created, type(created).__name__,
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all "bad" values
        for created in BadDateTimes:
            try:
                test_object._set_created(created)
                self.fail(
                    'BaseDataObject objects should not accept "%s" '
                    '(%s) as created values, but it was allowed to '
                    'be set' % 
                    (created, type(created).__name__)
                )
            except (TypeError, ValueError):
                pass
            except Exception as error:
                self.fail(
                    'BaseDataObject objects should raise TypeError '
                    'or ValueError if passed a created value of '
                    '"%s" (%s), but %s was raised instead:\n'
                    '    %s' % 
                    (
                        created, type(created).__name__, 
                        error.__class__.__name__, error
                    )
                )

    def test_set_is_active(self):
        # Tests the _set_is_active method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        # - Test all "good" values
        for is_active in GoodBooleanOrIntEquivalents:
            test_object._set_is_active(is_active)
            expected = True if is_active else False
            actual = test_object.is_active
            self.assertEqual(
                actual, expected, 
                'Setting is_active to "%s" (%s) should return '
                '"%s" (%s) through the property, but "%s" (%s) '
                'was returned instead' % 
                (
                    is_active, type(is_active).__name__,
                    expected, type(expected).__name__,
                    actual, type(actual).__name__,
                )
            )
        # - Test all "bad" values
        for is_active in BadBooleanOrIntEquivalents:
            try:
                test_object._set_is_active(is_active)
                self.fail(
                    'BaseDataObject objects should not accept '
                    '"%s" (%s) as valid is_active values, but it '
                    'was allowed to be set' % 
                    (is_active, type(is_active).__name__)
                )
            except (TypeError, ValueError):
                pass
            except Exception as error:
                self.fail(
                    'BaseDataObject objects should raise TypeError '
                    'or ValueError if passed an is_active value '
                    'of "%s" (%s), but %s was raised instead:\n'
                    '    %s' % 
                    (
                        is_active, type(is_active).__name__,
                        error.__class__.__name__, error
                    )
                )

    def test_set_is_deleted(self):
        # Tests the _set_is_deleted method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        # - Test all "good" values
        for is_deleted in GoodBooleanOrIntEquivalents:
            test_object._set_is_deleted(is_deleted)
            expected = True if is_deleted else False
            actual = test_object.is_deleted
            self.assertEqual(
                actual, expected, 
                'Setting is_deleted to "%s" (%s) should return '
                '"%s" (%s) through the property, but "%s" (%s) '
                'was returned instead' % 
                (
                    is_deleted, type(is_deleted).__name__,
                    expected, type(expected).__name__,
                    actual, type(actual).__name__,
                )
            )
        # - Test all "bad" values
        for is_deleted in BadBooleanOrIntEquivalents:
            try:
                test_object._set_is_deleted(is_deleted)
                self.fail(
                    'BaseDataObject objects should not accept '
                    '"%s" (%s) as valid is_deleted values, but it '
                    'was allowed to be set' % 
                    (is_deleted, type(is_deleted).__name__)
                )
            except (TypeError, ValueError):
                pass
            except Exception as error:
                self.fail(
                    'BaseDataObject objects should raise TypeError '
                    'or ValueError if passed an is_deleted value '
                    'of "%s" (%s), but %s was raised instead:\n'
                    '    %s' % 
                    (
                        is_deleted, type(is_deleted).__name__,
                        error.__class__.__name__, error
                    )
                )

    def test_set_is_dirty(self):
        # Tests the _set_is_dirty method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        # - Test all "good" values
        for is_dirty in GoodBooleanOrIntEquivalents:
            test_object._set_is_dirty(is_dirty)
            expected = True if is_dirty else False
            actual = test_object.is_dirty
            self.assertEqual(
                actual, expected, 
                'Setting is_dirty to "%s" (%s) should return '
                '"%s" (%s) through the property, but "%s" (%s) '
                'was returned instead' % 
                (
                    is_dirty, type(is_dirty).__name__,
                    expected, type(expected).__name__,
                    actual, type(actual).__name__,
                )
            )
        # - Test all "bad" values
        for is_dirty in BadBooleanOrIntEquivalents:
            try:
                test_object._set_is_dirty(is_dirty)
                self.fail(
                    'BaseDataObject objects should not accept '
                    '"%s" (%s) as valid is_dirty values, but it '
                    'was allowed to be set' % 
                    (is_dirty, type(is_dirty).__name__)
                )
            except (TypeError, ValueError):
                pass
            except Exception as error:
                self.fail(
                    'BaseDataObject objects should raise TypeError '
                    'or ValueError if passed an is_dirty value '
                    'of "%s" (%s), but %s was raised instead:\n'
                    '    %s' % 
                    (
                        is_dirty, type(is_dirty).__name__,
                        error.__class__.__name__, error
                    )
                )

    def test_set_is_new(self):
        # Tests the _set_is_new method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        # - Test all "good" values
        for is_new in GoodBooleanOrIntEquivalents:
            test_object._set_is_new(is_new)
            expected = True if is_new else False
            actual = test_object.is_new
            self.assertEqual(
                actual, expected, 
                'Setting is_new to "%s" (%s) should return '
                '"%s" (%s) through the property, but "%s" (%s) '
                'was returned instead' % 
                (
                    is_new, type(is_new).__name__,
                    expected, type(expected).__name__,
                    actual, type(actual).__name__,
                )
            )
        # - Test all "bad" values
        for is_new in BadBooleanOrIntEquivalents:
            try:
                test_object._set_is_new(is_new)
                self.fail(
                    'BaseDataObject objects should not accept '
                    '"%s" (%s) as valid is_new values, but it '
                    'was allowed to be set' % 
                    (is_new, type(is_new).__name__)
                )
            except (TypeError, ValueError):
                pass
            except Exception as error:
                self.fail(
                    'BaseDataObject objects should raise TypeError '
                    'or ValueError if passed an is_new value '
                    'of "%s" (%s), but %s was raised instead:\n'
                    '    %s' % 
                    (
                        is_new, type(is_new).__name__,
                        error.__class__.__name__, error
                    )
                )

    def test_set_modified(self):
        # Tests the _set_modified method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        # - Test all "good" values
        for modified in GoodDateTimes:
            if type(modified) == datetime:
                expected = modified
            elif type(modified) in (int, float):
                expected = datetime.fromtimestamp(modified)
            elif type(modified) == str:
                expected = datetime.strptime(
                    modified, BaseDataObject._data_time_string
                )
            test_object._set_modified(modified)
            actual = test_object.modified
            self.assertEqual(
                actual, expected, 
                'Setting modified to "%s" (%s) should return '
                '"%s" (%s) through the property, but "%s" (%s) '
                'was returned instead' % 
                (
                    modified, type(modified).__name__,
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all "bad" values
        for modified in BadDateTimes:
            try:
                test_object._set_modified(modified)
                self.fail(
                    'BaseDataObject objects should not accept "%s" '
                    '(%s) as modified values, but it was allowed to '
                    'be set' % 
                    (modified, type(modified).__name__)
                )
            except (TypeError, ValueError):
                pass
            except Exception as error:
                self.fail(
                    'BaseDataObject objects should raise TypeError '
                    'or ValueError if passed a modified value of '
                    '"%s" (%s), but %s was raised instead:\n'
                    '    %s' % 
                    (
                        modified, type(modified).__name__, 
                        error.__class__.__name__, error
                    )
                )

    def test_set_oid(self):
        # Tests the _set_oid method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        # - Test all "good" values
        for oid in GoodOIDs:
            if type(oid) == UUID:
                expected = oid
            elif type(oid) == str:
                expected = UUID(oid)
            test_object._set_oid(oid)
            actual = test_object.oid
            self.assertEqual(
                actual, expected, 
                'Setting oid to "%s" (%s) should return '
                '"%s" (%s) through the property, but "%s" '
                '(%s) was returned instead.' % 
                (
                    oid, type(oid).__name__, 
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all "bad" values
        for oid in BadOIDs:
            try:
                test_object._set_oid(oid)
                self.fail(
                    'BaseDatObject objects should not accept '
                    '"%s" (%s) as a valid oid, but it was '
                    'allowed to be set' % 
                    (oid, type(oid).__name__)
                )
            except (TypeError, ValueError):
                pass
            except Exception as error:
                self.fail(
                    'BaseDataObject objects should raise TypeError '
                    'or ValueError if passed a value of "%s" (%s) '
                    'as an oid, but %s was raised instead:\n'
                    '    %s' % 
                    (
                        oid, type(oid).__name__, 
                        error.__class__.__name__, error
                    )
                )

    def testsave(self):
        # Tests the save method of the BaseDataObject class
        test_object = BaseDataObjectDerived()
        # - Set things up to force a call to _create:
        test_object._is_new = True
        for dirty in (True, False, None):
            test_object._is_dirty = dirty
            try:
                test_object.save()
            except NotImplementedError as error:
                if str(error) != (
                    'BaseDataObjectDerived has not implemented '
                    '_create, as required by BaseDataObject'
                ):
                    self.fail(
                        'Calling _create should return a known '
                        'error-message, but the message returned '
                        'was not what was expected'
                    )
            except Exception as error:
                self.fail(
                    'BaseDataObject.save did not raise the '
                    'expected error while being tested'
                )
        # - Set things up to force a call to _update:
        test_object._is_new = False
        for dirty in (True, False, None):
            test_object._is_dirty = dirty
            try:
                test_object.save()
            except NotImplementedError as error:
                if str(error) != (
                    'BaseDataObjectDerived has not implemented '
                    '_update, as required by BaseDataObject'
                ):
                    self.fail(
                        'Calling _create should return a known '
                        'error-message, but the message returned '
                        'was not what was expected'
                    )
            except Exception as error:
                self.fail(
                    'BaseDataObject.save did not raise the '
                    'expected error while being tested'
                )

    ###################################
    # Tests of class properties       #
    ###################################

    def testcreated(self):
        # Tests the created property of the BaseDataObject class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseDataObject.created.fget, 
            BaseDataObject._get_created, 
            'BaseDataObject.created is expected to use the '
            '_get_created method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseDataObject.created.fset, 
            BaseDataObject._set_created, 
            'BaseDataObject.created is expected to use the '
            '_set_created method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseDataObject.created.fdel, 
            BaseDataObject._del_created, 
            'BaseDataObject.created is expected to use the '
            '_del_created method as its deleter-method'
        )

    def testis_active(self):
        # Tests the is_active property of the BaseDataObject class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseDataObject.is_active.fget, 
            BaseDataObject._get_is_active, 
            'BaseDataObject.is_active is expected to use the '
            '_get_is_active method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseDataObject.is_active.fset, 
            BaseDataObject._set_is_active, 
            'BaseDataObject.is_active is expected to use the '
            '_set_is_active method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseDataObject.is_active.fdel, 
            BaseDataObject._del_is_active, 
            'BaseDataObject.is_active is expected to use the '
            '_del_is_active method as its deleter-method'
        )

    def testis_deleted(self):
        # Tests the is_deleted property of the BaseDataObject class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseDataObject.is_deleted.fget, 
            BaseDataObject._get_is_deleted, 
            'BaseDataObject.is_deleted is expected to use the '
            '_get_is_deleted method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseDataObject.is_deleted.fset, 
            BaseDataObject._set_is_deleted, 
            'BaseDataObject.is_deleted is expected to use the '
            '_set_is_deleted method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseDataObject.is_deleted.fdel, 
            BaseDataObject._del_is_deleted, 
            'BaseDataObject.is_deleted is expected to use the '
            '_del_is_deleted method as its deleter-method'
        )

    def testis_dirty(self):
        # Tests the is_dirty property of the BaseDataObject class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseDataObject.is_dirty.fget, 
            BaseDataObject._get_is_dirty, 
            'BaseDataObject.is_dirty is expected to use the '
            '_get_is_dirty method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseDataObject.is_dirty.fset, 
            BaseDataObject._set_is_dirty, 
            'BaseDataObject.is_dirty is expected to use the '
            '_set_is_dirty method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseDataObject.is_dirty.fdel, 
            BaseDataObject._del_is_dirty, 
            'BaseDataObject.is_dirty is expected to use the '
            '_del_is_dirty method as its deleter-method'
        )

    def testis_new(self):
        # Tests the is_new property of the BaseDataObject class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseDataObject.is_new.fget, 
            BaseDataObject._get_is_new, 
            'BaseDataObject.is_new is expected to use the '
            '_get_is_new method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseDataObject.is_new.fset, 
            BaseDataObject._set_is_new, 
            'BaseDataObject.is_new is expected to use the '
            '_set_is_new method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseDataObject.is_new.fdel, 
            BaseDataObject._del_is_new, 
            'BaseDataObject.is_new is expected to use the '
            '_del_is_new method as its deleter-method'
        )

    def testmodified(self):
        # Tests the modified property of the BaseDataObject class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseDataObject.modified.fget, 
            BaseDataObject._get_modified, 
            'BaseDataObject.modified is expected to use the '
            '_get_modified method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseDataObject.modified.fset, 
            BaseDataObject._set_modified, 
            'BaseDataObject.modified is expected to use the '
            '_set_modified method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseDataObject.modified.fdel, 
            BaseDataObject._del_modified, 
            'BaseDataObject.modified is expected to use the '
            '_del_modified method as its deleter-method'
        )

    def testoid(self):
        # Tests the oid property of the BaseDataObject class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseDataObject.oid.fget, 
            BaseDataObject._get_oid, 
            'BaseDataObject.oid is expected to use the '
            '_get_oid method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseDataObject.oid.fset, 
            BaseDataObject._set_oid, 
            'BaseDataObject.oid is expected to use the '
            '_set_oid method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseDataObject.oid.fdel, 
            BaseDataObject._del_oid, 
            'BaseDataObject.oid is expected to use the '
            '_del_oid method as its deleter-method'
        )

#    def testproperty_name(self):
#        # Tests the property_name property of the BaseDataObject class
#        # - Assert that the getter is correct:
#        self.assertEqual(
#            BaseDataObject.property_name.fget, 
#            BaseDataObject._get_property_name, 
#            'BaseDataObject.property_name is expected to use the '
#            '_get_property_name method as its getter-method'
#        )
#        # - If property_name is not expected to be publicly settable,
#        #   the second item here (BaseDataObject._set_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the setter is correct:
#        self.assertEqual(
#            BaseDataObject.property_name.fset, 
#            BaseDataObject._set_property_name, 
#            'BaseDataObject.property_name is expected to use the '
#            '_set_property_name method as its setter-method'
#        )
#        # - If property_name is not expected to be publicly deletable,
#        #   the second item here (BaseDataObject._del_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the deleter is correct:
#        self.assertEqual(
#            BaseDataObject.property_name.fdel, 
#            BaseDataObject._del_property_name, 
#            'BaseDataObject.property_name is expected to use the '
#            '_del_property_name method as its deleter-method'
#        )

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testBaseDataObject
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
        SaveTestReport(results, 'hms_core.data_objects',
            'hms_core.data_objects.test-results')
