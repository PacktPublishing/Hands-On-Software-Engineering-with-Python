#!/usr/bin/env python
"""
Provides classes and functionality for augmenting the standard unit-
testing capabilities and functionality of the unittest module.
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
    'PrintTestResults',
    'SaveTestReport',
    # ABC "interface" classes
    # ABC abstract classes
    # Concrete classes
    'ModuleCoverageTest',
]

#######################################
# Module metadata/dunder-names        #
#######################################

__author__  = 'Brian D. Allbee'
__version__ = '0.1'
__copyright__ = 'Copyright 2018, Some rights reserved by Brian D. Allbee'
__license__ = (
    'This work is licensed under a Creative Commons Attribution-'
    'ShareAlike 4.0 International License '
    '(http://creativecommons.org/licenses/by-sa/4.0/).'
)
__credits__ = ['Brian D. Allbee']
__maintainer__ = 'Brian D. Allbee'
__email__ = 'brian.allbee+idic.unit_testing@gmail.com'
__status__ = 'Beta'

#######################################
# Standard library imports needed     #
#######################################

import inspect
import sys
import unittest

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

def PrintTestResults(results):
    """Prints the results of a unit-test run when passed a TestResult object."""
    print('#'*80)
    print('Unit-test results')
    print('#'*80)
    print('Tests were successful ..... %s' % (results.wasSuccessful()))
    print('Number of tests run ....... %s' % (results.testsRun))
    try:
        print(' + Tests ran in ........... %0.2f seconds' % (results.runTime))
    except AttributeError:
        print('No test run-time available.')
    print('Number of errors .......... %s' % (len(results.errors)))
    print('Number of failures ........ %s' % (len (results.failures)))
    print('Number of tests skipped ... %s' % (len (results.skipped)))
    print('#'*80)
    if results.skipped:
        print("SKIPPED")
        print('#' + '-'*78 + '#')
        itemCount = 0
        for theError in results.skipped:
            print(('%s\n - %s' % theError).strip())
        print('#'*80)
    if results.failures:
        print("FAILURES")
        print('#' + '-'*78 + '#')
        itemCount = 0
        for theError in results.failures:
            itemCount += 1
            print(('%s\n - %s' % theError).strip())
            if itemCount != len(results.failures):
                print('#' + '-'*78 + '#')
        print('#'*80)
    if results.errors:
        print("ERRORS")
        print('#' + '-'*78 + '#')
        itemCount = 0
        for theError in results.errors:
            itemCount += 1
            print(theError[1].strip())
            if itemCount != len(results.errors):
                print('#' + '-'*78 + '#')
        print('#'*80)
    if results.failures or results.errors:
        print('Unit-test results')
        print('#'*80)
        print('Tests were successful ..... %s' % (results.wasSuccessful()))
        print('Number of tests run ....... %s' % (results.testsRun))
        try:
            print(' + Tests ran in ........... %0.2f seconds' % (results.runTime))
        except AttributeError:
            print('No test run-time available.')
        print('Number of errors .......... %s' % (len(results.errors)))
        print('Number of failures ........ %s' % (len (results.failures)))
        print('Number of tests skipped ... %s' % (len (results.skipped)))
        print('#'*80)

def SaveTestReport(results, name, filePath):
    """
Writes the results of a unit-test run when passed a TestResult object.
"""
    fp = open(filePath, 'w')
    fp.write("""
################################################################################
Unit-test Results: %s
#------------------------------------------------------------------------------#
Tests were SUCCESSFUL
Number of tests run ....... %d
Number of tests skipped ... %d
""" % (name, results.testsRun, len(results.skipped)))
    try:
        fp.write('Tests ran in .......... %0.3f seconds\n' % (
            results.runTime)
    )
    except AttributeError:
        pass
    if results.skipped:
        fp.write('#' + '-'*78 + '#\n')
        fp.write('List of skipped tests and the reasons they were skipped:\n')
        for skip in results.skipped:
            fp.write('%s\n - %s\n' % skip)
    fp.write('#' * 80)
    fp.close()

#######################################
# ABC "interface" classes             #
#######################################

#######################################
# Abstract classes                    #
#######################################

#######################################
# Concrete classes                    #
#######################################

class ModuleCoverageTest(unittest.TestCase):
    """
