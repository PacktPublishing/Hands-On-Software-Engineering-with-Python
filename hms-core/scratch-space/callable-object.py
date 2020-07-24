class callable_class:
    def __init__(self, some_arg, some_other_arg):
        self._some_arg = some_arg
        self._some_other_arg = some_other_arg

    def __call__(self, arg):
        print('%s("%s") called:' % (self.__class__.__name__, arg))
        print('+- self._some_arg ......... %s' % (self._some_arg))
        print('+- self._some_other_arg ... %s' % (self._some_other_arg))

instance1 = callable_class('instance 1', 'other arg')
instance1('calling instance 1')

instance2 = callable_class(instance1, True)
instance2('calling instance 2')
