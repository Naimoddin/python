#Reading Input from the user
"""name = input("What is your name? ")
print(f"Hello, {name}!")
age = int(input("How old are you? "))
print(f"You are {age} years old.")  
income = float(input("What is your annual income? "))
print(f"name:{name} and age:{age} and income:{income}")"""

#Working with lists
print("Working with lists")
lt = [1, 2, 3, 4, 5]  
print(lt) 
print("append 7 to the end of the lt")
lt.append(7) # append 7 to the end of the lt
print(lt)
print("insert 8 at index 2")
lt.insert(2,8) # insert 8 at index 2
print(lt)
print("print the length of the lt")
print(len(lt)) # print the length of the lt
print("print the first element of the lt-lt[0]")
print(lt[0]) # print the first element of the lt
print("print the third element of the lt - lt[2]")
print(lt[2]) # print the third element of the lt
print("print the index of the first occurrence of 1 in the lt -lt.index(1) ")
print(lt.index(1)) # print the index of the first occurrence of 1 in the lt
print("print the number of times 1 appears in the lt-lt.count(1)")
print(lt.count(1)) # print the number of times 1 appears in the lt
print("print the index of the first occurrence of 7 in the lt - lt.index(7)")
print(lt.index(7)) # print the index of the first occurrence of 7 in the lt
print("print the number of times 7 appears in the lt")
print(lt.count(7)) # print the number of times 7 appears in the lt
print("print from the 2nd element to the 3rd element (not including the 3rd element) -lt[1:3]")
print(lt[1:3])   # print from the 2nd element to the 3rd element (not including the 3rd element) 
print("print from the 1st element to the end of the lt - lt[0:]")
print(lt[0:]) # print from the 1st element to the end of the lt
print("print from the 2nd element to the end of the lt - lt[1:]")
print(lt[1:]) # print from the 2nd element to the end of the lt
print("print from the last element to the end of the lt - lt[-1:]")
print(lt[-1:]) # print from the last element to the end of the lt (which is just the last element)
print("print all elements except the last one - lt[:-1]")
print(lt[:-1]) # print all elements except the last one
print("print first 3 elements - lt[:3]")
print(lt[:3]) # print first 3 elements
print("print last 3 elements- lt[-3:]")
print(lt[-3:]) # print last 3 elements
print(" print  all elements except last 3- lt[:-3]")
print(lt[:-3]) # print  all elements except last 3
print("# print 3rd and 2nd last elements - lt[-3:-1]")
print(lt[-3:-1]) # print 3rd and 2nd last elements
print("print 3rd last element to 1st element (empty lt because start index is greater than end index) - lt[-3:1]")
print(lt[-3:1]) # print 3rd last element to 1st element (empty lt because start index is greater than end index)    
print("print every 2nd element starting from the first element - lt[::2]")
print(lt[::2]) # print every 2nd element starting from the first element    
print("print every 2nd element starting from the second element")
print(lt[1::2]) # print every 2nd element starting from the second element
print("print the lt in reverse order - lt[::-1]")
print(lt[::-1])  # print the lt in reverse order
print("print every 3rd element starting from the first element -lt[::3]")
print(lt[::3]) # print every 3rd element starting from the first element
print("print every 2nd element starting from the second element up to the 5th element - lt[1:5:2]")
print(lt[1:5:2])  # print every 2nd element starting from the second element up to the 5th element
print("print every 3rd element starting from the second element up to the 5th element")
print(lt[1:5:3]) # print every 3rd element starting from the second element up to the 5th element

#Excerise: Create a lt of the first 10 square numbers and print it.
num = int(input("Enter a number: "))
l = []
for i in range(1, num+1):
    l.append(i**2)
print(l)
print(l.reverse()) # print the lt in reverse order
print(l)
print(l.sort(reverse=True)) # print the lt in sorted order
print(l)