A reusable unit-test that checks to make sure that all classes in the 
module being tested have corresponding test-case classes in the 
unit-test module where the derived class is defined.
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    # - Class constants that point to the namespace and module 
    #   being tested
    _testNamespace = None
    _testModule = None

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

#     property_name = property(
#         # TODO: Remove setter and deleter if access is not needed
#         _get_property_name, _set_property_name, _del_property_name, 
#         'Gets, sets or deletes the property_name (str) of the instance'
#  )

    ###################################
    # Object initialization           #
    ###################################

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Instance methods                #
    ###################################

    def testCodeCoverage(self):
        if not self.__class__._testModule:
            return
        self.assertEqual([], self._missingTestCases, 
            'Unit-testing policies require test-cases for all classes '
            'and functions in the %s module, but the following have not '
            'been defined: (%s)' % (
                self.__class__._testModule.__name__, 
                ', '.join(self._missingTestCases)
            )
        )

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    @classmethod
    def AddMethodTesting(cls, target):
        if cls.__name__ == 'ModuleCoverageTest':
            raise RuntimeError('ModuleCoverageTest should be extended '
                'into a local test-case class, not used as one directly.')
        if not cls._testModule:
            raise AttributeError('%s does not have a _testModule defined '
                'as a class attribute. Check that the decorator-method is '
                'being called from the extended local test-case class, not '
                'from ModuleCoverageTest itself.' % (cls.__name__))
        try:
            if cls._methodTestsByClass:
                populate = False
            else:
                populate = True
        except AttributeError:
            populate = True
        if populate:
            cls.setUpClass()
        def testMethodCoverage(self):
            requiredTestMethods = cls._methodTestsByClass[target.__name__]
#            print '###### requiredTestMethods: %s' % requiredTestMethods
            activeTestMethods = set(
                [
                    m[0] for m in 
                    inspect.getmembers(target, inspect.isfunction)
                    if m[0][0:4] == 'test'
                ]
            )
            missingMethods = sorted(
                requiredTestMethods.difference(activeTestMethods)
            )
            self.assertEqual([], missingMethods, 
                'Unit-testing policy requires test-methods to be created for '
                'all public and protected methods, but %s is missing the '
                'following test-methods: %s' % (
                    target.__name__, missingMethods
                )
            )
        target.testMethodCoverage = testMethodCoverage
        return target

    @classmethod
    def AddPropertyTesting(cls, target):
        if cls.__name__ == 'ModuleCoverageTest':
            raise RuntimeError('ModuleCoverageTest should be extended '
                'into a local test-case class, not used as one directly.')
        if not cls._testModule:
            raise AttributeError('%s does not have a _testModule defined '
                'as a class attribute. Check that the decorator-method is '
                'being called from the extended local test-case class, not '
                'from ModuleCoverageTest itself.' % (cls.__name__))
        try:
            if cls._propertyTestsByClass:
                populate = False
            else:
                populate = True
        except AttributeError:
            populate = True
        if populate:
            cls.setUpClass()
        def testPropertyCoverage(self):
            requiredTestMethods = cls._propertyTestsByClass[target.__name__]
