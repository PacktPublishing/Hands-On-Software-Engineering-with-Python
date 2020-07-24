class HasProducts(metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements, and 
type-identity for objects that can have a common products 
property whose membership is stored and handled in the same 
way.
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_products(self) -> (tuple,):
        return tuple(self._products)

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_products(self, value:(list, tuple)) -> None:
        # - Check first that the value is an iterable - list or 
        #   tuple, it doesn't really matter which, just so long 
        #   as it's a sequence-type collection of some kind.
        if type(value) not in (list, tuple):
            raise TypeError(
                '%s.products expects a list or tuple of BaseProduct '
                'objects, but was passed a %s instead' % 
                (self.__class__.__name__, type(value).__name__)
            )
        # - Start with a new, empty list
        new_items = []
        # - Iterate over the items in value, check each one, and 
        #   append them if they're OK
        bad_items = []
        for item in value:
            # - We're going to assume that all products will derive 
            #   from BaseProduct - That's why it's defined, after all
            if isinstance(item, BaseProduct):
                new_items.append(item)
            else:
                bad_items.append(item)
        # - If there are any bad items, then do NOT commit the 
        #   changes -- raise an error instead!
        if bad_items:
            raise TypeError(
                '%s.products expects a list or tuple of BaseProduct '
                'objects, but the value passed included %d items '
                'that are not of the right type: (%s)' % 
                (
                    self.__class__.__name__, len(bad_items), 
                    ', '.join([str(bi) for bi in bad_items])
                )
            )
        self._products = value

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_products(self) -> None:
        self._products = []

    ###################################
    # Instance property definitions   #
    ###################################

     products = property(
         _get_products, None, None,
         'Gets the products (BaseProduct) of the instance'
     )

    ###################################
    # Object initialization           #
    ###################################

    def __init__(self, *products):
        """
Object initialization.

self .............. (BaseOrder instance, required) The instance to 
                    execute against
products .......... (list or tuple of BaseProduct instances) The 
                    products that were ordered
"""
        # - Call parent initializers if needed
        # - Set default instance property-values using _del_... methods
        self._del_products()
        # - Set instance property-values from arguments using 
        #   _set_... methods
        if products:
            self._set_products(products)
        # - Perform any other initialization needed

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Abstract methods                #
    ###################################

    @abc.abstractmethod
    def add_product(self, product:BaseProduct) -> BaseProduct:
        """
Adds a product to the instance's collection of products.

Returns the product added.

self ....... (HasProducts instance, required) The instance to 
             execute against
product ...  (BaseProduct, required) The product to add to the 
             instance's collection of products

Raises TypeError if the product specified is not a BaseProduct-
  derived instance

May be implemented in derived classes by simply calling
    return HasProducts.add_product(self, product)
"""
        # - Make sure the product passed in is a BaseProduct
        if not isinstance(product, BaseProduct):
            raise TypeError(
                '%s.add_product expects an instance of '
                'BaseProduct to be passed in its product '
                'argument, but "%s" (%s) was passed instead' % 
                (
                    self.__class__.__name__, value, 
                    type(value).__name__
                )
            )
        # - Append it to the internal _products list
        self._products.append(product)
        # - Return it
        return product

    @abc.abstractmethod
    def remove_product(self, product:BaseProduct):
        """
Removes a product from the instance's collection of products.

Returns the product removed.

self ....... (HasProducts instance, required) The instance to 
             execute against
product ...  (BaseProduct, required) The product to remove from 
             the instance's collection of products

Raises TypeError if the product specified is not a BaseProduct-
  derived instance
Raises ValueError if the product specified is not a member of the 
  instance's products collection

May be implemented in derived classes by simply calling
    return HasProducts.remove_product(self, product)
"""
        # - Make sure the product passed in is a BaseProduct.
        #   Technically this may not be necessary, since type 
        #   is enforced in add_product, but it does no harm to 
        #   re-check here...
        if not isinstance(product, BaseProduct):
            raise TypeError(
                '%s.add_product expects an instance of '
                'BaseProduct to be passed in its product '
                'argument, but "%s" (%s) was passed instead' % 
                (
                    self.__class__.__name__, value, 
                    type(value).__name__
                )
            )
        try:
            self._products.remove(product)
            return product
        except ValueError:
            raise ValueError(
                '%s.remove_product could not remove %s from its '
                'products collection because it was not a member '
                'of that collection' % 
                (self.__class__.__name__, product)
            )

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    ###################################
    # Static methods                  #
    ###################################


class BaseArtisan(HasProducts, metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements, and 
type-identity for objects that can represent an Artisan in 
the context of the HMS system.
"""

    def __init__(self, 
        contact_name:str, contact_email:str, 
        address:Address, company_name:str=None, 
        **products
        ):
        """
Object initialization.

self .............. (BaseArtisan instance, required) The instance to 
                    execute against
contact_name ...... (str, required) The name of the primary contact 
                    for the Artisan that the instance represents
contact_email ..... (str [email address], required) The email address 
                    of the primary contact for the Artisan that the 
                    instance represents
address ........... (Address, required) The mailing/shipping address 
                    for the Artisan that the instance represents
company_name ...... (str, optional, defaults to None) The company-
                    name for the Artisan that the instance represents
products .......... (BaseProduct collection) The products associated 
                    with the Artisan that the instance represents
"""
        # - Call parent initializers if needed
        HasProducts.__init__(self, *products)
        # - Set default instance property-values using _del_... methods
        self._del_address()
        self._del_company_name()
        self._del_contact_email()
        self._del_contact_name()
# This can be deleted, or just commented out.
#        self._del_products()
        # - Set instance property-values from arguments using 
        #   _set_... methods
        self._set_contact_name(contact_name)
        self._set_contact_email(contact_email)
        self._set_address(address)
        if company_name:
            self._set_company_name(company_name)
# This also can be deleted, or just commented out.
#        if products:
#            self._set_products(products)
        # - Perform any other initialization needed

