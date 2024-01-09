#!/usr/bin/python3
if __name__ == "__main__":
a = 10

b = 5

from calculator_1 import add, sub, mul, div

result_add = add(a, b)
result_sub = sub(a, b)
result_mul = mul(a, b)
result_div = div(a, b)

print("Result of {} + {} = {}".format(a, b, result_add))
print("Result of {} - {} = {}".format(a, b, result_sub))
print("Result of {} * {} = {}".format(a, b, result_mul))
print("Result of {} / {} = {}".format(a, b, result_div))
