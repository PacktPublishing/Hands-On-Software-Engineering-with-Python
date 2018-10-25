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

class TestValues(list, object):
    """
Represents a collection of standard test-values, and provides filtering of 
those values."""
    #####################################
    # Class attributes (and instance-   #
    # attribute default values)         #
    #####################################

    #####################################
    # Instance property-getter methods  #
    #####################################

    def _GetAll(self):
        """
Gets the complete collection of all available test-values"""
        return self._valueSource.All

    def _GetValueSource(self):
        """
Gets the source of all available standard test-values"""
        return self._valueSource

    # -- Boolean property-getters------------#
    def _GetBoolean(self):
        """
Gets the current test-values that evaluate to True or False when used 
in comparison logic"""
        checkValues = (self.ValueSource._defaults['bools'] + 
            self.ValueSource._defaults['trueish'] + 
            self.ValueSource._defaults['falseish']
        )
        newValues = [v for v in self if v in checkValues]
        self._checkValues(newValues, 'Boolean')
        return self.__class__(self.ValueSource, newValues)

    def _GetStrict(self):
        """
Gets the current test-values that are True or False"""
        newValues = [v for v in self if v in (True, False)]
        self._checkValues(newValues, 'Strict')
        return self.__class__(self.ValueSource, newValues)

    def _GetStrictAndNone(self):
        """
Gets the current test-values that are True, False, or None"""
        newValues = [v for v in self if v in (True, False, None)]
        self._checkValues(newValues, 'StrictAndNone')
        return self.__class__(self.ValueSource, newValues)

    def _GetStrictAndNumeric(self):
        """
Gets the current test-values that are True, False, or any numeric 
value that is equivalent to True or False"""
        newValues = [
            v for v in self 
            if v in (True, False, 1, 0, 1.0, 0.0)
       ]
        self._checkValues(newValues, 'StrictAndNumeric')
        return self.__class__(self.ValueSource, newValues)

    def _GetStrictNumericNone(self):
        """
Gets the current test-values that are True, False, None, or any numeric 
value that is equivalent to True or False"""
        newValues = [
            v for v in self 
            if v in (True, False, None, 1, 0, 1.0, 0.0)
       ]
        self._checkValues(newValues, 'StrictNumericNone')
        return self.__class__(self.ValueSource, newValues)


    # -- Numeric property-getters------------#
    def _GetNumeric(self):
        """
Gets the current test-values that are numeric values (float, int or long types)"""
        newValues = [
            v for v in self 
            if type(v) in (int, float, long)
        ]
        self._checkValues(newValues, 'Numeric')
        return self.__class__(self.ValueSource, newValues)

    def _GetFloats(self):
        """
Gets the current test-values that are float-type numeric values"""
        newValues = [
            v for v in self 
            if type(v) == float
        ]
        self._checkValues(newValues, 'Floats')
        return self.__class__(self.ValueSource, newValues)

    def _GetIntegers(self):
        """
Gets the current test-values that are int-type numeric values"""
        newValues = [
            v for v in self 
            if type(v) == int
        ]
        self._checkValues(newValues, 'Integers')
        return self.__class__(self.ValueSource, newValues)

    def _GetEven(self):
        """
Gets the current test-values that are even numbers (int and long-int types only)"""
        newValues = [
            v for v in self 
            if type(v) in (int, long) 
            and v % 2 == 0
        ]
        self._checkValues(newValues, 'Even')
        return self.__class__(self.ValueSource, newValues)

    def _GetNegative(self):
        """
Gets the current test-values that are negative numeric values"""
        newValues = [
            v for v in self 
            if v < 0
        ]
        self._checkValues(newValues, 'Negative')
        return self.__class__(self.ValueSource, newValues)

    def _GetNonNegative(self):
        """
Gets the current test-values that are non-negative numeric values"""
        newValues = [
            v for v in self 
            if v >= 0
        ]
        self._checkValues(newValues, 'NonNegative')
        return self.__class__(self.ValueSource, newValues)

    def _GetNonPositive(self):
        """
Gets the current test-values that are non-positive numeric values"""
        newValues = [
            v for v in self 
            if v <= 0
        ]
        self._checkValues(newValues, 'NonPositive')
        return self.__class__(self.ValueSource, newValues)

    def _GetNonZero(self):
        """
Gets the current test-values that are non-zero numeric values"""
        newValues = [
            v for v in self 
            if v != 0
        ]
        self._checkValues(newValues, 'NonZero')
        return self.__class__(self.ValueSource, newValues)

    def _GetOdd(self):
        """
Gets the current test-values that are odd numbers (int and long-int types only)"""
        newValues = [
            v for v in self 
            if type(v) in (int, long) 
            and v % 2 == 1
        ]
        self._checkValues(newValues, 'Odd')
        return self.__class__(self.ValueSource, newValues)

    def _GetPositive(self):
        """
Gets the current test-values that are negative numeric values"""
        newValues = [
            v for v in self 
            if v > 0
        ]
        self._checkValues(newValues, 'Positive')
        return self.__class__(self.ValueSource, newValues)

    def _GetZero(self):
        """
Gets the current test-values that are numeric values equal to zero"""
        newValues = [
            v for v in self 
            if v == 0
        ]
        self._checkValues(newValues, 'Zero')
        return self.__class__(self.ValueSource, newValues)


    # -- Text property-getters---------------#
    def _GetText(self):
        """
Gets the current test-values that are str- or unicode-type text-values"""
        newValues = [
            v for v in self 
            if type(v) == str
        ]
        self._checkValues(newValues, 'Text')
        return self.__class__(self.ValueSource, newValues)

    def _GetStrings(self):
        """
Gets the current test-values that are str-type text-values"""
        newValues = [
            v for v in self 
            if type(v) == str
        ]
        self._checkValues(newValues, 'Strings')
        return self.__class__(self.ValueSource, newValues)

    def _GetUnicodes(self):
        """
Gets the current test-values that are unicode-type text-values"""
        newValues = [
            v for v in self 
            if type(v) == unicode
        ]
        self._checkValues(newValues, 'Unicodes')
        return self.__class__(self.ValueSource, newValues)

    def _GetEmpty(self):
        """
Gets the current test-values that are empty str- or unicode-values"""
        newValues = [
            v for v in self 
            if v == ''
        ]
        self._checkValues(newValues, 'Empty')
        return self.__class__(self.ValueSource, newValues)

    def _GetHasText(self):
        """
Gets the current test-values that are CRITERIA"""
        # TODO: Implement me
        raise NotImplementedError('%s.HasText has not been implemented '
            'yet' % (self.__class__.__name__))

    def _GetMultiline(self):
        """
Gets the current test-values that are str- or unicode-type values that have at 
least one line-break or carriage-return in them"""
        newValues = [
            v for v in self 
            if type(v) in  (str, unicode)
            and (
                len(v.split('\n')) > 1
                or
                len(v.split('\r')) > 1
            )
        ]
        self._checkValues(newValues, 'Multiline')
        return self.__class__(self.ValueSource, newValues)

    def _GetNoSpaces(self):
        """
Gets the current test-values that have no spaces in them"""
        newValues = [
            v for v in self 
            if type(v) in  (str, unicode)
            and len(v.split(' ')) == 1
        ]
        self._checkValues(newValues, 'NoSpaces')
        return self.__class__(self.ValueSource, newValues)

    def _GetNoTabs(self):
        """
Gets the current test-values that have no tab-characters in them"""
        newValues = [
            v for v in self 
            if type(v) in  (str, unicode)
            and len(v.split('\t')) == 1
        ]
        self._checkValues(newValues, 'NoTabs')
        return self.__class__(self.ValueSource, newValues)

    def _GetNotEmpty(self):
        """
Gets the current test-values that are non-empty str- or unicode-values"""
        newValues = [
            v for v in self 
            if type(v) == str
            and v != ''
        ]
        self._checkValues(newValues, 'NotEmpty')
        return self.__class__(self.ValueSource, newValues)

    def _GetSingleLine(self):
        """
Gets the current test-values that are str- or unicode-type values that have 
no line-breaks or carriage-returns in them"""
        newValues = [
            v for v in self 
            if type(v) == str
            and len(v.split('\n')) == 1
            and len(v.split('\r')) == 1
        ]
        self._checkValues(newValues, 'SingleLine')
        return self.__class__(self.ValueSource, newValues)

    def _GetTagName(self):
        """
Gets the current test-values that are CRITERIA"""
        # TODO: Implement me
        raise NotImplementedError('%s.TagName has not been implemented '
            'yet' % (self.__class__.__name__))

    #####################################
    # Instance property-setter methods  #
    #####################################

    def _SetValueSource(self, value):
        """
Sets the source of all available standard test-values"""
        if not isinstance(value, _UnitTestValuePolicy):
            raise TypeError('%s expects an instance of '
                '_UnitTestValuePolicy for its ValueSource property, but '
                'was passed "%s" (%s)' % (
                    self.__class__.__name__, value, 
                    type(value).__name__
                )
            )
        self._valueSource = value

    #####################################
    # Instance property-deleter methods #
    #####################################

    def _DelValueSource(self):
        """
Deletes the source of all available standard test-values by setting it to None"""
        self._valueSource = None

    #####################################
    # Instance Properties               #
    #####################################

    All = property(
        _GetAll, None, None, 
        'Gets the complete collection of all available test-values'
    )

    ValueSource = property(
        _GetValueSource, None, None, 
        'Gets the source of all available standard test-values'
    )

    # -- Boolean properties------------------#
    Boolean = property(
        _GetBoolean, None, None, 
        'Gets the current test-values that evaluate to True or False '
        'when used in comparison logic'
    )
    Strict = property(
        _GetStrict, None, None, 
        'Gets the current test-values that are True or False'
    )
    StrictAndNone = property(
        _GetStrictAndNone, None, None, 
        'Gets the current test-values that are True, False, or None'
    )
    StrictAndNumeric = property(
        _GetStrictAndNumeric, None, None, 
        'Gets the current test-values that are True, False, or any '
        'numeric value that is equivalent to True or False'
    )
    StrictNumericNone = property(
        _GetStrictNumericNone, None, None, 
        'Gets the current test-values that are True, False, None, or '
        'any numeric value that is equivalent to True or False'
    )

    # -- Numeric properties------------------#
    Numeric = property(
        _GetNumeric, None, None, 
        'Gets the current test-values that are numbers (int, long or '
        'float types)'
    )
    Floats = property(
        _GetFloats, None, None, 
        'Gets the current test-values that are float-type numbers'
    )
    Integers = property(
        _GetIntegers, None, None, 
        'Gets the current test-values that are int-type numbers'
    )
    Even = property(
        _GetEven, None, None, 
        'Gets the current test-values that are even numbers (int types '
        'only)',
    )
    Negative = property(
        _GetNegative, None, None, 
        'Gets the current test-values that are negative numeric values'
    )
    NonNegative = property(
        _GetNonNegative, None, None, 
        'Gets the current test-values that are non-negative numeric '
        'values'
    )
    NonPositive = property(
        _GetNonPositive, None, None, 
        'Gets the current test-values that are non-positive numeric '
        'values'
    )
    NonZero = property(
        _GetNonZero, None, None, 
        'Gets the current test-values that are non-zero values',
    )
    Odd = property(
        _GetOdd, None, None, 
        'Gets the current test-values that are odd numbers (int types '
        'only)',
    )
    Positive = property(
        _GetPositive, None, None, 
        'Gets the current test-values that are positive numeric values',
    )
    Zero = property(
        _GetZero, None, None, 
        'Gets the current test-values that are numeric and equal to zero',
    )

    # -- Text properties---------------------#
    Text = property(
        _GetText, None, None, 
        'Gets the current test-values that are str- or unicode-type '
        'text-values'
    )
    Strings = property(
        _GetStrings, None, None, 
        'Gets the current test-values that are str-type text-values'
    )
    Unicodes = property(
        _GetUnicodes, None, None, 
        'Gets the current test-values that are unicode-type text-values'
    )
    Empty = property(
        _GetEmpty, None, None, 
        'Gets the current test-values that are empty str-values'
    )
    HasText = property(
        _GetHasText, None, None, 
        'Gets the current test-values that are CRITERIA'
    )
    Multiline = property(
        _GetMultiline, None, None, 
        'Gets the current test-values that are str- or unicode-type '
        'values that have at least one line-break or carriage-return in '
        'them'
    )
    NoSpaces = property(
        _GetNoSpaces, None, None, 
        'Gets the current test-values that have no spaces in them'
    )
    NoTabs = property(
        _GetNoTabs, None, None, 
        'Gets the current test-values that have no tab-characters in them'
    )
    NotEmpty = property(
        _GetNotEmpty, None, None, 
        'Gets the current test-values that are non-empty str-values'
    )
    SingleLine = property(
        _GetSingleLine, None, None, 
        'Gets the current test-values that are str-type values that '
        'have no line-breaks or carriage-returns in them'
    )
    TagName = property(
        _GetTagName, None, None, 
        'Gets the current test-values that are CRITERIA',
    )

    #####################################
    # Instance Initializer              #
    #####################################
    def __init__(self, valueSource, iterable=None):
        """
Instance initializer"""
        # Call parent initializers, if applicable.
        # Set default instance property-values with _Del... methods as needed.
        self._DelValueSource
        # Set instance property values from arguments if applicable.
        self._SetValueSource(valueSource)
        if iterable == None:
            list.__init__(self, self.ValueSource.All)
        elif isinstance(iterable, (list, tuple)):
            list.__init__(self, iterable)
        else:
            raise TypeError('%s expects a list or tuple iterable, or an '
                'instance derived from either, for its iterable argument, '
                'but was passed "%s" (%s)' % (
                self.__class__.__name__, iterable, type(iterable).__name__
              )
          )
        # Other set-up

    #####################################
    # Instance Garbage Collection       #
    #####################################

    #####################################
    # Instance Methods                  #
    #####################################

    def _checkValues(self, newValues, name):
        if not isinstance(newValues, list):
            raise TypeError('%s.%s yielded a non-list value' % (
                self.__class__.__name__, name))
        if len(newValues) == 0:
            raise ValueError('%s.%s yielded an empty list' % (
                self.__class__.__name__, name))

    #####################################
    # Class Methods                     #
    #####################################

    def __add__(self, values):
        """
Override of the "+" operator callback for lists. Returns an instance of the 
class, populated with the members of the original instance, and with the 
provided value appended to it."""
        selfValues = list(self)
        result = self.__class__(self.ValueSource, selfValues + values)
        return result

    def __imul__(self, value):
        """
Override of the "*=" operator callback for lists. Prevents the use of the 
operator on instances of the class."""
        raise RuntimeError('%s does not support the "*=" operator' % (
            self.__class__.__name__))

    def __mul__(self, value):
        """
Override of the "*=" operator callback for lists. Prevents the use of the 
operator on instances of the class."""
        raise RuntimeError('%s does not support the "*=" operator' % (
            self.__class__.__name__))

    def __rmul__(self, value):
        """
Override of the "*=" operator callback for lists. Prevents the use of the 
operator on instances of the class."""
        raise RuntimeError('%s does not support the "*=" operator' % (
            self.__class__.__name__))

    def remove(self, values):
        """
Removes all instances of the value(s) supplied from the members of the 
instance."""
        if isinstance(values, (list, tuple)):
            for value in values:
                while self.count(value) != 0:
                    list.remove(self, value)
        else:
            while self.count(values) != 0:
                list.remove(self, values)

    #####################################
    # Static Class Methods              #
    #####################################

