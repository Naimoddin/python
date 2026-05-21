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
# Control Structures
if age > 18:
    print("You are an adult.")
else:    print("You are a minor.")
