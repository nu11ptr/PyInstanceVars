from functools import wraps
import inspect

def instancevars(func):
	"""
	A function decorator that automatically creates instance variables from
	function arguments. Arguments can be omitted by naming them with a
	trailing underscore. Names are retained on a one-to-one basis.
	"""
	names, varargs, keywargs, defaults = inspect.getargspec(func)

	@wraps(func)
	def wrapper(self, *args, **kwargs):
		argnames = names[1:]
		# This works because kwargs must always be last and zip trucates to shortest list
		allargs = zip(argnames, args) + kwargs.items()

		for name, arg in allargs:
			if name[-1] != '_':
				setattr(self, name, arg)

		if len(argnames) > len(allargs) and defaults is not None:
			for i in range(len(defaults)):
				idx = -(i+1)
				if not hasattr(self, names[idx]) and names[idx][-1] != '_':
					setattr(self, names[idx], defaults[idx])

		func(self, *args, **kwargs)

	return wrapper
