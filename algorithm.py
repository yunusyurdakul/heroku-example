#!/usr/bin/python

def _findElementsBetween(index1, index2, elements):
	elementsBetween = []
	fromIndex = index1
	toIndex = index2
	if elements is None or len(elements) == 0:
		return 'There is no elements to search'
	if index1 > index2:
		return 'index1 should be smaller than index2'
	if index1 >= len(elements) or index2 >= len(elements):
		return 'index parameters must be smaller than '+ str(len(elements)) 		
	while fromIndex <= toIndex:
   		elementsBetween.append(elements[fromIndex])
		fromIndex = fromIndex+1

	return elementsBetween
