
import math
import numpy as np

def tan_val(num) :
    if str(num).isdidgit :
        return math.tan(num)
    else :
        return 'Arguments should be number type'

def mul_num(a,b):
    multiply=a*b
    return multiply
    

def rem(a,b):
	return a%b

def quiotent(a, b):
    return a // b

def __init__():
    a, b = 10, 5
    q = quiotent(a, b)
    print(q)
    tan_value = tan_val(10)
    print('Tan value of number 10 is : ' + str(tan_val))
    print(rem(10,3))
    print(mul_num(5,10))
    print(np.pi)


__init__()
