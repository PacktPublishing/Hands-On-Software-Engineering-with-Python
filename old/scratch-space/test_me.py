#!/usr/bin/env python

import unittest

from idic.unit_testing import *

import me

from me import *

class testmeCodeCoverage(ModuleCoverageTest):
    _testModule = me

@testmeCodeCoverage.AddPropertyTesting
@testmeCodeCoverage.AddMethodTesting
class testChild(unittest.TestCase):
    pass

@testmeCodeCoverage.AddPropertyTesting
@testmeCodeCoverage.AddMethodTesting
class testChildOverride(unittest.TestCase):
    pass

@testmeCodeCoverage.AddPropertyTesting
@testmeCodeCoverage.AddMethodTesting
class testParent(unittest.TestCase):
    pass

@testmeCodeCoverage.AddPropertyTesting
@testmeCodeCoverage.AddMethodTesting
class testShowable(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
