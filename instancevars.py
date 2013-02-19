from functools import wraps
import inspect

def make_setter(args, def_args, names, omit):
    # Construct a function definition that will assign values
    # to instance variables
    function_defn = "def _setter(%s): %s" % (
        ", ".join(args + def_args),
        "; ".join(["self.%s = %s" % (name, name) for name in names
                  if name != "self" and name not in omit])
    )

    # Evaluate the string and extract the constructed function object
    tmp_locals = {}
    exec(function_defn, tmp_locals)
    return tmp_locals['_setter']


def instancevars(func=None, omit=[]):
    """
    A function decorator that automatically creates instance variables from
    function arguments. 

    Arguments can be omitted by adding them to the 'omit' list argument of the decorator.
    Names are retained on a one-to-one basis (i.e '_arg' -> 'self._arg'). Passing
    arguments as raw literals, using a keyword, or as defaults all work. If *args and/or
    **kwargs are used by the decorated function, they are not processed and must be handled
    explicitly.  
    """
    if func:
        names, varargs, keywargs, defaults = inspect.getargspec(func)

        if defaults:
            args, def_args = names[:-len(defaults)], names[-len(defaults):]
            def_args = ["%s=%s" % (arg, repr(default)) for arg, default
                        in zip(def_args, defaults)]
        else:
            def_args = []
            args = names

        _setter = make_setter(args, def_args, names, omit)

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            _setter(self, *args, **kwargs)
            func(self, *args, **kwargs)

        return wrapper
    else:
        return lambda func: instancevars(func, omit)
