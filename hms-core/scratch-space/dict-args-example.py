#!/usr/bin/env python
"""
Shows how passing keyword-like values, or a dict using a **keywords approach, still works
"""

def example( 
    street_address:(str,), city:(str,), 
    building_address:(str,None)=None, region:(str,None)=None, 
    postal_code:(str,None)=None, country:(str,None)=None
    ):
    print('street_address .............. %s' 
        % street_address)
    print('building_address ............ %s' 
        % building_address)
    print('city, region, postal_code ... %s, %s, %s' 
        % (city, region, postal_code))
    print('country ..................... %s' 
        % country)

example(
    street_address='1234 Main Street', city='Some Town', 
    region='OK', postal_code='00000'
)

my_address = {
    'street_address':'456 South Broadway',
    'building_address':'Suite 234',
    'city':'Nowhereville',
    'region':'WH',
    'postal_code':'B0RT0N',
    'country':'Imaginaria'
}

example(**my_address)
