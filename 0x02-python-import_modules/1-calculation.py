#!/usr/bin/python3
a = 10
b = 5
calculator_1 = __import__('calculator_1')

res_add = calculator_1.add(a, b)
res_sub = calculator_1.sub(a, b)
res_mul = calculator_1.mul(a, b)
res_div = calculator_1.div(a, b)

print("{} + {} = {}".format(a, b, res_add))
print("{} - {} = {}".format(a, b, res_sub))
print("{} * {} = {}".format(a, b, res_mul))
print("{} / {} = {}".format(a, b, res_div))

