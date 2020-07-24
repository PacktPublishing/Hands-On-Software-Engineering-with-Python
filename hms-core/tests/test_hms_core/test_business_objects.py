#!/usr/bin/env python

"""
Defines unit-tests for the module at hms_core.business_objects.
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
# Import the module being tested      #
#######################################

import hms_core.business_objects as business_objects
from hms_core.business_objects import *

#######################################
# Module-level Constants              #
#######################################

LocalSuite = unittest.TestSuite()

GoodBooleanOrIntEquivalents = [
    True, False, 1, 0
]
BadBooleanOrIntEquivalents = [
    'true', '', (1,2), tuple()
]

GoodStandardOptionalTextLines = [
    'word', 'hyphenated-word', 'short phrase', 
    'A complete sentence.', 
    'A short paragraph. This\'s got some punctuation, '
    'including "quoted text."',
    None # Because optional items are allowed to be None
]
BadStandardOptionalTextLines = [
    # Bad string values
    'multiple\nlines', 'also multiple\rlines', 
    'text\twith\tabs',
    # Values that aren't strings at all
    1, True, 0, False, object(), 
    # empty and whitespace-only strings
    '', '  ',
]
GoodStandardRequiredTextLines = [
    'word', 'hyphenated-word', 'short phrase', 
    'A complete sentence.', 
    'A short paragraph. This\'s got some punctuation, '
    'including "quoted text."',
]
BadStandardRequiredTextLines = [
    # Bad string values
    'multiple\nlines', 'also multiple\rlines', 
    'text\twith\tabs',
    # Values that aren't strings at all
    1, True, 0, False, object(), 
    # empty and whitespace-only strings
    '', '  ',
    None # Because optional items are NOT allowed to be None
]

GoodWeights = [
    0, 1, 2, 0.0, 1.0, 2.0, 1.5
]
BadWeights = [
    -1, -1.0, object(), 'true', '', (1,2), tuple()
]

BadDescriptions = [
    # Values that aren't strings at all
    1, True, 0, False, object(), 
    # empty and whitespace-only strings
    '', '  ',
]

GoodMetadataDicts = [
    {},
    {'spam':'eggs'}
]
BadMetadataDicts = [
    -1, -1.0, object(), 'true', '', (1,2), tuple()
]

GoodAddress = Address('street-address', 'city')
GoodAddresses = [
    Address('street-address', 'city')
]
BadAddresses = [
    -1, -1.0, object(), 'true', '', (1,2), tuple()
]

GoodEmails = [
    'someone@somewhere.com',
    'brian.allbee+hosewp@gmail.com',
]
BadEmails = [
    '', 'string', -1, -1.0, object(), 'true', '', (1,2), tuple()
]

GoodURLs = [
    'http://www.google.com',
    'https://www.google.com',
]
BadURLs = [
    '', 'string', -1, -1.0, object(), 'true', '', (1,2), tuple()
]

#######################################
# Code-coverage test-case and         #
# decorator-methods                   #
#######################################

class testbusiness_objectsCodeCoverage(ModuleCoverageTest):
    _testNamespace = 'hms_core'
    _testModule = business_objects

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testbusiness_objectsCodeCoverage
   )
)

#######################################
# Test-cases in the module            #
#######################################

@testbusiness_objectsCodeCoverage.AddMethodTesting
@testbusiness_objectsCodeCoverage.AddPropertyTesting
class testAddress(unittest.TestCase):

    ###################################
    # Tests of class methods          #
    ###################################

    def test__init__(self):
        # Tests the __init__ method of the Address class
        # - Test all permutations of "good" argument-values:
        for building_address in GoodStandardOptionalTextLines:
            for city in GoodStandardRequiredTextLines:
                for country in GoodStandardOptionalTextLines:
                    for postal_code in GoodStandardOptionalTextLines:
                        for region in GoodStandardOptionalTextLines:
                            for street_address in GoodStandardRequiredTextLines:
                                test_object = Address(
                                    street_address, city, building_address,
                                    region, postal_code, country
                                )
                                self.assertEqual(test_object.street_address, street_address)
                                self.assertEqual(test_object.city, city)
                                self.assertEqual(test_object.building_address, building_address)
                                self.assertEqual(test_object.region, region)
                                self.assertEqual(test_object.postal_code, postal_code)
                                self.assertEqual(test_object.country, country)

    def test_del_building_address(self):
        # Tests the _del_building_address method of the Address class
        test_object = Address('street address', 'city')
        self.assertEqual(
            test_object.building_address, None, 
            'An Address object is expected to have None as its default '
            'building_address value if no value was provided'
        )
        # - Hard-set the storage-property's value, call the 
        #   deleter-method, and assert that it's what's expected 
        #   afterwards:
        test_object._building_address = 'a test value'
        test_object._del_building_address()
        self.assertEqual(
            test_object.building_address, None, 
            'An Address object is expected to have None as its '
            'building_address value after the deleter is called'
        )

    def test_del_city(self):
        # Tests the _del_city method of the Address class
        expected = 'city'
        test_object = Address('street address', expected)
        self.assertEqual(
            test_object.city, expected, 
            'An Address object is expected to have "%s" (%s) as its '
            'current city value, since that value was provided' % 
            (expected, type(expected).__name__)
        )
        # - Since we have a value, just call the deleter-method, and 
        #   assert that it's what's expected afterwards:
        test_object._del_city()
        self.assertEqual(
            test_object.city, None, 
            'An Address object is expected to have None as its '
            'city value after the deleter is called'
        )

    def test_del_country(self):
        # Tests the _del_country method of the Address class
        test_object = Address('street address', 'country')
        self.assertEqual(
            test_object.country, None, 
            'An Address object is expected to have None as its default '
            'country value if no value was provided'
        )
        # - Hard-set the storage-property's value, call the 
        #   deleter-method, and assert that it's what's expected 
        #   afterwards:
        test_object._country = 'a test value'
        test_object._del_country()
        self.assertEqual(
            test_object.country, None, 
            'An Address object is expected to have None as its '
            'country value after the deleter is called'
        )

    def test_del_postal_code(self):
        # Tests the _del_postal_code method of the Address class
        test_object = Address('street address', 'postal_code')
        self.assertEqual(
            test_object.postal_code, None, 
            'An Address object is expected to have None as its default '
            'postal_code value if no value was provided'
        )
        # - Hard-set the storage-property's value, call the 
        #   deleter-method, and assert that it's what's expected 
        #   afterwards:
        test_object._postal_code = 'a test value'
        test_object._del_postal_code()
        self.assertEqual(
            test_object.postal_code, None, 
            'An Address object is expected to have None as its '
            'postal_code value after the deleter is called'
        )

    def test_del_region(self):
        # Tests the _del_region method of the Address class
        test_object = Address('street address', 'region')
        self.assertEqual(
            test_object.region, None, 
            'An Address object is expected to have None as its default '
            'region value if no value was provided'
        )
        # - Hard-set the storage-property's value, call the 
        #   deleter-method, and assert that it's what's expected 
        #   afterwards:
        test_object._region = 'a test value'
        test_object._del_region()
        self.assertEqual(
            test_object.region, None, 
            'An Address object is expected to have None as its '
            'region value after the deleter is called'
        )

    def test_del_street_address(self):
        # Tests the _del_street_address method of the Address class
        expected = 'street_address'
        test_object = Address(expected, 'city')
        self.assertEqual(
            test_object.street_address, expected, 
            'An Address object is expected to have "%s" (%s) as its '
            'curent street_address value, since that value was '
            'provided' % (expected, type(expected).__name__)
        )
        # - Since we have a value, just call the deleter-method, and 
        #   assert that it's what's expected afterwards:
        test_object._del_street_address()
        self.assertEqual(
            test_object.street_address, None, 
            'An Address object is expected to have None as its '
            'street_address value after the deleter is called'
        )

    def test_get_building_address(self):
        # Tests the _get_building_address method of the Address class
        test_object = Address('street address', 'city')
        expected = 'a test-value'
        test_object._building_address = expected
        actual = test_object._get_building_address()
        self.assertEqual(
            actual, expected, 
            'Address._get_building_address was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_city(self):
        # Tests the _get_city method of the Address class
        test_object = Address('street address', 'city')
        expected = 'a test-value'
        test_object._city = expected
        actual = test_object._get_city()
        self.assertEqual(
            actual, expected, 
            'Address._get_city was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_country(self):
        # Tests the _get_country method of the Address class
        test_object = Address('street address', 'country')
        expected = 'a test-value'
        test_object._country = expected
        actual = test_object._get_country()
        self.assertEqual(
            actual, expected, 
            'Address._get_country was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_postal_code(self):
        # Tests the _get_postal_code method of the Address class
        test_object = Address('street address', 'postal_code')
        expected = 'a test-value'
        test_object._postal_code = expected
        actual = test_object._get_postal_code()
        self.assertEqual(
            actual, expected, 
            'Address._get_postal_code was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_region(self):
        # Tests the _get_region method of the Address class
        test_object = Address('street address', 'region')
        expected = 'a test-value'
        test_object._region = expected
        actual = test_object._get_region()
        self.assertEqual(
            actual, expected, 
            'Address._get_region was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_street_address(self):
        # Tests the _get_street_address method of the Address class
        test_object = Address('street address', 'street_address')
        expected = 'a test-value'
        test_object._street_address = expected
        actual = test_object._get_street_address()
        self.assertEqual(
            actual, expected, 
            'Address._get_street_address was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_set_building_address(self):
        # Tests the _set_building_address method of the Address class
        # - Create an object to test with:
        test_object = Address('street address', 'street_address')
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardOptionalTextLines:
            test_object._set_building_address(expected)
            actual = test_object._get_building_address()
            self.assertEqual(
                expected, actual, 
                'Address expects a building_address value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardOptionalTextLines:
            try:
                test_object._set_building_address(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'Address._set_business_address should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'Address._set_business_address should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_city(self):
        # Tests the _set_city method of the Address class
        # - Create an object to test with:
        test_object = Address('street address', 'street_address')
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardRequiredTextLines:
            test_object._set_city(expected)
            actual = test_object._get_city()
            self.assertEqual(
                expected, actual, 
                'Address expects a city value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardRequiredTextLines:
            try:
                test_object._set_city(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'Address._set_business_address should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'Address._set_business_address should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_country(self):
        # Tests the _set_country method of the Address class
        # - Create an object to test with:
        test_object = Address('street address', 'street_address')
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardOptionalTextLines:
            test_object._set_country(expected)
            actual = test_object._get_country()
            self.assertEqual(
                expected, actual, 
                'Address expects a country value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardOptionalTextLines:
            try:
                test_object._set_country(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'Address._set_business_address should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'Address._set_business_address should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_country(self):
        # Tests the _set_country method of the Address class
        # - Create an object to test with:
        test_object = Address('street address', 'street_address')
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardOptionalTextLines:
            test_object._set_country(expected)
            actual = test_object._get_country()
            self.assertEqual(
                expected, actual, 
                'Address expects a country value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardOptionalTextLines:
            try:
                test_object._set_country(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'Address._set_business_address should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'Address._set_business_address should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_postal_code(self):
        # Tests the _set_postal_code method of the Address class
        # - Create an object to test with:
        test_object = Address('street address', 'street_address')
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardOptionalTextLines:
            test_object._set_postal_code(expected)
            actual = test_object._get_postal_code()
            self.assertEqual(
                expected, actual, 
                'Address expects a postal_code value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardOptionalTextLines:
            try:
                test_object._set_postal_code(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'Address._set_business_address should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'Address._set_business_address should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_region(self):
        # Tests the _set_region method of the Address class
        # - Create an object to test with:
        test_object = Address('street address', 'street_address')
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardOptionalTextLines:
            test_object._set_region(expected)
            actual = test_object._get_region()
            self.assertEqual(
                expected, actual, 
                'Address expects a region value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardOptionalTextLines:
            try:
                test_object._set_region(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'Address._set_business_address should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'Address._set_business_address should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_street_address(self):
        # Tests the _set_street_address method of the Address class
        # - Create an object to test with:
        test_object = Address('street address', 'street_address')
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardRequiredTextLines:
            test_object._set_street_address(expected)
            actual = test_object._get_street_address()
            self.assertEqual(
                expected, actual, 
                'Address expects a street_address value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardRequiredTextLines:
            try:
                test_object._set_street_address(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'Address._set_business_address should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'Address._set_business_address should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    @unittest.skip(
        'This was tested elsewhere by accident (see test_co_objects), '
        'and can probably be safely skipped for now.'
    )
    def testfrom_dict(self):
        # Tests the from_dict method of the Address class
        # - Test all permutations of "good" argument-values:
        # - Test all permutations of each "bad" argument-value 
        #   set against "good" values for the other arguments:
        self.fail('testfrom_dict is not yet implemented')

    def teststandard_address(self):
        # Tests the standard_address method of the Address class
        # - Test all permutations of "good" argument-values:
        for street_address in GoodStandardRequiredTextLines:
            for building_address in GoodStandardOptionalTextLines:
                for city in GoodStandardRequiredTextLines:
                    for region in GoodStandardOptionalTextLines:
                        for postal_code in GoodStandardOptionalTextLines:
                            for country in GoodStandardOptionalTextLines:
                                test_object = Address.standard_address(
                                    street_address, building_address, 
                                    city, region, postal_code, 
                                    country
                                )
                                self.assertEqual(test_object.street_address, street_address)
                                self.assertEqual(test_object.building_address, building_address)
                                self.assertEqual(test_object.city, city)
                                self.assertEqual(test_object.region, region)
                                self.assertEqual(test_object.postal_code, postal_code)
                                self.assertEqual(test_object.country, country)

    @unittest.skip(
        'This was tested elsewhere by accident (see test_co_objects), '
        'and can probably be safely skipped for now.'
    )
    def testto_dict(self):
        # Tests the to_dict method of the Address class
        # - Test all permutations of "good" argument-values:
        # - Test all permutations of each "bad" argument-value 
        #   set against "good" values for the other arguments:
        self.fail('testto_dict is not yet implemented')

#    def testmethod_name(self):
#        # Tests the method_name method of the Address class
#        # - Test all permutations of "good" argument-values:
#        # - Test all permutations of each "bad" argument-value 
#        #   set against "good" values for the other arguments:
#        self.fail('testmethod_name is not yet implemented')

    ###################################
    # Tests of class properties       #
    ###################################

    def testbuilding_address(self):
        # Tests the building_address property of the Address class
        # - Assert that the getter is correct:
        self.assertEqual(
            Address.building_address.fget, 
            Address._get_building_address, 
            'Address.building_address is expected to use the '
            '_get_building_address method as its getter-method'
        )
        # - If building_address is not expected to be publicly settable,
        #   the second item here (Address._set_building_address) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            Address.building_address.fset, 
            Address._set_building_address, 
            'Address.building_address is expected to use the '
            '_set_building_address method as its setter-method'
        )
        # - If building_address is not expected to be publicly deletable,
        #   the second item here (Address._del_building_address) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            Address.building_address.fdel, 
            Address._del_building_address, 
            'Address.building_address is expected to use the '
            '_del_building_address method as its deleter-method'
        )

    def testcity(self):
        # Tests the city property of the Address class
        # - Assert that the getter is correct:
        self.assertEqual(
            Address.city.fget, 
            Address._get_city, 
            'Address.city is expected to use the '
            '_get_city method as its getter-method'
        )
        # - If city is not expected to be publicly settable,
        #   the second item here (Address._set_city) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            Address.city.fset, 
            Address._set_city, 
            'Address.city is expected to use the '
            '_set_city method as its setter-method'
        )
        # - If city is not expected to be publicly deletable,
        #   the second item here (Address._del_city) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            Address.city.fdel, 
            Address._del_city, 
            'Address.city is expected to use the '
            '_del_city method as its deleter-method'
        )

    def testcountry(self):
        # Tests the country property of the Address class
        # - Assert that the getter is correct:
        self.assertEqual(
            Address.country.fget, 
            Address._get_country, 
            'Address.country is expected to use the '
            '_get_country method as its getter-method'
        )
        # - If country is not expected to be publicly settable,
        #   the second item here (Address._set_country) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            Address.country.fset, 
            Address._set_country, 
            'Address.country is expected to use the '
            '_set_country method as its setter-method'
        )
        # - If country is not expected to be publicly deletable,
        #   the second item here (Address._del_country) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            Address.country.fdel, 
            Address._del_country, 
            'Address.country is expected to use the '
            '_del_country method as its deleter-method'
        )

    def testpostal_code(self):
        # Tests the postal_code property of the Address class
        # - Assert that the getter is correct:
        self.assertEqual(
            Address.postal_code.fget, 
            Address._get_postal_code, 
            'Address.postal_code is expected to use the '
            '_get_postal_code method as its getter-method'
        )
        # - If postal_code is not expected to be publicly settable,
        #   the second item here (Address._set_postal_code) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            Address.postal_code.fset, 
            Address._set_postal_code, 
            'Address.postal_code is expected to use the '
            '_set_postal_code method as its setter-method'
        )
        # - If postal_code is not expected to be publicly deletable,
        #   the second item here (Address._del_postal_code) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            Address.postal_code.fdel, 
            Address._del_postal_code, 
            'Address.postal_code is expected to use the '
            '_del_postal_code method as its deleter-method'
        )

    def testregion(self):
        # Tests the region property of the Address class
        # - Assert that the getter is correct:
        self.assertEqual(
            Address.region.fget, 
            Address._get_region, 
            'Address.region is expected to use the '
            '_get_region method as its getter-method'
        )
        # - If region is not expected to be publicly settable,
        #   the second item here (Address._set_region) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            Address.region.fset, 
            Address._set_region, 
            'Address.region is expected to use the '
            '_set_region method as its setter-method'
        )
        # - If region is not expected to be publicly deletable,
        #   the second item here (Address._del_region) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            Address.region.fdel, 
            Address._del_region, 
            'Address.region is expected to use the '
            '_del_region method as its deleter-method'
        )

    def teststreet_address(self):
        # Tests the street_address property of the Address class
        # - Assert that the getter is correct:
        self.assertEqual(
            Address.street_address.fget, 
            Address._get_street_address, 
            'Address.street_address is expected to use the '
            '_get_street_address method as its getter-method'
        )
        # - If street_address is not expected to be publicly settable,
        #   the second item here (Address._set_street_address) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            Address.street_address.fset, 
            Address._set_street_address, 
            'Address.street_address is expected to use the '
            '_set_street_address method as its setter-method'
        )
        # - If street_address is not expected to be publicly deletable,
        #   the second item here (Address._del_street_address) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            Address.street_address.fdel, 
            Address._del_street_address, 
            'Address.street_address is expected to use the '
            '_del_street_address method as its deleter-method'
        )

#    def testproperty_name(self):
#        # Tests the property_name property of the Address class
#        # - Assert that the getter is correct:
#        self.assertEqual(
#            Address.property_name.fget, 
#            Address._get_property_name, 
#            'Address.property_name is expected to use the '
#            '_get_property_name method as its getter-method'
#        )
#        # - If property_name is not expected to be publicly settable,
#        #   the second item here (Address._set_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the setter is correct:
#        self.assertEqual(
#            Address.property_name.fset, 
#            Address._set_property_name, 
#            'Address.property_name is expected to use the '
#            '_set_property_name method as its setter-method'
#        )
#        # - If property_name is not expected to be publicly deletable,
#        #   the second item here (Address._del_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the deleter is correct:
#        self.assertEqual(
#            Address.property_name.fdel, 
#            Address._del_property_name, 
#            'Address.property_name is expected to use the '
#            '_del_property_name method as its deleter-method'
#        )

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testAddress
    )
)

class BaseArtisanDerived(BaseArtisan):
    def add_product(self):
        pass
    def remove_product(self):
        pass

@testbusiness_objectsCodeCoverage.AddMethodTesting
@testbusiness_objectsCodeCoverage.AddPropertyTesting
class testBaseArtisan(unittest.TestCase):

    ###################################
    # Tests of class methods          #
    ###################################

    def test__init__(self):
        # Tests the __init__ method of the BaseArtisan class
        for contact_name in GoodStandardRequiredTextLines:
            for contact_email in GoodEmails:
                for address in GoodAddresses:
                    for company_name in GoodStandardOptionalTextLines:
                        # - Testing an object without a website
                        test_object = BaseArtisanDerived(
                            contact_name, contact_email, address,
                            company_name
                        )
                        self.assertEqual(test_object.contact_name, contact_name)
                        self.assertEqual(test_object.contact_email, contact_email)
                        self.assertEqual(test_object.address, address)
                        self.assertEqual(test_object.company_name, company_name)
                        if company_name:
                            for website in GoodURLs:
                                # - Testing an object with a company-name and a website
                                test_object = BaseArtisanDerived(
                                    contact_name, contact_email, address, 
                                    company_name, website
                                )
                                self.assertEqual(test_object.website, website)
                        else:
                            for website in GoodURLs:
                                # - Testing an object with a website, but no company-name
                                test_object = BaseArtisanDerived(
                                    contact_name, contact_email, address, 
                                    website=website
                                )
                                self.assertEqual(test_object.website, website)

    def test_del_address(self):
        # Tests the _del_address method of the BaseArtisan class
        test_object = BaseArtisanDerived(
            'contact-name', 'contact@email.com', GoodAddress
        )
        test_object._address = 'any type value will work here'
        test_object._del_address()
        self.assertEqual(test_object.address, None)

    def test_del_company_name(self):
        # Tests the _del_company_name method of the BaseArtisan class
        test_object = BaseArtisanDerived(
            'contact-name', 'contact@email.com', GoodAddress
        )
        test_object._company_name = 'any type value will work here'
        test_object._del_company_name()
        self.assertEqual(test_object.company_name, None)

    def test_del_contact_email(self):
        # Tests the _del_contact_email method of the BaseArtisan class
        test_object = BaseArtisanDerived(
            'contact-name', 'contact@email.com', GoodAddress
        )
        test_object._contact_email = 'any type value will work here'
        test_object._del_contact_email()
        self.assertEqual(test_object.contact_email, None)

    def test_del_contact_name(self):
        # Tests the _del_contact_name method of the BaseArtisan class
        test_object = BaseArtisanDerived(
            'contact-name', 'contact@email.com', GoodAddress
        )
        test_object._del_contact_name()
        self.assertEqual(test_object.contact_name, None)

    def test_del_website(self):
        # Tests the _del_website method of the BaseArtisan class
        test_object = BaseArtisanDerived(
            'contact-name', 'contact@email.com', GoodAddress
        )
        test_object._website = 'any type value will work here'
        test_object._del_website()
        self.assertEqual(test_object.website, None)

    def test_get_address(self):
        # Tests the _get_address method of the BaseArtisan class
        test_object = BaseArtisanDerived(
            'contact-name', 'contact@email.com', GoodAddress
        )
        expected = 'any type of value will work here'
        test_object._address = expected
        actual = test_object._get_address()
        self.assertEqual(
            actual, expected, 
            'BaseArtisan._get_address was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_company_name(self):
        # Tests the _get_company_name method of the BaseArtisan class
        test_object = BaseArtisanDerived(
            'contact-name', 'contact@email.com', GoodAddress
        )
        expected = 'any type value will work here'
        test_object._company_name = expected
        actual = test_object._get_company_name()
        self.assertEqual(
            actual, expected, 
            'BaseArtisan._get_company_name was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_contact_email(self):
        # Tests the _get_contact_email method of the BaseArtisan class
        expected = 'contact@email.com'
        test_object = BaseArtisanDerived(
            'contact-name', expected, GoodAddress
        )
        test_object._contact_email = expected
        actual = test_object._get_contact_email()
        self.assertEqual(
            actual, expected, 
            'BaseArtisan._get_contact_email was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_contact_name(self):
        # Tests the _get_contact_name method of the BaseArtisan class
        test_object = BaseArtisanDerived(
            'contact-name', 'contact@email.com', GoodAddress
        )
        expected = 'any type value will work here'
        test_object._contact_name = expected
        actual = test_object._get_contact_name()
        self.assertEqual(
            actual, expected, 
            'BaseArtisan._get_contact_name was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_website(self):
        # Tests the _get_website method of the BaseArtisan class
        test_object = BaseArtisanDerived(
            'contact-name', 'contact@email.com', GoodAddress
        )
        expected = 'any type value will work here'
        test_object._website = expected
        actual = test_object._get_website()
        self.assertEqual(
            actual, expected, 
            'BaseArtisan._get_website was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_set_address(self):
        # Tests the _set_address method of the BaseArtisan class
        test_object = BaseArtisanDerived(
            'contact-name', 'contact@email.com', GoodAddress
        )
        # - Test all permutations of "good" argument-values:
        for expected in GoodAddresses:
            test_object._set_address(expected)
            actual = test_object._get_address()
            self.assertEqual(
                expected, actual, 
                'BaseArtisan expects a address value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadAddresses:
            try:
                test_object._set_address(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'BaseArtisan._set_address should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'BaseArtisan._set_address should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_company_name(self):
        # Tests the _set_company_name method of the BaseArtisan class
        test_object = BaseArtisanDerived(
            'contact-name', 'contact@email.com', GoodAddress
        )
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardOptionalTextLines:
            test_object._set_company_name(expected)
            actual = test_object._get_company_name()
            self.assertEqual(
                expected, actual, 
                'BaseArtisan expects a company_name value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardOptionalTextLines:
            try:
                test_object._set_company_name(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'BaseArtisan._set_company_name should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'BaseArtisan._set_company_name should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_contact_email(self):
        # Tests the _set_contact_email method of the BaseArtisan class
        test_object = BaseArtisanDerived(
            'contact-name', 'contact@email.com', GoodAddress
        )
        # - Test all permutations of "good" argument-values:
        for expected in GoodEmails:
            test_object._set_contact_email(expected)
            actual = test_object._get_contact_email()
            self.assertEqual(
                expected, actual, 
                'BaseArtisan expects a contact_email value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadEmails:
            try:
                test_object._set_contact_email(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'BaseArtisan._set_contact_email should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'BaseArtisan._set_contact_email should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_contact_name(self):
        # Tests the _set_contact_name method of the BaseArtisan class
        test_object = BaseArtisanDerived(
            'contact-name', 'contact@email.com', GoodAddress
        )
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardRequiredTextLines:
            test_object._set_contact_name(expected)
            actual = test_object._get_contact_name()
            self.assertEqual(
                expected, actual, 
                'BaseArtisan expects a contact_name value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardRequiredTextLines:
            try:
                test_object._set_contact_name(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'BaseArtisan._set_contact_name should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'BaseArtisan._set_contact_name should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_website(self):
        # Tests the _set_website method of the BaseArtisan class
        test_object = BaseArtisanDerived(
            'contact-name', 'contact@email.com', GoodAddress
        )
        # - Test all permutations of "good" argument-values:
        for expected in GoodURLs:
            test_object._set_website(expected)
            actual = test_object._get_website()
            self.assertEqual(
                expected, actual, 
                'BaseArtisan expects a website value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadURLs:
            try:
                test_object._set_website(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'BaseArtisan._set_website should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'BaseArtisan._set_website should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    ###################################
    # Tests of class properties       #
    ###################################

    def testaddress(self):
        # Tests the address property of the BaseArtisan class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseArtisan.address.fget, 
            BaseArtisan._get_address, 
            'BaseArtisan.address is expected to use the '
            '_get_address method as its getter-method'
        )
        # - If address is not expected to be publicly settable,
        #   the second item here (BaseArtisan._set_address) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseArtisan.address.fset, 
            BaseArtisan._set_address, 
            'BaseArtisan.address is expected to use the '
            '_set_address method as its setter-method'
        )
        # - If address is not expected to be publicly deletable,
        #   the second item here (BaseArtisan._del_address) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseArtisan.address.fdel, 
            BaseArtisan._del_address, 
            'BaseArtisan.address is expected to use the '
            '_del_address method as its deleter-method'
        )

    def testcompany_name(self):
        # Tests the company_name property of the BaseArtisan class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseArtisan.company_name.fget, 
            BaseArtisan._get_company_name, 
            'BaseArtisan.company_name is expected to use the '
            '_get_company_name method as its getter-method'
        )
        # - If company_name is not expected to be publicly settable,
        #   the second item here (BaseArtisan._set_company_name) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseArtisan.company_name.fset, 
            BaseArtisan._set_company_name, 
            'BaseArtisan.company_name is expected to use the '
            '_set_company_name method as its setter-method'
        )
        # - If company_name is not expected to be publicly deletable,
        #   the second item here (BaseArtisan._del_company_name) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseArtisan.company_name.fdel, 
            BaseArtisan._del_company_name, 
            'BaseArtisan.company_name is expected to use the '
            '_del_company_name method as its deleter-method'
        )

    def testcontact_email(self):
        # Tests the contact_email property of the BaseArtisan class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseArtisan.contact_email.fget, 
            BaseArtisan._get_contact_email, 
            'BaseArtisan.contact_email is expected to use the '
            '_get_contact_email method as its getter-method'
        )
        # - If contact_email is not expected to be publicly settable,
        #   the second item here (BaseArtisan._set_contact_email) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseArtisan.contact_email.fset, 
            BaseArtisan._set_contact_email, 
            'BaseArtisan.contact_email is expected to use the '
            '_set_contact_email method as its setter-method'
        )
        # - If contact_email is not expected to be publicly deletable,
        #   the second item here (BaseArtisan._del_contact_email) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseArtisan.contact_email.fdel, 
            BaseArtisan._del_contact_email, 
            'BaseArtisan.contact_email is expected to use the '
            '_del_contact_email method as its deleter-method'
        )

    def testcontact_name(self):
        # Tests the contact_name property of the BaseArtisan class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseArtisan.contact_name.fget, 
            BaseArtisan._get_contact_name, 
            'BaseArtisan.contact_name is expected to use the '
            '_get_contact_name method as its getter-method'
        )
        # - If contact_name is not expected to be publicly settable,
        #   the second item here (BaseArtisan._set_contact_name) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseArtisan.contact_name.fset, 
            BaseArtisan._set_contact_name, 
            'BaseArtisan.contact_name is expected to use the '
            '_set_contact_name method as its setter-method'
        )
        # - If contact_name is not expected to be publicly deletable,
        #   the second item here (BaseArtisan._del_contact_name) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseArtisan.contact_name.fdel, 
            BaseArtisan._del_contact_name, 
            'BaseArtisan.contact_name is expected to use the '
            '_del_contact_name method as its deleter-method'
        )

    def testwebsite(self):
        # Tests the website property of the BaseArtisan class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseArtisan.website.fget, 
            BaseArtisan._get_website, 
            'BaseArtisan.website is expected to use the '
            '_get_website method as its getter-method'
        )
        # - If website is not expected to be publicly settable,
        #   the second item here (BaseArtisan._set_website) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseArtisan.website.fset, 
            BaseArtisan._set_website, 
            'BaseArtisan.website is expected to use the '
            '_set_website method as its setter-method'
        )
        # - If website is not expected to be publicly deletable,
        #   the second item here (BaseArtisan._del_website) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseArtisan.website.fdel, 
            BaseArtisan._del_website, 
            'BaseArtisan.website is expected to use the '
            '_del_website method as its deleter-method'
        )

#    def testproperty_name(self):
#        # Tests the property_name property of the BaseArtisan class
#        # - Assert that the getter is correct:
#        self.assertEqual(
#            BaseArtisan.property_name.fget, 
#            BaseArtisan._get_property_name, 
#            'BaseArtisan.property_name is expected to use the '
#            '_get_property_name method as its getter-method'
#        )
#        # - If property_name is not expected to be publicly settable,
#        #   the second item here (BaseArtisan._set_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the setter is correct:
#        self.assertEqual(
#            BaseArtisan.property_name.fset, 
#            BaseArtisan._set_property_name, 
#            'BaseArtisan.property_name is expected to use the '
#            '_set_property_name method as its setter-method'
#        )
#        # - If property_name is not expected to be publicly deletable,
#        #   the second item here (BaseArtisan._del_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the deleter is correct:
#        self.assertEqual(
#            BaseArtisan.property_name.fdel, 
#            BaseArtisan._del_property_name, 
#            'BaseArtisan.property_name is expected to use the '
#            '_del_property_name method as its deleter-method'
#        )

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testBaseArtisan
    )
)

class BaseCustomerDerived(BaseCustomer):
    pass

GoodCustomers = [
    BaseCustomerDerived(
        'customer name', Address('street-address', 'city')
    )
]
BadCustomers = [
    '', 'string', 1, 0, True, False, 1.0, 0.0, object(), [],
]

@testbusiness_objectsCodeCoverage.AddMethodTesting
@testbusiness_objectsCodeCoverage.AddPropertyTesting
class testBaseCustomer(unittest.TestCase):

    ###################################
    # Tests of class methods          #
    ###################################

    def test__init__(self):
        # Tests the __init__ method of the BaseCustomer class
        # - BaseCustomer is an abstract class, but has no abstract 
        #   members, so this was set up to keep it from being 
        #   accidentally used in an inappropriate fashion
        try:
            test_object = BaseCustomer(
                'customer name', Address('street-address', 'city')
            )
            self.fail(
                'BaseCustomer is expected to raise '
                'NotImplementedError if instantiated directly, '
                'but did not do so'
            )
        except NotImplementedError:
            pass
        # - Test all permutations of "good" argument-values:
        for name in GoodStandardRequiredTextLines:
            for billing_address in GoodAddresses:
                # - Testing without a shipping-address first
                test_object = BaseCustomerDerived(
                    name, billing_address
                )
                self.assertEqual(test_object.name, name)
                self.assertEqual(
                    test_object.billing_address, 
                    billing_address
                )
                for shipping_address in GoodAddresses:
                    test_object = BaseCustomerDerived(
                        name, billing_address, 
                        shipping_address
                    )
                    self.assertEqual(
                        test_object.shipping_address, 
                        shipping_address
                    )

    def test_del_billing_address(self):
        # Tests the _del_billing_address method of the BaseCustomer class
        test_object = BaseCustomerDerived('customer name', GoodAddress)
        test_object._del_billing_address()
        self.assertEqual(test_object.billing_address, None)

    def test_del_name(self):
        # Tests the _del_name method of the BaseCustomer class
        test_object = BaseCustomerDerived('customer name', GoodAddress)
        test_object._del_name()
        self.assertEqual(test_object.name, None)

    def test_del_shipping_address(self):
        # Tests the _del_shipping_address method of the BaseCustomer class
        test_object = BaseCustomerDerived('customer name', GoodAddress)
        self.assertEqual(test_object.shipping_address, None)
        test_object._shipping_address = Address('street-address', 'city')
        self.assertNotEqual(test_object.shipping_address, None)
        test_object._del_shipping_address()
        self.assertEqual(test_object.shipping_address, None)

    def test_get_billing_address(self):
        # Tests the _get_billing_address method of the BaseCustomer class
        test_object = BaseCustomerDerived('customer name', GoodAddress)
        expected = 'Any type value is OK here'
        test_object._billing_address = expected
        self.assertEqual(test_object.billing_address, expected)

    def test_get_name(self):
        # Tests the _get_name method of the BaseCustomer class
        expected = 'a test-value'
        test_object = BaseCustomerDerived(expected, GoodAddress)
        actual = test_object._get_name()
        self.assertEqual(actual, expected)
        expected = 'A longer name, different from the first one'
        test_object._name = expected
        actual = test_object._get_name()
        self.assertEqual(
            actual, expected, 
            'BaseCustomer._get_name was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_shipping_address(self):
        # Tests the _get_shipping_address method of the BaseCustomer class
        test_object = BaseCustomerDerived('customer name', GoodAddress)
        expected = 'Any type value is OK here'
        test_object._shipping_address = expected
        self.assertEqual(test_object.shipping_address, expected)

    def test_set_billing_address(self):
        # Tests the _set_billing_address method of the BaseCustomer class
        test_object = BaseCustomerDerived('customer name', GoodAddress)
        self.assertEqual(test_object.billing_address, GoodAddress)
        for expected in GoodAddresses:
            test_object._set_billing_address(expected)
            self.assertEqual(test_object.billing_address, expected)
        for value in BadAddresses:
            try:
                test_object._set_billing_address(value)
                self.fail(
                    'BaseCustomer-derived objects should not accept '
                    '"%s" (%s) as a valid billing_address value, '
                    'but it was allowed to be set' % 
                    (value, type(value).__name__)
                )
            except (TypeError,ValueError):
                pass
            except Exception as error:
                self.fail(
                    'BaseCustomer-derived objects should raise '
                    'TypeError or ValueError if passed "%s" (%s) '
                    'as a billing_address value, but %s was '
                    'raised instead:\n    %s' % 
                    (
                        value, type(value).__name__,
                        error.__class__.__name__, error
                    )
                )

    def test_set_name(self):
        # Tests the _set_name method of the BaseCustomer class
        test_object = GoodCustomers[0]
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardOptionalTextLines:
            test_object._set_name(expected)
            actual = test_object._get_name()
            self.assertEqual(
                expected, actual, 
                'BaseCustomer expects a name value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardOptionalTextLines:
            try:
                test_object._set_name(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'BaseCustomer._set_business_BaseCustomer should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                pass
            except Exception as error:
                self.fail(
                    'BaseCustomer._set_business_BaseCustomer should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_shipping_address(self):
        # Tests the _set_shipping_address method of the BaseCustomer class
        test_object = BaseCustomerDerived(
            'customer name', Address('street-address', 'city')
        )
        self.assertEqual(test_object.shipping_address, None)
        for expected in GoodAddresses:
            test_object._set_shipping_address(expected)
            self.assertEqual(test_object.shipping_address, expected)
        for value in BadAddresses:
            try:
                test_object._set_shipping_address(value)
                self.fail(
                    'BaseCustomer-derived objects should not accept '
                    '"%s" (%s) as a valid shipping_address value, '
                    'but it was allowed to be set' % 
                    (value, type(value).__name__)
                )
            except (TypeError,ValueError):
                pass
            except Exception as error:
                self.fail(
                    'BaseCustomer-derived objects should raise '
                    'TypeError or ValueError if passed "%s" (%s) '
                    'as a shipping_address value, but %s was '
                    'raised instead:\n    %s' % 
                    (
                        value, type(value).__name__,
                        error.__class__.__name__, error
                    )
                )

    ###################################
    # Tests of class properties       #
    ###################################

    def testbilling_address(self):
        # Tests the billing_address property of the BaseCustomer class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseCustomer.billing_address.fget, 
            BaseCustomer._get_billing_address, 
            'BaseCustomer.billing_address is expected to use the '
            '_get_billing_address method as its getter-method'
        )
        # - If billing_address is not expected to be publicly settable,
        #   the second item here (BaseCustomer._set_billing_address) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseCustomer.billing_address.fset, 
            BaseCustomer._set_billing_address, 
            'BaseCustomer.billing_address is expected to use the '
            '_set_billing_address method as its setter-method'
        )
        # - If billing_address is not expected to be publicly deletable,
        #   the second item here (BaseCustomer._del_billing_address) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseCustomer.billing_address.fdel, 
            BaseCustomer._del_billing_address, 
            'BaseCustomer.billing_address is expected to use the '
            '_del_billing_address method as its deleter-method'
        )

    def testname(self):
        # Tests the name property of the BaseCustomer class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseCustomer.name.fget, 
            BaseCustomer._get_name, 
            'BaseCustomer.name is expected to use the '
            '_get_name method as its getter-method'
        )
        # - If name is not expected to be publicly settable,
        #   the second item here (BaseCustomer._set_name) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseCustomer.name.fset, 
            BaseCustomer._set_name, 
            'BaseCustomer.name is expected to use the '
            '_set_name method as its setter-method'
        )
        # - If name is not expected to be publicly deletable,
        #   the second item here (BaseCustomer._del_name) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseCustomer.name.fdel, 
            BaseCustomer._del_name, 
            'BaseCustomer.name is expected to use the '
            '_del_name method as its deleter-method'
        )

    def testshipping_address(self):
        # Tests the shipping_address property of the BaseCustomer class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseCustomer.shipping_address.fget, 
            BaseCustomer._get_shipping_address, 
            'BaseCustomer.shipping_address is expected to use the '
            '_get_shipping_address method as its getter-method'
        )
        # - If shipping_address is not expected to be publicly settable,
        #   the second item here (BaseCustomer._set_shipping_address) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseCustomer.shipping_address.fset, 
            BaseCustomer._set_shipping_address, 
            'BaseCustomer.shipping_address is expected to use the '
            '_set_shipping_address method as its setter-method'
        )
        # - If shipping_address is not expected to be publicly deletable,
        #   the second item here (BaseCustomer._del_shipping_address) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseCustomer.shipping_address.fdel, 
            BaseCustomer._del_shipping_address, 
            'BaseCustomer.shipping_address is expected to use the '
            '_del_shipping_address method as its deleter-method'
        )

#    def testproperty_name(self):
#        # Tests the property_name property of the BaseCustomer class
#        # - Assert that the getter is correct:
#        self.assertEqual(
#            BaseCustomer.property_name.fget, 
#            BaseCustomer._get_property_name, 
#            'BaseCustomer.property_name is expected to use the '
#            '_get_property_name method as its getter-method'
#        )
#        # - If property_name is not expected to be publicly settable,
#        #   the second item here (BaseCustomer._set_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the setter is correct:
#        self.assertEqual(
#            BaseCustomer.property_name.fset, 
#            BaseCustomer._set_property_name, 
#            'BaseCustomer.property_name is expected to use the '
#            '_set_property_name method as its setter-method'
#        )
#        # - If property_name is not expected to be publicly deletable,
#        #   the second item here (BaseCustomer._del_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the deleter is correct:
#        self.assertEqual(
#            BaseCustomer.property_name.fdel, 
#            BaseCustomer._del_property_name, 
#            'BaseCustomer.property_name is expected to use the '
#            '_del_property_name method as its deleter-method'
#        )

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testBaseCustomer
    )
)

class BaseOrderDerived(BaseOrder):
    def add_product(self):
        pass
    def remove_product(self):
        pass

@testbusiness_objectsCodeCoverage.AddMethodTesting
@testbusiness_objectsCodeCoverage.AddPropertyTesting
class testBaseOrder(unittest.TestCase):

    ###################################
    # Tests of class methods          #
    ###################################

    def test__init__(self):
        # Tests the __init__ method of the BaseOrder class
        # - Test all permutations of "good" argument-values:
        expected = BaseCustomerDerived('customer name', GoodAddress)
        test_object = BaseOrderDerived(expected)
        self.assertEqual(test_object.customer, expected)
        for customer in GoodCustomers:
            for products in GoodProducts:
                test_object = BaseOrderDerived(customer, *products)
                self.assertEqual(test_object.customer, customer)
                if type(products) != tuple:
                    products = tuple(products)
                self.assertEqual(test_object.products, products)

    def test_del_customer(self):
        # Tests the _del_customer method of the BaseOrder class
        expected = BaseCustomerDerived('customer name', GoodAddress)
        test_object = BaseOrderDerived(expected)
        test_object._del_customer()
        self.assertEqual(test_object.customer, None)

    def test_get_customer(self):
        expected = BaseCustomerDerived('customer name', GoodAddress)
        test_object = BaseOrderDerived(expected)
        expected = 'Non-customer value is OK here'
        test_object._customer = expected
        self.assertEqual(test_object._get_customer(), expected)

    def test_set_customer(self):
        # Tests the _set_customer method of the BaseOrder class
        expected = BaseCustomerDerived('customer name', GoodAddress)
        test_object = BaseOrderDerived(expected)
        # - Test all permutations of "good" argument-values:
        for expected in GoodCustomers:
            test_object._set_customer(expected)
            self.assertEqual(test_object.customer, expected)
        # - Test all permutations of each "bad" argument-value 
        #   set against "good" values for the other arguments:
        for value in BadCustomers:
            try:
                test_object._set_customer(value)
                self.fail(
                    'BaseCustomer._set_customer should not accept '
                    '"%s" (%s) as a valid customer-value, but it '
                    'was allowed to be set' % 
                    (value, type(value).__name)
                )
            except (TypeError,ValueError):
                pass
            except Exception as error:
                self.fail(
                    'BaseCustomer._set_customer should raise '
                    'TypeError or ValueError if passed "%s" (%s) '
                    'as a customer-value, but %s was raised '
                    'instead:\n    %s' % 
                    (
                        value, type(value).__name, 
                        error.__class__.__name__, error
                    )
                )

    ###################################
    # Tests of class properties       #
    ###################################

    def testcustomer(self):
        # Tests the customer property of the BaseOrder class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseOrder.customer.fget, 
            BaseOrder._get_customer, 
            'BaseOrder.customer is expected to use the '
            '_get_customer method as its getter-method'
        )
        # - If customer is not expected to be publicly settable,
        #   the second item here (BaseOrder._set_customer) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseOrder.customer.fset, None, 
            'BaseOrder.customer is expected to be read-only, '
            'with no associated setter-method'
        )
        # - If customer is not expected to be publicly deletable,
        #   the second item here (BaseOrder._del_customer) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseOrder.customer.fdel, None, 
            'BaseOrder.customer is expected to be read-only, '
            'with no associated deleter-method'
        )

#    def testproperty_name(self):
#        # Tests the property_name property of the BaseOrder class
#        # - Assert that the getter is correct:
#        self.assertEqual(
#            BaseOrder.property_name.fget, 
#            BaseOrder._get_property_name, 
#            'BaseOrder.property_name is expected to use the '
#            '_get_property_name method as its getter-method'
#        )
#        # - If property_name is not expected to be publicly settable,
#        #   the second item here (BaseOrder._set_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the setter is correct:
#        self.assertEqual(
#            BaseOrder.property_name.fset, 
#            BaseOrder._set_property_name, 
#            'BaseOrder.property_name is expected to use the '
#            '_set_property_name method as its setter-method'
#        )
#        # - If property_name is not expected to be publicly deletable,
#        #   the second item here (BaseOrder._del_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the deleter is correct:
#        self.assertEqual(
#            BaseOrder.property_name.fdel, 
#            BaseOrder._del_property_name, 
#            'BaseOrder.property_name is expected to use the '
#            '_del_property_name method as its deleter-method'
#        )

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testBaseOrder
    )
)

class BaseProductDerived(BaseProduct):
    def __init__(self, 
        name, summary, available, store_available, 
        description=None, dimensions=None, metadata={}, 
        shipping_weight=0):
        BaseProduct.__init__(self, 
            name, summary, available, store_available, 
            description, dimensions, metadata, shipping_weight
        )

# - Since we needed this class in order to generate good product-
#   setter test-values, but it wasn't defined until now, we'll 
#   create the GoodProducts test-values here...
GoodProducts = [
    [
        BaseProductDerived('test1', 'summary1', True, True),
        BaseProductDerived('test2', 'summary2', True, True),
    ],
    (
        BaseProductDerived('test3', 'summary3', True, True),
        BaseProductDerived('test4', 'summary4', True, True),
    ),
]
BadProducts = [
    object(), 'string', 1, 1.0, True, None,
    ['list','with','invalid','values'],
    [
        BaseProductDerived('test4', 'summary4', True, True), 
        'list','with','invalid','values'
    ],
    ('tuple','with','invalid','values'),
    (
        BaseProductDerived('test4', 'summary4', True, True), 
        'tuple','with','invalid','values'
    ),
]

@testbusiness_objectsCodeCoverage.AddMethodTesting
@testbusiness_objectsCodeCoverage.AddPropertyTesting
class testBaseProduct(unittest.TestCase):

    ###################################
    # Tests of class methods          #
    ###################################

    def test__init__(self):
        # Tests the __init__ method of the BaseProduct class
        # - Test all permutations of "good" argument-values:
        name = 'name'           # - tested elsewhere
        summary = 'summary'     # - tested elsewhere
        available = True        # - tested elsewhere
        store_available = True  # - tested elsewhere
        for description in GoodStandardOptionalTextLines:
            for dimensions in GoodStandardOptionalTextLines:
                for metadata in GoodMetadataDicts:
                    for shipping_weight in GoodWeights:
                        test_object = BaseProductDerived(
                            name, summary, available, store_available, 
                            description, dimensions, metadata, 
                            shipping_weight
                        )
                        self.assertEqual(test_object.name, name)
                        self.assertEqual(test_object.summary, summary)
                        self.assertEqual(test_object.available, available)
                        self.assertEqual(test_object.store_available, store_available)
                        self.assertEqual(test_object.description, description)
                        self.assertEqual(test_object.dimensions, dimensions)
                        self.assertEqual(test_object.metadata, metadata)
                        self.assertEqual(test_object.shipping_weight, shipping_weight)

    def test_del_available(self):
        # Tests the _del_available method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        test_object._del_available()
        self.assertEqual(test_object.available, False)

    def test_del_description(self):
        # Tests the _del_description method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        test_object._description='value-type does not matter here'
        test_object._del_description()
        self.assertEqual(test_object.description, None)

    def test_del_dimensions(self):
        # Tests the _del_dimensions method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        test_object._dimensions='value-type does not matter here'
        test_object._del_dimensions()
        self.assertEqual(test_object.dimensions, None)

    def test_del_metadata(self):
        # Tests the _del_metadata method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        test_object._metadata='value-type does not matter here'
        test_object._del_metadata()
        self.assertEqual(test_object.metadata, {})

    def test_del_name(self):
        # Tests the _del_name method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        test_object._del_name()
        self.assertEqual(test_object.name, None)

    def test_del_shipping_weight(self):
        # Tests the _del_shipping_weight method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        test_object._shipping_weight='value-type does not matter here'
        test_object._del_shipping_weight()
        self.assertEqual(test_object.shipping_weight, 0)

    def test_del_store_available(self):
        # Tests the _del_store_available method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        test_object._del_store_available()
        self.assertEqual(test_object.store_available, False)

    def test_del_summary(self):
        # Tests the _del_summary method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        test_object._del_summary()
        self.assertEqual(test_object.summary, None)

    def test_get_available(self):
        # Tests the _get_available method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        expected = 'Non-boolean value is OK for this test'
        test_object._available = expected
        actual = test_object._get_available()
        self.assertEqual(
            actual, expected, 
            'BaseProduct._get_available was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )
 
    def test_get_description(self):
        # Tests the _get_description method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        expected = '3x5x2'
        test_object._description = expected
        actual = test_object._get_description()
        self.assertEqual(
            actual, expected, 
            'BaseProduct._get_description was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_dimensions(self):
        # Tests the _get_dimensions method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        expected = '3x5x2'
        test_object._dimensions = expected
        actual = test_object._get_dimensions()
        self.assertEqual(
            actual, expected, 
            'BaseProduct._get_dimensions was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_metadata(self):
        # Tests the _get_metadata method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        expected = {'spam':'eggs'}
        test_object._metadata = expected
        actual = test_object._get_metadata()
        self.assertEqual(
            actual, expected, 
            'BaseProduct._get_metadata was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_name(self):
        # Tests the _get_name method of the BaseProduct class
        expected = 'a test-value'
        test_object = BaseProductDerived(expected, 'summary', True, True)
        actual = test_object._get_name()
        self.assertEqual(actual, expected)
        expected = 'A longer name, different from the first one'
        test_object._name = expected
        actual = test_object._get_name()
        self.assertEqual(
            actual, expected, 
            'BaseProduct._get_name was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_shipping_weight(self):
        # Tests the _get_shipping_weight method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        expected = '3x5x2'
        test_object._shipping_weight = expected
        actual = test_object._get_shipping_weight()
        self.assertEqual(
            actual, expected, 
            'BaseProduct._get_shipping_weight was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_store_available(self):
        # Tests the _get_store_available method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        expected = 'Non-boolean value is OK here'
        test_object._store_available = expected
        actual = test_object._get_store_available()
        self.assertEqual(
            actual, expected, 
            'BaseProduct._get_store_available was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_summary(self):
        # Tests the _get_summary method of the BaseProduct class
        expected = 'a test-value'
        test_object = BaseProductDerived('name', expected, True, True)
        actual = test_object._get_summary()
        self.assertEqual(actual, expected)
        expected = 'A longer summary, different from the first one'
        test_object._summary = expected
        actual = test_object._get_summary()
        self.assertEqual(
            actual, expected, 
            'BaseProduct._get_summary was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_set_available(self):
        # Tests the _set_available method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        # - Test all permutations of "good" argument-values:
        for expected in GoodBooleanOrIntEquivalents:
            test_object._set_available(expected)
            actual = test_object._get_available()
            self.assertEqual(
                expected, actual, 
                'BaseProduct expects a available value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadBooleanOrIntEquivalents:
            try:
                test_object._set_available(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'BaseProduct._set_available should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'BaseProduct._set_available should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_description(self):
        # Tests the _set_description method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardOptionalTextLines:
            test_object._set_description(expected)
            actual = test_object._get_description()
            self.assertEqual(
                expected, actual, 
                'BaseProduct expects a description value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadDescriptions:
            try:
                test_object._set_description(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'BaseProduct._set_description should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'BaseProduct._set_description should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_dimensions(self):
        # Tests the _set_dimensions method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardOptionalTextLines:
            test_object._set_dimensions(expected)
            actual = test_object._get_dimensions()
            self.assertEqual(
                expected, actual, 
                'BaseProduct expects a dimensions value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardOptionalTextLines:
            try:
                test_object._set_dimensions(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'BaseProduct._set_dimensions should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'BaseProduct._set_dimensions should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_metadata(self):
        # Tests the _set_metadata method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        # - Test all permutations of "good" argument-values:
        for expected in GoodMetadataDicts:
            test_object._set_metadata(expected)
            actual = test_object._get_metadata()
            self.assertEqual(
                expected, actual, 
                'BaseProduct expects a metadata value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadMetadataDicts:
            try:
                test_object._set_metadata(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'BaseProduct._set_metadata should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'BaseProduct._set_metadata should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_name(self):
        # Tests the _set_name method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardRequiredTextLines:
            test_object._set_name(expected)
            actual = test_object._get_name()
            self.assertEqual(
                expected, actual, 
                'BaseProduct expects a name value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardRequiredTextLines:
            try:
                test_object._set_name(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'BaseProduct._set_name should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'BaseProduct._set_name should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_shipping_weight(self):
        # Tests the _set_shipping_weight method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        # - Test all permutations of "good" argument-values:
        for expected in GoodWeights:
            test_object._set_shipping_weight(expected)
            actual = test_object._get_shipping_weight()
            self.assertEqual(
                expected, actual, 
                'BaseProduct expects a shipping_weight value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadWeights:
            try:
                test_object._set_shipping_weight(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'BaseProduct._set_shipping_weight should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'BaseProduct._set_shipping_weight should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_store_available(self):
        # Tests the _set_store_available method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        # - Test all permutations of "good" argument-values:
        for expected in GoodBooleanOrIntEquivalents:
            test_object._set_store_available(expected)
            actual = test_object._get_store_available()
            self.assertEqual(
                expected, actual, 
                'BaseProduct expects a store_available value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadBooleanOrIntEquivalents:
            try:
                test_object._set_store_available(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'BaseProduct._set_store_available should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'BaseProduct._set_store_available should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_summary(self):
        # Tests the _set_summary method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardOptionalTextLines:
            test_object._set_summary(expected)
            actual = test_object._get_summary()
            self.assertEqual(
                expected, actual, 
                'BaseProduct expects a summary value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardOptionalTextLines:
            try:
                test_object._set_summary(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'BaseProduct._set_summary should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'BaseProduct._set_summary should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def testremove_metadata(self):
        # Tests the remove_metadata method of the BaseProduct class
        # - First we need sopme meadata to remove
        test_object = BaseProductDerived('name', 'summary', True, True)
        expected = {
            'materials':'wood',
            'material-names':'cherry,oak',
            'finish':'gloss'
        }
        for key in expected:
            test_object.set_metadata(key, expected[key])
        self.assertEqual(test_object.metadata, expected)
        # - Test all permutations of "good" argument-values:
        keys = list(expected.keys())
        for key in keys:
            del expected[key]
            test_object.remove_metadata(key)
            self.assertEqual(test_object.metadata, expected)

    def testset_metadata(self):
        # Tests the set_metadata method of the BaseProduct class
        test_object = BaseProductDerived('name', 'summary', True, True)
        expected = {}
        # - Test all permutations of "good" argument-values:
        for key in GoodStandardRequiredTextLines:
            value = '%s value'
            expected[key] = value
            test_object.set_metadata(key, value)
            self.assertEqual(test_object.metadata, expected)
        # - Test all permutations of each "bad" argument-value 
        #   set against "good" values for the other arguments:
        value = GoodStandardRequiredTextLines[0]
        for key in BadStandardRequiredTextLines:
            try:
                test_object.set_metadata(key, value)
                self.fail(
                    'BaseProduct.set_metadata should not allow '
                    '"%s" (%s) as a key, but it raised no error' 
                    % (key, type(key).__name__)
                )
            except (TypeError,ValueError):
                pass
            except Exception as error:
                self.fail(
                    'BaseProduct.set_metadata should raise TypeError '
                    'or ValueError if passed  "%s" (%s) as a key, '
                    'but %s was raised instead:\n    %s' % 
                    (
                        key, type(key).__name__,
                        error.__class__.__name__, error
                    )
                )
        key = GoodStandardRequiredTextLines[0]
        for value in BadStandardRequiredTextLines:
            try:
                test_object.set_metadata(key, value)
                self.fail(
                    'BaseProduct.set_metadata should not allow '
                    '"%s" (%s) as a value, but it raised no error' 
                    % (value, type(value).__name__)
                )
            except (TypeError,ValueError):
                pass
            except Exception as error:
                self.fail(
                    'BaseProduct.set_metadata should raise TypeError '
                    'or ValueError if passed  "%s" (%s) as a value, '
                    'but %s was raised instead:\n    %s' % 
                    (
                        value, type(value).__name__,
                        error.__class__.__name__, error
                    )
                )

    ###################################
    # Tests of class properties       #
    ###################################

    def testavailable(self):
        # Tests the available property of the BaseProduct class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseProduct.available.fget, 
            BaseProduct._get_available, 
            'BaseProduct.available is expected to use the '
            '_get_available method as its getter-method'
        )
        # - If available is not expected to be publicly settable,
        #   the second item here (BaseProduct._set_available) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseProduct.available.fset, 
            BaseProduct._set_available, 
            'BaseProduct.available is expected to use the '
            '_set_available method as its setter-method'
        )
        # - If available is not expected to be publicly deletable,
        #   the second item here (BaseProduct._del_available) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseProduct.available.fdel, 
            BaseProduct._del_available, 
            'BaseProduct.available is expected to use the '
            '_del_available method as its deleter-method'
        )

    def testdescription(self):
        # Tests the description property of the BaseProduct class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseProduct.description.fget, 
            BaseProduct._get_description, 
            'BaseProduct.description is expected to use the '
            '_get_description method as its getter-method'
        )
        # - If description is not expected to be publicly settable,
        #   the second item here (BaseProduct._set_description) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseProduct.description.fset, 
            BaseProduct._set_description, 
            'BaseProduct.description is expected to use the '
            '_set_description method as its setter-method'
        )
        # - If description is not expected to be publicly deletable,
        #   the second item here (BaseProduct._del_description) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseProduct.description.fdel, 
            BaseProduct._del_description, 
            'BaseProduct.description is expected to use the '
            '_del_description method as its deleter-method'
        )

    def testdimensions(self):
        # Tests the dimensions property of the BaseProduct class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseProduct.dimensions.fget, 
            BaseProduct._get_dimensions, 
            'BaseProduct.dimensions is expected to use the '
            '_get_dimensions method as its getter-method'
        )
        # - If dimensions is not expected to be publicly settable,
        #   the second item here (BaseProduct._set_dimensions) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseProduct.dimensions.fset, 
            BaseProduct._set_dimensions, 
            'BaseProduct.dimensions is expected to use the '
            '_set_dimensions method as its setter-method'
        )
        # - If dimensions is not expected to be publicly deletable,
        #   the second item here (BaseProduct._del_dimensions) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseProduct.dimensions.fdel, 
            BaseProduct._del_dimensions, 
            'BaseProduct.dimensions is expected to use the '
            '_del_dimensions method as its deleter-method'
        )

    def testmetadata(self):
        # Tests the metadata property of the BaseProduct class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseProduct.metadata.fget, 
            BaseProduct._get_metadata, 
            'BaseProduct.metadata is expected to use the '
            '_get_metadata method as its getter-method'
        )
        # - If metadata is not expected to be publicly settable,
        #   the second item here (BaseProduct._set_metadata) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseProduct.metadata.fset,None, 
            'BaseProduct.metadata is expected to be read-pnly, '
            'with no associated setter-method'
        )
        # - If metadata is not expected to be publicly deletable,
        #   the second item here (BaseProduct._del_metadata) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseProduct.metadata.fdel, None, 
            'BaseProduct.metadata is expected to be read-pnly, '
            'with no associated setter-method'
        )

    def testname(self):
        # Tests the name property of the BaseProduct class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseProduct.name.fget, 
            BaseProduct._get_name, 
            'BaseProduct.name is expected to use the '
            '_get_name method as its getter-method'
        )
        # - If name is not expected to be publicly settable,
        #   the second item here (BaseProduct._set_name) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseProduct.name.fset, 
            BaseProduct._set_name, 
            'BaseProduct.name is expected to use the '
            '_set_name method as its setter-method'
        )
        # - If name is not expected to be publicly deletable,
        #   the second item here (BaseProduct._del_name) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseProduct.name.fdel, 
            BaseProduct._del_name, 
            'BaseProduct.name is expected to use the '
            '_del_name method as its deleter-method'
        )

    def testshipping_weight(self):
        # Tests the shipping_weight property of the BaseProduct class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseProduct.shipping_weight.fget, 
            BaseProduct._get_shipping_weight, 
            'BaseProduct.shipping_weight is expected to use the '
            '_get_shipping_weight method as its getter-method'
        )
        # - If shipping_weight is not expected to be publicly settable,
        #   the second item here (BaseProduct._set_shipping_weight) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseProduct.shipping_weight.fset, 
            BaseProduct._set_shipping_weight, 
            'BaseProduct.shipping_weight is expected to use the '
            '_set_shipping_weight method as its setter-method'
        )
        # - If shipping_weight is not expected to be publicly deletable,
        #   the second item here (BaseProduct._del_shipping_weight) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseProduct.shipping_weight.fdel, 
            BaseProduct._del_shipping_weight, 
            'BaseProduct.shipping_weight is expected to use the '
            '_del_shipping_weight method as its deleter-method'
        )

    def teststore_available(self):
        # Tests the store_available property of the BaseProduct class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseProduct.store_available.fget, 
            BaseProduct._get_store_available, 
            'BaseProduct.store_available is expected to use the '
            '_get_store_available method as its getter-method'
        )
        # - If store_available is not expected to be publicly settable,
        #   the second item here (BaseProduct._set_store_available) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseProduct.store_available.fset, 
            BaseProduct._set_store_available, 
            'BaseProduct.store_available is expected to use the '
            '_set_store_available method as its setter-method'
        )
        # - If store_available is not expected to be publicly deletable,
        #   the second item here (BaseProduct._del_store_available) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseProduct.store_available.fdel, 
            BaseProduct._del_store_available, 
            'BaseProduct.store_available is expected to use the '
            '_del_store_available method as its deleter-method'
        )

    def testsummary(self):
        # Tests the summary property of the BaseProduct class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseProduct.summary.fget, 
            BaseProduct._get_summary, 
            'BaseProduct.summary is expected to use the '
            '_get_summary method as its getter-method'
        )
        # - If summary is not expected to be publicly settable,
        #   the second item here (BaseProduct._set_summary) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            BaseProduct.summary.fset, 
            BaseProduct._set_summary, 
            'BaseProduct.summary is expected to use the '
            '_set_summary method as its setter-method'
        )
        # - If summary is not expected to be publicly deletable,
        #   the second item here (BaseProduct._del_summary) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            BaseProduct.summary.fdel, 
            BaseProduct._del_summary, 
            'BaseProduct.summary is expected to use the '
            '_del_summary method as its deleter-method'
        )

#    def testproperty_name(self):
#        # Tests the property_name property of the BaseProduct class
#        # - Assert that the getter is correct:
#        self.assertEqual(
#            BaseProduct.property_name.fget, 
#            BaseProduct._get_property_name, 
#            'BaseProduct.property_name is expected to use the '
#            '_get_property_name method as its getter-method'
#        )
#        # - If property_name is not expected to be publicly settable,
#        #   the second item here (BaseProduct._set_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the setter is correct:
#        self.assertEqual(
#            BaseProduct.property_name.fset, 
#            BaseProduct._set_property_name, 
#            'BaseProduct.property_name is expected to use the '
#            '_set_property_name method as its setter-method'
#        )
#        # - If property_name is not expected to be publicly deletable,
#        #   the second item here (BaseProduct._del_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the deleter is correct:
#        self.assertEqual(
#            BaseProduct.property_name.fdel, 
#            BaseProduct._del_property_name, 
#            'BaseProduct.property_name is expected to use the '
#            '_del_property_name method as its deleter-method'
#        )

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testBaseProduct
    )
)

class HasProductsDerived(HasProducts):
    def __init__(self, *products):
        HasProducts.__init__(self, *products)
    # NOTE: These do NOT have to actually *do* anything, they 
    #       merely have to *exist* in order to allow an instance 
    #       to be created:
    def add_product(self, product):
        pass
    def remove_product(self, product):
        pass

@testbusiness_objectsCodeCoverage.AddMethodTesting
@testbusiness_objectsCodeCoverage.AddPropertyTesting
class testHasProducts(unittest.TestCase):

    ###################################
    # Tests of class methods          #
    ###################################

    def test__init__(self):
        # Tests the __init__ method of the HasProducts class
        # - Test all permutations of "good" argument-values:
        for expected in GoodProducts:
            test_object = HasProductsDerived(*expected)
            if type(expected) != tuple:
                expected = tuple(expected)
            self.assertEqual(test_object.products, expected)

    def test_del_products(self):
        # Tests the _del_products method of the HasProducts class
        test_object = HasProductsDerived()
        self.assertEqual(test_object.products, (),
            'HasProducts-derived instances are expected to return '
            'an empty tuple as a default/deleted value'
        )
        # - Test all permutations of "good" argument-values:
        test_object._set_products(GoodProducts[0])
        self.assertNotEqual(test_object.products, ())
        test_object._del_products()
        self.assertEqual(test_object.products, ())

    def test_get_products(self):
        # Tests the _get_products method of the HasProducts class
        test_object = HasProductsDerived()
        # - Test all permutations of "good" argument-values:
        expected = GoodProducts[1]
        test_object._products = expected
        self.assertEqual(test_object._get_products(), expected)

    def test_set_products(self):
        # Tests the _set_products method of the HasProducts class
        test_object = HasProductsDerived()
        # - Test all permutations of "good" argument-values:
        for expected in GoodProducts:
            test_object._set_products(expected)
            if type(expected) != tuple:
                expected = tuple(expected)
            self.assertEqual(expected, test_object._get_products())
        # - Test all permutations of each "bad" argument-value 
        #   set against "good" values for the other arguments:
        for value in BadProducts:
            try:
                test_object._set_products(value)
                self.fail(
                    'HasProducts-derived classes should not allow '
                    '"%s" (%s) as a valid products value, but it '
                    'was allowed to be set.' % 
                    (str(value), type(value).__name__)
                )
            except (TypeError, ValueError):
                pass

    ###################################
    # Tests of class properties       #
    ###################################

    def testproducts(self):
        # Tests the products property of the HasProducts class
        # - Assert that the getter is correct:
        self.assertEqual(
            HasProducts.products.fget, 
            HasProducts._get_products, 
            'HasProducts.products is expected to use the '
            '_get_products method as its getter-method'
        )
        # - If products is not expected to be publicly settable,
        #   the second item here (HasProducts._set_products) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the setter is correct:
        self.assertEqual(
            HasProducts.products.fset, None, 
            'HasProducts.products is expected to be read-only, with '
            'no associated setter-method'
        )
        # - If products is not expected to be publicly deletable,
        #   the second item here (HasProducts._del_products) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            HasProducts.products.fdel, None, 
            'HasProducts.products is expected to be read-only, with '
            'no associated deleter-method'
        )

#    def testproperty_name(self):
#        # Tests the property_name property of the HasProducts class
#        # - Assert that the getter is correct:
#        self.assertEqual(
#            HasProducts.property_name.fget, 
#            HasProducts._get_property_name, 
#            'HasProducts.property_name is expected to use the '
#            '_get_property_name method as its getter-method'
#        )
#        # - If property_name is not expected to be publicly settable,
#        #   the second item here (HasProducts._set_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the setter is correct:
#        self.assertEqual(
#            HasProducts.property_name.fset, 
#            HasProducts._set_property_name, 
#            'HasProducts.property_name is expected to use the '
#            '_set_property_name method as its setter-method'
#        )
#        # - If property_name is not expected to be publicly deletable,
#        #   the second item here (HasProducts._del_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the deleter is correct:
#        self.assertEqual(
#            HasProducts.property_name.fdel, 
#            HasProducts._del_property_name, 
#            'HasProducts.property_name is expected to use the '
#            '_del_property_name method as its deleter-method'
#        )

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testHasProducts
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
        SaveTestReport(results, 'hms_core.business_objects',
            'hms_core.business_objects.test-results')
