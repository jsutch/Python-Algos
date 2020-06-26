In [213]: mystr
Out[213]: 'The operation we are calling put is sometimes named set, insertAt, or atPut. The get operation is sometimes termed at. In our containers a get with an invalid key will produce an assertion error. In some variations on the container this operation will raise an exception, or return a special value, such as null. We include an iterator for the key set as part of the specification, but will leave the implementation of this feature as an exercise for the reader.'

def addletter(letter):
    letter = letter.lower()
    lettercount[letter] +=1
def newletter(letter):
    letter = letter.lower()
    lettercount[letter] = 1

lettercount={}
[addletter(l) if l.lower() in lettercount else newletter(l) for l in list(mystr)]


# return the list of frequencies
sorted(lettercount.items(), key=lambda x: x[1], reverse=True)

"""
In [369]: lettercount
Out[369]:
{'t': 40,
 'h': 11,
 'e': 53,
 ' ': 80,
 'o': 27,
 'p': 11,
 'r': 29,
 'a': 35,
 'i': 35,
 'n': 28,
 'w': 6,
 'c': 11,
 'l': 16,
 'g': 3,
 'u': 11,
 's': 24,
 'm': 9,
 'd': 6,
 ',': 5,
 '.': 5,
 'v': 4,
 'k': 2,
 'y': 2,
 'x': 2,
 'f': 6,
 'b': 1}

 In [370]: sorted(lettercount.items(), key=lambda x: x[1], reverse=True)
Out[370]:
[(' ', 80),
 ('e', 53),
 ('t', 40),
 ('a', 35),
 ('i', 35),
 ('r', 29),
 ('n', 28),
 ('o', 27),
 ('s', 24),
 ('l', 16),
 ('h', 11),
 ('p', 11),
 ('c', 11),
 ('u', 11),
 ('m', 9),
 ('w', 6),
 ('d', 6),
 ('f', 6),
 (',', 5),
 ('.', 5),
 ('v', 4),
 ('g', 3),
 ('k', 2),
 ('y', 2),
 ('x', 2),
 ('b', 1)]
 """
