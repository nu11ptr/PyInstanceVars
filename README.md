PyInstanceVars
==============

A function decorator that automatically creates instance variables from function arguments. 

Arguments can be omitted by adding them to the 'omit' list argument of the decorator.
Names are retained on a one-to-one basis (i.e '_arg' --> 'self._arg'). Passing
arguments as raw literals, using a keyword, or as defaults all work. If *args and/or
**kwargs are used by the decorated function, they are not processed and must be handled
explicitly. 

Basic Usage
===========

The simplest way to explain how to use it is with a quick code example:

```python
>>> from instancevars import *
>>> class SimpleDemo(object):
...     @instancevars
...     def __init__(self, arg1, arg2, arg3):
...             pass
... 
>>> simple = SimpleDemo(1, 2, 3)
>>> simple.arg1
1
>>> simple.arg2
2
>>> simple.arg3
3
```

This example shows how you can optionally skip arguments by adding them to the omit list. You can still manually
do whatever you need with them in the function body.

```python
>>> from instancevars import *
>>> class TestMe(object):
...     @instancevars(omit=['arg2_'])
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

Because Python initializer functions can get lengthy doing nothing more than one-to-one variable assignment.
Languages such as Scala already have the ability to convert arguments to instance variables using 'val' or 'var'.
Given Python's reputation of being succinct and terse it seems like this should be builtin. 

Some may think this is 'unpythonic', but I would respectfully disagree. We've listed a decorator and 
an omit list denoting our intent, so I think we've been plenty 'explicit'. In my opinion, the terseness gained
by the decorator aids readability. Just my opinion, decide for yourself.

Requirements
============

It has been tested under CPython 2.7/3.3, PyPy 1.9, and Jython 2.5/2.7.

There are no library dependencies other than the standard library.

Performance
===========

Thanks to a contributed rewrite, performance is now only 30-40% worse than explicit initialization under CPython.
This is likely to be an acceptable amount of degradation for nearly all scenarios.

Credits
=======

The code was originally based on a great comment and snippet from StackOverflow (http://stackoverflow.com/questions/1389180/python-automatically-initialize-instance-variables).
