#!/usr/bin/env python3

a = int(input('First  number = '))
b = int(input('Second number = '))

op = input('Add or subtract? (+/-) ')

if op == '+':
	print(f'Sum = {a+b}')
elif op == '-':
	print(f'Difference = {a-b}')
else:
	raise ValueError('invalid operator')
