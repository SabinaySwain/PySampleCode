""" Math Function """
import math
def math_function(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        sqrt_n = math.sqrt(n)
        log_base= math.log(n)
        sign=math.sin(n)
        return sqrt_n,log_base,sign

num= int(input("Enter a number: "))
sqrt_num = math_function(num)
logarithim=math.log(num)
sing_num=math.sin(num)
print(f"The square root of {num} is {sqrt_num}")
print(f"logarithm of {num} is {logarithim}")
print(f"sing num of {num} is {sing_num}")