import math
operation = input ("Enter the desired operation: (+,-,*,/,Exponent,SquareRoot,AbsoluteValue,Rounding) exactly as listed:  ")
if operation=="+":
    num1 = input ("Number 1: ")
    num2 = input("Number 2: ")
    print(float(num1)+float(num2))
elif operation=="-":
    num1 = input ("Number 1: ")
    num2 = input("Number 2: ")
    print(float(num1)-float(num2))
elif operation == "*":
    num1 = input("Number 1: ")
    num2 = input("Number 2: ")
    print(float(num1) * float(num2))
elif operation == "/":
    num1 = input("Number 1: ")
    num2 = input("Number 2: ")
    print(float(num1) / float(num2))
elif operation == "Exponent":
    num1 = input("Number 1: ")
    num2 = input("Number 2: ")
    print(float(num1) ** float(num2))
elif operation == "Rounding":
    num = input("Number: ")
    print(round(float(num)))
elif operation == "AbsoluteValue":
    num = input("Number: ")
    print(abs(float(num)))
elif operation == "SquareRoot":
    num = input("Number: ")
    if float(num) > 0:
     print(float(math.sqrt(float(num))))
    else:
     print("!!!Negative values cannot be entered for this operation!!!")