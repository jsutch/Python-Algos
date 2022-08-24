
#  also: sum(xi != yi for xi, yi in zip(x, y))

In [18]: def hamming_distance(string1, string2):
    ...:     dist_counter = 0
    ...:     for n in range(len(string1)):
    ...:         if string1[n] != string2[n]:
    ...:             dist_counter += 1
    ...:     return dist_counter
    ...:



In [20]: str1='tommy'

In [21]: str2='timmy'

In [22]: hamming_distance(str1,str2)
Out[22]: 1

In [23]: str3='teresa'

In [24]: hamming_distance(str1,str3)
Out[24]: 4

In [25]: str4='foofarah'

In [26]: hamming_distance(str1,str4)
Out[26]: 4

In [27]: str5='terrible force of junior'

In [28]: hamming_distance(str1,str5)
Out[28]: 4

In [29]: str6='Timmmy'

In [30]: hamming_distance(str1,str6)
Out[30]: 3

In [31]: hamming_distance(str2,str6)
Out[31]: 2

In [32]: str7='Timmy'

In [33]: hamming_distance(str2,str7)
Out[33]: 1

In [34]: hamming_distance(str1,str7)
Out[34]: 2

# see also:
In [36]: sum(xi != yi for xi, yi in zip(str1, str7))
Out[36]: 2

In [37]: sum(xi != yi for xi, yi in zip(str1, str6))
Out[37]: 3


