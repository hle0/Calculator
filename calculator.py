#!/usr/bin/env python3

a = int(input('First  number = '))
b = int(input('Second number = '))

op = input('Addition, subtraction, multiplication, or division? (+|-|*|/) ')

if op == '+':
	print(f'Sum = {a+b}')
elif op == '-':
	print(f'Difference = {a-b}')
elif op == '*':
	print(f'Product = {a*b}')
elif op == '/':
	print(f'Quotient = {a/b}')
else:
	raise ValueError('invalid operator')
