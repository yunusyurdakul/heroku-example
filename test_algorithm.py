#!/usr/bin/python

import unittest
from algorithm import _findElementsBetween

class TestSearch(unittest.TestCase):

	#Set up
	def setUp(self):
		self.array = [10, 'yunus', 'cagri', 'yurdakul', 1, 'test']
	#Successful	
	def test_successful(self):
		resultArr =  [10,'yunus']
		self.assertEqual(_findElementsBetween(0,1,self.array), resultArr)
	#Erroneous
	def test_failed(self):
		resultArr =  [10,'yunus']
		self.assertNotEqual(_findElementsBetween(3,4,self.array), resultArr)
	#Empty array
	def test_emptyArray(self):
		resultMsg = 'There is no elements to search'
		self.assertEqual(_findElementsBetween(0,3,[]), resultMsg)
	#Index range is wrong	
	def test_whenRangeIsWrong(self):
		resultMsg = 'index1 should be smaller than index2'
		self.assertEquals(_findElementsBetween(2,1,self.array), resultMsg)
	#One of the index is out of range 	
	def test_indexIsOutOfRange(self):
		resultMsg = 'index parameters must be smaller than '+ str(len(self.array))
		self.assertEquals(_findElementsBetween(1,12,self.array), resultMsg)

if __name__ == '__main__':
	unittest.main()