#            print '###### requiredTestMethods: %s' % requiredTestMethods
            activeTestMethods = set(
                [
                    m[0] for m in 
                    inspect.getmembers(target, inspect.isfunction)
                    if m[0][0:4] == 'test'
                ]
            )
            missingMethods = sorted(
                requiredTestMethods.difference(activeTestMethods)
            )
            self.assertEqual([], missingMethods, 
                'Unit-testing policy requires test-methods to be created for '
                'all public properties, but %s is missing the following test-'
                'methods: %s' % (target.__name__, missingMethods)
            )
        target.testPropertyCoverage = testPropertyCoverage
        return target

    @classmethod
    def setUpClass(cls):
        if not cls._testModule:
            cls._missingTestCases = []
            return
        # Get all the classes available in the module
        cls._moduleClasses = inspect.getmembers(
            cls._testModule, inspect.isclass)
        # Get all the functions available in the module
        cls._moduleFunctions = inspect.getmembers(
            cls._testModule, inspect.isfunction)
        # Collect all the *LOCAL* items
        cls._testModuleName = cls._testModule.__name__
        # Find and keep track of all of the test-cases that relate to 
        # classes in the module being tested
        cls._classTests = dict(
            [
                ('test%s' % m[0], m[1]) 
                for m in cls._moduleClasses
                if m[1].__module__ == cls._testModuleName
            ]
        )
        # Ditto for the functions in the module being tested
        cls._functionTests = dict(
            [
                ('test%s' % m[0], m[1]) 
                for m in cls._moduleFunctions
                if m[1].__module__ == cls._testModuleName
            ]
        )
        # The list of required test-case class-names is the aggregated 
        # list of all class- and function-test-case-class names
        cls._requiredTestCases = sorted(
            list(cls._classTests.keys()) + list(cls._functionTests.keys())
        )
        # Find and keep track of all of the actual test-case classes in 
        # the module the class resides in
        cls._actualTestCases = dict(
            [
                item for item in 
                inspect.getmembers(inspect.getmodule(cls), 
                  inspect.isclass) 
                if item[1].__name__[0:4] == 'test'
                and issubclass(item[1], unittest.TestCase)
            ]
        )
        # Calculate the missing test-case-class names, for use by 
        # the testCodeCoverage test-method
        cls._missingTestCases = sorted(
            set(cls._requiredTestCases).difference(
                set(cls._actualTestCases.keys())))

        # Calculate the property test-case names for all the 
        # module's classes
        cls._propertyTestsByClass = {}
        for testClass in cls._classTests:
            cls._propertyTestsByClass[testClass] = set()
            sourceClass = cls._classTests[testClass]
            sourceMRO = list(sourceClass.__mro__)
            sourceMRO.reverse()
            # Get all the item's properties
            properties = [
                member for member in inspect.getmembers(
                    sourceClass, inspect.isdatadescriptor)
                if member[0][0:2] != '__'
            ]
            # Create and populate data-structures that keep track of where 
            # property-members originate from, and what their implementation 
            # looks like. Initially populated with None values:
            propSources = {}
            propImplementations = {}
            for name, value in properties:
                propSources[name] = None
                propImplementations[name] = None
            for memberName in propSources:
                implementation = sourceClass.__dict__.get(memberName)
                if implementation \
                    and propImplementations[memberName] != implementation:
                    propImplementations[memberName] = implementation
                    propSources[memberName] = sourceClass
            cls._propertyTestsByClass[testClass] = set(
                [
                    'test%s' % key for key in propSources 
                    if propSources[key] == sourceClass
                ]
            )

        # Calculate the method test-case names for all the module's classes
        cls._methodTestsByClass = {}
        for testClass in cls._classTests:
            cls._methodTestsByClass[testClass] = set()
            sourceClass = cls._classTests[testClass]
            sourceMRO = list(sourceClass.__mro__)
            sourceMRO.reverse()
            # Get all the item's methods
            methods = [
                member for member in inspect.getmembers(
                    sourceClass, inspect.ismethod)
            ] + [
                member for member in inspect.getmembers(
                    sourceClass, inspect.isfunction)
            ]
            # Create and populate data-structures that keep track of where 
            # method-members originate from, and what their implementation 
            # looks like. Initially populated with None values:
            methSources = {}
            methImplementations = {}
            for name, value in methods:
                if name.startswith('_%s__' % sourceClass.__name__):
                    # Locally-defined private method - Don't test it
                    continue
                if hasattr(value, '__isabstractmethod__') \
                    and value.__isabstractmethod__:
                    # Locally-defined abstract method - Don't test it
                    continue
                methSources[name] = None
                methImplementations[name] = None
            for memberName in methSources:
                implementation = sourceClass.__dict__.get(memberName)
                if implementation \
                    and methImplementations[memberName] != implementation:
                    methImplementations[memberName] = implementation
                    methSources[memberName] = sourceClass
            cls._methodTestsByClass[testClass] = set(
                [
                    'test%s' % key for key in methSources 
                    if methSources[key] == sourceClass
                ]
            )

    ###################################
    # Static methods                  #
    ###################################

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
    from pprint import pprint
    pprint(StandardTestValuePolicy.All)

