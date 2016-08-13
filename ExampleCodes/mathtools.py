"""
Simple Mathtool utility function

This tool can check prime numbers and can generate fibonacci series
"""

VERSION = 1.0
AOUTHER = "Suman Debnath"
def fibbo(num):
    """

    Generates num fibonacci series
    :param num:
    :return:
    """
    a , b = 0 , 1
    for i in xrange(num):
         yield a
         a , b = b , a + b

def is_prime(num):
    """

    Retruns True if num is prime, else returns false
    num must be a number
    :param num:
    :return:

    """

    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    else:
        return True





