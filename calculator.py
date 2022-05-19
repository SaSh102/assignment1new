import math

a=int(input())
b=int(input())

op=input()

if op=="+":
    result = a+b
if op=="-":
    result = a-b
if op=="*":
    result = a*b
if op=="/":
    if b != 0:
        result = a/b
    else:
        result = 'error'

if op=="sin":
    result = math.sin(a)
if op=="cos":
    result = math.cos(a)
if op=="tan":
    result = math.tan(a)
if op=="cot":
    result = math.cot(a)
if op=="radical":
    result = math.sqrt(a)
if op=="factorial":
    result = math.factorial(a)
print(result)