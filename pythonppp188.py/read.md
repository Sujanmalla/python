# operation  

The use of the operator in programming is to perform a specific operation on data. 

```python
operator = input("Enter an operator (+, -, *, /): ")

# Example usage
a, b = 10, 5
if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
elif operator == '/':
    result = a / b if b != 0 else 'Infinity'
else:
    result = 'Invalid operator'

print(f"{a} {operator} {b} = {result}")
```
# if condition1:
    # do this if condition1 is True
elif condition2:
    # do this if condition1 is False AND condition2 is True
elif condition3:
    # do this if all above are False AND condition3 is True
else:
    # do this if all above conditions are False
