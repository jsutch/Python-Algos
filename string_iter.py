#!/usr/local/bin/python

def iterate_word(word):
	for x in range(0,len(word)):
		print("Forward:" , word[x], "Reverse", word[(len(word) -x -1)])

iterate_word('alphabet')