"""
more of an example than a python script.
"""

In [107]: [print(backoff(x)) for x in range(7)]
(0, 1, 0.016666666666666666, '2022-03-06-13:47:07.061847')
(1, 1, 0.016666666666666666, '2022-03-06-13:47:08.066669')
(2, 4, 0.06666666666666667, '2022-03-06-13:47:12.067255')
(3, 27, 0.45, '2022-03-06-13:47:39.070920')
(4, 256, 4.266666666666667, '2022-03-06-13:51:55.066956')
(5, 3125, 52.083333333333336, '2022-03-06-14:43:59.986201')

(6, 46656, 777.6, '2022-03-07-03:41:34.762197')
Out[107]: [None, None, None, None, None, None, None]

In [108]:

In [108]: def now():
     ...:     return datetime.now().strftime('%Y-%m-%d-%H:%M:%S.%f')
     ...:

In [108]: def backoff(n):
     ...:    """display the round, the exponent (num of seconds before retry), the exponent secs in minutes and the current timestamp"""
     ...:     expo = n ** n
     ...:     time.sleep(expo)
     ...:     return (n, expo, expo / 60, now())
     ...:
