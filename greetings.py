In [84]: def greeting_func_gen(lang):
    ...:     def customized_greeting(name):
    ...:         if lang == "de":   # German
    ...:             phrase = "Guten Morgen "
    ...:         elif lang == "fr": # French
    ...:             phrase = "Bonjour "
    ...:         elif lang == "it": # Italian
    ...:             phrase = "Buongiorno "
    ...:         elif lang == "tr": # Turkish
    ...:             phrase = "Günaydın "
    ...:         elif lang == "gr": # Greek
    ...:             phrase = "Καλημερα "
    ...:         elif lang == "ru": # Russian
    ...:             phrase = "Здравствуйте"
    ...:         else:
    ...:             phrase = "Hi"
    ...:         return phrase + name + "!"
    ...:     return customized_greeting
    ...:

In [85]: greeting_func_gen("fr")
Out[85]: <function __main__.greeting_func_gen.<locals>.customized_greeting(name)>

In [86]: print(greeting_func_gen("fr"))
<function greeting_func_gen.<locals>.customized_greeting at 0x112c70280>

In [87]: french_hello = greeting_func_gen("fr")

In [88]: print(french_hello)
<function greeting_func_gen.<locals>.customized_greeting at 0x112c901f0>

In [89]: print(french_hello('David'))
Bonjour David!
