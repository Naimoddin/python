print("Python Fundamentals")
# Variables and Data Types
name = "Alice"
age = 30
height = 5.5
is_student = True
print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")
print("Type Conversion Examples:")
print(str(age))  # Type conversion - String conversion
print(int(height))  # Type conversion - int conversion
print(float(age))  # Type conversion - float conversion
print(bool(0))  # Type conversion - blooean conversion
print(bool(1))  # Type conversion - boolean conversion
print(bool(""))  # Type conversion - boolean conversion
print(bool("Hello"))  # Type conversion - boolean conversion
print(bool([]))  # Type conversion - boolean conversion
print(bool([1, 2, 3]))  # Type conversion - boolean conversion
print("None")  # Type conversion - boolean conversion
print(bool(None))  # Type conversion - boolean conversion
print(bool(0.0))  # Type conversion - boolean conversion
print(bool(0.1))  # Type conversion - boolean conversion
print(bool(False))  # Type conversion - boolean conversion
print(bool(True))  # Type conversion - boolean conversion
print(bool({}))  # Type conversion - boolean conversion
print(bool({"key": "value"}))  # Type conversion - boolean conversion
print(bool(set()))  # Type conversion - boolean conversion
print(bool({1, 2, 3}))  # Type conversion - boolean conversion
print(bool(()))  # Type conversion - boolean conversion
print(bool((1, 2, 3)))  # Type conversion - boolean conversion

#Arithmetic Operators
x = 15  
y = 4
print(f"Addition: {x} + {y} = {x + y}") 
print(f"Subtraction: {x} - {y} = {x - y}")
print(f"Multiplication: {x} * {y} = {x * y}")
print(f"Division: {x} / {y} = {x / y}")
print(f"Floor Division: {x} // {y} = {x // y}")
print(f"Modulus: {x} % {y} = {x % y}")
print(f"Exponentiation: {x} ** {y} = {x ** y}") 
print(f"Operator Precedence: {x} + {y} * 2 = {x + y * 2}")
print(f"Operator Precedence: ({x} + {y}) * 2 = {(x + y) * 2}")

#Assignment Operators
a = 10
print(f"Initial value of a: {a}")
a += 5  # a = a + 5
print(f"After a += 5: {a}")
a -= 3  # a = a - 3
print(f"After a -= 3: {a}")
a *= 2  # a = a * 2
print(f"After a *= 2: {a}")
a /= 4  # a = a / 4
print(f"After a /= 4: {a}")
a //= 2  # a = a // 2
print(f"After a //= 2: {a}")
a %= 3  # a = a % 3
print(f"After a %= 3: {a}")
a **= 2  # a = a ** 2
print(f"After a **= 2: {a}")
a = int(a)  # Convert a to an integer for bitwise operations
a &= 1  # a = a & 1
print(f"After a &= 1: {a}")
a |= 1  # a = a | 1
print(f"After a |= 1: {a}")
a ^= 1  # a = a ^ 1
print(f"After a ^= 1: {a}")
a >>= 1  # a = a >> 1
print(f"After a >>= 1: {a}")
a <<= 1  # a = a << 1
print(f"After a <<= 1: {a}")        
print(f"Final value of a: {a}")

#Comparison Operators
x = 10
y = 20
print(f"{x} > {y} = {x > y}")
print(f"{x} < {y} = {x < y}")
print(f"{x} == {y} = {x == y}")
print(f"{x} != {y} = {x != y}")
print(f"{x} >= {y} = {x >= y}")
print(f"{x} <= {y} = {x <= y}")
print(f"{x} > 5 and {y} < 30 = {x > 5 and y < 30}")
print(f"{x} > 15 or {y} < 25 = {x > 15 or y < 25}")
print(f"not {x} > 5 = {not x > 5}")
print(f"not {y} < 30 = {not y < 30}")


#Relational Operators
x = 10
y = 20
print(f"{x} > {y} = {x > y}")
print(f"{x} < {y} = {x < y}")
print(f"{x} == {y} = {x == y}")
print(f"{x} != {y} = {x != y}")
print(f"{x} >= {y} = {x >= y}")
print(f"{x} <= {y} = {x <= y}")

#Identity Operators
print(f"{x} is {y} = {x is y}")
print(f"{x} is not {y} = {x is not y}")

#Logical Operators
print(f"{x} > 5 and {y} < 30 = {x > 5 and y < 30}")
print(f"{x} > 15 or {y} < 25 = {x > 15 or y < 25}")
print(f"not {x} > 5 = {not x > 5}")
print(f"not {y} < 30 = {not y < 30}")
print(f"({x} > 5 and {y} < 30) or ({x} > 15 and {y} < 25) = {(x > 5 and y < 30) or (x > 15 and y < 25)}")   


#Membership Operators
print(f"{x} in [10, 20, 30] = {x in [10, 20, 30]}")
print(f"{y} not in [10, 20, 30] = {y not in [10, 20, 30]}")

#Operators
a = 10
b = 5
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}") 
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")  
print(f"Exponentiation: {a} ** {b} = {a ** b}")
print(f"Comparison: {a} > {b} = {a > b}")
print(f"Comparison: {a} < {b} = {a < b}")   
print(f"Comparison: {a} == {b} = {a == b}")
print(f"Comparison: {a} != {b} = {a != b}")
print(f"Logical AND: {a > 5 and b < 10} = {a > 5 and b < 10}")
print(f"Logical OR: {a > 5 or b < 3} = {a > 5 or b < 3}")
print(f"Logical NOT: not {a > 5} = {not a > 5}")
print(f"Bitwise AND: {a} & {b} = {a & b}")
print(f"Bitwise OR: {a} | {b} = {a | b}")
print(f"Bitwise XOR: {a} ^ {b} = {a ^ b}")
print(f"Bitwise NOT: ~{a} = {~a}")
print(f"Bitwise Left Shift: {a} << 1 = {a << 1}")
print(f"Bitwise Right Shift: {a} >> 1 = {[a >> 1]}")
print(f"Identity: {a} is {b} = {a is b}")
print(f"Identity: {a} is not {b} = {a is not b}")
print(f"Membership: {a} in [1, 10, 20] = {a in [1, 10, 20]}")
print(f"Membership: {b} not in [1, 10, 20] = {b not in [1, 10, 20]}")   
print(f"Operator Precedence: {a} + {b} * 2 = {a + b * 2}")
print(f"Operator Precedence: ({a} + {b}) * 2 = {(a + b) * 2}")
print(f"Augmented Assignment: a += {b} = {a + b}")
a += b  # Augmented Assignment  
print(f"Updated a: {a}")
print(f"Augmented Assignment: a *= 2 = {a * 2}")
a *= 2  # Augmented Assignment
print(f"Updated a: {a}")
print(f"Augmented Assignment: a -= {b} = {a - b}")
a -= b  # Augmented Assignment
print(f"Updated a: {a}")
print(f"Augmented Assignment: a /= 2 = {a / 2}")
a /= 2  # Augmented Assignment
print(f"Updated a: {a}")
print(f"Augmented Assignment: a //= {b} = {a // b}")
a //= b  # Augmented Assignment
print(f"Updated a: {a}")
print(f"Augmented Assignment: a %= {b} = {a % b}")
a %= b  # Augmented Assignment
print(f"Updated a: {a}")
print(f"Augmented Assignment: a **= 2 = {a ** 2}")
a **= 2  # Augmented Assignment
print(f"Updated a: {a}")
a=int(a)  # Convert a to an integer for bitwise operations
b=int(b)  # Convert b to an integer for bitwise operations
print(f"Augmented Assignment: a &= {b} = {a & b}")
a &= b  # Augmented Assignment
print(f"Updated a: {a}")
print(f"Augmented Assignment: a |= {b} = {a | b}")
a |= b  # Augmented Assignment
print(f"Updated a: {a}")
print(f"Augmented Assignment: a ^= {b} = {a ^ b}")
a ^= b  # Augmented Assignment
print(f"Updated a: {a}")
print(f"Augmented Assignment: a >>= 1 = {a >> 1}")
a >>= 1  # Augmented Assignment 
print(f"Updated a: {a}")
print(f"Augmented Assignment: a <<= 1 = {a << 1}")
a <<= 1  # Augmented Assignment 
print(f"Updated a: {a}")
# Excercise: 
age = 25;
education = "Bachelor's Degree"
is_pan = False

if ((age >= 18 and education == "Bachelor's Degree") or is_pan):
    print("You are eligible for the vote.")
else:    print("You are not eligible for the vote.")


# Control Structures
if age > 18:
    print("You are an adult.")
else:    print("You are a minor.")
