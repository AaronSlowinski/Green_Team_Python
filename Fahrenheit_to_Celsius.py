#!/usr/bin/env python 3.7

fahrenheit = float(input("What temperature (in Fahrenheit) would you like coverted to Celsius? "))
celsius = (fahrenheit - 32) * 5 / 9

print(fahrenheit," F is ", round(celsius,2), "C")