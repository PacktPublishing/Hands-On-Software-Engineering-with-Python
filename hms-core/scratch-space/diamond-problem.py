class Root:
    def method(self, arg, *args, **kwargs):
        print('Root.method(%s, %s, %s)' % (arg, str(args), kwargs))

class Left(Root):
    def method(self, arg, *args, **kwargs):
        print('Left.method(%s, %s, %s)' % (arg, str(args), kwargs))

class Right(Root):
    def method(self, arg, *args, **kwargs):
        print('Right.method(%s, %s, %s)' % (arg, str(args), kwargs))

class Bottom(Left, Right):
    pass

b = Bottom()
b.method('arg', 'args1', 'args2', keyword='value')
# Outputs "Left.method(arg, ('args1', 'args2'), {'keyword': 'value'})"
