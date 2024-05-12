
from time import time

def LCG(upper_limit : int) -> int:
    """
    membuat angka random dengan rentang 1-upper_limit
    """    
    a = 1664525
    c = 1013904223
    m = 2**32
    seed = int(time())
    seed = (a*seed + c) % m
    return seed % (upper_limit + 1)

if __name__ == '__main__':
    x=LCG()
