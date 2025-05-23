# -*- coding: utf-8 -*-
"""Calculator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nK8W47EN0vJQvEjYZeR7nF0E4TMdLOOF
"""

def get_number(number):
  while True:
    operand = input("Number" + str(number) + ": ")
    try:
      return float(operand)
    except:
      print("Please enter a valid number: ")

operand1 = get_number(1)
operand2 = get_number(2)
sign = input("Input operation: ")

result = 0
if sign == "+":
  print(operand1 + operand2)
elif sign == "-":
  print(operand1 - operand2)
elif sign == "*":
  print(operand1 * operand2)
elif sign == "/":
  if operand2 != 0:
    print(operand1 / operand2)
  else:
    print("Cannot divide by zero")
    get_number(1)
else:
  print("Invalid operation")

