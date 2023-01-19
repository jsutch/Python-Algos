"""
Simple example of the 'doubling grains of rice' problem
not a script. mostly here to remind me about the comma formatting for large numbers
"""
In [47]: # 7k grains of rice in a pound, $30 for 50lbs bag, so .60/lb
    ...: y=1
    ...: for x in range(1,65):
    ...:     lbs, price = 0, 0
    ...:     if x == 1:
    ...:         print(f"{x}  1 grain of rice - 0lbs")
    ...:     else:
    ...:         y = y * 2
    ...:         if (y / 7000) > 1:
    ...:             lbs = round((y / 7000),2)
    ...:             price = round(lbs *.6)
    ...:         print(x," {:,}".format(y), 'grains of rice', " {:,}".format(lbs), 'lbs', 'at', "$ {:,}".format(price))
    ...:


"""
output:

1  1 grain of rice - 0lbs
2  2 grains of rice  0 lbs at $ 0
3  4 grains of rice  0 lbs at $ 0
4  8 grains of rice  0 lbs at $ 0
5  16 grains of rice  0 lbs at $ 0
6  32 grains of rice  0 lbs at $ 0
7  64 grains of rice  0 lbs at $ 0
8  128 grains of rice  0 lbs at $ 0
9  256 grains of rice  0 lbs at $ 0
10  512 grains of rice  0 lbs at $ 0
11  1,024 grains of rice  0 lbs at $ 0
12  2,048 grains of rice  0 lbs at $ 0
13  4,096 grains of rice  0 lbs at $ 0
14  8,192 grains of rice  1.17 lbs at $ 1
15  16,384 grains of rice  2.34 lbs at $ 1
16  32,768 grains of rice  4.68 lbs at $ 3
17  65,536 grains of rice  9.36 lbs at $ 6
18  131,072 grains of rice  18.72 lbs at $ 11
19  262,144 grains of rice  37.45 lbs at $ 22
20  524,288 grains of rice  74.9 lbs at $ 45
21  1,048,576 grains of rice  149.8 lbs at $ 90
22  2,097,152 grains of rice  299.59 lbs at $ 180
23  4,194,304 grains of rice  599.19 lbs at $ 360
24  8,388,608 grains of rice  1,198.37 lbs at $ 719
25  16,777,216 grains of rice  2,396.75 lbs at $ 1,438
26  33,554,432 grains of rice  4,793.49 lbs at $ 2,876
27  67,108,864 grains of rice  9,586.98 lbs at $ 5,752
28  134,217,728 grains of rice  19,173.96 lbs at $ 11,504
29  268,435,456 grains of rice  38,347.92 lbs at $ 23,009
30  536,870,912 grains of rice  76,695.84 lbs at $ 46,018
31  1,073,741,824 grains of rice  153,391.69 lbs at $ 92,035
32  2,147,483,648 grains of rice  306,783.38 lbs at $ 184,070
33  4,294,967,296 grains of rice  613,566.76 lbs at $ 368,140
34  8,589,934,592 grains of rice  1,227,133.51 lbs at $ 736,280
35  17,179,869,184 grains of rice  2,454,267.03 lbs at $ 1,472,560
36  34,359,738,368 grains of rice  4,908,534.05 lbs at $ 2,945,120
37  68,719,476,736 grains of rice  9,817,068.11 lbs at $ 5,890,241
38  137,438,953,472 grains of rice  19,634,136.21 lbs at $ 11,780,482
39  274,877,906,944 grains of rice  39,268,272.42 lbs at $ 23,560,963
40  549,755,813,888 grains of rice  78,536,544.84 lbs at $ 47,121,927
41  1,099,511,627,776 grains of rice  157,073,089.68 lbs at $ 94,243,854
42  2,199,023,255,552 grains of rice  314,146,179.36 lbs at $ 188,487,708
43  4,398,046,511,104 grains of rice  628,292,358.73 lbs at $ 376,975,415
44  8,796,093,022,208 grains of rice  1,256,584,717.46 lbs at $ 753,950,830
45  17,592,186,044,416 grains of rice  2,513,169,434.92 lbs at $ 1,507,901,661
46  35,184,372,088,832 grains of rice  5,026,338,869.83 lbs at $ 3,015,803,322
47  70,368,744,177,664 grains of rice  10,052,677,739.67 lbs at $ 6,031,606,644
48  140,737,488,355,328 grains of rice  20,105,355,479.33 lbs at $ 12,063,213,288
49  281,474,976,710,656 grains of rice  40,210,710,958.67 lbs at $ 24,126,426,575
50  562,949,953,421,312 grains of rice  80,421,421,917.33 lbs at $ 48,252,853,150
51  1,125,899,906,842,624 grains of rice  160,842,843,834.66 lbs at $ 96,505,706,301
52  2,251,799,813,685,248 grains of rice  321,685,687,669.32 lbs at $ 193,011,412,602
53  4,503,599,627,370,496 grains of rice  643,371,375,338.64 lbs at $ 386,022,825,203
54  9,007,199,254,740,992 grains of rice  1,286,742,750,677.28 lbs at $ 772,045,650,406
55  18,014,398,509,481,984 grains of rice  2,573,485,501,354.57 lbs at $ 1,544,091,300,813
56  36,028,797,018,963,968 grains of rice  5,146,971,002,709.14 lbs at $ 3,088,182,601,625
57  72,057,594,037,927,936 grains of rice  10,293,942,005,418.28 lbs at $ 6,176,365,203,251
58  144,115,188,075,855,872 grains of rice  20,587,884,010,836.55 lbs at $ 12,352,730,406,502
59  288,230,376,151,711,744 grains of rice  41,175,768,021,673.11 lbs at $ 24,705,460,813,004
60  576,460,752,303,423,488 grains of rice  82,351,536,043,346.22 lbs at $ 49,410,921,626,008
61  1,152,921,504,606,846,976 grains of rice  164,703,072,086,692.44 lbs at $ 98,821,843,252,015
62  2,305,843,009,213,693,952 grains of rice  329,406,144,173,384.9 lbs at $ 197,643,686,504,031
63  4,611,686,018,427,387,904 grains of rice  658,812,288,346,769.8 lbs at $ 395,287,373,008,062
64  9,223,372,036,854,775,808 grains of rice  1,317,624,576,693,539.5 lbs at $ 790,574,746,016,124
"""
