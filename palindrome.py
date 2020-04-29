#!/usr/local/bin/python

#broken - doesn't recognize some words. Doesn't handle multi-word palindromes
def palindrome(word):
	MISS = 0
	wordlist = word.split()
	#print word.split()
	string = ''.join(wordlist)
	#print string
	for x in range(0,len(string)):
		#print word[x], word[len(word) -x - 1]
		if string[x] == string[len(string) -x - 1]:
			#print word[x], " is ", word[len(word) -x - 1]
			pass
		else: 
			#print word[x], " is NOT", word[len(word) -x - 1]
			MISS += 1
	if MISS != 0:
		return "FALSE"
	else: 
		return "TRUE"


#print palindrome('amanaplanacanalpanama')
print(palindrome('a man a plan a canal panama'))