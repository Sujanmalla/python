operator = input ("Enter an operator (+ - * /);")
num1 = float(input ("Enter the first number:"))
num2 = float(input ("enter the second number:"))

if operator == "+" :
   result = num1 + num2
elif operator == "-":
   result = num1 - num2
elif operator == "*":
   result = num1 * num2
elif operator == "/":
   if num2 == 0:
       print("Error: Division by zero")
       result = None
   else:
       result = num1 / num2
else:
   print("Error: Invalid operator")
   result = None

if result is not None:
   print(round(result, 3))
   

