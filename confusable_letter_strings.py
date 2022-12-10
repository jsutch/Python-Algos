"""
not a script. Example of using the 'confusable' library to convert english strings to polyglot dictionaries
"""

In [92]: from confusables import confusable_characters

In [93]: mystr='zippity doo dah'

In [94]: ''.join([random.choice(confusable_characters(x)) for x in list(mystr)])
Out[94]: 'Ẓ𝙞𝝦𝜌𝖨𝙏Ỷ\u2008Ḑ𝑂𝝾\u2029ⅾａ𝙷'

In [95]: ''.join([random.choice(confusable_characters(x)) for x in list(mystr)])
Out[95]: '𝗓۱𝘱𝙥ͺ𝘁𝞬 ⅅОỠ\u2005ḌẳՀ'

In [96]: ''.join([random.choice(confusable_characters(x)) for x in list(mystr)])
Out[96]: 'ℨĪ𝞎𝙥𝕴ṮỴ\xa0𝐷ھ𝝈\u2008ḓ𝖺𝗛'

In [97]: ''.join([random.choice(confusable_characters(x)) for x in list(mystr)])
Out[97]: '𑢤𝑰pｐӏŤ𖼇\u2029𝓭𝐨𝐎 𝖽ẲᎻ'

In [98]: ''.join([random.choice(confusable_characters(x)) for x in list(mystr)])
Out[98]: 'Ž𝗜𝙥𝘗𝖨𝗧ẏ\u2009ⅆہṎ\u2005𝗱𝔞ĥ'

In [99]: ''.join([random.choice(confusable_characters(x)) for x in list(mystr)])
Out[99]: 'ζΙ𝚸𝜚𝟭𝑇𝖸\u2008ⅅۃỞ\u2005DаΗ'
