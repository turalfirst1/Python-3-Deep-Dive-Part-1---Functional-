import math

s = [1,2,3]

print(len(s))

from math import sqrt
import math

print(sqrt(4))

print(math.pi)

print(math.exp(1))

def func_1():
    print('running func_1')

func_1()

def func_2(a, #:int
           b  #:int
            ):
    return a * b

print(func_2(2,3))

print(func_2('a', 3))

print(func_2([1, 2], 3))

def func_3():
    return func_4()

def func_4():
    return 'running func_4'

print(func_3())


def func_5():
    return func_6()

def func_6():
    print('running func_6')


print(type(func_5))

my_func = func_4

print(func_4())

print(my_func())


print(lambda x: x**2)

fn1 = lambda x: x**2

print(fn1(2))