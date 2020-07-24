@testModuleNameCodeCoverage.AddMethodTesting
@testModuleNameCodeCoverage.AddPropertyTesting
class testClassName(unittest.TestCase):

    ###################################
    # Tests of class methods          #
    ###################################

    def testmethod_name(self):
        # Tests the method_name method of the ClassName class
        # - Test all permutations of "good" argument-values:
        # - Test all permutations of each "bad" argument-value 
        #   set against "good" values for the other arguments:
        self.fail('testmethod_name is not yet implemented')

    ###################################
    # Tests of class properties       #
    ###################################

#    def testproperty_name(self):
#        # Tests the property_name property of the ClassName class
#        # - Assert that the getter is correct:
#        self.assertEqual(
#            ClassName.property_name.fget, 
#            ClassName._get_property_name, 
#            'ClassName.property_name is expected to use the '
#            '_get_property_name method as its getter-method'
#        )
#        # - If property_name is not expected to be publicly settable,
#        #   the second item here (ClassName._set_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the setter is correct:
#        self.assertEqual(
#            ClassName.property_name.fset, 
#            ClassName._set_property_name, 
#            'ClassName.property_name is expected to use the '
#            '_set_property_name method as its setter-method'
#        )
#        # - If property_name is not expected to be publicly deletable,
#        #   the second item here (ClassName._del_property_name) should 
#        #   be changed to None, and the failure message adjusted 
#        #   accordingly:
#        # - Assert that the deleter is correct:
#        self.assertEqual(
#            ClassName.property_name.fdel, 
#            ClassName._del_property_name, 
#            'ClassName.property_name is expected to use the '
#            '_del_property_name method as its deleter-method'
#        )

LocalSuite.addTests(
    unittest.TestLoader().loadTestsFromTestCase(
        testClassName
    )
)

