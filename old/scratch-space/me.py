#!/usr/bin/env python
"""
A collection of classes to demonstrate unit-testing coverage-policy
"""

import abc

__all__ = [
    'Showable', 'Parent', 'Child', 'ChildOverride'
]

class Showable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def show(self):
        pass

class Parent(Showable):

    _lead_len = 33

    prop = property()

    def __init__(self, arg, *args, **kwargs):
        self.arg = arg
        self.args = args
        self.kwargs = kwargs

    def public(self):
        return (
            ('%s.arg [public] ' % self.__class__.__name__).ljust(
                self.__class__._lead_len, '.') + ' %s' % self.arg
            )

    def _protected(self):
        return (
            ('%s.arg [protected] ' % self.__class__.__name__).ljust(
                self.__class__._lead_len, '.') + ' %s' % self.arg
            )

    def __private(self):
        return (
            ('%s.arg [private] ' % self.__class__.__name__).ljust(
                self.__class__._lead_len, '.') + ' %s' % self.arg
            )

    def show(self):
        print(self.public())
        print(self._protected())
        print(self.__private())

class Child(Parent):
    pass

class ChildOverride(Parent):

    def public(self):
        return (
            ('%s.arg [PUBLIC] ' % self.__class__.__name__).ljust(
                self.__class__._lead_len, '.') + ' %s' % self.arg
            )

    def _protected(self):
        return (
            ('%s.arg [PROTECTED] ' % self.__class__.__name__).ljust(
                self.__class__._lead_len, '.') + ' %s' % self.arg
            )

    def __private(self):
        return (
            ('%s.arg [PRIVATE] ' % self.__class__.__name__).ljust(
                self.__class__._lead_len, '.') + ' %s' % self.arg
            )

if __name__ == '__main__':
    p = Parent('parent', 1, 2, 3, key='value')
    p.show()

    c = Child('child', 1, 2, 3, key='value')
    c.show()

    co = ChildOverride('child-override', 1, 2, 3, key='value')
    co.show()
