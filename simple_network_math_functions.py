def ipmax(n):
    """total ip addresses in a mas:  2^ 32bits - n is total, remove two for broadcast and gateway """
    return f"total usable IP addresses for a mask of /{n} mask", (2 **(32 - n) - 2 )



def symkey(n):
   """Sum of n Natural Numbers - total number of connections required in a full mesh"""
   return n * (n -1) / 2
