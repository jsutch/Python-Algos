scoring weights per domain
In [462]: weights.items()
Out[462]: dict_items([(1, 0.16), (2, 0.1), (3, 0.14), (4, 0.17), (5, 0.16), (6, 0.14), (7, 0.13)])

max scores vs actual scores per domain
In [461]: test1.items()
Out[461]: dict_items([(1, [20, 17]), (2, [11, 9]), (3, [13, 11]), (4, [20, 17]), (5, [20, 14]), (6, [16, 10]), (7, [16, 13])])



In [474]: total,full = 0, 0
     ...: for k, v in test1.items():
     ...:     for k1, v1 in weights.items():
     ...:         if k == k1:
     ...:             print(f"Domain {k} score {v[1]} weighted at {v1}%  ==  {v[1] * v1}")
     ...:             full += v[0] * v1
     ...:             total += v[1] * v1
     ...: print(f"possible weighted high {round(full,2)} my weighted total {total} graded score by weight {round(total / full, 2)}")
Domain 1 score 17 weighted at 0.16%  ==  2.72
Domain 2 score 9 weighted at 0.1%  ==  0.9
Domain 3 score 11 weighted at 0.14%  ==  1.54
Domain 4 score 17 weighted at 0.17%  ==  2.89
Domain 5 score 14 weighted at 0.16%  ==  2.24
Domain 6 score 10 weighted at 0.14%  ==  1.4000000000000001
Domain 7 score 13 weighted at 0.13%  ==  1.69
possible weighted high 17.04 
my weighted total 13.38 
graded score by weight 0.79


# shoveled the  dicts into lists to use with a function
In [480]: myweights
Out[480]: [0.16, 0.1, 0.14, 0.17, 0.16, 0.14, 0.13]

In [484]: def weighted_average_manual(values, weights):
     ...:     weighted_sum = sum(v * w for v, w in zip(values, weights))
     ...:     total_weight = sum(weights)
     ...:     if total_weight == 0:
     ...:         return 0 # Or raise an error
     ...:     return weighted_sum / total_weight
     ...:

In [485]: weighted_average_manual(test1scores,myweights)
Out[485]: 13.38

In [486]: weighted_average_manual(test1max,myweights)
Out[486]: 17.040000000000003