class _UnitTestValuePolicy(object):
    """
Represents a collection of standard unit-testing test-method values to be 
tested."""
    #####################################
    # Class attributes (and instance-   #
    # attribute default values)         #
    #####################################

    _genericObject = object()
    _defaults = {
        'bools':[True, False],
        'falseish':[0.0, 0, None, '', u'', False],
        'floats':[-1.0, 0.0, 1.0, 2.0],
        'ints':[-1, 0, 1, 2],
        'none':[None],
        'objects':[_genericObject],
        'strings':[
            '',
            ' ',
            '\t',
            '\r',
            '\n',
            'word',
            'multiple words',
            'A complete sentence,',
            'Multiple sentences. Separated with punctuation.',
            'String\tcontaining a tab',
            'Multiline\nstring',
       ],
        'trueish':[1.0, 0.5, 1, 'a', u'a', _genericObject, True],
    }

    #####################################
    # Instance property-getter methods  #
    #####################################

    def _GetAll(self):
        try:
            return self._all
        except AttributeError:
            self._all = []
            for key in self._defaults:
                self._all += self._defaults[key]
            return TestValues(self)

    #####################################
    # Instance property-setter methods  #
    #####################################

    #####################################
    # Instance property-deleter methods #
    #####################################

    #####################################
    # Instance Properties               #
    #####################################

    All = property(
        _GetAll, None, None, 
        'the complete collection of all test-values'
    )

    #####################################
    # Instance Initializer              #
    #####################################
    def __init__(self, **values):
        """
Instance initializer"""
        # Call parent initializers, if applicable.
        # Set default instance property-values with _Del... methods as needed.
        # Set instance property values from arguments if applicable.
        # Set _defaults values from **values members, if they are provided
        # - bools
        bools = values.get('bools')
        if bools == None:
            self._defaults['bools'] = self.__class__._defaults['bools']
        else:
            self._defaults['bools'] = bools

        # - falseish
        falseish = values.get('falseish')
        if falseish == None:
            self._defaults['falseish'] = self.__class__._defaults['falseish']
        else:
            self._defaults['falseish'] = falseish

        # - floats
        floats = values.get('floats')
        if floats == None:
            self._defaults['floats'] = self.__class__._defaults['floats']
        else:
            self._defaults['floats'] = floats

        # - ints
        ints = values.get('ints')
        if ints == None:
            self._defaults['ints'] = self.__class__._defaults['ints']
        else:
            self._defaults['ints'] = ints

        # - none
        none = values.get('none')
        if none == None:
            self._defaults['none'] = self.__class__._defaults['none']
        else:
            self._defaults['none'] = none

        # - objects
        objects = values.get('objects')
        if objects == None:
            self._defaults['objects'] = self.__class__._defaults['objects']
        else:
            self._defaults['objects'] = objects

        # - strings
        strings = values.get('strings')
        if strings == None:
            self._defaults['strings'] = self.__class__._defaults['strings']
        else:
            self._defaults['strings'] = strings

        # - trueish
        trueish = values.get('trueish')
        if trueish == None:
            self._defaults['trueish'] = self.__class__._defaults['trueish']
        else:
            self._defaults['trueish'] = trueish

        # Other set-up

    #####################################
    # Instance Garbage Collection       #
    #####################################

    #####################################
    # Instance Methods                  #
    #####################################

    #####################################
    # Class Methods                     #
    #####################################

    #####################################
    # Static Class Methods              #
    #####################################

#######################################
# Initialization needed after member  #
#   definition is complete            #
#######################################

# Define a standard UnitTestValuePolicy constant
StandardTestValuePolicy = _UnitTestValuePolicy()

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

