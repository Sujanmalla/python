from one import add_number  
from two import sub_number

input1 = float(input("Enter first number: "))
input2= float(input("Enter second number: "))
input3= input("Enter operation (+ or -): ")
if __name__ == "__main__": 
    if input3 == "+":
        sum_result = add_number(input1,input2) 
        print("The sum is:", sum_result)
    elif input3 == "-":
        diff_result = sub_number(input1,input2) 
        print("The difference is:", diff_result)
    else:
        print("Invalid operation. Please enter + or -.")
