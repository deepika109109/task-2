# 1.Invert a dictionary with list values (group keys by their values) Input:
# d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}


# d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
# tem={}
# for x,y in d.items():
#     tem.setdefault(y,[]).append(x)
# print(tem)

# # Output:
# # {1: ['a', 'c'], 2: ['b'], 3: ['d']}

# # 2. Find Max and Min Value in Dictionary 

# d = {'a': 10, 'b': 5, 'c': 15}
# print("max",max(d.values()))
# print("min",min(d.values()))

# output:max 15
#        min 5

# 3. Create a dictionary using dictionary comprehension for the given list of numbers, 
# where: 
#  Each number is a key.   
# The value is "prime" if the number is prime. 
# The value is "notprime" if the number is not prime

# d={x:"prime" if (x%y!=0 for y in range(2,x)) else "not prime" for x in range(2,6)}
# print(d)

# output:{2: 'prime', 3: 'prime', 4: 'prime', 5: 'prime'}

# 4. Create a dictionary from a list of words, keys as words, values as word lengths, but 
# only for words   longer than 3 characters 
# List: ["hi", "hello", "world", "is", "great"] 

# m=["hi", "hello", "world", "is", "great"] 
# res={x:len(x) for x in m if (len(m))>3}
# print(res)

#    output:{'hi': 2, 'hello': 5, 'world': 5, 'is': 2, 'great': 5}  

# 5.Create a dictionary with uppercase letters as keys and their ASCII values as values use dict comprehension .
# Input: letters = ['a', 'b', 'c']

# letters = ['a', 'b', 'c']
# res={chr(ord(x)-32):ord(x)-32 for x in letters}
# print(res)

# output:{'A': 65, 'B': 66, 'C': 67}

# 6. Explain about setdefault function in dictionary data type ? 
# The setdefault() method in Python dictionaries offers a way to retrieve a value associated with a given key, while also providing a mechanism to insert that key with a specified default value if the key does not already exist in the dictionary.
# Syntax:
#         dict.setdefault(key[, default_value])


# 7. Difference between d[key] and d.get(key)?

# get() will always return a value, whereas dict[key] will raise a KeyError if the given key is missing.

# 8. What is the difference between Shallow Copy and Deep Copy in Python? Explain with examples.
 
# Shallow Copy:
# 1.Creates a new object, but does not create copies of nested objects.
# 2.The nested objects are referenced, not copied.
# 3.Changes made to nested objects in the original or the copy affect both.

# Example of Shallow Copy:
import copy
s=[[1, 2], [3, 4]]
shallow=copy.copy(s)
shallow[0][0]=99
print("s:",original)  
print("shallow:",shallow)

#  Deep Copy:
# 1.Creates a new object and recursively copies all nested objects.
# 2.Changes to nested objects in the copy do not affect the original.

#  Example of Deep Copy:
# list1 = [[1, 2], [3, 4]]
# deep_copy = copy.deepcopy(list1)

# deep_copy[0][0] = 100