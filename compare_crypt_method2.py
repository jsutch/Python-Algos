# Extension Guess workaround
# some very old password databases using DES crypt(3) hashes will truncate the stored string from 13 chars down to 10 chars, including a 2 byte salt at the beginning
# e.g.
# properly formatted with be:
# crypt.crypt("MyDumbPassword","My")'
# MyKy9iPtz5SPM ==  13bytes. 11 bytes + 2 byte salt
# so, what would be stored in this logic is a truncated 10 byte string -  MyKy9iPtz5, 8 bytes + 2 byte salt (My)
# 
# this breaks the input scrubbing logic for tools like john the ripper or hashcat which are expecting the correct 13byte length
# which will lead to the infamous
# "No password hashes loaded (see FAQ)" or "Token length exception" errors
# hashcat --identify will guess these as type 16000 and flail
# 
# This is a pain because you lose the power of default string mangling rules
# In this example since we have 10bytes and just need 3, we'll just add the characters to make input files which are valid for hashcat and john to read
# we can use python's permutations module with a limit of 3 output to create suffixes, then mash them together to make a 13byte string
# that will pass format scrutiny.:
# valid chars are 0x00 to 0xFF which will be seen as ascii. basically a-zA-Z0-9 and ./ will work in my case 

# in this case we're just going to build the output files per-hash for one user. TODO: add logic for larger files.
#userdb = {'alana': 'XLhxUSodwL.V', 'billyb': 'JoGotXZk/v', 'carlc': 'HezNf0NIYm9J', 'darad': 'DhdGPUVK/3'}

# use carlc's hash
userhash = 'HezNf0NIYm9J'
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ./'
perm = [''.join(i) for i in permutations(chars, 3)]
userarr = [userhash + x for x in perm]

# make an output that hashcat with mode 1500 can attack
f = open('user_hashcat', 'a', encoding="utf-8")
for x in userarr:
    f.write(f"{x}\n")
f.close()


# make an output that john the ripper with mode crypt in "unshadowed" mode can attack
# we could add carl's name to this to take advantage of name munging, but we won't in this example
f = open('user_john_combined', 'a', encoding="utf-8")
for x in userarr:
    y = f"bob:{x}:500:500:Bob Smith:/home/bob:/bin/bash"
    f.write(f"{y}\n")
f.close()


