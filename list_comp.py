"""
LIST COMPREHENSION
"""
# Generate list from other lists
# by applying a new an expression at each element of an iterable

# SYNTAX: newlist = [expression for item in iterable if condition == True]
my_list = 1,2,3,4
sq= [x*x for x in my_list ]
print(sq)

# comprehended
der = [str(i) for i in my_list]
print(der)  # ['1', '2', '3', '4']

#normal
the_list = []

for z in my_list:
   conv =  the_list.append(z*2)
   

print(the_list) # [2, 4, 6, 8]

#### ------Else------> change of syntax. if statement comes before the for loop

dap = [x if x in 'aeiou' else '*' for x in 'apple']
print(dap) # ['a', '*', '*', '*', 'e']

#### ------double iteration-----------> follow the equivalent for loop
# syntax [... for x in ... for y in ...]

inv_lst = [[1,2,3,4,5],[6,7,8,9,0,]]

double_comprehension = [x for g in inv_lst for x in g]
print(double_comprehension) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#### ------in-place mutation and other side effects------->  functions return the same object while in-place functions modifies the existing object. Which is called a side effect. 


# list.sort(). modifies the original list. and returns --None--. wont work in a list comprehension

det = [x.sort() for x in [[19,6],[4,3],[2,6]]]
print(det) # [None, None, None]

# instead use sorted() ==> returns a sorted list rather than sorting in-place


dez = [sorted(x) for x in [[9,6],[4,3],[2,6]]]
print(dez) # [[6, 9], [3, 4], [2, 6]]

man = [sorted(x) for x in [[2, 1], [4, 3], [0, 1]]]
print(man) # [[1, 2], [3, 4], [0, 1]]



#### -----whitespace in list comprehension----> More complicated list comprehensions can reach an undesired length, or become less readable.

dix = [x for x in 'foo' if x not in 'bar']
print(dix) # ['f', 'o', 'o']

"""
CONDITIONAL LIST COMPREHENSION
"""
 
DEV = [x for x in range(19) if x % 2 ==0]
print(DEV) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# normal 
even_numbers = []

for x in range(19):
    if x % 2 ==0:
        even_numbers.append(x)

print(even_numbers) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

try1 = [x if x % 2 == 0 else None for x in range(10)]
# print(try1) [0, None, 2, None, 4, None, 6, None, 8, None]

""""
Avoid repetitive and expensive conditions
"""


## === do === ##
"""
DICTIONARY COMPREHENSION
"""
print({x: x*x for x in (1,2,3,4)}) # {1: 1, 2: 4, 3: 9, 4: 16}

print({p: p-1 for p in (7,8,9,6)}) # {7: 6, 8: 7, 9: 8, 6: 5}

dit = {name: len(name) for name in ('stack','overflow','exchange')}
print(dit) # {'stack': 5, 'overflow': 8, 'exchange': 8}

# starting with a dictionary
intitial_dic = {'a':1, 'b':2}

new_dicl = {key: value for key, value in intitial_dic.items() if key == 'b'}
print(new_dicl) # {'b': 2}


initial_dict = {'x': 1, 'y': 2}
print({key: value for key, value in initial_dict.items() if key == 'x'}) #{'x': 1}
 
 ## inverted dictionary ==> swutching key and value of the dictionary
my_dict = {1: 'a', 2: 'b', 3: 'c'}

    # approach1
print({v:k for k , v in my_dict.items()}) # {'a': 1, 'b': 2, 'c': 3}

### merging dictionaries
dict_1 = {'w':1,'x':2}
dict_2 = {'x':2, 'y':2,'z':2}

print({k : v for d in [dict_1,dict_2] for k,v in d.items()}) # {'w': 1, 'x': 2, 'y': 2, 'z': 2} two of them have bbeen added together

# dictionary unpacking
print({**dict_1, **dict_2}) # {'w': 1, 'x': 2, 'y': 2, 'z': 2}

""""
list comprehension with nested loops
"""

## GENERAL STRUCTURE
# [ expression for target1 in iterable1 [if condition1]
# for target2 in iterable2 [if condition2]...
# for targetN in iterableN [if conditionN] ]

data = [[1,2],[3,4],[5,6]]

# empty list
# looping through the list (data)
# get each element in each list. inside the list=data
# appending it to the empy list


output = []
for each_list in data:
    for element in each_list:
        output.append(element)

print(output) # [1, 2, 3, 4, 5, 6]

# COMPREHEND NEW
# all in one list each element(y) in data(list)
#outer loop comes first
# and each element in y 
# automatically append to a new list. oneliner

output2 = [x for y in data for x in y]
print(output2) #[1, 2, 3, 4, 5, 6]

## comprehending nested loops with a condition 
# if statement comes anywhere after the loop(for)
print(data) # [[1, 2], [3, 4], [5, 6]]
output3 = [y for x in data
                if len(x) == 2
                for y in x
                if y != 5]
print(output3) # [1, 2, 3, 4, 6]
                
"""
Generator expression
"""
# same as list comprehension but not create a full set of results at once. it creates a generator object which can be iterated over.

#### list comprehension
print([x**2 for x in range(10)]) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
### print(x**2 for x in xrange(10)) # no longer exists in python 3
