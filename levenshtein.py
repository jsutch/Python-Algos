import numpy as np

def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    return (matrix[size_x - 1, size_y - 1])


# helper test:
# evaluate all the files in a directory and compte the distance for the same files presuming differing naming conventions.
# and write them out into a csv file. Can then filter by lev_distance and find dupes
#
# e.g.
#b'Donnie_Darko-theatrical.m4v', b'The_Darjeeling_Limited.m4v', 19.0
#b'Donnie_Darko-theatrical.m4v', b'Uncle_Vanya-1991.m4v', 18.0
#b'Donnie_Darko-theatrical.m4v', b'Voyage_en_Ballon.mp4', 21.0
#In [174]: name2='Donnie_Darko.m4v'
#In [175]: name3='donniedarko.mp4'
#In [176]: name4='The_Darjeeling_Limited.m4v'
#In [177]: levenshtein(name2,name3)
#Out[177]: 5.0
#
#In [178]: levenshtein(name2,name4)
#Out[178]: 19.0
#
#In [179]: name5='donnie-darko-directors.mp4'
#
#In [180]: levenshtein(name2,name5)
#Out[180]: 15.0
"""
Some expansion on this and using lower() to improve scores
In [42]: name3='donniedarko.mp4'

In [43]: name44='donniedarkotheatrical.mp4'

In [44]: name4='Donnie_Darko-theatrical.m4v'

In [45]: name5='Donnie_Darko-directors.m4v'

In [46]: name55='donniedarkodirectors.mp4'

In [48]: name2.lower()
Out[48]: 'donnie_darko.m4v'

In [49]: lev(name2,name3)
Out[49]: 5.0

In [50]: lev(name2.lower(),name3.lower())
Out[50]: 3.0

In [51]: lev(name4,name44)
Out[51]: 6.0

In [52]: lev(name4.lower(),name44.lower())
Out[52]: 4.0

The counter example:
	In [53]:  name6='The_Darjeeling_Limited.m4v'

	In [54]: lev(name2,name6)
	Out[54]: 19.0

	In [55]: lev(name2.lower(),name6.lower())
	Out[55]: 19.0

"""

# handle writing in binary to handle utf-8/cyrillic letters
# verbose - print before write
import os
files2 = os.listdir(b'.')
with open('output.csv',mode='a',encoding="utf-8-sig") as f:
     for f1 in files2:
         for f2 in files2:
             cmp = f'{f1}, {f2}, {levenshtein(f1, f2)}\n'
             print(cmp)
             f.write(cmp)




