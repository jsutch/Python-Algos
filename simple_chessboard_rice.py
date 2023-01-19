"""
Simple example of the 'doubling grains of rice' problem
not a script. mostly here to remind me about the comma formatting for large numbers
"""

In [41]: # 7k grains of rice in a pound
    ...: y=1
    ...: for x in range(1,65):
    ...:     lbs = 0
    ...:     if x == 1:
    ...:         print(f"{x}  1")
    ...:     else:
    ...:         y = y * 2
    ...:         if (y / 7000) > 1:
    ...:             lbs = round((y / 7000),2)
    ...:         print(x," {:,}".format(y), 'grains of rice', " {:,}".format(lbs), 'lbs')
    ...:
"""
1  1
2  2 grains of rice  0 lbs
3  4 grains of rice  0 lbs
4  8 grains of rice  0 lbs
5  16 grains of rice  0 lbs
6  32 grains of rice  0 lbs
7  64 grains of rice  0 lbs
8  128 grains of rice  0 lbs
9  256 grains of rice  0 lbs
10  512 grains of rice  0 lbs
11  1,024 grains of rice  0 lbs
12  2,048 grains of rice  0 lbs
13  4,096 grains of rice  0 lbs
14  8,192 grains of rice  1.17 lbs
15  16,384 grains of rice  2.34 lbs
16  32,768 grains of rice  4.68 lbs
17  65,536 grains of rice  9.36 lbs
18  131,072 grains of rice  18.72 lbs
19  262,144 grains of rice  37.45 lbs
20  524,288 grains of rice  74.9 lbs
21  1,048,576 grains of rice  149.8 lbs
22  2,097,152 grains of rice  299.59 lbs
23  4,194,304 grains of rice  599.19 lbs
24  8,388,608 grains of rice  1,198.37 lbs
25  16,777,216 grains of rice  2,396.75 lbs
26  33,554,432 grains of rice  4,793.49 lbs
27  67,108,864 grains of rice  9,586.98 lbs
28  134,217,728 grains of rice  19,173.96 lbs
29  268,435,456 grains of rice  38,347.92 lbs
30  536,870,912 grains of rice  76,695.84 lbs
31  1,073,741,824 grains of rice  153,391.69 lbs
32  2,147,483,648 grains of rice  306,783.38 lbs
33  4,294,967,296 grains of rice  613,566.76 lbs
34  8,589,934,592 grains of rice  1,227,133.51 lbs
35  17,179,869,184 grains of rice  2,454,267.03 lbs
36  34,359,738,368 grains of rice  4,908,534.05 lbs
37  68,719,476,736 grains of rice  9,817,068.11 lbs
38  137,438,953,472 grains of rice  19,634,136.21 lbs
39  274,877,906,944 grains of rice  39,268,272.42 lbs
40  549,755,813,888 grains of rice  78,536,544.84 lbs
41  1,099,511,627,776 grains of rice  157,073,089.68 lbs
42  2,199,023,255,552 grains of rice  314,146,179.36 lbs
43  4,398,046,511,104 grains of rice  628,292,358.73 lbs
44  8,796,093,022,208 grains of rice  1,256,584,717.46 lbs
45  17,592,186,044,416 grains of rice  2,513,169,434.92 lbs
46  35,184,372,088,832 grains of rice  5,026,338,869.83 lbs
47  70,368,744,177,664 grains of rice  10,052,677,739.67 lbs
48  140,737,488,355,328 grains of rice  20,105,355,479.33 lbs
49  281,474,976,710,656 grains of rice  40,210,710,958.67 lbs
50  562,949,953,421,312 grains of rice  80,421,421,917.33 lbs
51  1,125,899,906,842,624 grains of rice  160,842,843,834.66 lbs
52  2,251,799,813,685,248 grains of rice  321,685,687,669.32 lbs
53  4,503,599,627,370,496 grains of rice  643,371,375,338.64 lbs
54  9,007,199,254,740,992 grains of rice  1,286,742,750,677.28 lbs
55  18,014,398,509,481,984 grains of rice  2,573,485,501,354.57 lbs
56  36,028,797,018,963,968 grains of rice  5,146,971,002,709.14 lbs
57  72,057,594,037,927,936 grains of rice  10,293,942,005,418.28 lbs
58  144,115,188,075,855,872 grains of rice  20,587,884,010,836.55 lbs
59  288,230,376,151,711,744 grains of rice  41,175,768,021,673.11 lbs
60  576,460,752,303,423,488 grains of rice  82,351,536,043,346.22 lbs
61  1,152,921,504,606,846,976 grains of rice  164,703,072,086,692.44 lbs
62  2,305,843,009,213,693,952 grains of rice  329,406,144,173,384.9 lbs
63  4,611,686,018,427,387,904 grains of rice  658,812,288,346,769.8 lbs
64  9,223,372,036,854,775,808 grains of rice  1,317,624,576,693,539.5 lbs
"""
