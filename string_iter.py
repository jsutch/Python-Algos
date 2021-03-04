#!/usr/local/bin/python

def iterate_word(word):
	for x in range(0,len(word)):
		print("Forward:" , word[x], "Reverse", word[(len(word) -x -1)])

iterate_word('alphabet')


# doing this with list comprehension returning reversed tuple pairs:
In [240]: [(word[x], word[(len(word) - x - 1)]) for x in range(0,len(word))]
Out[240]:
[('a', 't'),
 ('l', 'e'),
 ('p', 'b'),
 ('h', 'a'),
 ('a', 'h'),
 ('b', 'p'),
 ('e', 'l'),
 ('t', 'a')]


# as a function:
In [241]: def iter_string(word):
     ...:     return [(word[x], word[(len(word) - x - 1)]) for x in range(0,len(word))]
     ...:

In [242]: iter_string('alphabet')
Out[242]:
[('a', 't'),
 ('l', 'e'),
 ('p', 'b'),
 ('h', 'a'),
 ('a', 'h'),
 ('b', 'p'),
 ('e', 'l'),
 ('t', 'a')]


