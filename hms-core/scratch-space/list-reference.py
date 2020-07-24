#!/usr/bin/env python
"""
Example showing that objects are accessed by reference in collections
"""

# - Create a class to demonstrate with
class Example:
    pass

# -  Create a list of instances of the class
example_list = [
    Example(), Example(), Example(), Example()
]

print('Items in the original list (at %s):' % hex(id(example_list)))
for item in example_list:
    print(item)
print()

# Items in the original list (at 0x7f9cd9ed6a48):
# <__main__.Example object at 0x7f9cd9eed550>
# <__main__.Example object at 0x7f9cd9eed5c0>
# <__main__.Example object at 0x7f9cd9eed5f8>
# <__main__.Example object at 0x7f9cd9eed630>

new_list = list(example_list)
print('Items in the new list (at %s):' % hex(id(new_list)))
for item in new_list:
    print(item)
print()

# Items in the new list (at 0x7f9cd89dca88):
# <__main__.Example object at 0x7f9cd9eed550>
# <__main__.Example object at 0x7f9cd9eed5c0>
# <__main__.Example object at 0x7f9cd9eed5f8>
# <__main__.Example object at 0x7f9cd9eed630>

new_tuple = tuple(example_list)
print('Items in the new tuple (at %s):' % hex(id(new_tuple)))
for item in new_tuple:
    print(item)
print()

# Items in the new tuple (at 0x7f9cd9edd4a8):
# <__main__.Example object at 0x7f9cd9eed550>
# <__main__.Example object at 0x7f9cd9eed5c0>
# <__main__.Example object at 0x7f9cd9eed5f8>
# <__main__.Example object at 0x7f9cd9eed630>
