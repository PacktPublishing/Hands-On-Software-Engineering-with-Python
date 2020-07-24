#!/usr/bin/env python
"""
Executes the project's test-suite
"""

#######################################
# Standard library imports needed     #
#######################################

import os
import sys
import time
import unittest

#######################################
# Third-party imports needed          #
#######################################

#######################################
# Local imports needed                #
#######################################

from idic.unit_testing import *
from test_hms_core import LocalSuite

#######################################
# Module functions                    #
#######################################

def main():
    results = unittest.TestResult()
    testStartTime = time.time()
    LocalSuite.run(results)
    results.runTime = time.time() - testStartTime
    PrintTestResults(results)
    if not results.errors and not results.failures:
        SaveTestReport(results, 'hms_core',
            'hms_core.test-results')
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
