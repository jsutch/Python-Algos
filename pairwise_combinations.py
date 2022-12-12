"""
not a script
"""
# list all combinations - dont' find uniqueness
In [112]: mylist = [1,'alice',2,'bob',3,'charlie',4,'david',5,'eve']

In [113]: output=[]
     ...: for x in range(0,len(mylist)):
     ...:     for y in range(0,len(mylist)):
     ...:         #
     ...:         if (x != y):
     ...:             output.append((mylist[x],mylist[y]))
     ...: print(output)
[(1, 'alice'), (1, 2), (1, 'bob'), (1, 3), (1, 'charlie'), (1, 4), (1, 'david'), (1, 5), (1, 'eve'), ('alice', 1), ('alice', 2), ('alice', 'bob'), ('alice', 3), ('alice', 'charlie'), ('alice', 4), ('alice', 'david'), ('alice', 5), ('alice', 'eve'), (2, 1), (2, 'alice'), (2, 'bob'), (2, 3), (2, 'charlie'), (2, 4), (2, 'david'), (2, 5), (2, 'eve'), ('bob', 1), ('bob', 'alice'), ('bob', 2), ('bob', 3), ('bob', 'charlie'), ('bob', 4), ('bob', 'david'), ('bob', 5), ('bob', 'eve'), (3, 1), (3, 'alice'), (3, 2), (3, 'bob'), (3, 'charlie'), (3, 4), (3, 'david'), (3, 5), (3, 'eve'), ('charlie', 1), ('charlie', 'alice'), ('charlie', 2), ('charlie', 'bob'), ('charlie', 3), ('charlie', 4), ('charlie', 'david'), ('charlie', 5), ('charlie', 'eve'), (4, 1), (4, 'alice'), (4, 2), (4, 'bob'), (4, 3), (4, 'charlie'), (4, 'david'), (4, 5), (4, 'eve'), ('david', 1), ('david', 'alice'), ('david', 2), ('david', 'bob'), ('david', 3), ('david', 'charlie'), ('david', 4), ('david', 5), ('david', 'eve'), (5, 1), (5, 'alice'), (5, 2), (5, 'bob'), (5, 3), (5, 'charlie'), (5, 4), (5, 'david'), (5, 'eve'), ('eve', 1), ('eve', 'alice'), ('eve', 2), ('eve', 'bob'), ('eve', 3), ('eve', 'charlie'), ('eve', 4), ('eve', 'david'), ('eve', 5)]



# find unique combinations usig itertools:
n [114]: from itertools import combinations

In [115]: combinations(mylist,2)
Out[115]: <itertools.combinations at 0x111d79590>

In [116]: list(combinations(mylist,2))
Out[116]:
[(1, 'alice'),
 (1, 2),
 (1, 'bob'),
 (1, 3),
 (1, 'charlie'),
 (1, 4),
 (1, 'david'),
 (1, 5),
 (1, 'eve'),
 ('alice', 2),
 ('alice', 'bob'),
 ('alice', 3),
 ('alice', 'charlie'),
 ('alice', 4),
 ('alice', 'david'),
 ('alice', 5),
 ('alice', 'eve'),
 (2, 'bob'),
 (2, 3),
 (2, 'charlie'),
 (2, 4),
 (2, 'david'),
 (2, 5),
 (2, 'eve'),
 ('bob', 3),
 ('bob', 'charlie'),
 ('bob', 4),
 ('bob', 'david'),
 ('bob', 5),
 ('bob', 'eve'),
 (3, 'charlie'),
 (3, 4),
 (3, 'david'),
 (3, 5),
 (3, 'eve'),
 ('charlie', 4),
 ('charlie', 'david'),
 ('charlie', 5),
 ('charlie', 'eve'),
 (4, 'david'),
 (4, 5),
 (4, 'eve'),
 ('david', 5),
 ('david', 'eve'),
 (5, 'eve')]
