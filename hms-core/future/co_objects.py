# These are stubs for data-object classes that aren't "in play" yet.

class Customer(BaseCustomer, HMSMongoDataObject):
    """
Represents a Customer in the context of the central office 
applications and services
"""
    ###################################
    # Class attributes/constants      #
    ###################################

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
#     )

    ###################################
    # Object initialization           #
    ###################################

    # TODO: Add and document arguments if/as needed
    def __init__(self,
        # - Arguments from HMSMongoDataObject
        oid:(UUID,str,None)=None, 
        created:(datetime,str,float,int,None)=None, 
        modified:(datetime,str,float,int,None)=None,
        is_active:(bool,int,None)=None, 
        is_deleted:(bool,int,None)=None,
        is_dirty:(bool,int,None)=None, 
        is_new:(bool,int,None)=None,
    ):
        """
Object initialization.

self .............. (Customer instance, required) The instance to 
                    execute against

oid ............... (UUID|str, optional, defaults to None) The unique 
                    identifier of the object's state-data record in the 
                    back-end data-store
created ........... (datetime|str|float|int, optional, defaults to None) 
                    The date/time that the object was created
modified .......... (datetime|str|float|int, optional, defaults to None) 
                    The date/time that the object was last modified
is_active ......... (bool|int, optional, defaults to None) A flag 
                    indicating that the object is active
is_deleted ........ (bool|int, optional, defaults to None) A flag 
                    indicating that the object should be considered 
                    deleted (and may be in the near future)
is_dirty .......... (bool|int, optional, defaults to None) A flag 
                    indicating that the object's data needs to be 
                    updated in the back-end data-store
is_new ............ (bool|int, optional, defaults to None) A flag 
                    indicating that the object's data needs to be 
                    created in the back-end data-store
"""
        # - Call parent initializers if needed
        BaseCustomer.__init__()
        HMSMongoDataObject.__init__(self, 
            oid, created, modified, is_active, is_deleted, 
            is_dirty, is_new
        )
        # - Set default instance property-values using _del_... methods
        # - Set instance property-values from arguments using 
        #   _set_... methods
        # - Perform any other initialization needed
        pass # Remove this line 

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Instance methods                #
    ###################################

    def matches(self, **criteria) -> (bool,):
        return HMSMongoDataObject.matches(self, **criteria)

    def to_data_dict(self):
        return {
            # - BaseCustomer-derived items
            # - BaseDataObject-derived items
            'created':datetime.strftime(
                self.created, self.__class__._data_time_string
            ),
            'is_active':self.is_active,
            'is_deleted':self.is_deleted,
            'modified':datetime.strftime(
                self.modified, self.__class__._data_time_string
            ),
            'oid':str(self.oid),
        }

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    @classmethod
    def sort(cls, objects:(list,tuple), sort_by:(str,)) -> (list,):
        return BaseDataObject.sort(cls, objects, sort_by)

    ###################################
    # Static methods                  #
    ###################################

class Order(BaseOrder, HMSMongoDataObject):
    """
Represents an Order in the context of the central office 
applications and services
"""
    ###################################
    # Class attributes/constants      #
    ###################################

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
#     )

    ###################################
    # Object initialization           #
    ###################################

    # TODO: Add and document arguments if/as needed
    def __init__(self,
        customer:(BaseCustomer,), 
        # - Arguments from HMSMongoDataObject
        oid:(UUID,str,None)=None, 
        created:(datetime,str,float,int,None)=None, 
        modified:(datetime,str,float,int,None)=None,
        is_active:(bool,int,None)=None, 
        is_deleted:(bool,int,None)=None,
        is_dirty:(bool,int,None)=None, 
        is_new:(bool,int,None)=None, 
        *products
    ):
        """
Object initialization.

self .............. (Order instance, required) The instance to 
                    execute against
customer .......... (BaseCustomer, required) The customer that placed 
                    the order
oid ............... (UUID|str, optional, defaults to None) The unique 
                    identifier of the object's state-data record in the 
                    back-end data-store
created ........... (datetime|str|float|int, optional, defaults to None) 
                    The date/time that the object was created
modified .......... (datetime|str|float|int, optional, defaults to None) 
                    The date/time that the object was last modified
is_active ......... (bool|int, optional, defaults to None) A flag 
                    indicating that the object is active
is_deleted ........ (bool|int, optional, defaults to None) A flag 
                    indicating that the object should be considered 
                    deleted (and may be in the near future)
is_dirty .......... (bool|int, optional, defaults to None) A flag 
                    indicating that the object's data needs to be 
                    updated in the back-end data-store
is_new ............ (bool|int, optional, defaults to None) A flag 
                    indicating that the object's data needs to be 
                    created in the back-end data-store
products .......... (list or tuple of BaseProduct instances) The 
                    products that were ordered
"""
        # - Call parent initializers if needed
        BaseOrder.__init__()
        HMSMongoDataObject.__init__(self, 
            oid, created, modified, is_active, is_deleted, 
            is_dirty, is_new
        )
        # - Set default instance property-values using _del_... methods
        # - Set instance property-values from arguments using 
        #   _set_... methods
        # - Perform any other initialization needed
        pass # Remove this line 

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Instance methods                #
    ###################################

#     def instance_method(self, arg:str, *args, **kwargs):
#         """TODO: Document method
# DOES_WHATEVER
# 
# self .............. (Order instance, required) The instance to 
#                     execute against
# arg ............... (str, required) The string argument
# *args ............. (object*, optional) The arglist
# **kwargs .......... (dict, optional) keyword-args, accepts:
#  - kwd_arg ........ (type, optional, defaults to SOMETHING) The SOMETHING 
#                     to apply
# """
#         pass

    def to_data_dict(self):
        return {
            # - BaseOrder-derived items
            # - BaseDataObject-derived items
            'created':datetime.strftime(
                self.created, self.__class__._data_time_string
            ),
            'is_active':self.is_active,
            'is_deleted':self.is_deleted,
            'modified':datetime.strftime(
                self.modified, self.__class__._data_time_string
            ),
            'oid':str(self.oid),
        }

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    ###################################
    # Static methods                  #
    ###################################