#Working with tuples
print("Working with tuples")
t = (1, 2, 3, 4, 5)
print(t) # print the tuple
print("print the first element of the tuple - t[0]")
print(t[0]) # print the first element of the tuple      
print("print the third element of the tuple - t[2]")
print(t[2]) # print the third element of the tuple
print("print the index of the first occurrence of 1 in the tuple - t.index(1)")
print(t.index(1)) # print the index of the first occurrence of 1 in the tuple
print("print the number of times 1 appears in the tuple - tuple.count(1)")
print(t.count(1)) # print the number of times 1 appears in the tuple
print("print from the 2nd element to the 3rd element (not including the 3rd element) - t[1:3]")
print(t[1:3]) # print from the 2nd element to the 3rd element (not including the 3rd element)
print("print from the 1st element to the end of the tuple - t[0:]")
print(t[0:]) # print from the 1st element to the end of the tuple
print("print from the 2nd element to the end of the tuple - t[1:]")
print(t[1:]) # print from the 2nd element to the end of the tuple
print("print from the last element to the end of the tuple - t[-1:]")   
print(t[-1:]) # print from the last element to the end of the tuple (which is just the last element)
print("print all elements except the last one - t[:-1]")
print(t[:-1]) # print all elements except the last one
print("print first 3 elements - t[:3]")
print(t[:3]) # print first 3 elements
print("print last 3 elements- t[-3:]")
print(t[-3:]) # print last 3 elements
print(" print  all elements except last 3- t[:-3]")
print(t[:-3]) # print  all elements except last 3
print("print 3rd and 2nd last elements - t[-3:-1]")
print(t[-3:-1]) # print 3rd and 2nd last elements
print("print 3rd last element to 1st element (empty tuple because start index is greater than end index) - t[-3:1]")
print(t[-3:1]) # print 3rd last element to 1st element (empty tuple because start index is greater than end index)
print("print every 2nd element starting from the first element - t[::2]")
print(t[::2]) # print every 2nd element starting from the first element
print("print every 2nd element starting from the second element")
print(t[1::2]) # print every 2nd element starting from the second element
print("print the tuple in reverse order - t[::-1]")
print(t[::-1]) # print the tuple in reverse order
print("print every 3rd element starting from the first element -t[::3]")
print(t[::3]) # print every 3rd element starting from the first element
print("print every 2nd element starting from the second element up to the 5th element - t[1:5:2]")
print(t[1:5:2]) # print every 2nd element starting from the second element up to the 5th element
print("print every 3rd element starting from the second element up to the 5th element")
print(t[1:5:3]) # print every 3rd element starting from the second element up to the 5th element    

#Convert tuple to lt and vice versa
print("Convert tuple to lt and vice versa")
t = (1, 2, 3, 4, 5) 
print(t) # print the tuple
li = list(t) # convert tuple to lt
print(li) # print the lt    
t2 = tuple(li) # convert lt to tuple
print(t2) # print the tuple  

#work with sets
print("Working with sets")
s = {1,2,3,4,5}
print(s) # print the set  
print("add 6 to the set - s.add(6)")
s.add(6) # add 6 to the set   
print(s) # print the set
print("remove 3 from the set - s.remove(3)")
s.remove(3) # remove 3 from the set
print(s) # print the set
print("check if 4 is in the set - 4 in s")
print(4 in s) # check if 4 is in the set  
print("check if 3 is in the set - 3 in s")
print(3 in s) # check if 3 is in the set
print("print the length of the set - len(s)")
print(len(s)) # print the length of the set   
print("print the union of the set with another set {4,5,6,7} - s.union({4,5,6,7})")
print(s.union({4,5,6,7})) # print the union of the set with another set {4,5,6,7}
print("print the intersection of the set with another set {4,5,6,7} - s.intersection({4,5,6,7})")
print(s.intersection({4,5,6,7})) # print the intersection of the set with another set {4,5,6,7}
print("print the difference of the set with another set {4,5,6,7} - s.difference({4,5,6,7})")
print(s.difference({4,5,6,7})) # print the difference of the set with another set {4,5,6,7}
print("print the symmetric difference of the set with another set {4,5,6,7} - s.symmetric_difference({4,5,6,7})")
print(s.symmetric_difference({4,5,6,7})) # print the symmetric difference of the set with another set {4,5,6,7}   
print("print the set in reverse order - s[::-1] (not possible because sets are unordered)")
print(s) # print the set (not in reverse order because sets are unordered)
print("print every 2nd element starting from the first element - s[::2] (not possible because sets are unordered)")
print(s) # print the set (not every 2nd element because sets are unordered)
print("print every 2nd element starting from the second element - s[1::2] (not possible because sets are unordered)")
print(s) # print the set (not every 2nd element because sets are unordered)

