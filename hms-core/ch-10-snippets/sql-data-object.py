# NOTE: This is an example class, NOT INTENDED FOR USE YET!
class HMSSQLDataObject(BaseDataObject, metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements, and 
type-identity for objects that can persist their state-data to 
a (GENERIC) SQL-based RDBMS back-end data-store.
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    # - Keeps track of the global configuration for data-access
    _configuration = None
    # - Keeps track of the keys allowed for object-creation from 
    #   retrieved data
    _data_dict_keys = None
    # - SQL for various expected CRUD actions:
    _sql_create = """Some SQL string goes here"""
    _sql_read_oids = """Some SQL string goes here"""
    _sql_read_all = """Some SQL string goes here"""
    _sql_read_criteria = """Some SQL string goes here"""
    _sql_update = """Some SQL string goes here"""
    _sql_delete = """Some SQL string goes here"""

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_connection(self):
        try:
            return self.__class__._connection
        except AttributeError:
            # - Most RDBMS libraries provide a "connect" function, or 
            #   allow the creation of a "connection" object, using the 
            #   parameters we've named in DatastoreConfig, or simple 
            #   variations of them, so all we need to do is connect:
            self.__class__._connection = RDBMS.connect(
                **self.configuration
            )
            return self.__class__._connection

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_connection(self) -> None:
        try:
            del self.__class__._connection
        except AttributeError:
            # - It may already not exist
            pass

    ###################################
    # Instance property definitions   #
    ###################################

    connection = property(
        _get_connection, None, _del_connection, 
        'Gets or deletes the database-connection that the instance '
        'will use to manage its persistent state-data'
    )

    ###################################
    # Object initialization           #
    ###################################

    def __init__(self, 
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

self .............. (HMSMongoDataObject instance, required) The 
                    instance to execute against
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
        BaseDataObject.__init__(self, 
            oid, created, modified, is_active, is_deleted, 
            is_dirty, is_new
        )
        # - Perform any other initialization needed

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Abstract methods                #
    ###################################

    ###################################
    # Instance methods                #
    ###################################

    def _create(self):
        # - The base SQL is in self.__class__._sql_create, and the 
        #   field-values would be retrieved from self.to_data_dict():
        data_dict = self.to_data_dict()
        SQL = self.__class__._sql_create
        # - Some process would have to add the values, if not the keys, 
        #   into the SQL, and the result sanitized, but once that was 
        #   done, it'd become a simple query-execution:
        self.connection.execute(SQL)

    def _update(self):
        # - The base SQL is in self.__class__._sql_update, and the 
        #   field-values would be retrieved from self.to_data_dict():
        data_dict = self.to_data_dict()
        SQL = self.__class__._sql_update
        # - Some process would have to add the values, if not the keys, 
        #   into the SQL, and the result sanitized, but once that was 
        #   done, it'd become a simple query-execution:
        self.connection.execute(SQL)

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    @classmethod
    def delete(cls, *oids):
        # - First, we need the database-connection that we're 
        #   working with:
        connection = cls.get_connection()
        SQL = cls._sql_delete % oids
        # - Don't forget to sanitize it before executing it!
        result_set = connection.execute(SQL)

    @classmethod
    def get(cls, *oids, **criteria) -> list:
        # - First, we need the database-connection that we're 
        #   working with:
        connection = cls.get_connection()
        # - The first pass of the process retrieves documents based 
        #   on oids or criteria.
        # - We also need to keep track of whether or not to do a 
        #   matches call on the results after the initial data-
        #   retrieval:
        post_filter = False
        # - Records are often returned as a tuple (result_set) 
        #   of tuples (rows) of tuples (field-name, field-value):
        #   ( ..., ( ('field-name', 'value' ), (...), ... ), ...)
        if oids:
            # - Need to replace any placeholder values in the raw SQL
            #   with actual values, AND sanitize the SQL string, but 
            #   it starts with the SQL in cls._sql_read_oids
            SQL = cls._sql_read_oids
            result_set = connection.execute(SQL)
            if criteria:
                post_filter = True
        elif criteria:
            # - The same sort of replacement would need to happen here 
            #   as happens for oids, above. If the query uses just 
            #   one criteria key/value pair initially, we can use the 
            #   match-based filtering later to filter further as needed
            key = criteria.keys()[0]
            value = criteria[key]
            SQL = cls._sql_read_criteria % (key, value)
            result_set = connection.execute(SQL)
            if len(criteria) > 1:
                post_filter = True
        else:
            SQL = cls._sql_read_all
            result_set = connection.execute(SQL)
        # - We should have a result_set value here, so we can convert 
        #   it from the tuple of tuples of tuples (or whatever) into 
        #   data_dict-compatible dictionaries:
        data_dicts = [
            dict(
                [field_tuple for field_tuple in row]
            )
            for row in result_set
        ]
        # - With those, we can create the initial list of instances:
        results = [
            cls.from_data_dict(data_dict) 
            for data_dict in data_dicts
        ]
        # - If post_filter has been set to True, then the request 
        #   was for items by oid *and* that have certain criteria
        if post_filter:
            results = [
                obj for obj in results if obj.matches(**criteria)
            ]
        # - Data-objects that have related child items, like the 
        #   Artisan to Product relationship, may need to acquire 
        #   those children here before returning the results. If 
        #   they do, then a structure like this should work most 
        #   of the time:
#        for artisan in results:
#            artisan._set_products(
#                Product.get(artisan_oid=artisan.oid)
#            )
        return results

    ###################################
    # Static methods                  #
    ###################################

