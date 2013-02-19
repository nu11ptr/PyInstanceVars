from functools import wraps
import inspect

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

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            argnames = names[1:]
            # This works because kwargs must always be last and zip trucates to shortest list
            allargs = list(zip(argnames, args)) + list(kwargs.items())

            for name, arg in allargs:
                if name not in omit:
                    setattr(self, name, arg)

            if len(argnames) > len(allargs) and defaults is not None:
                for i in range(len(defaults)):
                    idx = -(i+1)
                    name = names[idx]
                    if not hasattr(self, name) and name not in omit:
                        setattr(self, name, defaults[idx])

            func(self, *args, **kwargs)

        return wrapper
    else:
        return lambda func: instancevars(func, omit)