#working with dictionaries
print("Working with dictionaries")
dic={}
print(dic) # print the empty dictionary
d = {"name": "Alice", "age": 30, "income": 50000}
print(d) # print the dictionary 
print("print the value of the name key - d['name']")
print(d['name']) # print the value of the name key  
print("print the value of the age key - d['age']")
print(d['age']) # print the value of the age key
print("print the value of the income key - d['income']")
print(d['income']) # print the value of the income key
print("add a new key-value pair to the dictionary - d['city'] = 'New York'")
d['city'] = 'New York' # add a new key-value pair to the dictionary
print(d) # print the dictionary
print("remove the age key from the dictionary - del d['age']")
del d['age'] # remove the age key from the dictionary
print(d) # print the dictionary
print("check if the name key is in the dictionary - 'name' in d")
print('name' in d) # check if the name key is in the dictionary     
print("check if the age key is in the dictionary - 'age' in d")
print('age' in d) # check if the age key is in the dictionary
print("print the keys of the dictionary - d.keys()")
print(d.keys()) # print the keys of the dictionary
print("print the values of the dictionary - d.values()")
print(d.values()) # print the values of the dictionary
print("print the key-value pairs of the dictionary - d.items()")
print(d.items()) # print the key-value pairs of the dictionary
print("print the dictionary in reverse order - d[::-1] (not possible because dictionaries are unordered)")
print(d) # print the dictionary (not in reverse order because dictionaries are unordered)
print("print every 2nd key-value pair starting from the first key-value pair - d[::2] (not possible because dictionaries are unordered)")
print(d) # print the dictionary (not every 2nd key-value pair because dictionaries are unordered)
print("print every 2nd key-value pair starting from the second key-value pair - d[1::2] (not possible because dictionaries are unordered)")
print(d) # print the dictionary (not every 2nd key-value pair because dictionaries are unordered)   
print("print the dictionary sorted by keys - dict(sorted(d.items()))")
print(dict(sorted(d.items()))) # print the dictionary sorted by keys    
print("print the dictionary sorted by values - dict(sorted(d.items(), key=lambda item: item[1]))")
print(dict(sorted(d.items(), key=lambda item: str(item[1])))) # print the dictionary sorted by values
print("print the dictionary sorted by values in reverse order - dict(sorted(d.items(), key=lambda item: item[1], reverse=True))")
print(dict(sorted(d.items(), key=lambda item: str(item[1]), reverse=True))) # print the dictionary sorted by values in reverse order
print("print the dictionary sorted by keys in reverse order - dict(sorted(d.items(), reverse=True))")
print(dict(sorted(d.items(), reverse=True))) # print the dictionary sorted by keys in reverse order
print("print the dictionary sorted by values in reverse order - dict(sorted(d.items(), key=lambda item: item[1], reverse=True))")
print(dict(sorted(d.items(), key=lambda item: str(item[1]), reverse=True))) # print the dictionary sorted by values in reverse order
print("print the dictionary sorted by keys in reverse order - dict(sorted(d.items(), reverse=True))")
print(dict(sorted(d.items(), reverse=True))) # print the dictionary sorted by keys in reverse order

print("Exercise")
stm = [{"id": 1, "name": "Alice", "age": 30, "income": 50000},
        {"id": 2, "name": "Bob", "age": 25, "income": 40000},
        {"id": 3, "name": "Charlie", "age": 35, "income": 60000}]

print(stm) # print the list of dictionaries
print("print the names of all students")
for student in stm:
    print(student['name']) # print the names of all students    
    print(student['age']) # print the ages of all students
    print("print the incomes of all students")
    print(student['income']) # print the incomes of all students
stm.sort(key=lambda student: student['age']) # sort the list of dictionaries by age
print(stm) # print the sorted list of dictionaries
stm.sort(key=lambda student: student['income'], reverse=True) # sort the list of dictionaries by income in reverse order
print(stm) # print the sorted list of dictionaries
print("print the names of all students sorted by age")
for student in stm:
    print(student['name']) # print the names of all students sorted by age  

for student in stm:
    print(set(student.values())) # print the set of values for each student