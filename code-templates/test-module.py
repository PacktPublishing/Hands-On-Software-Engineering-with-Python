#!/usr/bin/env python

# Python unit-test-module template. Copy the template to a new
# unit-test-module location, and start replacing names as needed:
#
# PackagePath  ==> The path/namespace of the parent of the module/package
#                  being tested in this file.
# ModuleName   ==> The name of the module being tested
#
# Then remove this comment-block

"""
Defines unit-tests for the module at PackagePath.ModuleName.
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
# Module-level Constants              #
#######################################

LocalSuite = unittest.TestSuite()

#######################################
# Import the module being tested      #
#######################################

import PackagePath.ModuleName as ModuleName
from PackagePath.ModuleName import *

#######################################
# Code-coverage test-case and         #
# decorator-methods                   #
#######################################

class testModuleNameCodeCoverage(ModuleCoverageTest):
    _testNamespace = 'PackagePath'
    _testModule = ModuleName

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testModuleNameCodeCoverage
   )
)

#######################################
# Test-cases in the module            #
#######################################

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
        SaveTestReport(results, 'PackagePath.ModuleName',
            'PackagePath.ModuleName.test-results')
