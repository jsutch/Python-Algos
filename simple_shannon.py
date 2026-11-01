from collections import Counter
from math import log

def shannon(string):
    """ Simple Shannon Entropy Calculator for Strings"""
    counts = Counter(string)
    frequencies = ((i / len(string)) for i in counts.values())
    return - sum(f * log(f, 2) for f in frequencies)

# examples
# all lower case
In [23]: shannon('lksajdlakjsdlaskjdlaskjdlaksjdlaskjdlaksjdlakjsd')
Out[23]: 2.584962500721156

# upper and lower case +2 special character (hash)
In [24]: shannon('UWvXlCcIGVGWJoJhoTENbJafzElatDFAzEmB/BvYx1I=')
Out[24]: 4.834209459448049

# remove one special character
In [25]: shannon('UWvXlCcIGVGWJoJhoTENbJafzElatDFAzEmB/BvYx1I')
Out[25]: 4.786502545299146

# replace some letters with numbers and special characters
In [26]: shannon('5W#XlCc^0VGWJ8J_oT3NbJa-zElatD2AzE6wB/BvYx1I')
Out[26]: 5.078638720860855

# long word - all lower case
In [27]: shannon('supercalifragilisticexplialodocius')
Out[27]: 3.6823323262263004

# same length - add upper case
In [28]: shannon('SuperCaliFragilisticExplialodocius')
Out[28]: 3.903208061647681

# same length - add numbers
In [29]: shannon('Sup3rC4liFr4g1l15t1cExp14l0d0c1u5')
Out[29]: 4.040775468486825

# same length - add special characters, including unusual ones
In [30]: shannon('S_π3rC4liFr4©1l15t1çE*π14l0d0ç1_5')
Out[30]: 4.040775468486825
