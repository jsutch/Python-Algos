# neanderthal brute force hash comparison v.0.0.3
#
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
# This is a pain because you lose the power of default string mangling rules. 
#
# In this case my sloppy workaround is to take pubicly available pre-mangled stringfiles, chop them down to 8 chars max, then split the multi-GB file
# into smaller chunks to not overload local memory. this was faster than rewriting a good mangler.
# ProTip: as modern testers we get used to baseline minumum lengths and complexity requirements - this was not a baseline with much older systems
# When generating precompiled lists you will also want to run the permutations of alphanumerics from 1-7 characters and add them to your inputs.
# in the test I ran more than 60% of the accounts utilized a single character.
# 
# splitting large password inputs into smaller chunks then iterating through them to compare hashes against the local hash
# need to install legacycrypt - crypt(3) no longer supported in python3 crypt libraries
import legacycrypt
import os

# datastores
userdb = {'alana': 'XLhxUSodwL.V', 'billyb': 'JoGotXZk/v', 'carlc': 'HezNf0NIYm9J', 'darad': 'DhdGPUVK/3'}
outcomes = {}
passfiles = ['john8.av', 'john8.aw', 'john8.ax', 'john8.ay', 'john8.az', 'john8.ba', 'john8.bb', 'john8.bc', 'john8.bd', 'john8.be', 'john8.bf', 'john8.bj', 'john8.bs']
completedchunks = []

# main
print("Starting loop with passfiles")
for chunkfile in passfiles:
    print(chunkfile)
    chunk = open(chunkfile,'r').read().splitlines()
    print(chunk[:3])

    for k, v in userdb.items():
	    SALT = v[:2]
	    print(k, v, SALT)
	    outcomes[k] = {}
	    for guess in chunk:
	            if legacycrypt.crypt(guess, SALT)[:10] == v:
	                    print('MATCH', k, v, guess)
	                    outcomes[k][v] = guess
	                    userdb.pop(k)
	                    break
    print('Completed chunk',chunkfile)
    
    completedchunks.append(chunkfile)
    del chunk
print("Completed run")
print(outcomes.items())
