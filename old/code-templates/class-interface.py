# Remember to import abc!

class InterfaceName(metaclass=abc.ABCMeta):
    """TODO: Document the class.
Provides interface requirements, and type-identity for objects that 
can REPRESENT_SOMETHING
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    ###################################
    # Instance property definitions   #
    ###################################

#     abstract_property = abc.abstractproperty()

    ###################################
    # Object initialization           #
    ###################################

    # TODO: Add and document arguments if/as needed
    def __init__(self):
        """
Object initialization.

self .............. (InterfaceName instance, required) The instance to 
                    execute against
"""
        # - Call parent initializers if needed
        # - Perform any other initialization needed
        pass # Remove this line 

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Abstract methods                #
    ###################################

#     @abc.abstractmethod
#     def instance_method(self, arg:str, *args, **kwargs):
#         """TODO: Document method
# DOES_WHATEVER
# 
# self .............. (InterfaceName instance, required) The 
#                     instance to execute against
# arg ............... (str, required) The string argument
# *args ............. (object*, optional) The arglist
# **kwargs .......... (dict, optional) keyword-args, accepts:
#  - kwd_arg ........ (type, optional, defaults to SOMETHING) The SOMETHING 
#                     to apply
# """
#         pass

    ###################################
    # Class methods                   #
    ###################################

    ###################################
    # Static methods                  #
    ###################################

