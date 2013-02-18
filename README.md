PyInstanceVars
==============

A function decorator that automatically creates instance variables from  function arguments. Arguments can be omitted by naming them with a trailing underscore. Names are retained on a one-to-one basis (i.e. '_arg_name' becomes 'self._arg_name'). It works with arguments in any form (passed as keyword, default, or regular).

Basic Usage
===========

The simplest way to explain how to use it is with a quick code example. Notice how 'arg2_' is omitted since it has a trailing underscore. I created 'arg2' to show that you can easily mix and match auto initialization with explicit intialization (which is required for any non-trivial assignment or if further testing of the argument is required).

```python
>>> from instancevars import *
>>> class TestMe(object):
...     @instancevars
...     def __init__(self, _arg1, arg2_, arg3='test'):
...             self.arg2 = arg2_ + 1
...
>>> testme = TestMe(1, 2)
>>> testme._arg1
1
>>> testme.arg2_
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'TestMe' object has no attribute 'arg2_'
>>> testme.arg2
3
>>> testme.arg3
'test'
>>>
```

Why?
====

Because Python initializer functions can get lengthy doing nothing more than one-to-one variable assignment. Languages such as Scala already have the ability to convert arguments to instance variables using 'val' or 'var'. Given Python's reputation of being succinct and terse it seems like this should be builtin. Some might believe this to be 'unpythonic', but I would respectfully disagree. We've listed a decorator and argument names denoting our intent, so IMHO we've been plenty 'explicit'. Still, I wouldn't recommend using this unless you have several initializer arguments.

Requirements
============

It was tested under both Python 2.7.x and Python 3.3.x.

There are no library dependencies outside of the standard library.

Credits
=======

The base code is from a snippet on StackOverflow (http://stackoverflow.com/questions/1389180/python-automatically-initialize-instance-variables). I merely added the capability to omit function arguments, fixed a bug with default argument handling, and added some tests.
