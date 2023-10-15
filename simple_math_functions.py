def mycomma(num:int):
    """
    return integer with a string that has commas demarcating the thousands using f-strings
    """
    return f'{num:,}'



def uncomma(num:str):
    """
    takes in a string of a number that has commas for separators and return the stripped token as an integer.
    """
    return int(num.replace(',',''))

