"""
A simple example of using XORs to do stream encryption

Ignore the .py - this is not actually a script.
"""
# set some strings and keys
In [36]: str1 = 'theres a lady whos sure all that glitters is gold'

In [37]: str2 = 'a man a plan a canal panama'

In [38]: key1 = 'abcdefg'

# first example of key-length encryption - 
# e.g. the string is longer (49 chars), but this only creates ciphertext the length of the key - (7 chars), then stops
In [42]: [ chr(ord(a) ^ ord(b)) for (a,b) in zip(str1, key1) ]
Out[42]: ['\x15', '\n', '\x06', '\x16', '\x00', '\x15', 'G']

In [43]: encrypted = [ chr(ord(a) ^ ord(b)) for (a,b) in zip(str1, key1) ]

In [44]: decrypted = [ chr(ord(a) ^ ord(b)) for (a,b) in zip(encrypted, key1) ]

In [45]: decrypted
Out[45]: ['t', 'h', 'e', 'r', 'e', 's', ' ']


# another example of key-length encryption with the second string
In [46]: encrypted2 = [ chr(ord(a) ^ ord(b)) for (a,b) in zip(str2, key1) ]

In [47]: decrypted2 = [ chr(ord(a) ^ ord(b)) for (a,b) in zip(encrypted2, key1) ]

In [48]: decrypted2
Out[48]: ['a', ' ', 'm', 'a', 'n', ' ', 'a']


# adding itertools.cycle to apply multiple cycles of the keys for longer messages
In [49]: from itertools import cycle

In [51]: encrypted3 = [ chr(ord(a) ^ ord(b)) for (a,b) in zip(str1, cycle(key1)) ]

# print out the encrypted string - exactly the length of the message. No padding, etc.
In [54]: encrypted3
Out[54]: ['\x15', '\n', '\x06', '\x16', '\x00', '\x15', 'G', '\x00', 'B', '\x0f', '\x05', '\x01', '\x1f', 'G', '\x16', '\n', '\x0c', '\x17', 'E', '\x15', '\x12', '\x13', '\x07', 'C', '\x05', '\t', '\n', 'G', '\x15', '\n', '\x02', '\x10', 'E', '\x01', '\x0b', '\x08', '\x16', '\x17', '\x01', '\x17', '\x15', 'G', '\x08', '\x11', 'C', '\x03', '\n', '\n', '\x03']

In [56]: decrypted3 = [ chr(ord(a) ^ ord(b)) for (a,b) in zip(encrypted3, cycle(key1)) ]

# print out the decrypted string to compare against the original
In [58]: "".join(decrypted3)
Out[58]: 'theres a lady whos sure all that glitters is gold'



"""
helping to visualize the key byte and string byte streams
"""
# first with a string and a short key
In [21]: key3='qwerty'

In [22]: str3='hello there ladies and gentlemen'

In [23]: [print(a, b) for (a,b) in zip(str3, cycle(key3)) ]
h q
e w
l e
l r
o t
  y
t q
h w
e e
r r
e t
  y
l q
a w
d e
i r
e t
s y
  q
a w
n e
d r
  t
g y
e q
n w
t e
l r
e t
m y
e q
n w

In [23]: key4='homeboy throw in the towel'

In [24]: str4='i wish i was a little bit taller i wish i was a baller'


# then with two longer strings/keys
In [25]: [print(a, b) for (a,b) in zip(str4, cycle(key4)) ]
i h
  o
w m
i e
s b
h o
  y
i
  t
w h
a r
s o
  w
a
  i
l n
i
t t
t h
l e
e
  t
b o
i w
t e
  l
t h
a o
l m
l e
e b
r o
  y
i
  t
w h
i r
s o
h w

i i
  n
w
a t
s h
  e
a
  t
b o
a w
l e
l l
e h
r o

