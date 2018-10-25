#!/usr/bin/env python
"""
An example of public, protected and private class-members
"""

import sys

print('='*72)
print('Python version: %s' % sys.version)
print('='*72)

class ExampleParent:

    def __init__(self):
        pass

    def public_method(self, arg, *args, **kwargs):
        print('%s.public_method called:' % self.__class__.__name__)
        print('+- arg ...... %s' % arg)
        print('+- args ..... %s' % str(args))
        print('+- kwargs ... %s' % kwargs)

    def _protected_method(self, arg, *args, **kwargs):
        print('%s._protected_method called:' % self.__class__.__name__)
        print('+- arg ...... %s' % arg)
        print('+- args ..... %s' % str(args))
        print('+- kwargs ... %s' % kwargs)

    def __private_method(self, arg, *args, **kwargs):
        print('%s.__private_method called:' % self.__class__.__name__)
        print('+- arg ...... %s' % arg)
        print('+- args ..... %s' % str(args))
        print('+- kwargs ... %s' % kwargs)

    def show(self):
        self.public_method('example public', 1, 2, 3, key='value')
        self._protected_method('example "protected"', 1, 2, 3, key='value')
        self.__private_method('example "private"', 1, 2, 3, key='value')

class ExampleChild(ExampleParent):
    pass

parent = ExampleParent()
parent.show()
print('-'*72)
print(dir(ExampleParent))
print('-'*72)
child = ExampleChild()
child.show()
print('-'*72)
print(dir(ExampleChild))
print('='*72)
