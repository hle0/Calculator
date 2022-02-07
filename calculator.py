#!/usr/bin/env python3

a = float(input('First  number = '))
b = float(input('Second number = '))

op = input('Addition, subtraction, multiplication, or division? (+|-|*|/) ')

if op == '+':
	print(f'Sum = {a+b}')
elif op == '-':
	print(f'Difference = {a-b}')
elif op == '*':
	print(f'Product = {a*b}')
elif op == '/':
	if b == 0:
		print('Error: Divide by Zero')
	else:
		print(f'Quotient = {a/b}')
else:
	raise ValueError('invalid operator')
