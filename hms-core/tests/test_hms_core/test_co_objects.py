#!/usr/bin/env python

# Python unit-test-module template. Copy the template to a new
# unit-test-module location, and start replacing names as needed:
#
# hms_core  ==> The path/namespace of the parent of the module/package
#                  being tested in this file.
# co_objects   ==> The name of the module being tested
#
# Then remove this comment-block

"""
Defines unit-tests for the module at hms_core.co_objects.
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
from uuid import uuid4, UUID

#######################################
# Third-party imports needed          #
#######################################

from hms_core.business_objects import Address, BaseArtisan, \
    BaseProduct

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

import hms_core.co_objects as co_objects
from hms_core.co_objects import *

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

GoodAddress = Address('street-address', 'city')
GoodAddresses = [
    Address('street-address', 'city')
]
BadAddresses = [
    -1, -1.0, object(), 'true', '', (1,2), tuple()
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

#######################################
# Code-coverage test-case and         #
# decorator-methods                   #
#######################################

class testco_objectsCodeCoverage(ModuleCoverageTest):
    _testNamespace = 'hms_core'
    _testModule = co_objects

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testco_objectsCodeCoverage
   )
)

#######################################
# Test-cases in the module            #
#######################################

@testco_objectsCodeCoverage.AddMethodTesting
@testco_objectsCodeCoverage.AddPropertyTesting
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

#    def testproperty_name(self):
#        # Tests the property_name property of the Artisan class
#        # - Assert that the getter is correct:
#        self.assertEqual(
#            Artisan.property_name.fget, 
#            Artisan._get_property_name, 
#            'Artisan.property_name is expected to use the '
#            '_get_property_name method as its getter-method'
#        )
#        # - If property_name is not expected to be publicly settable,
#        #   the second item here (Artisan._set_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the setter is correct:
#        self.assertEqual(
#            Artisan.property_name.fset, 
#            Artisan._set_property_name, 
#            'Artisan.property_name is expected to use the '
#            '_set_property_name method as its setter-method'
#        )
#        # - If property_name is not expected to be publicly deletable,
#        #   the second item here (Artisan._del_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the deleter is correct:
#        self.assertEqual(
#            Artisan.property_name.fdel, 
#            Artisan._del_property_name, 
#            'Artisan.property_name is expected to use the '
#            '_del_property_name method as its deleter-method'
#        )

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testArtisan
    )
)

@testco_objectsCodeCoverage.AddMethodTesting
@testco_objectsCodeCoverage.AddPropertyTesting
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

    def testmatches(self):
        # Tests the matches method of the Product class
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
        SaveTestReport(results, 'hms_core.co_objects',
            'hms_core.co_objects.test-results')
