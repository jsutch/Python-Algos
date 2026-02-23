# simple trie example using setdefault builtin function. 
# this looks up a key in the dictionary (here, letter or _end). If the key is present, it returns the associated value; if not, it assigns a default value to that key and returns the value ({} or _end). (It's like a version of get that also updates the dictionary.) 
# simple example - not a script
# Operation	Average	Worst case
#Search	O(n)	O(n)
#Insert	O(n)	O(n)
#Delete	O(n)	O(n)

In [1]: _end = '_end_'

In [2]: def make_trie(*words):
   ...:     root = dict()
   ...:     for word in words:
   ...:         current_dict = root
   ...:         for letter in word:
   ...:             current_dict = current_dict.setdefault(letter, {})
   ...:         current_dict[_end] = _end
   ...:     return root
   ...:

In [16]: make_trie('alice', 'bob', 'chuck', 'bot')
Out[16]:
{'a': {'l': {'i': {'c': {'e': {'_end_': '_end_'}}}}},
 'b': {'o': {'b': {'_end_': '_end_'}, 't': {'_end_': '_end_'}}},
 'c': {'h': {'u': {'c': {'k': {'_end_': '_end_'}}}}}}

In [4]: def in_trie(trie, word):
   ...:     current_dict = trie
   ...:     for letter in word:
   ...:         if letter not in current_dict:
   ...:             return False
   ...:         current_dict = current_dict[letter]
   ...:     return _end in current_dict
   ...:

In [7]: in_trie(make_trie('alice', 'bob', 'billy', 'tim'), 'tom')
Out[7]: False

In [8]: in_trie(make_trie('alice', 'bob', 'billy', 'tim'), 'tim')
Out[8]: True

In [9]: in_trie(make_trie('alice', 'bob', 'billy', 'tim'), 'ti')
Out[9]: False

In [10]: in_trie(make_trie('alice', 'bob', 'billy', 'tim','timmy'), 'ti')
Out[10]: False

In [11]: in_trie(make_trie('alice', 'bob', 'billy', 'tim','timmy'), 'tim')
Out[11]: True

In [12]: in_trie(make_trie('alice', 'bob', 'billy', 'tim','timmy'), 'timm')
Out[12]: False

In [13]: in_trie(make_trie('alice', 'bob', 'billy', 'tim','timmy'), 'timmy')

In [17]: foo = make_trie('alice', 'bob', 'chuck', 'bot')

In [18]: in_trie(foo,'alice')
Out[18]: True

In [19]: in_trie(foo,'bo')
Out[19]: False

In [20]: in_trie(foo,'bot')
Out[20]: True

In [5]: make_trie('babs', 'bob', 'bill', 'bobby','bob')
Out[5]:
{'b': {'a': {'b': {'s': {'_end_': '_end_'}}},
  'o': {'b': {'_end_': '_end_', 'b': {'y': {'_end_': '_end_'}}}},
  'i': {'l': {'l': {'_end_': '_end_'}}}}}

In [6]: bar = make_trie('babs', 'bob', 'bill', 'bobby','bob')

In [7]: in_trie(bar,'bob')
Out[7]: True

In [8]: in_trie(bar,'bob')

In [9]: make_trie('a', 'aa', 'aaa', 'aab','aaab','abba')
Out[9]:
{'a': {'_end_': '_end_',
  'a': {'_end_': '_end_',
   'a': {'_end_': '_end_', 'b': {'_end_': '_end_'}},
   'b': {'_end_': '_end_'}},
  'b': {'b': {'a': {'_end_': '_end_'}}}}}


