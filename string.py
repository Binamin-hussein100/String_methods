# str.alpha() => retuns true if all characters are alphabetic

# print('Hello World'.isalpha()) # false
# print("Hello2world".isalpha()) #false
# print("Helloworld!".isalpha()) #false
# print("Helloworld".isalpha())  #true evaluates everything including space, number and punctuation


# str.isupper(), str.islower() and str.istitle()
# they all test for capitalization.

###str.isupper()
# print("HeLLO WORLD".isupper()) #false
# print("HOLLO WORLD".isupper()) #true

##str.islower()
# print("HeLLO WORLD".islower()) #false
# print("hello world".islower()) #true
# print("".islower()) #false

### str.istitle() true is string is title cases
# print("HeLLO WORLD".istitle()) #false
# print("Hello World".istitle()) # true


""""
str.isdecimal , str.isdigit , str.isnumeric
"""
## isdecimal => whether the string is a sequence of decimal digit. suitable for representing decimal number.

# print('12345'.isdecimal()) # true

# # isdigit => whether it is suitable for representing a number
# print('12345'.isdigit()) #true

""""
isalnum() => checks if the string is alpha numeric #contains alphabetic or numeric characters 
 """
# print('12345'.isalnum()) #true


"""
isspace() => true if string contains only whitespace
"""
# print(" ".isspace()) #true
# print(''.isspace()) #false

# my_str = ''
# print(not my_str.strip()) #true


"""
STRING CONTAINS
"""
# checking if a string contains a sub string
# print("foo" in "foo.baz.bar") # true

#NT: testing an empty string will always return true

"""
Join a list of strings into one string using .join()
"""
print(" ".join(["once","upon","a","time"])) # once upon a time
print(["once","upon","a","time"])

print("---".join(['once','upon','a','time'])) #once---upon---a---time

"""
Counting the number of times a sub string has appeared
"""
###str.count(sub[,start[, end]])###

# sent = 'My name is binamin hussein hassan'
# print(sent.count('s'))

"""
Case insensitive string comparison
"""



"""
JUSTIFYING STRING
"""


Jina = 'John'

clam  = 'His name is {}'

# print(clam.format(Jina))
# print(clam.format(Jina.rjust(10)))

"""
TESTING THE STARTING AND ENDING CHARACTERS OF A STRING
"""
### str.startswith()



s = 'This is a test string'
print(s.startswith('Th', 2))

# addition of an int specifies which position to search from

# checking multiple
# print(s.startswith(('Th', 'th')))
# print(s.startswith(('Th', 'th')))

## str.endswith()
#a tuple can also be used
b = 'this ends with a fullstop.'
print(b.endswith('.'))

"""
Conversion between str or bytes data and unicode characters
"""
s = b'\xc2\xa9 abc' # this is a byte not a string
print(type(s))
z = s.decode('utf-8')
print(type(z))

"""
string slicing
"""
###string[start:end:step]


""""
programix
"""

# def county(str_1):
#   if len(str_1) < 2:
#     return ''
    
#   else:
#     striped_1 = str_1[0:2]
#     striped_2 = str_1[-2:]
    
#     combined = striped_1 + striped_2
    
  
#   return combined

# print(county("binamin"))

"""
replace exersice
"""

# def interchange(str_1, str_2):
  
#   first = str_1[0]
#   second = str_2[0]
  
#   new_str_1 = str_1.replace(str_1[0], second)
#   print(new_str_1)
#   new_str_2 = str_2.replace(str_2[0], first)
#   print(new_str_2)
  
#   combined = new_str_1 + new_str_2
  
#   return combined

# print(interchange("binamin", "hussein"))
  