#!/usr/bin/env python

"""
Defines unit-tests for the module at hms_artisan.artisan_objects.
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
from random import choice
from shutil import rmtree
from uuid import uuid4, UUID

#######################################
# Third-party imports needed          #
#######################################

from hms_core.business_objects import *

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

import hms_artisan.artisan_objects as artisan_objects
from hms_artisan.artisan_objects import *

#######################################
# Constants for testing purposes      #
#######################################

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

GoodOrderItems = [
    {
        str(uuid4()):1,
    },
    {
        str(uuid4()):2,
        str(uuid4()):1,
    },
]

GoodProducts = [
    [
        Product('test1', 'summary1', True, True),
        Product('test2', 'summary2', True, True),
    ],
    (
        Product('test3', 'summary3', True, True),
        Product('test4', 'summary4', True, True),
    ),
]
BadProducts = [
    object(), 'string', 1, 1.0, True, None,
    ['list','with','invalid','values'],
    [
        Product('test4', 'summary4', True, True), 
        'list','with','invalid','values'
    ],
    ('tuple','with','invalid','values'),
    (
        Product('test4', 'summary4', True, True), 
        'tuple','with','invalid','values'
    ),
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

class testartisan_objectsCodeCoverage(ModuleCoverageTest):
    _testNamespace = 'hms_artisan'
    _testModule = artisan_objects

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testartisan_objectsCodeCoverage
   )
)

#######################################
# Test-cases in the module            #
#######################################

@testartisan_objectsCodeCoverage.AddMethodTesting
@testartisan_objectsCodeCoverage.AddPropertyTesting
class testArtisan(unittest.TestCase):

    ###################################
    # Tests of class methods          #
    ###################################

    def test__init__(self):
        # Tests the __init__ method of the Artisan class
        for contact_name in GoodStandardRequiredTextLines[0:2]:
            for contact_email in GoodEmails[0:2]:
                for address in GoodAddresses[0:2]:
                    for company_name in GoodStandardOptionalTextLines[0:2]:
                        for website in GoodURLs[0:2]:
                            test_object = Artisan(
                                contact_name=contact_name,
                                contact_email=contact_email,
                                address=address,
                                company_name=company_name,
                                website=website,
                            )
                            self.assertEqual(test_object.contact_name, contact_name)
                            self.assertEqual(test_object.contact_email, contact_email)
                            self.assertEqual(test_object.address, address)
                            self.assertEqual(test_object.company_name, company_name)
                            self.assertEqual(test_object.website, website)

    def test_del_address(self):
        # Tests the _del_address method of the Artisan class
        test_object = Artisan('name', 'me@email.com', GoodAddress)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Artisan should '
            'have is_dirty of False'
        )
        test_object._del_address()
        self.assertEqual(test_object.is_dirty, True, 
            'The deletion of an Artisan address should set '
            'is_dirty to True'
        )

    def test_del_company_name(self):
        # Tests the _del_company_name method of the Artisan class
        test_object = Artisan('name', 'me@email.com', GoodAddress)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Artisan should '
            'have is_dirty of False'
        )
        test_object._del_company_name()
        self.assertEqual(test_object.is_dirty, True, 
            'The deletion of an Artisan company_name should set '
            'is_dirty to True'
        )

    def test_del_contact_email(self):
        # Tests the _del_contact_email method of the Artisan class
        test_object = Artisan('name', 'me@email.com', GoodAddress)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Artisan should '
            'have is_dirty of False'
        )
        test_object._del_contact_email()
        self.assertEqual(test_object.is_dirty, True, 
            'The deletion of an Artisan contact_email should set '
            'is_dirty to True'
        )

    def test_del_contact_name(self):
        # Tests the _del_contact_name method of the Artisan class
        test_object = Artisan('name', 'me@email.com', GoodAddress)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Artisan should '
            'have is_dirty of False'
        )
        test_object._del_contact_name()
        self.assertEqual(test_object.is_dirty, True, 
            'The deletion of an Artisan contact_name should set '
            'is_dirty to True'
        )

    def test_del_website(self):
        # Tests the _del_website method of the Artisan class
        test_object = Artisan('name', 'me@email.com', GoodAddress)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Artisan should '
            'have is_dirty of False'
        )
        test_object._del_website()
        self.assertEqual(test_object.is_dirty, True, 
            'The deletion of an Artisan website should set '
            'is_dirty to True'
        )

    def test_set_address(self):
        # Tests the _set_address method of the Artisan class
        test_object = Artisan('name', 'me@email.com', GoodAddress)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Artisan should '
            'have is_dirty of False'
        )
        test_object._set_address(GoodAddresses[0])
        self.assertEqual(test_object.is_dirty, True, 
            'Setting an Artisan address should set '
            'is_dirty to True'
        )

    def test_set_company_name(self):
        # Tests the _set_company_name method of the Artisan class
        test_object = Artisan('name', 'me@email.com', GoodAddress)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Artisan should '
            'have is_dirty of False'
        )
        test_object._set_company_name('new_value')
        self.assertEqual(test_object.is_dirty, True, 
            'Setting an Artisan company_name should set '
            'is_dirty to True'
        )

    def test_set_contact_email(self):
        # Tests the _set_contact_email method of the Artisan class
        test_object = Artisan('name', 'me@email.com', GoodAddress)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Artisan should '
            'have is_dirty of False'
        )
        test_object._set_contact_email('me@email.com')
        self.assertEqual(test_object.is_dirty, True, 
            'Setting an Artisan contact_email should set '
            'is_dirty to True'
        )

    def test_set_contact_name(self):
        # Tests the _set_contact_name method of the Artisan class
        test_object = Artisan('name', 'me@email.com', GoodAddress)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Artisan should '
            'have is_dirty of False'
        )
        test_object._set_contact_name('new_value')
        self.assertEqual(test_object.is_dirty, True, 
            'Setting an Artisan contact_name should set '
            'is_dirty to True'
        )

    def test_set_website(self):
        # Tests the _set_website method of the Artisan class
        test_object = Artisan('name', 'me@email.com', GoodAddress)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Artisan should '
            'have is_dirty of False'
        )
        test_object._set_website('http://www.google.com')
        self.assertEqual(test_object.is_dirty, True, 
            'Setting an Artisan website should set '
            'is_dirty to True'
        )

    def testadd_product(self):
        # Tests the add_product method of the Artisan class
        test_object = Artisan('name', 'me@email.com', GoodAddress)
        self.assertEqual(test_object.products, ())
        check_list = []
        for product in GoodProducts[0]:
            test_object.add_product(product)
            check_list.append(product)
            self.assertEqual(test_object.products, tuple(check_list))
        test_object = Artisan('name', 'me@email.com', GoodAddress)
        for product in BadProducts:
            try:
                test_object.add_product(product)
                self.fail(
                    'Artisan.add_product should not allow the '
                    'addition of "%s" (%s) as a product-item, but '
                    'it was allowed' % (product, type(product).__name__)
                )
            except (TypeError, ValueError):
                pass

    def testfrom_data_dict(self):
        # Tests the from_data_dict method of the Artisan class
        self.maxDiff=None
        defaults = {
            'website':None,
            'company_name':None,
        }
        for contact_name in GoodStandardRequiredTextLines[0:2]:
            for contact_email in GoodEmails[0:2]:
                for address in GoodAddresses[0:2]:
                    # - At this point, we have all the required 
                    #   arguments, so we can start testing with 
                    #   partial expected dict-values
                    data_dict = {
                        'contact_name':contact_name,
                        'contact_email':contact_email,
                        'address':address.to_dict(),
                    }
                    test_object = Artisan.from_data_dict(data_dict)
                    actual = test_object.to_data_dict()
                    # - Create a copy of the defaults as a starting-point
                    expected = dict(defaults)
                    instance_values = {
                        'created':datetime.strftime(
                                test_object.created, 
                                test_object._data_time_string
                            ),
                        'modified':datetime.strftime(
                                test_object.modified, 
                                test_object._data_time_string
                            ),
                        'oid':str(test_object.oid),
                        'is_active':test_object.is_active,
                        'is_deleted':test_object.is_deleted,
                    }
                    expected.update(instance_values)
                    expected.update(data_dict)
                    if address:
                        expected['address'] = address.to_dict()
                    self.assertEqual(actual, expected)
                    for company_name in GoodStandardOptionalTextLines[0:2]:
                        data_dict = {
                            'contact_name':contact_name,
                            'contact_email':contact_email,
                            'address':address.to_dict(),
                            'company_name':company_name,
                        }
                        test_object = Artisan.from_data_dict(data_dict)
                        actual = test_object.to_data_dict()
                        # - Create a copy of the defaults as a starting-point
                        expected = dict(defaults)
                        instance_values = {
                            'created':datetime.strftime(
                                    test_object.created, 
                                    test_object._data_time_string
                                ),
                            'modified':datetime.strftime(
                                    test_object.modified, 
                                    test_object._data_time_string
                                ),
                            'oid':str(test_object.oid),
                            'is_active':test_object.is_active,
                            'is_deleted':test_object.is_deleted,
                        }
                        expected.update(instance_values)
                        expected.update(data_dict)
                        if address:
                            expected['address'] = address.to_dict()
                        self.assertEqual(actual, expected)
                        for website in GoodURLs[0:2]:
                            data_dict = {
                                'contact_name':contact_name,
                                'contact_email':contact_email,
                                'address':address.to_dict(),
                                'company_name':company_name,
                                'website':website,
                            }
                            test_object = Artisan.from_data_dict(data_dict)
                            actual = test_object.to_data_dict()
                            # - Create a copy of the defaults as a starting-point
                            expected = dict(defaults)
                            instance_values = {
                                'created':datetime.strftime(
                                        test_object.created, 
                                        test_object._data_time_string
                                    ),
                                'modified':datetime.strftime(
                                        test_object.modified, 
                                        test_object._data_time_string
                                    ),
                                'oid':str(test_object.oid),
                                'is_active':test_object.is_active,
                                'is_deleted':test_object.is_deleted,
                            }
                            expected.update(instance_values)
                            expected.update(data_dict)
                            if address:
                                expected['address'] = address.to_dict()
                            self.assertEqual(actual, expected)

    def test_load_objects(self):
        # Tests the _load_objects method of the Artisan class
        # - First, forcibly change Artisan._file_store_dir to a disposable 
        #   temp-directory, and clear the in-memory and on-disk stores
        Artisan._file_store_dir = '/tmp/test_artisan_objects/'
        Artisan._loaded_objects = None
        if os.path.exists(Artisan._file_store_dir):
            rmtree(Artisan._file_store_dir)
        self.assertEqual(Artisan._loaded_objects, None)
        # - Iterate through some objects, creating them and saving them.
        for contact_name in GoodStandardRequiredTextLines[0:2]:
            for contact_email in GoodEmails[0:2]:
                for address in GoodAddresses[0:2]:
                    test_object = Artisan(contact_name, contact_email, address)
                    test_object.save()
                    # - Verify that the object exists
                    #   - in memory
                    self.assertNotEqual(
                        Artisan._loaded_objects.get(test_object.oid), 
                        None
                    )
                    #   - on disk
                    file_path = '%s/Artisan-data/%s.json' % (Artisan._file_store_dir, test_object.oid)
                    self.assertTrue(
                        os.path.exists(file_path), 
                        'The file was not written at %s' % file_path
                    )
            # - Make a copy of the OIDs to check with after clearing 
            #   the in-memory copy:
            oids_before = sorted([str(key) for key in Artisan._loaded_objects.keys()])
            # - Clear the in-memory copy and verify all the oids 
            #   exist after a _load_objects is called
            Artisan._loaded_objects = None
            Artisan._load_objects()
            oids_after = sorted([str(key) for key in Artisan._loaded_objects.keys()])
            self.assertEqual(oids_before, oids_after)
        # - Delete items at random and verify deletion and load after each
        instances = list(Artisan._loaded_objects.values())
        while instances:
            target = choice(instances)
            Artisan.delete(target.oid)
            # - Verify that the object no longer exists
            #   - in memory
            self.assertEqual(
                Artisan._loaded_objects.get(str(test_object.oid)), 
                None
            )
            #   - on disk
            file_path = '%s/Artisan-data/%s.json' % (Artisan._file_store_dir, target.oid)
            self.assertFalse(
                os.path.exists(file_path), 
                'File at %s was not deleted' % file_path
            )
            # - Make a copy of the OIDs to check with after clearing 
            #   the in-memory copy:
            oids_before = sorted([str(key) for key in Artisan._loaded_objects.keys()])
            # - Clear the in-memory copy and verify all the oids 
            #   exist after a _load_objects is called
            Artisan._loaded_objects = None
            Artisan._load_objects()
            oids_after = sorted([str(key) for key in Artisan._loaded_objects.keys()])
            self.assertEqual(oids_before, oids_after)
            instances.remove(target)
        # - Clean up any remaining in-memory and on-disk store items
        Artisan._loaded_objects = None
        if os.path.exists(Artisan._file_store_dir):
            rmtree(Artisan._file_store_dir)

    def testmatches(self):
        # Tests the matches method of the Artisan class
        # - First, create an object to test against, with as complete 
        #   a data-set as we can manage
        test_object = Artisan(
            contact_name = GoodStandardRequiredTextLines[0],
            contact_email = GoodEmails[0],
            company_name = GoodStandardRequiredTextLines[0],
            address=GoodAddress,
        )
        # - Then we'll iterate over some "good" values, create criteria
        for contact_name_num in range(0,2):
            contact_name = GoodStandardRequiredTextLines[contact_name_num]
            criteria = {'contact_name':contact_name}
            expected = (contact_name == test_object.contact_name)
            self.assertEqual(expected, test_object.matches(**criteria))
            for contact_email_num in range(0,2):
                contact_email = GoodEmails[contact_email_num]
                criteria['contact_email'] = contact_email
                expected = (expected and contact_email == test_object.contact_email)
                self.assertEqual(expected, test_object.matches(**criteria))
                for company_name_num in range(0,2):
                    company_name = GoodStandardOptionalTextLines[contact_email_num]
                    criteria['company_name'] = company_name
                    expected = (expected and company_name == test_object.company_name)
                    self.assertEqual(expected, test_object.matches(**criteria))

    def testremove_product(self):
        # Tests the remove_product method of the Artisan class
        test_object = Artisan('name', 'me@email.com', GoodAddress)
        self.assertEqual(test_object.products, ())
        for product in GoodProducts[0]:
            test_object.add_product(product)
        check_list = list(test_object.products)
        while test_object.products:
            product = test_object.products[0]
            check_list.remove(product)
            test_object.remove_product(product)
            self.assertEqual(test_object.products, tuple(check_list))

    @unittest.skip(
        'Sort will be implemented once there\'s a need for it, '
        'and tested as part of that implementation'
    )
    def testsort(self):
        # Tests the sort method of the Artisan class
        # - Test all permutations of "good" argument-values:
        # - Test all permutations of each "bad" argument-value 
        #   set against "good" values for the other arguments:
        self.fail('testsort is not yet implemented')

    def testto_data_dict(self):
        # Tests the to_data_dict method of the Artisan class
        for contact_name in GoodStandardRequiredTextLines[0:2]:
            for contact_email in GoodEmails[0:2]:
                for address in GoodAddresses[0:2]:
                    # - At this point, we have all the required 
                    #   arguments, so we can start testing with 
                    #   partial expected dict-values
                    test_object = Artisan(
                        contact_name, contact_email, address,
                    )
                    expected = {
                        'contact_name':contact_name,
                        'contact_email':contact_email,
                        'address':address.to_dict(),
                        # - The balance are default values...
                        'company_name':None,
                        'website':None,
                        # - We also need to include the data-object 
                        #   items that should appear!
                        'created':datetime.strftime(
                                test_object.created, 
                                test_object._data_time_string
                            ),
                        'modified':datetime.strftime(
                                test_object.modified, 
                                test_object._data_time_string
                            ),
                        'oid':str(test_object.oid),
                        'is_active':test_object.is_active,
                        'is_deleted':test_object.is_deleted,
                    }
                    self.assertEqual(
                        test_object.to_data_dict(), expected
                    )
                    for company_name in GoodStandardOptionalTextLines[0:2]:
                        test_object = Artisan(
                            contact_name, contact_email, address,
                            company_name=company_name,
                        )
                        expected = {
                            'contact_name':contact_name,
                            'contact_email':contact_email,
                            'address':address.to_dict(),
                            # - The balance are default values...
                            'company_name':company_name,
                            'website':None,
                            # - We also need to include the data-object 
                            #   items that should appear!
                            'created':datetime.strftime(
                                    test_object.created, 
                                    test_object._data_time_string
                                ),
                            'modified':datetime.strftime(
                                    test_object.modified, 
                                    test_object._data_time_string
                                ),
                            'oid':str(test_object.oid),
                            'is_active':test_object.is_active,
                            'is_deleted':test_object.is_deleted,
                        }
                        self.assertEqual(
                            test_object.to_data_dict(), expected
                        )

    ###################################
    # Tests of class properties       #
    ###################################

    def testaddress(self):
        # Tests the address property of the Artisan class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseArtisan.address.fget, 
            Artisan._get_address, 
            'Artisan.address is expected to use the '
            'BaseArtisan._get_address method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Artisan.address.fset, 
            Artisan._set_address, 
            'Artisan.address is expected to use the '
            '_set_address method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Artisan.address.fdel, 
            Artisan._del_address, 
            'Artisan.address is expected to use the '
            '_del_address method as its deleter-method'
        )

    def testcompany_name(self):
        # Tests the company_name property of the Artisan class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseArtisan.company_name.fget, 
            Artisan._get_company_name, 
            'Artisan.company_name is expected to use the '
            'BaseArtisan._get_company_name method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Artisan.company_name.fset, 
            Artisan._set_company_name, 
            'Artisan.company_name is expected to use the '
            '_set_company_name method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Artisan.company_name.fdel, 
            Artisan._del_company_name, 
            'Artisan.company_name is expected to use the '
            '_del_company_name method as its deleter-method'
        )

    def testcontact_email(self):
        # Tests the contact_email property of the Artisan class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseArtisan.contact_email.fget, 
            Artisan._get_contact_email, 
            'Artisan.contact_email is expected to use the '
            'BaseArtisan._get_contact_email method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Artisan.contact_email.fset, 
            Artisan._set_contact_email, 
            'Artisan.contact_email is expected to use the '
            '_set_contact_email method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Artisan.contact_email.fdel, 
            Artisan._del_contact_email, 
            'Artisan.contact_email is expected to use the '
            '_del_contact_email method as its deleter-method'
        )

    def testcontact_name(self):
        # Tests the contact_name property of the Artisan class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseArtisan.contact_name.fget, 
            Artisan._get_contact_name, 
            'Artisan.contact_name is expected to use the '
            'BaseArtisan._get_contact_name method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Artisan.contact_name.fset, 
            Artisan._set_contact_name, 
            'Artisan.contact_name is expected to use the '
            '_set_contact_name method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Artisan.contact_name.fdel, 
            Artisan._del_contact_name, 
            'Artisan.contact_name is expected to use the '
            '_del_contact_name method as its deleter-method'
        )

    def testwebsite(self):
        # Tests the website property of the Artisan class
        # - Assert that the getter is correct:
        self.assertEqual(
            BaseArtisan.website.fget, 
            Artisan._get_website, 
            'Artisan.website is expected to use the '
            'BaseArtisan._get_website method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Artisan.website.fset, 
            Artisan._set_website, 
            'Artisan.website is expected to use the '
            '_set_website method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Artisan.website.fdel, 
            Artisan._del_website, 
            'Artisan.website is expected to use the '
            '_del_website method as its deleter-method'
        )

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testArtisan
    )
)

@testartisan_objectsCodeCoverage.AddMethodTesting
@testartisan_objectsCodeCoverage.AddPropertyTesting
class testOrder(unittest.TestCase):

    ###################################
    # Tests of class methods          #
    ###################################

    def test__init__(self):
        # Tests the __init__ method of the Order class
        for name in GoodStandardRequiredTextLines[0:2]:
            for street_address in GoodStandardRequiredTextLines[0:2]:
                for city in GoodStandardRequiredTextLines[0:2]:
                    for items in GoodOrderItems:
                        for building_address in GoodStandardOptionalTextLines[0:2]:
                            for region in GoodStandardOptionalTextLines[0:2]:
                                for postal_code in GoodStandardOptionalTextLines[0:2]:
                                    for country in GoodStandardOptionalTextLines[0:2]:
                                        test_object = Order(
                                            name=name, 
                                            street_address=street_address, 
                                            city=city, 
                                            items=items, 
                                            building_address=building_address, 
                                            region=region, 
                                            postal_code=postal_code, 
                                            country=country
                                        )
                                        expected_items = dict(
                                            [
                                                (str(oid), items[oid])
                                                for oid in items
                                            ]
                                        )
                                        actual_items = dict(
                                            [
                                                (str(oid), test_object.items[oid])
                                                for oid in test_object.items
                                            ]
                                        )
                                        self.assertEqual(test_object.name, name)
                                        self.assertEqual(test_object.street_address, street_address)
                                        self.assertEqual(test_object.city, city)
                                        self.assertEqual(expected_items, actual_items)
                                        self.assertEqual(test_object.building_address, building_address)
                                        self.assertEqual(test_object.region, region)
                                        self.assertEqual(test_object.postal_code, postal_code)
                                        self.assertEqual(test_object.country, country)

    def test_del_building_address(self):
        # Tests the _del_building_address method of the Order class
        test_object = Order('name', 'street_address', 'city')
        self.assertEqual(
            test_object.building_address, None, 
            'An Order object is expected to have None as its default '
            'building_address value if no value was provided'
        )
        # - Hard-set the storage-property's value, call the 
        #   deleter-method, and assert that it's what's expected 
        #   afterwards:
        test_object._set_is_dirty(False)
        test_object._building_address = 'a test value'
        test_object._del_building_address()
        self.assertEqual(
            test_object.building_address, None, 
            'An Order object is expected to have None as its '
            'building_address value after the deleter is called'
        )
        self.assertTrue(test_object.is_dirty,
            'Deleting Order.building_address should set is_dirty to True'
        )

    def test_del_city(self):
        # Tests the _del_city method of the Order class
        expected = 'city'
        test_object = Order('street address', 'street_address', expected)
        self.assertEqual(
            test_object.city, expected, 
            'An Order object is expected to have "%s" (%s) as its '
            'current city value, since that value was provided' % 
            (expected, type(expected).__name__)
        )
        # - Since we have a value, just call the deleter-method, and 
        #   assert that it's what's expected afterwards:
        test_object._set_is_dirty(False)
        test_object._del_city()
        self.assertEqual(
            test_object.city, None, 
            'An Order object is expected to have None as its '
            'city value after the deleter is called'
        )
        self.assertTrue(test_object.is_dirty,
            'Deleting Order.city should set is_dirty to True'
        )

    def test_del_country(self):
        # Tests the _del_country method of the Order class
        test_object = Order('name', 'street_address', 'city')
        self.assertEqual(
            test_object.country, None, 
            'An Order object is expected to have None as its default '
            'country value if no value was provided'
        )
        # - Hard-set the storage-property's value, call the 
        #   deleter-method, and assert that it's what's expected 
        #   afterwards:
        test_object._set_is_dirty(False)
        test_object._country = 'a test value'
        test_object._del_country()
        self.assertEqual(
            test_object.country, None, 
            'An Order object is expected to have None as its '
            'country value after the deleter is called'
        )
        self.assertTrue(test_object.is_dirty,
            'Deleting Order.country should set is_dirty to True'
        )

    def test_del_items(self):
        # Tests the _del_items method of the Order class
        test_object = Order('name', 'street_address', 'city')
        self.assertEqual(
            test_object.items, {}, 
            'An Order object is expected to have {} as its default '
            'postal_code value if no value was provided'
        )
        # - Hard-set the storage-property's value, call the 
        #   deleter-method, and assert that it's what's expected 
        #   afterwards:
        test_object._set_is_dirty(False)
        test_object._items = 'a test value'
        test_object._del_items()
        self.assertEqual(
            test_object.items, {}, 
            'An Order object is expected to have {} as its '
            'postal_code value after the deleter is called'
        )
        self.assertTrue(test_object.is_dirty,
            'Deleting Order.items should set is_dirty to True'
        )

    def test_del_name(self):
        # Tests the _del_name method of the Order class
        expected = 'test-value'
        test_object = Order(expected, 'street_address', 'city')
        self.assertEqual(
            test_object.name, expected, 
            'An Order object is expected to have None as its default '
            'name value if no value was provided'
        )
        # - Hard-set the storage-property's value, call the 
        #   deleter-method, and assert that it's what's expected 
        #   afterwards:
        test_object._set_is_dirty(False)
        test_object._name = 'A different test-value'
        test_object._del_name()
        self.assertEqual(
            test_object.name, None, 
            'An Order object is expected to have None as its '
            'name value after the deleter is called'
        )
        self.assertTrue(test_object.is_dirty,
            'Deleting Order.name should set is_dirty to True'
        )

    def test_del_postal_code(self):
        # Tests the _del_postal_code method of the Order class
        test_object = Order('name', 'street_address', 'city')
        self.assertEqual(
            test_object.postal_code, None, 
            'An Order object is expected to have None as its default '
            'postal_code value if no value was provided'
        )
        # - Hard-set the storage-property's value, call the 
        #   deleter-method, and assert that it's what's expected 
        #   afterwards:
        test_object._set_is_dirty(False)
        test_object._postal_code = 'a test value'
        test_object._del_postal_code()
        self.assertEqual(
            test_object.postal_code, None, 
            'An Order object is expected to have None as its '
            'postal_code value after the deleter is called'
        )
        self.assertTrue(test_object.is_dirty,
            'Deleting Order.postal_code should set is_dirty to True'
        )

    def test_del_region(self):
        # Tests the _del_region method of the Order class
        test_object = Order('name', 'street_address', 'city')
        self.assertEqual(
            test_object.region, None, 
            'An Order object is expected to have None as its default '
            'region value if no value was provided'
        )
        # - Hard-set the storage-property's value, call the 
        #   deleter-method, and assert that it's what's expected 
        #   afterwards:
        test_object._set_is_dirty(False)
        test_object._region = 'a test value'
        test_object._del_region()
        self.assertEqual(
            test_object.region, None, 
            'An Order object is expected to have None as its '
            'region value after the deleter is called'
        )
        self.assertTrue(test_object.is_dirty,
            'Deleting Order.region should set is_dirty to True'
        )

    def test_del_street_address(self):
        # Tests the _del_street_address method of the Order class
        expected = 'street_address'
        test_object = Order(expected, 'street_address', 'city')
        self.assertEqual(
            test_object.street_address, expected, 
            'An Order object is expected to have "%s" (%s) as its '
            'curent street_address value, since that value was '
            'provided' % (expected, type(expected).__name__)
        )
        # - Since we have a value, just call the deleter-method, and 
        #   assert that it's what's expected afterwards:
        test_object._set_is_dirty(False)
        test_object._del_street_address()
        self.assertEqual(
            test_object.street_address, None, 
            'An Order object is expected to have None as its '
            'street_address value after the deleter is called'
        )
        self.assertTrue(test_object.is_dirty,
            'Deleting Order.street_address should set is_dirty to True'
        )

    def test_get_building_address(self):
        # Tests the _get_building_address method of the Order class
        test_object = Order('name', 'street_address', 'city')
        expected = 'a test-value'
        test_object._building_address = expected
        actual = test_object._get_building_address()
        self.assertEqual(
            actual, expected, 
            'Order._get_building_address was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_city(self):
        # Tests the _get_city method of the Order class
        test_object = Order('name', 'street_address', 'city')
        expected = 'a test-value'
        test_object._city = expected
        actual = test_object._get_city()
        self.assertEqual(
            actual, expected, 
            'Order._get_city was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_country(self):
        # Tests the _get_country method of the Order class
        test_object = Order('name', 'street_address', 'city')
        expected = 'a test-value'
        test_object._country = expected
        actual = test_object._get_country()
        self.assertEqual(
            actual, expected, 
            'Order._get_country was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_items(self):
        # Tests the _get_items method of the Order class
        test_object = Order('name', 'street_address', 'city')
        expected = {}
        test_object._items = expected
        actual = test_object._get_items()
        self.assertEqual(
            actual, expected, 
            'Order._get_items was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_name(self):
        # Tests the _get_name method of the Order class
        expected = 'a test-value'
        test_object = Order(expected, 'street_address', 'city')
        actual = test_object._get_name()
        self.assertEqual(actual, expected)
        expected = 'A longer name, different from the first one'
        test_object._name = expected
        actual = test_object._get_name()
        self.assertEqual(
            actual, expected, 
            'Order._get_name was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_postal_code(self):
        # Tests the _get_postal_code method of the Order class
        test_object = Order('name', 'street_address', 'city')
        expected = 'a test-value'
        test_object._postal_code = expected
        actual = test_object._get_postal_code()
        self.assertEqual(
            actual, expected, 
            'Order._get_postal_code was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_region(self):
        # Tests the _get_region method of the Order class
        test_object = Order('name', 'street_address', 'city')
        expected = 'a test-value'
        test_object._region = expected
        actual = test_object._get_region()
        self.assertEqual(
            actual, expected, 
            'Order._get_region was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_get_street_address(self):
        # Tests the _get_street_address method of the Order class
        test_object = Order('name', 'street_address', 'city')
        expected = 'a test-value'
        test_object._street_address = expected
        actual = test_object._get_street_address()
        self.assertEqual(
            actual, expected, 
            'Order._get_street_address was expected to return '
            '"%s" (%s), but returned "%s" (%s) instead' % 
            (
                expected, type(expected).__name__,
                actual, type(actual).__name__,
            )
        )

    def test_load_objects(self):
        # Tests the _load_objects method of the Order class
        # - First, forcibly change Order._file_store_dir to a disposable 
        #   temp-directory, and clear the in-memory and on-disk stores
        Order._file_store_dir = '/tmp/test_artisan_objects/'
        Order._loaded_objects = None
        if os.path.exists(Order._file_store_dir):
            rmtree(Order._file_store_dir)
        self.assertEqual(Order._loaded_objects, None)
        # - Iterate through some objects, creating them and saving them.
        for name in GoodStandardRequiredTextLines[0:2]:
            for street_address in GoodStandardRequiredTextLines[0:2]:
                for city in GoodStandardRequiredTextLines[0:2]:
                    test_object = Order(name, street_address, city)
                    test_object.save()
                    # - Verify that the object exists
                    #   - in memory
                    self.assertNotEqual(
                        Order._loaded_objects.get(test_object.oid),
                        None
                    )
                    #   - on disk
                    file_path = '%s/Order-data/%s.json' % (Order._file_store_dir, test_object.oid)
                    self.assertTrue(
                        os.path.exists(file_path), 
                        'The file was not written at %s' % file_path
                    )
            # - Make a copy of the OIDs to check with after clearing 
            #   the in-memory copy:
            oids_before = sorted([str(key) for key in Order._loaded_objects.keys()])
            # - Clear the in-memory copy and verify all the oids 
            #   exist after a _load_objects is called
            Order._loaded_objects = None
            Order._load_objects()
            oids_after = sorted([str(key) for key in Order._loaded_objects.keys()])
            self.assertEqual(oids_before, oids_after)
        # - Delete items at random and verify deletion and load after each
        instances = list(Order._loaded_objects.values())
        while instances:
            target = choice(instances)
            Order.delete(target.oid)
            # - Verify that the object no longer exists
            #   - in memory
            self.assertEqual(
                Order._loaded_objects.get(str(test_object.oid)), 
                None
            )
            #   - on disk
            file_path = '%s/Order-data/%s.json' % (Order._file_store_dir, target.oid)
            self.assertFalse(
                os.path.exists(file_path), 
                'File at %s was not deleted' % file_path
            )
            # - Make a copy of the OIDs to check with after clearing 
            #   the in-memory copy:
            oids_before = sorted([str(key) for key in Order._loaded_objects.keys()])
            # - Clear the in-memory copy and verify all the oids 
            #   exist after a _load_objects is called
            Order._loaded_objects = None
            Order._load_objects()
            oids_after = sorted([str(key) for key in Order._loaded_objects.keys()])
            self.assertEqual(oids_before, oids_after)
            instances.remove(target)
        # - Clean up any remaining in-memory and on-disk store items
        Order._loaded_objects = None
        if os.path.exists(Order._file_store_dir):
            rmtree(Order._file_store_dir)

    def test_set_building_address(self):
        # Tests the _set_building_address method of the Order class
        # - Create an object to test with:
        test_object = Order('name', 'street_address', 'city')
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardOptionalTextLines:
            test_object._set_building_address(expected)
            actual = test_object._get_building_address()
            self.assertEqual(
                expected, actual, 
                'Order expects a building_address value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test is_dirty after a set
        test_object._set_is_dirty(False)
        test_object._set_building_address(GoodStandardOptionalTextLines[1])
        self.assertTrue(test_object.is_dirty,
            'Setting a new value in Order.business_address should '
            'also set the instance\'s is_dirty to True'
        )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardOptionalTextLines:
            try:
                test_object._set_building_address(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'Order._set_business_address should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'Order._set_business_address should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_city(self):
        # Tests the _set_city method of the Order class
        # - Create an object to test with:
        test_object = Order('name', 'street_address', 'city')
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardRequiredTextLines:
            test_object._set_city(expected)
            actual = test_object._get_city()
            self.assertEqual(
                expected, actual, 
                'Order expects a city value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test is_dirty after a set
        test_object._set_is_dirty(False)
        test_object._set_city(GoodStandardRequiredTextLines[1])
        self.assertTrue(test_object.is_dirty,
            'Setting a new value in Order.city should '
            'also set the instance\'s is_dirty to True'
        )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardRequiredTextLines:
            try:
                test_object._set_city(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'Order._set_business_address should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'Order._set_business_address should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_country(self):
        # Tests the _set_country method of the Order class
        # - Create an object to test with:
        test_object = Order('name', 'street_address', 'city')
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardOptionalTextLines:
            test_object._set_country(expected)
            actual = test_object._get_country()
            self.assertEqual(
                expected, actual, 
                'Order expects a country value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test is_dirty after a set
        test_object._set_is_dirty(False)
        test_object._set_country(GoodStandardRequiredTextLines[1])
        self.assertTrue(test_object.is_dirty,
            'Setting a new value in Order.country should '
            'also set the instance\'s is_dirty to True'
        )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardOptionalTextLines:
            try:
                test_object._set_country(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'Order._set_business_address should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'Order._set_business_address should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    # - Noteworty on text because of the type-changes
    def test_set_items(self):
        # Tests the _set_items method of the Order class
        test_object = Order('name', 'street_address', 'city')
        items = dict(
            (oid if type(oid)==UUID else UUID(oid), 2) 
            for oid in GoodOIDs
        )
        # - Test is_dirty after a set
        test_object._set_is_dirty(False)
        test_object._set_items(items)
        self.assertTrue(test_object.is_dirty,
            'Setting a new value in Order.items should '
            'also set the instance\'s is_dirty to True'
        )
        self.assertEqual(test_object.items, items)
        test_object = Order('name', 'street_address', 'city', 
            items=items
        )
        self.assertEqual(test_object.items, items)

    def test_set_name(self):
        # Tests the _set_name method of the Order class
        test_object = Order('name', 'street_address', 'city')
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardRequiredTextLines:
            test_object._set_name(expected)
            self.assertEqual(test_object.name, expected)
        # - Test is_dirty after a set
        test_object._set_is_dirty(False)
        test_object._set_name(GoodStandardRequiredTextLines[1])
        self.assertTrue(test_object.is_dirty,
            'Setting a new value in Order.name should '
            'also set the instance\'s is_dirty to True'
        )
        # - Test all permutations of each "bad" argument-value 
        #   set against "good" values for the other arguments:
        for name in BadStandardRequiredTextLines:
            try:
                test_object._set_name(name)
                self.fail(
                    'Order should not accept "%s" (%s) as a valid '
                    'name, but it was allowed to be set' % 
                    (name, type(name).__name__)
                )
            except (TypeError, ValueError):
                pass

    def test_set_postal_code(self):
        # Tests the _set_postal_code method of the Order class
        # - Create an object to test with:
        test_object = Order('name', 'street_address', 'city')
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardOptionalTextLines:
            test_object._set_postal_code(expected)
            actual = test_object._get_postal_code()
            self.assertEqual(
                expected, actual, 
                'Order expects a postal_code value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test is_dirty after a set
        test_object._set_is_dirty(False)
        test_object._set_postal_code(GoodStandardRequiredTextLines[1])
        self.assertTrue(test_object.is_dirty,
            'Setting a new value in Order.postal_code should '
            'also set the instance\'s is_dirty to True'
        )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardOptionalTextLines:
            try:
                test_object._set_postal_code(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'Order._set_business_address should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'Order._set_business_address should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_region(self):
        # Tests the _set_region method of the Order class
        # - Create an object to test with:
        test_object = Order('name', 'street_address', 'city')
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardOptionalTextLines:
            test_object._set_region(expected)
            actual = test_object._get_region()
            self.assertEqual(
                expected, actual, 
                'Order expects a region value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test is_dirty after a set
        test_object._set_is_dirty(False)
        test_object._set_region(GoodStandardRequiredTextLines[1])
        self.assertTrue(test_object.is_dirty,
            'Setting a new value in Order.region should '
            'also set the instance\'s is_dirty to True'
        )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardOptionalTextLines:
            try:
                test_object._set_region(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'Order._set_business_address should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'Order._set_business_address should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def test_set_street_address(self):
        # Tests the _set_street_address method of the Order class
        # - Create an object to test with:
        test_object = Order('name', 'street_address', 'city')
        # - Test all permutations of "good" argument-values:
        for expected in GoodStandardRequiredTextLines:
            test_object._set_street_address(expected)
            actual = test_object._get_street_address()
            self.assertEqual(
                expected, actual, 
                'Order expects a street_address value set to '
                '"%s" (%s) to be retrieved with a corresponding '
                'getter-method call, but "%s" (%s) was returned '
                'instead' % 
                (
                    expected, type(expected).__name__, 
                    actual, type(actual).__name__, 
                )
            )
        # - Test is_dirty after a set
        test_object._set_is_dirty(False)
        test_object._set_country(GoodStandardRequiredTextLines[1])
        self.assertTrue(test_object.is_dirty,
            'Setting a new value in Order.country should '
            'also set the instance\'s is_dirty to True'
        )
        # - Test all permutations of "bad" argument-values:
        for value in BadStandardRequiredTextLines:
            try:
                test_object._set_street_address(value)
                # - If this setter-call succeeds, that's a 
                #   test-failure!
                self.fail(
                    'Order._set_business_address should raise '
                    'TypeError or ValueError if passed "%s" (%s), '
                    'but it was allowed to be set instead.' % 
                    (value, type(value).__name__)
                )
            except (TypeError, ValueError):
                # - This is expected, so it passes
                pass
            except Exception as error:
                self.fail(
                    'Order._set_business_address should raise '
                    'TypeError or ValueError if passed an invalid '
                    'value, but %s was raised instead: %s.' % 
                    (error.__class__.__name__, error)
                )

    def testfrom_data_dict(self):
        # Tests the from_data_dict method of the Order class
        defaults = {
            'building_address':None,
            'region':None,
            'postal_code':None,
            'country':None,
            'items':{},
        }
        for name in GoodStandardRequiredTextLines[0:2]:
            for street_address in GoodStandardRequiredTextLines[0:2]:
                for city in GoodStandardRequiredTextLines[0:2]:
                    # - At this point, we have all the required 
                    #   arguments, so we can start testing with 
                    #   partial expected dict-values
                    data_dict = {
                        'name':name,
                        'street_address':street_address,
                        'city':city,
                    }
                    test_object = Order.from_data_dict(data_dict)
                    actual = test_object.to_data_dict()
                    # - Create a copy of the defaults as a starting-point
                    expected = dict(defaults)
                    instance_values = {
                        'created':datetime.strftime(
                                test_object.created, 
                                test_object._data_time_string
                            ),
                        'modified':datetime.strftime(
                                test_object.modified, 
                                test_object._data_time_string
                            ),
                        'oid':str(test_object.oid),
                        'is_active':test_object.is_active,
                        'is_deleted':test_object.is_deleted,
                    }
                    expected.update(instance_values)
                    expected.update(data_dict)
                    self.assertEqual(expected, actual)
                    for items in GoodOrderItems:
                        # - Same structure as above, but adding items
                        data_dict = {
                            'name':name,
                            'street_address':street_address,
                            'city':city,
                            'items':items,
                        }
                        test_object = Order.from_data_dict(data_dict)
                        actual = test_object.to_data_dict()
                        expected = dict(defaults)
                        instance_values = {
                            'created':datetime.strftime(
                                    test_object.created, 
                                    test_object._data_time_string
                                ),
                            'modified':datetime.strftime(
                                    test_object.modified, 
                                    test_object._data_time_string
                                ),
                            'oid':str(test_object.oid),
                            'is_active':test_object.is_active,
                            'is_deleted':test_object.is_deleted,
                        }
                        expected.update(instance_values)
                        expected.update(data_dict)
                        self.assertEqual(expected, actual)
                        for building_address in GoodStandardOptionalTextLines[0:2]:
                            data_dict = {
                                'name':name,
                                'street_address':street_address,
                                'city':city,
                                'items':items,
                                'building_address':building_address,
                            }
                            test_object = Order.from_data_dict(data_dict)
                            actual = test_object.to_data_dict()
                            expected = dict(defaults)
                            instance_values = {
                                'created':datetime.strftime(
                                        test_object.created, 
                                        test_object._data_time_string
                                    ),
                                'modified':datetime.strftime(
                                        test_object.modified, 
                                        test_object._data_time_string
                                    ),
                                'oid':str(test_object.oid),
                                'is_active':test_object.is_active,
                                'is_deleted':test_object.is_deleted,
                            }
                            expected.update(instance_values)
                            expected.update(data_dict)
                            self.assertEqual(expected, actual)
                            for region in GoodStandardOptionalTextLines[0:2]:
                                data_dict = {
                                    'name':name,
                                    'street_address':street_address,
                                    'city':city,
                                    'items':items,
                                    'building_address':building_address,
                                    'region':region,
                                }
                                test_object = Order.from_data_dict(data_dict)
                                actual = test_object.to_data_dict()
                                expected = dict(defaults)
                                instance_values = {
                                    'created':datetime.strftime(
                                            test_object.created, 
                                            test_object._data_time_string
                                        ),
                                    'modified':datetime.strftime(
                                            test_object.modified, 
                                            test_object._data_time_string
                                        ),
                                    'oid':str(test_object.oid),
                                    'is_active':test_object.is_active,
                                    'is_deleted':test_object.is_deleted,
                                }
                                expected.update(instance_values)
                                expected.update(data_dict)
                                self.assertEqual(expected, actual)
                                for postal_code in GoodStandardOptionalTextLines[0:2]:
                                    data_dict = {
                                        'name':name,
                                        'street_address':street_address,
                                        'city':city,
                                        'items':items,
                                        'building_address':building_address,
                                        'region':region,
                                        'postal_code':postal_code,
                                    }
                                    test_object = Order.from_data_dict(data_dict)
                                    actual = test_object.to_data_dict()
                                    expected = dict(defaults)
                                    instance_values = {
                                        'created':datetime.strftime(
                                                test_object.created, 
                                                test_object._data_time_string
                                            ),
                                        'modified':datetime.strftime(
                                                test_object.modified, 
                                                test_object._data_time_string
                                            ),
                                        'oid':str(test_object.oid),
                                        'is_active':test_object.is_active,
                                        'is_deleted':test_object.is_deleted,
                                    }
                                    expected.update(instance_values)
                                    expected.update(data_dict)
                                    self.assertEqual(expected, actual)
                                    for country in GoodStandardOptionalTextLines[0:2]:
                                        data_dict = {
                                            'name':name,
                                            'street_address':street_address,
                                            'city':city,
                                            'items':items,
                                            'building_address':building_address,
                                            'region':region,
                                            'postal_code':postal_code,
                                            'country':country,
                                        }
                                        test_object = Order.from_data_dict(data_dict)
                                        actual = test_object.to_data_dict()
                                        expected = dict(defaults)
                                        instance_values = {
                                            'created':datetime.strftime(
                                                    test_object.created, 
                                                    test_object._data_time_string
                                                ),
                                            'modified':datetime.strftime(
                                                    test_object.modified, 
                                                    test_object._data_time_string
                                                ),
                                            'oid':str(test_object.oid),
                                            'is_active':test_object.is_active,
                                            'is_deleted':test_object.is_deleted,
                                        }
                                        expected.update(instance_values)
                                        expected.update(data_dict)
                                        self.assertEqual(expected, actual)

    def testmatches(self):
        # Tests the matches method of the Order class
        # - First, create an object to test against, with as complete 
        #   a data-set as we can manage
        test_object = Order(
            name = GoodStandardRequiredTextLines[0],
            street_address = GoodStandardRequiredTextLines[0],
            city = GoodStandardRequiredTextLines[0],
            building_address = GoodStandardOptionalTextLines[0],
            region = GoodStandardOptionalTextLines[0],
            postal_code = GoodStandardOptionalTextLines[0],
            country = GoodStandardOptionalTextLines[0],
        )
        # - Then we'll iterate over some "good" values, create criteria
        for name_num in range(0,2):
            name = GoodStandardRequiredTextLines[name_num]
            criteria = {'name':name}
            expected = (name == test_object.name)
            self.assertEqual(expected, test_object.matches(**criteria))
            for str_addr_num in range(0,2):
                street_address = GoodStandardRequiredTextLines[str_addr_num]
                criteria['street_address'] = street_address
                expected = (expected and street_address == test_object.street_address)
                self.assertEqual(expected, test_object.matches(**criteria))
                for city_num in range(0,2):
                    city = GoodStandardRequiredTextLines[city_num]
                    criteria['city'] = city
                    expected = (expected and city == test_object.city)
                    self.assertEqual(expected, test_object.matches(**criteria))
                    for bldg_addr_num in range(0,2):
                        building_address = GoodStandardOptionalTextLines[bldg_addr_num]
                        criteria['building_address'] = building_address
                        expected = (expected and building_address == test_object.building_address)
                        self.assertEqual(expected, test_object.matches(**criteria))
                        for region_num in range(0,2):
                            region = GoodStandardOptionalTextLines[region_num]
                            criteria['region'] = region
                            expected = (expected and region == test_object.region)
                            self.assertEqual(expected, test_object.matches(**criteria))
                            for pc_num in range(0,2):
                                postal_code=GoodStandardOptionalTextLines[pc_num]
                                criteria['postal_code'] = postal_code
                                expected = (expected and postal_code == test_object.postal_code)
                                self.assertEqual(expected, test_object.matches(**criteria))
                                for cntry_num in range(0,2):
                                    country=GoodStandardOptionalTextLines[cntry_num]
                                    criteria['country'] = country
                                    expected = (expected and country == test_object.country)
                                    self.assertEqual(expected, test_object.matches(**criteria))

    ##########
    # - Noteworthy in book because of type-conversion, similar to 
    #   others in previous tests?
    def testset_item_quantity(self):
        # Tests the set_item_quantity method of the Order class
        test_object = Order('name', 'street_address', 'city')
        # - Test all permutations of "good" argument-values:
        expected = {}
        for oid in GoodOIDs:
            for quantity in [1,2,3]:
                if type(oid) == str:
                    expected[UUID(oid)] = quantity
                else:
                    expected[oid] = quantity
                test_object.set_item_quantity(oid, quantity)
                self.assertEqual(test_object.items, expected)
        oid = list(expected.keys())[0]
        del expected[oid]
        test_object.set_item_quantity(oid, 0)
        self.assertEqual(test_object.items, expected)
        # - Test all permutations of each "bad" argument-value 
        #   set against "good" values for the other arguments:
        oid = GoodOIDs[-1]
        for quantity in [-1, '', object(), True, False]:
            try:
                test_object.set_item_quantity(oid, quantity)
                self.fail(
                    'Order.set_item_quantity should not accept '
                    '"%s" (%s) as a valid quantity, but it was '
                    'allowed to be set' % 
                    (quantity, type(quantity).__name__)
                )
            except (TypeError, ValueError):
                pass
        quantity = 1
        for oid in BadOIDs:
            try:
                test_object.set_item_quantity(oid, quantity)
                self.fail(
                    'Order.set_item_quantity should not accept '
                    '"%s" (%s) as a valid oid, but it was '
                    'allowed to be set' % 
                    (oid, type(oid).__name__)
                )
            except (TypeError, ValueError):
                pass

    @unittest.skip(
        'Sort will be implemented once there\'s a need for it, '
        'and tested as part of that implementation'
    )
    def testsort(self):
        # Tests the sort method of the Order class
        # - Test all permutations of "good" argument-values:
        # - Test all permutations of each "bad" argument-value 
        #   set against "good" values for the other arguments:
        self.fail('testsort is not yet implemented')

    def teststandard_address(self):
        # Tests the standard_address method of the Order class
        # - Test all permutations of "good" argument-values:
        for name in GoodStandardRequiredTextLines[0:2]:
            for street_address in GoodStandardRequiredTextLines[0:2]:
                for building_address in GoodStandardOptionalTextLines[0:2]:
                    for city in GoodStandardRequiredTextLines[0:2]:
                        for region in GoodStandardOptionalTextLines[0:2]:
                            for postal_code in GoodStandardOptionalTextLines[0:2]:
                                for country in GoodStandardRequiredTextLines[0:2]:
                                    test_object = Order.standard_address(
                                        name,
                                        street_address, 
                                        building_address, 
                                        city, region, postal_code, 
                                        country
                                    )
                                    self.assertEqual(test_object.street_address, street_address)
                                    self.assertEqual(test_object.building_address, building_address)
                                    self.assertEqual(test_object.city, city)
                                    self.assertEqual(test_object.region, region)
                                    self.assertEqual(test_object.postal_code, postal_code)
                                    self.assertEqual(test_object.country, country)

    def testto_data_dict(self):
        # Tests the to_data_dict method of the Order class
        for name in GoodStandardRequiredTextLines[0:2]:
            for street_address in GoodStandardRequiredTextLines[0:2]:
                for city in GoodStandardRequiredTextLines[0:2]:
                    # - At this point, we have all the required 
                    #   arguments, so we can start testing with 
                    #   partial expected dict-values
                    test_object = Order(
                        name, street_address, city,
                    )
                    expected = {
                        'name':name,
                        'street_address':street_address,
                        'city':city,
                        # - The balance are default values...
                        'building_address':None,
                        'region':None,
                        'postal_code':None,
                        'country':None,
                        'items':{},
                        # - We also need to include the data-object 
                        #   items that should appear!
                        'created':datetime.strftime(
                                test_object.created, 
                                test_object._data_time_string
                            ),
                        'modified':datetime.strftime(
                                test_object.modified, 
                                test_object._data_time_string
                            ),
                        'oid':str(test_object.oid),
                        'is_active':test_object.is_active,
                        'is_deleted':test_object.is_deleted,
                    }
                    self.assertEqual(
                        test_object.to_data_dict(), expected
                    )
                    for items in GoodOrderItems:
                        test_object = Order(
                            name, street_address, city,
                            items=items,
                        )
                        expected = {
                            'name':name,
                            'street_address':street_address,
                            'city':city,
                            'building_address':None,
                            'region':None,
                            'postal_code':None,
                            'country':None,
                            'items':items,
                            'created':datetime.strftime(
                                    test_object.created, 
                                    test_object._data_time_string
                                ),
                            'modified':datetime.strftime(
                                    test_object.modified, 
                                    test_object._data_time_string
                                ),
                            'oid':str(test_object.oid),
                            'is_active':test_object.is_active,
                            'is_deleted':test_object.is_deleted,
                        }
                        self.assertEqual(
                            test_object.to_data_dict(), expected
                        )
                        for building_address in GoodStandardOptionalTextLines[0:2]:
                            test_object = Order(
                                name, street_address, city,
                                items=items, 
                                building_address=building_address,
                            )
                            expected = {
                                'name':name,
                                'street_address':street_address,
                                'city':city,
                                'building_address':building_address,
                                'region':None,
                                'postal_code':None,
                                'country':None,
                                'items':items,
                                'created':datetime.strftime(
                                        test_object.created, 
                                        test_object._data_time_string
                                    ),
                                'modified':datetime.strftime(
                                        test_object.modified, 
                                        test_object._data_time_string
                                    ),
                                'oid':str(test_object.oid),
                                'is_active':test_object.is_active,
                                'is_deleted':test_object.is_deleted,
                            }
                            self.assertEqual(
                                test_object.to_data_dict(), expected
                            )
                            for region in GoodStandardOptionalTextLines[0:2]:
                                test_object = Order(
                                    name, street_address, city,
                                    items=items, region=region, 
                                    building_address=building_address,
                                )
                                expected = {
                                    'name':name,
                                    'street_address':street_address,
                                    'city':city,
                                    'building_address':building_address,
                                    'region':region,
                                    'postal_code':None,
                                    'country':None,
                                    'items':items,
                                    'created':datetime.strftime(
                                            test_object.created, 
                                            test_object._data_time_string
                                        ),
                                    'modified':datetime.strftime(
                                            test_object.modified, 
                                            test_object._data_time_string
                                        ),
                                    'oid':str(test_object.oid),
                                    'is_active':test_object.is_active,
                                    'is_deleted':test_object.is_deleted,
                                }
                                self.assertEqual(
                                    test_object.to_data_dict(), expected
                                )
                                for postal_code in GoodStandardOptionalTextLines[0:2]:
                                    test_object = Order(
                                        name, street_address, city,
                                        items=items, region=region, 
                                        building_address=building_address,
                                        postal_code=postal_code
                                    )
                                    expected = {
                                        'name':name,
                                        'street_address':street_address,
                                        'city':city,
                                        'building_address':building_address,
                                        'region':region,
                                        'postal_code':postal_code,
                                        'country':None,
                                        'items':items,
                                        'created':datetime.strftime(
                                                test_object.created, 
                                                test_object._data_time_string
                                            ),
                                        'modified':datetime.strftime(
                                                test_object.modified, 
                                                test_object._data_time_string
                                            ),
                                        'oid':str(test_object.oid),
                                        'is_active':test_object.is_active,
                                        'is_deleted':test_object.is_deleted,
                                    }
                                    self.assertEqual(
                                        test_object.to_data_dict(), expected
                                    )
                                    for country in GoodStandardOptionalTextLines[0:2]:
                                        test_object = Order(
                                            name, street_address, city,
                                            items=items, region=region, 
                                            building_address=building_address,
                                            postal_code=postal_code, 
                                            country=country
                                        )
                                        expected = {
                                            'name':name,
                                            'street_address':street_address,
                                            'city':city,
                                            'building_address':building_address,
                                            'region':region,
                                            'postal_code':postal_code,
                                            'country':country,
                                            'items':items,
                                            'created':datetime.strftime(
                                                    test_object.created, 
                                                    test_object._data_time_string
                                                ),
                                            'modified':datetime.strftime(
                                                    test_object.modified, 
                                                    test_object._data_time_string
                                                ),
                                            'oid':str(test_object.oid),
                                            'is_active':test_object.is_active,
                                            'is_deleted':test_object.is_deleted,
                                        }
                                        self.assertEqual(
                                            test_object.to_data_dict(), expected
                                        )

    ###################################
    # Tests of class properties       #
    ###################################

    def testbuilding_address(self):
        # Tests the building_address property of the Order class
        # - Assert that the getter is correct:
        self.assertEqual(
            Order.building_address.fget, 
            Order._get_building_address, 
            'Order.building_address is expected to use the '
            '_get_building_address method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Order.building_address.fset, 
            Order._set_building_address, 
            'Order.building_address is expected to use the '
            '_set_building_address method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Order.building_address.fdel, 
            Order._del_building_address, 
            'Order.building_address is expected to use the '
            '_del_building_address method as its deleter-method'
        )

    def testcity(self):
        # Tests the city property of the Order class
        # - Assert that the getter is correct:
        self.assertEqual(
            Order.city.fget, 
            Order._get_city, 
            'Order.city is expected to use the '
            '_get_city method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Order.city.fset, 
            Order._set_city, 
            'Order.city is expected to use the '
            '_set_city method as its setter-method'
        )
        # - If city is not expected to be publicly deletable,
        #   the second item here (Order._del_city) should 
        #   be changed to None, and the failure message adjusted 
        #   accordingly:
        # - Assert that the deleter is correct:
        self.assertEqual(
            Order.city.fdel, 
            Order._del_city, 
            'Order.city is expected to use the '
            '_del_city method as its deleter-method'
        )

    def testcountry(self):
        # Tests the country property of the Order class
        # - Assert that the getter is correct:
        self.assertEqual(
            Order.country.fget, 
            Order._get_country, 
            'Order.country is expected to use the '
            '_get_country method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Order.country.fset, 
            Order._set_country, 
            'Order.country is expected to use the '
            '_set_country method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Order.country.fdel, 
            Order._del_country, 
            'Order.country is expected to use the '
            '_del_country method as its deleter-method'
        )

    def testitems(self):
        # Tests the items property of the Order class
        # - Assert that the getter is correct:
        self.assertEqual(
            Order.items.fget, 
            Order._get_items, 
            'Order.items is expected to use the '
            '_get_items method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Order.items.fset, None, 
            'Order.items is expected to be read-only, with no '
            'setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Order.items.fdel, None, 
            'Order.items is expected to be read-only, with no '
            'deleter-method'
        )

    def testname(self):
        # Tests the name property of the Order class
        # - Assert that the getter is correct:
        self.assertEqual(
            Order.name.fget, 
            Order._get_name, 
            'Order.name is expected to use the '
            '_get_name method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Order.name.fset, 
            Order._set_name, 
            'Order.name is expected to use the '
            '_set_name method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Order.name.fdel, 
            Order._del_name, 
            'Order.name is expected to use the '
            '_del_name method as its deleter-method'
        )

    def testpostal_code(self):
        # Tests the postal_code property of the Order class
        # - Assert that the getter is correct:
        self.assertEqual(
            Order.postal_code.fget, 
            Order._get_postal_code, 
            'Order.postal_code is expected to use the '
            '_get_postal_code method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Order.postal_code.fset, 
            Order._set_postal_code, 
            'Order.postal_code is expected to use the '
            '_set_postal_code method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Order.postal_code.fdel, 
            Order._del_postal_code, 
            'Order.postal_code is expected to use the '
            '_del_postal_code method as its deleter-method'
        )

    def testregion(self):
        # Tests the region property of the Order class
        # - Assert that the getter is correct:
        self.assertEqual(
            Order.region.fget, 
            Order._get_region, 
            'Order.region is expected to use the '
            '_get_region method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Order.region.fset, 
            Order._set_region, 
            'Order.region is expected to use the '
            '_set_region method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Order.region.fdel, 
            Order._del_region, 
            'Order.region is expected to use the '
            '_del_region method as its deleter-method'
        )

    def teststreet_address(self):
        # Tests the street_address property of the Order class
        # - Assert that the getter is correct:
        self.assertEqual(
            Order.street_address.fget, 
            Order._get_street_address, 
            'Order.street_address is expected to use the '
            '_get_street_address method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Order.street_address.fset, 
            Order._set_street_address, 
            'Order.street_address is expected to use the '
            '_set_street_address method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Order.street_address.fdel, 
            Order._del_street_address, 
            'Order.street_address is expected to use the '
            '_del_street_address method as its deleter-method'
        )

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testOrder
    )
)

@testartisan_objectsCodeCoverage.AddMethodTesting
@testartisan_objectsCodeCoverage.AddPropertyTesting
class testProduct(unittest.TestCase):

    ###################################
    # Tests of class methods          #
    ###################################

    def test__init__(self):
        # Tests the __init__ method of the Product class
        # - Test all permutations of "good" argument-values:
        name = 'name'           # - tested elsewhere
        summary = 'summary'     # - tested elsewhere
        available = True        # - tested elsewhere
        store_available = True  # - tested elsewhere
        for description in GoodStandardOptionalTextLines:
            for dimensions in GoodStandardOptionalTextLines:
                for metadata in GoodMetadataDicts:
                    for shipping_weight in GoodWeights:
                        test_object = Product(
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
        # Tests the _del_available method of the Product class
        test_object = Product('name', 'summary', False, True)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Product should '
            'have is_dirty of False'
        )
        test_object._del_available()
        self.assertEqual(test_object.is_dirty, True, 
            'The deletion of Product.available should set '
            'is_dirty to True'
        )

    def test_del_description(self):
        # Tests the _del_description method of the Product class
        test_object = Product('name', 'summary', False, True)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Product should '
            'have is_dirty of False'
        )
        test_object._del_description()
        self.assertEqual(test_object.is_dirty, True, 
            'The deletion of Product.description should set '
            'is_dirty to True'
        )

    def test_del_dimensions(self):
        # Tests the _del_dimensions method of the Product class
        test_object = Product('name', 'summary', False, True)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Product should '
            'have is_dirty of False'
        )
        test_object._del_dimensions()
        self.assertEqual(test_object.is_dirty, True, 
            'The deletion of Product.dimensions should set '
            'is_dirty to True'
        )

    def test_del_metadata(self):
        # Tests the _del_metadata method of the Product class
        test_object = Product('name', 'summary', False, True)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Product should '
            'have is_dirty of False'
        )
        test_object._del_metadata()
        self.assertEqual(test_object.is_dirty, True, 
            'The deletion of Product.metadata should set '
            'is_dirty to True'
        )

    def test_del_name(self):
        # Tests the _del_name method of the Product class
        test_object = Product('name', 'summary', False, True)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Product should '
            'have is_dirty of False'
        )
        test_object._del_name()
        self.assertEqual(test_object.is_dirty, True, 
            'The deletion of Product.name should set '
            'is_dirty to True'
        )

    def test_del_shipping_weight(self):
        # Tests the _del_shipping_weight method of the Product class
        test_object = Product('name', 'summary', False, True)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Product should '
            'have is_dirty of False'
        )
        test_object._del_shipping_weight()
        self.assertEqual(test_object.is_dirty, True, 
            'The deletion of Product.shipping_weight should set '
            'is_dirty to True'
        )

    def test_del_store_available(self):
        # Tests the _del_store_available method of the Product class
        test_object = Product('name', 'summary', False, True)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Product should '
            'have is_dirty of False'
        )
        test_object._del_store_available()
        self.assertEqual(test_object.is_dirty, True, 
            'The deletion of Product.store_available should set '
            'is_dirty to True'
        )

    def test_del_summary(self):
        # Tests the _del_summary method of the Product class
        test_object = Product('name', 'summary', False, True)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Product should '
            'have is_dirty of False'
        )
        test_object._del_summary()
        self.assertEqual(test_object.is_dirty, True, 
            'The deletion of Product.summary should set '
            'is_dirty to True'
        )

    def test_set_available(self):
        # Tests the _set_available method of the Product class
        test_object = Product('name', 'summary', False, True)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Product should '
            'have is_dirty of False'
        )
        test_object._set_available(not test_object.available)
        self.assertEqual(test_object.is_dirty, True, 
            'Setting Product.available should also set '
            'is_dirty to True'
        )

    def test_set_description(self):
        # Tests the _set_description method of the Product class
        test_object = Product('name', 'summary', False, True)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Product should '
            'have is_dirty of False'
        )
        test_object._set_description('new value')
        self.assertEqual(test_object.is_dirty, True, 
            'Setting Product.description should also set '
            'is_dirty to True'
        )

    def test_set_dimensions(self):
        # Tests the _set_dimensions method of the Product class
        test_object = Product('name', 'summary', False, True)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Product should '
            'have is_dirty of False'
        )
        test_object._set_dimensions('new value')
        self.assertEqual(test_object.is_dirty, True, 
            'Setting Product.dimensions should also set '
            'is_dirty to True'
        )

    def test_set_metadata(self):
        # Tests the _set_metadata method of the Product class
        test_object = Product('name', 'summary', False, True)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Product should '
            'have is_dirty of False'
        )
        test_object._set_metadata({'color':'red'})
        self.assertEqual(test_object.is_dirty, True, 
            'Setting Product.available should also set '
            'is_dirty to True'
        )

    def test_set_name(self):
        # Tests the _set_name method of the Product class
        test_object = Product('name', 'summary', False, True)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Product should '
            'have is_dirty of False'
        )
        test_object._set_name('new value')
        self.assertEqual(test_object.is_dirty, True, 
            'Setting Product.name should also set '
            'is_dirty to True'
        )

    def test_set_shipping_weight(self):
        # Tests the _set_shipping_weight method of the Product class
        test_object = Product('name', 'summary', False, True)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Product should '
            'have is_dirty of False'
        )
        test_object._set_shipping_weight(1.23)
        self.assertEqual(test_object.is_dirty, True, 
            'Setting Product.shipping_weight should also set '
            'is_dirty to True'
        )

    def test_set_store_available(self):
        # Tests the _set_store_store_available method of the Product class
        test_object = Product('name', 'summary', False, True)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Product should '
            'have is_dirty of False'
        )
        test_object._set_store_available(not test_object.store_available)
        self.assertEqual(test_object.is_dirty, True, 
            'Setting Product.store_available should also set '
            'is_dirty to True'
        )

    def test_set_summary(self):
        # Tests the _set_summary method of the Product class
        test_object = Product('name', 'summary', False, True)
        self.assertEqual(test_object.is_dirty, False, 
            'A newly-created instance of an Product should '
            'have is_dirty of False'
        )
        test_object._set_summary('new value')
        self.assertEqual(test_object.is_dirty, True, 
            'Setting Product.summary should also set '
            'is_dirty to True'
        )

    def testfrom_data_dict(self):
        # Tests the from_data_dict method of the Product class
        defaults = {
            'description':None,
            'dimensions':None,
            'metadata':{},
            'shipping_weight':0,
        }
        for name in GoodStandardRequiredTextLines[0:2]:
            for summary in GoodStandardRequiredTextLines[0:2]:
                for available in GoodBooleanOrIntEquivalents[0:2]:
                    for store_available in GoodBooleanOrIntEquivalents[0:2]:
                        # - At this point, we have all the required 
                        #   arguments, so we can start testing with 
                        #   partial expected dict-values
                        data_dict = {
                            'name':name,
                            'summary':summary,
                            'available':available,
                            'store_available':store_available,
                        }
                        test_object = Product.from_data_dict(data_dict)
                        actual = test_object.to_data_dict()
                        # - Create a copy of the defaults as a starting-point
                        expected = dict(defaults)
                        instance_values = {
                            'created':datetime.strftime(
                                    test_object.created, 
                                    test_object._data_time_string
                                ),
                            'modified':datetime.strftime(
                                    test_object.modified, 
                                    test_object._data_time_string
                                ),
                            'oid':str(test_object.oid),
                            'is_active':test_object.is_active,
                            'is_deleted':test_object.is_deleted,
                        }
                        expected.update(instance_values)
                        expected.update(data_dict)
                        self.assertEqual(expected, actual)
                        for description in GoodStandardOptionalTextLines[0:2]:
                            data_dict = {
                                'name':name,
                                'summary':summary,
                                'available':available,
                                'store_available':store_available,
                                'description':description,
                            }
                            test_object = Product.from_data_dict(data_dict)
                            actual = test_object.to_data_dict()
                            # - Create a copy of the defaults as a starting-point
                            expected = dict(defaults)
                            instance_values = {
                                'created':datetime.strftime(
                                        test_object.created, 
                                        test_object._data_time_string
                                    ),
                                'modified':datetime.strftime(
                                        test_object.modified, 
                                        test_object._data_time_string
                                    ),
                                'oid':str(test_object.oid),
                                'is_active':test_object.is_active,
                                'is_deleted':test_object.is_deleted,
                            }
                            expected.update(instance_values)
                            expected.update(data_dict)
                            self.assertEqual(expected, actual)
                            for dimensions in GoodStandardOptionalTextLines[0:2]:
                                data_dict = {
                                    'name':name,
                                    'summary':summary,
                                    'available':available,
                                    'store_available':store_available,
                                    'description':description,
                                    'dimensions':dimensions,
                                }
                                test_object = Product.from_data_dict(data_dict)
                                actual = test_object.to_data_dict()
                                # - Create a copy of the defaults as a starting-point
                                expected = dict(defaults)
                                instance_values = {
                                    'created':datetime.strftime(
                                            test_object.created, 
                                            test_object._data_time_string
                                        ),
                                    'modified':datetime.strftime(
                                            test_object.modified, 
                                            test_object._data_time_string
                                        ),
                                    'oid':str(test_object.oid),
                                    'is_active':test_object.is_active,
                                    'is_deleted':test_object.is_deleted,
                                }
                                expected.update(instance_values)
                                expected.update(data_dict)
                                self.assertEqual(expected, actual)
                                for metadata in GoodMetadataDicts[0:2]:
                                    data_dict = {
                                        'name':name,
                                        'summary':summary,
                                        'available':available,
                                        'store_available':store_available,
                                        'description':description,
                                        'dimensions':dimensions,
                                        'metadata':metadata,
                                    }
                                    test_object = Product.from_data_dict(data_dict)
                                    actual = test_object.to_data_dict()
                                    # - Create a copy of the defaults as a starting-point
                                    expected = dict(defaults)
                                    instance_values = {
                                        'created':datetime.strftime(
                                                test_object.created, 
                                                test_object._data_time_string
                                            ),
                                        'modified':datetime.strftime(
                                                test_object.modified, 
                                                test_object._data_time_string
                                            ),
                                        'oid':str(test_object.oid),
                                        'is_active':test_object.is_active,
                                        'is_deleted':test_object.is_deleted,
                                    }
                                    expected.update(instance_values)
                                    expected.update(data_dict)
                                    self.assertEqual(expected, actual)
                                    for shipping_weight in GoodWeights[0:2]:
                                        data_dict = {
                                            'name':name,
                                            'summary':summary,
                                            'available':available,
                                            'store_available':store_available,
                                            'description':description,
                                            'dimensions':dimensions,
                                            'metadata':metadata,
                                            'shipping_weight':shipping_weight,
                                        }
                                        test_object = Product.from_data_dict(data_dict)
                                        actual = test_object.to_data_dict()
                                        # - Create a copy of the defaults as a starting-point
                                        expected = dict(defaults)
                                        instance_values = {
                                            'created':datetime.strftime(
                                                    test_object.created, 
                                                    test_object._data_time_string
                                                ),
                                            'modified':datetime.strftime(
                                                    test_object.modified, 
                                                    test_object._data_time_string
                                                ),
                                            'oid':str(test_object.oid),
                                            'is_active':test_object.is_active,
                                            'is_deleted':test_object.is_deleted,
                                        }
                                        expected.update(instance_values)
                                        expected.update(data_dict)
                                        self.assertEqual(expected, actual)

    def test_load_objects(self):
        # Tests the _load_objects method of the Product class
        # - First, forcibly change Product._file_store_dir to a disposable 
        #   temp-directory, and clear the in-memory and on-disk stores
        Product._file_store_dir = '/tmp/test_Product_objects/'
        Product._loaded_objects = None
        if os.path.exists(Product._file_store_dir):
            rmtree(Product._file_store_dir)
        self.assertEqual(Product._loaded_objects, None)
        # - Iterate through some objects, creating them and saving them.
        for name in GoodStandardRequiredTextLines[0:2]:
            for summary in GoodStandardRequiredTextLines[0:2]:
                for available in GoodBooleanOrIntEquivalents[0:2]:
                    for store_available in GoodBooleanOrIntEquivalents[0:2]:
                        test_object = Product(
                            name, summary, available, store_available
                        )
                        test_object.save()
                        # - Verify that the object exists
                        #   - in memory
                        self.assertNotEqual(
                            Product._loaded_objects.get(test_object.oid), 
                            None
                        )
                        #   - on disk
                        file_path = '%s/Product-data/%s.json' % (Product._file_store_dir, test_object.oid)
                        self.assertTrue(
                            os.path.exists(file_path), 
                            'The file was not written at %s' % file_path
                        )
                # - Make a copy of the OIDs to check with after clearing 
                #   the in-memory copy:
                oids_before = sorted([str(key) for key in Product._loaded_objects.keys()])
                # - Clear the in-memory copy and verify all the oids 
                #   exist after a _load_objects is called
                Product._loaded_objects = None
                Product._load_objects()
                oids_after = sorted([str(key) for key in Product._loaded_objects.keys()])
                self.assertEqual(oids_before, oids_after)
        # - Delete items at random and verify deletion and load after each
        instances = list(Product._loaded_objects.values())
        while instances:
            target = choice(instances)
            Product.delete(target.oid)
            # - Verify that the object no longer exists
            #   - in memory
            self.assertEqual(
                Product._loaded_objects.get(str(test_object.oid)), 
                None
            )
            #   - on disk
            file_path = '%s/Product-data/%s.json' % (Product._file_store_dir, target.oid)
            self.assertFalse(
                os.path.exists(file_path), 
                'File at %s was not deleted' % file_path
            )
            # - Make a copy of the OIDs to check with after clearing 
            #   the in-memory copy:
            oids_before = sorted([str(key) for key in Product._loaded_objects.keys()])
            # - Clear the in-memory copy and verify all the oids 
            #   exist after a _load_objects is called
            Product._loaded_objects = None
            Product._load_objects()
            oids_after = sorted([str(key) for key in Product._loaded_objects.keys()])
            self.assertEqual(oids_before, oids_after)
            instances.remove(target)
        # - Clean up any remaining in-memory and on-disk store items
        Product._loaded_objects = None
        if os.path.exists(Product._file_store_dir):
            rmtree(Product._file_store_dir)

    def testmatches(self):
        # Tests the matches method of the Product class
        # - First, create an object to test against, with as complete 
        #   a data-set as we can manage
        test_object = Product(
            name=GoodStandardRequiredTextLines[0],
            summary=GoodStandardRequiredTextLines[0],
            available=GoodBooleanOrIntEquivalents[0],
            store_available=GoodBooleanOrIntEquivalents[0],
            description=GoodStandardOptionalTextLines[0],
            dimensions=GoodStandardOptionalTextLines[0],
            metadata=GoodMetadataDicts[0],
            shipping_weight=GoodWeights[0]
        )
        # - Then we'll iterate over some "good" values, create criteria
        for name_num in range(0,2):
            name = GoodStandardRequiredTextLines[name_num]
            criteria = {'name':name}
            expected = (name == test_object.name)
            self.assertEqual(expected, test_object.matches(**criteria))
            for summary_num in range(0,2):
                summary = GoodStandardRequiredTextLines[summary_num]
                criteria['summary'] = summary
                expected = (expected and summary == test_object.summary)
                self.assertEqual(expected, test_object.matches(**criteria))
                for available_num in range(0,2):
                    available = GoodBooleanOrIntEquivalents[available_num]
                    criteria['available'] = available
                    expected = (expected and available == test_object.available)
                    self.assertEqual(expected, test_object.matches(**criteria))
                    for store_available_num in range(0,2):
                        store_available = GoodBooleanOrIntEquivalents[store_available_num]
                        criteria['store_available'] = store_available
                        expected = (expected and store_available == test_object.store_available)
                        self.assertEqual(expected, test_object.matches(**criteria))
                        for description_num in range(0,2):
                            description = GoodStandardOptionalTextLines[description_num]
                            criteria['description'] = description
                            expected = (expected and description == test_object.description)
                            self.assertEqual(expected, test_object.matches(**criteria))
                            for dimensions_num in range(0,2):
                                dimensions = GoodStandardOptionalTextLines[dimensions_num]
                                criteria['dimensions'] = dimensions
                                expected = (expected and dimensions == test_object.dimensions)
                                self.assertEqual(expected, test_object.matches(**criteria))
                                for metadata_num in range(0,2):
                                    metadata = GoodMetadataDicts[metadata_num]
                                    criteria['metadata'] = metadata
                                    expected = (expected and metadata == test_object.metadata)
                                    self.assertEqual(expected, test_object.matches(**criteria))
                                    for shipping_weight_num in range(0,2):
                                        shipping_weight = GoodWeights[shipping_weight_num]
                                        criteria['shipping_weight'] = shipping_weight
                                        expected = (expected and shipping_weight == test_object.shipping_weight)
                                        self.assertEqual(expected, test_object.matches(**criteria))

    @unittest.skip(
        'Sort will be implemented once there\'s a need for it, '
        'and tested as part of that implementation'
    )
    def testsort(self):
        # Tests the sort method of the Product class
        # - Test all permutations of "good" argument-values:
        # - Test all permutations of each "bad" argument-value 
        #   set against "good" values for the other arguments:
        self.fail('testsort is not yet implemented')

    def testto_data_dict(self):
        # Tests the to_data_dict method of the Product class
        for name in GoodStandardRequiredTextLines[0:1]:
            for summary in GoodStandardRequiredTextLines[0:1]:
                for available in GoodBooleanOrIntEquivalents[0:1]:
                    for store_available in GoodBooleanOrIntEquivalents[0:1]:
                        test_object = Product(
                            name, summary, available, store_available, 
                        )
                        expected = {
                            'name':name, 
                            'summary':summary, 
                            'available':available, 
                            'store_available':store_available,
                            'description':None,
                            'dimensions':None,
                            'metadata':{},
                            'shipping_weight':0,
                            'created':datetime.strftime(
                                    test_object.created, 
                                    test_object._data_time_string
                                ),
                            'modified':datetime.strftime(
                                    test_object.modified, 
                                    test_object._data_time_string
                                ),
                            'oid':str(test_object.oid),
                            'is_active':test_object.is_active,
                            'is_deleted':test_object.is_deleted,
                        }
                        actual = test_object.to_data_dict()
                        self.assertEqual(expected, actual)
                        for description in GoodStandardOptionalTextLines[0:1]:
                            test_object = Product(
                                name, summary, available, 
                                store_available, description, 
                            )
                            expected = {
                                'name':name, 
                                'summary':summary, 
                                'available':available, 
                                'store_available':store_available,
                                'description':description,
                                'dimensions':None,
                                'metadata':{},
                                'shipping_weight':0,
                                'created':datetime.strftime(
                                        test_object.created, 
                                        test_object._data_time_string
                                    ),
                                'modified':datetime.strftime(
                                        test_object.modified, 
                                        test_object._data_time_string
                                    ),
                                'oid':str(test_object.oid),
                                'is_active':test_object.is_active,
                                'is_deleted':test_object.is_deleted,
                            }
                            actual = test_object.to_data_dict()
                            self.assertEqual(expected, actual)
                            for dimensions in GoodStandardOptionalTextLines[0:1]:
                                test_object = Product(
                                    name, summary, available, 
                                    store_available, description, 
                                    dimensions
                                )
                                expected = {
                                    'name':name, 
                                    'summary':summary, 
                                    'available':available, 
                                    'store_available':store_available,
                                    'description':description,
                                    'dimensions':dimensions,
                                    'metadata':{},
                                    'shipping_weight':0,
                                    'created':datetime.strftime(
                                            test_object.created, 
                                            test_object._data_time_string
                                        ),
                                    'modified':datetime.strftime(
                                            test_object.modified, 
                                            test_object._data_time_string
                                        ),
                                    'oid':str(test_object.oid),
                                    'is_active':test_object.is_active,
                                    'is_deleted':test_object.is_deleted,
                                }
                                actual = test_object.to_data_dict()
                                self.assertEqual(expected, actual)
                                for metadata in GoodMetadataDicts[0:1]:
                                    test_object = Product(
                                        name, summary, available, 
                                        store_available, description, 
                                        dimensions, metadata
                                    )
                                    expected = {
                                        'name':name, 
                                        'summary':summary, 
                                        'available':available, 
                                        'store_available':store_available,
                                        'description':description,
                                        'dimensions':dimensions,
                                        'metadata':metadata,
                                        'shipping_weight':0,
                                        'created':datetime.strftime(
                                                test_object.created, 
                                                test_object._data_time_string
                                            ),
                                        'modified':datetime.strftime(
                                                test_object.modified, 
                                                test_object._data_time_string
                                            ),
                                        'oid':str(test_object.oid),
                                        'is_active':test_object.is_active,
                                        'is_deleted':test_object.is_deleted,
                                    }
                                    actual = test_object.to_data_dict()
                                    self.assertEqual(expected, actual)
                                    for shipping_weight in GoodWeights[0:1]:
                                        test_object = Product(
                                            name, summary, available, 
                                            store_available, description, 
                                            dimensions, metadata, 
                                            shipping_weight
                                        )
                                        expected = {
                                            'name':name, 
                                            'summary':summary, 
                                            'available':available, 
                                            'store_available':store_available,
                                            'description':description,
                                            'dimensions':dimensions,
                                            'metadata':metadata,
                                            'shipping_weight':shipping_weight,
                                            'created':datetime.strftime(
                                                    test_object.created, 
                                                    test_object._data_time_string
                                                ),
                                            'modified':datetime.strftime(
                                                    test_object.modified, 
                                                    test_object._data_time_string
                                                ),
                                            'oid':str(test_object.oid),
                                            'is_active':test_object.is_active,
                                            'is_deleted':test_object.is_deleted,
                                        }
                                        actual = test_object.to_data_dict()
                                        self.assertEqual(expected, actual)

    ###################################
    # Tests of class properties       #
    ###################################

    def testavailable(self):
        # Tests the available property of the Product class
        # - Assert that the getter is correct:
        self.assertEqual(
            Product.available.fget, 
            BaseProduct._get_available, 
            'Product.available is expected to use the '
            'BaseProduct._get_available method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Product.available.fset, 
            Product._set_available, 
            'Product.available is expected to use the '
            '_set_available method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Product.available.fdel, 
            Product._del_available, 
            'Product.available is expected to use the '
            '_del_available method as its deleter-method'
        )

    def testdescription(self):
        # Tests the description property of the Product class
        # - Assert that the getter is correct:
        self.assertEqual(
            Product.description.fget, 
            BaseProduct._get_description, 
            'Product.description is expected to use the '
            'BaseProduct._get_description method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Product.description.fset, 
            Product._set_description, 
            'Product.description is expected to use the '
            '_set_description method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Product.description.fdel, 
            Product._del_description, 
            'Product.description is expected to use the '
            '_del_description method as its deleter-method'
        )

    def testdimensions(self):
        # Tests the dimensions property of the Product class
        # - Assert that the getter is correct:
        self.assertEqual(
            Product.dimensions.fget, 
            BaseProduct._get_dimensions, 
            'Product.dimensions is expected to use the '
            'BaseProduct._get_dimensions method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Product.dimensions.fset, 
            Product._set_dimensions, 
            'Product.dimensions is expected to use the '
            '_set_dimensions method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Product.dimensions.fdel, 
            Product._del_dimensions, 
            'Product.dimensions is expected to use the '
            '_del_dimensions method as its deleter-method'
        )

    def testmetadata(self):
        # Tests the metadata property of the Product class
        # - Assert that the getter is correct:
        self.assertEqual(
            Product.metadata.fget, 
            BaseProduct._get_metadata, 
            'Product.metadata is expected to use the '
            'BaseProduct._get_metadata method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Product.metadata.fset, 
            None, 
            'Product.metadata is expected to be read-only, with no setter'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Product.metadata.fdel, 
            None, 
            'Product.metadata is expected to be read-only, with no deleter'
        )

    def testname(self):
        # Tests the name property of the Product class
        # - Assert that the getter is correct:
        self.assertEqual(
            Product.name.fget, 
            BaseProduct._get_name, 
            'Product.name is expected to use the '
            'BaseProduct._get_name method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Product.name.fset, 
            Product._set_name, 
            'Product.name is expected to use the '
            '_set_name method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Product.name.fdel, 
            Product._del_name, 
            'Product.name is expected to use the '
            '_del_name method as its deleter-method'
        )

    def testshipping_weight(self):
        # Tests the shipping_weight property of the Product class
        # - Assert that the getter is correct:
        self.assertEqual(
            Product.shipping_weight.fget, 
            BaseProduct._get_shipping_weight, 
            'Product.shipping_weight is expected to use the '
            'BaseProduct._get_shipping_weight method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Product.shipping_weight.fset, 
            Product._set_shipping_weight, 
            'Product.shipping_weight is expected to use the '
            '_set_shipping_weight method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Product.shipping_weight.fdel, 
            Product._del_shipping_weight, 
            'Product.shipping_weight is expected to use the '
            '_del_shipping_weight method as its deleter-method'
        )

    def teststore_available(self):
        # Tests the store_available property of the Product class
        # - Assert that the getter is correct:
        self.assertEqual(
            Product.store_available.fget, 
            BaseProduct._get_store_available, 
            'Product.store_available is expected to use the '
            'BaseProduct._get_store_available method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Product.store_available.fset, 
            Product._set_store_available, 
            'Product.store_available is expected to use the '
            '_set_store_available method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Product.store_available.fdel, 
            Product._del_store_available, 
            'Product.store_available is expected to use the '
            '_del_store_available method as its deleter-method'
        )

    def testsummary(self):
        # Tests the summary property of the Product class
        # - Assert that the getter is correct:
        self.assertEqual(
            Product.summary.fget, 
            BaseProduct._get_summary, 
            'Product.summary is expected to use the '
            'BaseProduct._get_summary method as its getter-method'
        )
        # - Assert that the setter is correct:
        self.assertEqual(
            Product.summary.fset, 
            Product._set_summary, 
            'Product.summary is expected to use the '
            '_set_summary method as its setter-method'
        )
        # - Assert that the deleter is correct:
        self.assertEqual(
            Product.summary.fdel, 
            Product._del_summary, 
            'Product.summary is expected to use the '
            '_del_summary method as its deleter-method'
        )

#    def testproperty_name(self):
#        # Tests the property_name property of the Product class
#        # - Assert that the getter is correct:
#        self.assertEqual(
#            Product.property_name.fget, 
#            Product._get_property_name, 
#            'Product.property_name is expected to use the '
#            '_get_property_name method as its getter-method'
#        )
#        # - If property_name is not expected to be publicly settable,
#        #   the second item here (Product._set_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the setter is correct:
#        self.assertEqual(
#            Product.property_name.fset, 
#            Product._set_property_name, 
#            'Product.property_name is expected to use the '
#            '_set_property_name method as its setter-method'
#        )
#        # - If property_name is not expected to be publicly deletable,
#        #   the second item here (Product._del_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the deleter is correct:
#        self.assertEqual(
#            Product.property_name.fdel, 
#            Product._del_property_name, 
#            'Product.property_name is expected to use the '
#            '_del_property_name method as its deleter-method'
#        )

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testProduct
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
        SaveTestReport(results, 'hms_artisan.artisan_objects',
            'hms_artisan.artisan_objects.test-results')
