import unittest
from instancevars import *

class BasicTestClass(object):
	@instancevars(omit=['arg2_', 'arg3_'])
	def __init__(self, arg1, arg2_, arg3_='456', _arg4='789'):
		self.arg3 = arg3_

class InheritTestClass(BasicTestClass):
	@instancevars(omit=['arg1_', 'arg3_', 'arg4_'])
	def __init__(self, arg1_, arg2, _newarg, arg3_, arg4_='123'):
		super(InheritTestClass, self).__init__(arg1_, arg2, arg3_, arg4_)

class NoDefaultsTestClass(object):
	@instancevars(omit=['arg1_'])
	def __init__(self, arg1_, arg2, _arg3, arg4):
		pass

class TestInstanceVars(unittest.TestCase):
	def assertNotExist(self, func):
		try:
			func()
		except AttributeError:
			pass
		else:
			self.fail('AttributeError should have been thrown')

	def test_basic(self):
		obj = BasicTestClass(1, 2, 3)
		assert obj.arg1 == 1
		self.assertNotExist(lambda: obj.arg2_ == 2)
		self.assertNotExist(lambda: obj.arg3_ == 3)
		assert obj.arg3 == 3
		assert obj._arg4 == '789'

	def test_inheritance(self):
		obj = InheritTestClass(1, 2, 3, 4)
		assert obj.arg1 == 1
		self.assertNotExist(lambda: obj.arg1_ == 1)

		self.assertNotExist(lambda: obj.arg2_ == 2)
		assert obj.arg2 == 2

		assert obj._newarg == 3
		self.assertNotExist(lambda: obj.arg3_ == 3)

		self.assertNotExist(lambda: obj.arg4_ == '123')
		assert obj._arg4 == '123'

	def test_nodefaults(self):
		obj = NoDefaultsTestClass(1, 2, 3, 4)
		self.assertNotExist(lambda: obj.arg1_ == 1)
		assert obj.arg2 == 2
		assert obj._arg3 == 3
		assert obj.arg4 == 4

if __name__ == '__main__':
	unittest.main()