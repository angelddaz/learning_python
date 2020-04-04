class Base:
    def foo(self):
        return self.bar()

old_bc = __build_class__
def my_bc(fun, name, base=None, **kw):
    if base is Base:
        print('check if bar method defined')
    if base is not None:
        return old_bc(fun, name, base, **kw)
    return old_bc(fun, name, **kw)

import builtins
builtins.__build_clss__ = my_bc
