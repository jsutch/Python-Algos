"""
not a script - simple set of functions to calculate RF antenna/dipole element length for HF frequencies
"""

In [40]: def wavelength(n):
    ...:     return round(300 / n,2)
    ...:
In [41]: def halfwave(n):
    ...:     return round(n / 2,2)
    ...:
In [42]: def quarterwave(n):
    ...:     return round(n / 4,2)
    ...:

In [43]: def metersToFeet(n):
    ...:     return round(n * 3.28084,2)
    ...:

In [52]: for x in range(2,51):
    ...:     print(f"{x}Mhz is {wavelength(x)} meter wavelength. half wave == {halfwave(wavelength(x))} meters or {metersToFeet(halfwave(wavelength(x)))} feet, quarter wave {q
    ...: uarterwave(wavelength(x))} meters or {metersToFeet(quarterwave(wavelength(x)))} feet")
    ...:
'''
2Mhz is 150.0 meter wavelength. half wave == 75.0 meters or 246.06 feet, quarter wave 37.5 meters or 123.03 feet
3Mhz is 100.0 meter wavelength. half wave == 50.0 meters or 164.04 feet, quarter wave 25.0 meters or 82.02 feet
4Mhz is 75.0 meter wavelength. half wave == 37.5 meters or 123.03 feet, quarter wave 18.75 meters or 61.52 feet
5Mhz is 60.0 meter wavelength. half wave == 30.0 meters or 98.43 feet, quarter wave 15.0 meters or 49.21 feet
6Mhz is 50.0 meter wavelength. half wave == 25.0 meters or 82.02 feet, quarter wave 12.5 meters or 41.01 feet
7Mhz is 42.86 meter wavelength. half wave == 21.43 meters or 70.31 feet, quarter wave 10.71 meters or 35.14 feet
8Mhz is 37.5 meter wavelength. half wave == 18.75 meters or 61.52 feet, quarter wave 9.38 meters or 30.77 feet
9Mhz is 33.33 meter wavelength. half wave == 16.66 meters or 54.66 feet, quarter wave 8.33 meters or 27.33 feet
10Mhz is 30.0 meter wavelength. half wave == 15.0 meters or 49.21 feet, quarter wave 7.5 meters or 24.61 feet
11Mhz is 27.27 meter wavelength. half wave == 13.63 meters or 44.72 feet, quarter wave 6.82 meters or 22.38 feet
12Mhz is 25.0 meter wavelength. half wave == 12.5 meters or 41.01 feet, quarter wave 6.25 meters or 20.51 feet
13Mhz is 23.08 meter wavelength. half wave == 11.54 meters or 37.86 feet, quarter wave 5.77 meters or 18.93 feet
14Mhz is 21.43 meter wavelength. half wave == 10.71 meters or 35.14 feet, quarter wave 5.36 meters or 17.59 feet
15Mhz is 20.0 meter wavelength. half wave == 10.0 meters or 32.81 feet, quarter wave 5.0 meters or 16.4 feet
16Mhz is 18.75 meter wavelength. half wave == 9.38 meters or 30.77 feet, quarter wave 4.69 meters or 15.39 feet
17Mhz is 17.65 meter wavelength. half wave == 8.82 meters or 28.94 feet, quarter wave 4.41 meters or 14.47 feet
18Mhz is 16.67 meter wavelength. half wave == 8.34 meters or 27.36 feet, quarter wave 4.17 meters or 13.68 feet
19Mhz is 15.79 meter wavelength. half wave == 7.89 meters or 25.89 feet, quarter wave 3.95 meters or 12.96 feet
20Mhz is 15.0 meter wavelength. half wave == 7.5 meters or 24.61 feet, quarter wave 3.75 meters or 12.3 feet
21Mhz is 14.29 meter wavelength. half wave == 7.14 meters or 23.43 feet, quarter wave 3.57 meters or 11.71 feet
22Mhz is 13.64 meter wavelength. half wave == 6.82 meters or 22.38 feet, quarter wave 3.41 meters or 11.19 feet
23Mhz is 13.04 meter wavelength. half wave == 6.52 meters or 21.39 feet, quarter wave 3.26 meters or 10.7 feet
24Mhz is 12.5 meter wavelength. half wave == 6.25 meters or 20.51 feet, quarter wave 3.12 meters or 10.24 feet
25Mhz is 12.0 meter wavelength. half wave == 6.0 meters or 19.69 feet, quarter wave 3.0 meters or 9.84 feet
26Mhz is 11.54 meter wavelength. half wave == 5.77 meters or 18.93 feet, quarter wave 2.88 meters or 9.45 feet
27Mhz is 11.11 meter wavelength. half wave == 5.55 meters or 18.21 feet, quarter wave 2.78 meters or 9.12 feet
28Mhz is 10.71 meter wavelength. half wave == 5.36 meters or 17.59 feet, quarter wave 2.68 meters or 8.79 feet
29Mhz is 10.34 meter wavelength. half wave == 5.17 meters or 16.96 feet, quarter wave 2.58 meters or 8.46 feet
30Mhz is 10.0 meter wavelength. half wave == 5.0 meters or 16.4 feet, quarter wave 2.5 meters or 8.2 feet
31Mhz is 9.68 meter wavelength. half wave == 4.84 meters or 15.88 feet, quarter wave 2.42 meters or 7.94 feet
32Mhz is 9.38 meter wavelength. half wave == 4.69 meters or 15.39 feet, quarter wave 2.35 meters or 7.71 feet
33Mhz is 9.09 meter wavelength. half wave == 4.54 meters or 14.9 feet, quarter wave 2.27 meters or 7.45 feet
34Mhz is 8.82 meter wavelength. half wave == 4.41 meters or 14.47 feet, quarter wave 2.21 meters or 7.25 feet
35Mhz is 8.57 meter wavelength. half wave == 4.29 meters or 14.07 feet, quarter wave 2.14 meters or 7.02 feet
36Mhz is 8.33 meter wavelength. half wave == 4.17 meters or 13.68 feet, quarter wave 2.08 meters or 6.82 feet
37Mhz is 8.11 meter wavelength. half wave == 4.05 meters or 13.29 feet, quarter wave 2.03 meters or 6.66 feet
38Mhz is 7.89 meter wavelength. half wave == 3.94 meters or 12.93 feet, quarter wave 1.97 meters or 6.46 feet
39Mhz is 7.69 meter wavelength. half wave == 3.85 meters or 12.63 feet, quarter wave 1.92 meters or 6.3 feet
40Mhz is 7.5 meter wavelength. half wave == 3.75 meters or 12.3 feet, quarter wave 1.88 meters or 6.17 feet
41Mhz is 7.32 meter wavelength. half wave == 3.66 meters or 12.01 feet, quarter wave 1.83 meters or 6.0 feet
42Mhz is 7.14 meter wavelength. half wave == 3.57 meters or 11.71 feet, quarter wave 1.78 meters or 5.84 feet
43Mhz is 6.98 meter wavelength. half wave == 3.49 meters or 11.45 feet, quarter wave 1.75 meters or 5.74 feet
44Mhz is 6.82 meter wavelength. half wave == 3.41 meters or 11.19 feet, quarter wave 1.71 meters or 5.61 feet
45Mhz is 6.67 meter wavelength. half wave == 3.33 meters or 10.93 feet, quarter wave 1.67 meters or 5.48 feet
46Mhz is 6.52 meter wavelength. half wave == 3.26 meters or 10.7 feet, quarter wave 1.63 meters or 5.35 feet
47Mhz is 6.38 meter wavelength. half wave == 3.19 meters or 10.47 feet, quarter wave 1.59 meters or 5.22 feet
48Mhz is 6.25 meter wavelength. half wave == 3.12 meters or 10.24 feet, quarter wave 1.56 meters or 5.12 feet
49Mhz is 6.12 meter wavelength. half wave == 3.06 meters or 10.04 feet, quarter wave 1.53 meters or 5.02 feet
50Mhz is 6.0 meter wavelength. half wave == 3.0 meters or 9.84 feet, quarter wave 1.5 meters or 4.92 feet
'''
