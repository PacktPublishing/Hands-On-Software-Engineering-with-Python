#!/usr/bin/env python

from hms_core.data_storage import HMSMongoDataObject, DatastoreConfig

class ExampleObject(HMSMongoDataObject):

    _data_dict_keys = (
        'name', 'description', 'cost', 'oid', 'created', 'modified', 
        'is_active', 'is_deleted'
    )

    def __init__(self, name=None, description=None, cost=0, 
        oid=None, created=None, modified=None, is_active=None, 
        is_deleted=None, is_dirty=None, is_new=None
    ):
        HMSMongoDataObject.__init__(
            self, oid, created, modified, is_active, is_deleted, 
            is_dirty, is_new
        )
        self.name = name
        self.description = description
        self.cost = cost

    def __str__(self):
        return '<%s oid: %s>' % (self.__class__.__name__, self.oid)

    def matches(self, **criteria):
        return HMSMongoDataObject.matches(self, **criteria)

    def to_data_dict(self):
        return {
            # - "local" properties
            'name':self.name,
            'description':self.description,
            'cost':self.cost,
            # - standard items from HMSMongoDataObject/BaseDataObject
            'created':self.created.strftime(self.__class__._data_time_string),
            'is_active':self.is_active,
            'is_deleted':self.is_deleted,
            'modified':self.modified.strftime(self.__class__._data_time_string),
            'oid':str(self.oid),
        }

    @classmethod
    def sort(cls, objects, sorty_by):
        pass

if __name__ == '__main__':

    HMSMongoDataObject.configure(
        DatastoreConfig(database='demo_data')
    )

    print('Creating data-objects to demo with')
    names = ['Alice', 'Bob', 'Carl', 'Doug']
    costs = [1, 2, 3]
    descriptions = [None, 'Description']
    all_oids = []
    for name in names:
        for description in descriptions:
            for cost in costs:
                item = ExampleObject(
                    name=name, description=description, cost=cost
                )
                item.save()
