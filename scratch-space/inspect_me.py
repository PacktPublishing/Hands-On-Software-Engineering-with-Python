#!/usr/bin/env python
"""
A walk-through of the processes needed to perform automatic 
test-coverage detection and assurance.
"""

import inspect

import me as target_module

target_classes = set([
    member[0] for member in 
    inspect.getmembers(target_module, inspect.isclass)
])
# target_classes = {
#   'Child', 'ChildOverride', 'Parent', 'Showable'
# } at this point

expected_cases = set([
    'test%s' % class_name 
    for class_name in target_classes
    ]
)
# expected_cases = {
#   'testChild', 'testShowable', 'testChildOverride', 
#   'testParent'
# } at this point

import unittest

import test_me as test_module

test_cases = set([
    member[0] for member in 
    inspect.getmembers(test_module, inspect.isclass)
    if issubclass(member[1], unittest.TestCase)
])
# test_cases, before any TestCase classes have been defined, 
# is an empty set

missing_tests = expected_cases.difference(test_cases)
# missing_tests = {
#   'testShowable', 'testChild', 'testParent', 
#   'testChildOverride'
# }
if missing_tests:
    print(
        'Test-policies require test-case classes to be '
        'created for each class in the codebase. The '
        'following have not been created:\n * %s' % 
        '\n * '.join(missing_tests)
    )

target_class = target_module.Parent

from pprint import pprint
import json

property_tests = set()
sourceMRO = list(target_class.__mro__)
sourceMRO.reverse()
# Get all the item's properties
properties = [
    member for member in inspect.getmembers(
        target_class, inspect.isdatadescriptor)
    if member[0][0:2] != '__'
]
# sourceMRO = [
#   <class 'object'>, <class 'me.Showable'>, 
#   <class 'me.Parent'>
# ]
# Create and populate data-structures that keep track of where 
# property-members originate from, and what their implementation 
# looks like. Initially populated with None values:
propSources = {}
propImplementations = {}
for name, value in properties:
    propSources[name] = None
    propImplementations[name] = None
# Populate the dictionaries based on the names found
for memberName in propSources:
    implementation = target_class.__dict__.get(memberName)
    if implementation and propImplementations[memberName] != implementation:
        propImplementations[memberName] = implementation
        propSources[memberName] = target_class
# propImplementations = {
#   "prop": <property object at 0x7fa2f0edeb38>
# }
# propSources = {
#   "prop": <class 'me.Parent'>
# }
# If the target_class is changed to target_module.Child:
# propImplementations = {
#   "prop": None
# }
# propSources = {
#   "prop": None
# }
property_tests = set(
    [
        'test%s' % key for key in propSources 
        if propSources[key] == target_class
    ]
)
# property_tests = {'testprop'}
# If the target_class is changed to target_module.Child:
# property_tests = set()

target_class = target_module.Showable

method_tests = set()
sourceMRO = list(target_class.__mro__)
sourceMRO.reverse()
# Get all the item's methods
methods = [
    member for member in inspect.getmembers(
        target_class, inspect.isfunction)
] + [
    member for member in inspect.getmembers(
        target_class, inspect.ismethod)
]
# Create and populate data-structures that keep track of where 
# method-members originate from, and what their implementation 
# looks like. Initially populated with None values:
methSources = {}
methImplementations = {}
for name, value in methods:
    if name.startswith('_%s__' % target_class.__name__):
        # Locally-defined private method - Don't test it
        continue
    if hasattr(value, '__isabstractmethod__') and value.__isabstractmethod__:
        # Locally-defined abstract method - Don't test it
        continue
    methSources[name] = None
    methImplementations[name] = None
for memberName in methSources:
    implementation = target_class.__dict__.get(memberName)
    if implementation and methImplementations[memberName] != implementation:
        methImplementations[memberName] = implementation
        methSources[memberName] = target_class
method_tests = set(
    [
        'test%s' % key for key in methSources 
        if methSources[key] == target_class
    ]
)
# method_tests = {
#   'testpublic', 'test__init__', 'test_protected', 
#   'testshow'
# }
# If the target_class is changed to target_module.Child:
# method_tests = set()
# If the target_class is changed to target_module.Showable:
# method_tests = set()
