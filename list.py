a = ['i','me','him','she']

"""
LIST METHODS
"""

a = [1,2,3,4,5,6,7,8,9]

## append ==> appends a new element at the end of the list
b = [14,15,16,17]
a.append(10)
a.append(b)
a.append(12)

#==== [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [14, 15, 16, 17], 12] ====#

### extend(enumerate) ==> extends the list by appending elemnts from another enumerable
        # adds elements from--into the list

c = [12,34,56,8,90,0,6,54]
d = [1,2,3,4,5]

c.extend(d)

        # extend lists with a non-list enumerable

c.extend(range(4))
# print(c)
    # lists can also be concatinated
haas = [1,2,3,4,5] + [6,7,8,9,0]
# print(haas)

# ========== next ===========#
## index(value, [startIndex]) ==> gets the index of the 1st occurence of the iput value
my_list = [2,3,4,56,8,9,7,5,44,3,11,]

# print(my_list.index(7))

# print(my_list.index(7,5))

# print(my_list.index(7,7)) # valueError, there is no 7 starting at index 7

# ========== next ===========#


##3 insert(index, value) ==> inserts value just before the specified index

the_list = ['binamin','hassan','ahmed','moha']

my_list.insert(6,7)
print(my_list)

# ========== next ===========#

### pop([index]) ==> removes and returns the element at index. with no argument it will remove and return the last element in the  list

print(the_list) # ['binamin', 'hassan', 'ahmed', 'moha']
the_list.pop()
print(the_list) # ['binamin', 'hassan', 'ahmed']
the_list.pop(1)
print(the_list) # ['binamin', 'ahmed']

# ========== next ===========#

### remove(value) ==> Removes first occurnece of the specified value. ValueError if the provided value is not available

king_list = ['samir','khalid','abdul','ahmed','nuur']
king_list.remove('ahmed')
print(king_list) # ['samir', 'khalid', 'abdul', 'nuur']

# ========== next ===========#

### reverse() ==> reverses the list in place
king_list.reverse()
print(king_list) # ['nuur', 'abdul', 'khalid', 'samir']

# ========== next ===========#

### count(value) ==> counts the number of occurence of a value in a list

print(my_list) # [2, 3, 4, 56, 8, 9, 7, 7, 5, 44, 3, 11]

print(my_list.count(7)) # 2
print(my_list.count(56)) # 1
 
# ========== next ===========#

### sort() ==>  sorts a list in numerical or lexicographical order

print(my_list) # [2, 3, 4, 56, 8, 9, 7, 7, 5, 44, 3, 11]
my_list.sort()
print(my_list) # [2, 3, 3, 4, 5, 7, 7, 8, 9, 11, 44, 56]
    # with reverse
my_list.sort(reverse=True)
print(my_list) # [56, 44, 11, 9, 8, 7, 7, 5, 4, 3, 3, 2]
    # with strings

print(king_list) # ['nuur', 'abdul', 'khalid', 'samir']
king_list.sort()
print(king_list) # ['abdul', 'khalid', 'nuur', 'samir']
    # sort by attribute ......done after dictionary review

# ========== next ===========#

### clear() ==> removes all items from the list

print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [14, 15, 16, 17], 12]
a.clear()
print(a) # []

# ========== next ===========#

### Replication. multiplying an existing list with an integer will replicate the list. a large list consisting of copies of the original

b = ['bla'] * 5
print(b) # ['bla', 'bla', 'bla', 'bla', 'bla']

# ========== next ===========#

### element deletion ==> deleting multiple elements in a list using the del keyword
a = list(range(10))
print(a) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del a[::2]
print(a) # [1, 3, 5, 7, 9]

# ========== next ===========#

### copying
z = [1,2,3,4,5,]
y = z
z.append(100)
print(z) # [1, 2, 3, 4, 5, 100]
print(y) # [1, 2, 3, 4, 5, 100]
# definately not what you want. one change on all

    #option 1
# slice old list

master =[1,2,4,5,6,7,89]
new_list = master[:]
# print(new_list) # [1, 2, 4, 5, 6, 7, 89]
new_list.append(200)
print(master) # [1, 2, 4, 5, 6, 7, 89]
print(new_list) # [1, 2, 4, 5, 6, 7, 89, 200]

    #option 2
# built in list function
adc = [12,34,5,66,78,32,3,5,]
new_adc = list(adc)
print(new_adc) # [12, 34, 5, 66, 78, 32, 3, 5]
new_adc.append(10000)
print(new_adc) # [12, 34, 5, 66, 78, 32, 3, 5, 10000]
print(adc) # [12, 34, 5, 66, 78, 32, 3, 5]

    #option 3
# use generic copy.copy()
list_mpya = ['king','queen','prince','princess']
####copy.deepcopy()
import copy
perf = copy.copy(list_mpya)
print(perf) # ['king', 'queen', 'prince', 'princess']
perf.reverse()
print(perf) # ['princess', 'prince', 'queen', 'king']
print(list_mpya) # ['king', 'queen', 'prince', 'princess']

# NB: copy() returns a shallow copy of the list
aa = list_mpya.copy()
print(aa)

# ========== next ===========#

"""
 ACCESSING LIST VALUES
"""
# python lists are 0 indexed
# Attempting to access an index outside the bounds of the list will raise an IndexError .
# Negative indices are interpreted as counting from the end of the list.
# lst[len(lst)-1]

## list slice notation ==> list[start:end:step]

lst = [14,15,16,17,28,35,4,5]
print(lst[1:])
print(lst[:3]) # slice 1st 3
print(lst[::2]) # slice after every step
print(lst[::-1]) # reverse
print(lst[-1:0:-1]) # slices the last element NB: starting index should be greater than the ending index. otherwise the result will be an empty list.
print(lst[1:6]) # slice everything before and after 1 and 6 indexes
## slicing out of range gives an empty list []

# ========== next ===========#

## advanced slicing.
# When lists are sliced the __getitem__() method of the list object is called
# builtin slice method to generate slice objects.

data = 'binamin hussein    22 2000'
name_slice = slice(0,19)
age_slice = slice(19,21)
salary_slice = slice(22,None)

print(data[name_slice])
print(data[age_slice])
print(data[salary_slice])

"""
Checking if list is empty
"""
# emptiness is associated with boolean False.
lsty = ['data'] * 7
if not lsty:
    print('list is empty')
else:
    print(lsty)

# ========== next ===========#

"""
Iterating over a list
"""
list_n = ['foo','bar','baz']
for x in list_n:
    print(x)

# getting the position of the item at the same time
# for (index, item) in enumerate(the_list):
#     print('the item in position {} is: {}'.format(index,item))

for (index, item) in enumerate(list_n):
    print('the item in position {} is: {}'.format(index,item))

for seq in enumerate(the_list):
    print(seq)

# iterating a list based on the index value

for i in range(0, len(my_list)):
    print(my_list[i])

# ========== next ===========#    

"""
checking whether there is an item in a list
"""
   
king = [1,2,3,4,4,5,6,7,7,8,9]
print(3 in king)

# Note: the in operator on sets is asymptotically faster than on lists. If you need to use it many times on
# potentially large lists, you may want to convert your list to a set , and test the presence of elements on
# the set .

"""
Any and all
"""
print(all(king)) # True

print(any(king)) # True

print(any(val > 9 for val in king)) # False


# ========== next ===========#
"""
reversing list elements
"""
numbers = [1,2,3,4,5,6,6,7,8,9,4,5,3,2,4,9,7,2]
rev = reversed(numbers)
print(list(rev))

reved = numbers[::-1]

print(reved)

# ========== next ===========#

"""
Concatinate and merge lists
"""

list1 = [1,2,3,4,5,6]
list2 = [7,8,9,0]

    # simple and normal
marged = list1 + list2
print(marged)
    # zip ==> returns a list of tuples, Nth tuple contains nth elements of all the list
    # 
for a, b in zip(list1,list2):
    print(a,b)  #1 7
                # 2 8
                # 3 9
                # 4 0

# for a, b in itertools.zip_longest(list1, list2):
#     print(a,b)

##### insert is just like concatinate

alist = [123,'xyz','zara','abc']
blist = ['nice','good','perfect']

alist.insert(4, blist)
print(alist)


# ========== next ===========#

"""
length of the list
"""
print(len(alist)) # 5

# len() also works on strings, dictionaries, and other data structures similar to lists.
# Note that len() is a built-in function, not a method of a list object.
# Also note that the cost of len() is O(1) , meaning it will take the same amount of time to get the length of a list
# regardless of its length.


# ========== next ===========#

"""
Removing duplicate
"""
    # convert to set
sup_list = [1,2,3,3,4,5,6,6]
supp_l = set(sup_list)

print(supp_l) # {1, 2, 3, 4, 5, 6} if a list data structure is needed then the set can be converted back to a list using

# ========== next ===========#

"""
list comparison
"""
# compares lexicographically .===> from the 1st numeral

n_list = [1,10,100]
m_list = [2,10,100]

print(n_list < m_list) # True because 1 < 2

print([1, 10] < [1, 10, 100]) # true because it is the shortst and the values are the same up until the 2 index

# ========== next ===========#

"""
Accessing values in a nested loop
"""
alist = [[[1,2],[3,4]], [[5,6,7],[8,9,10], [12, 13, 14]]]
print(alist[0][0][1]) # 2 access the second element of the 1st list in the 1st list

print(alist[1][2][2]) # 14 access the the 3rd item in the 3rd list of the second list

    #perfoming support operations on nested lists

alist[1][1].append('binamin')
print(alist)
    # looping through a nested loop
for i in alist:
    print(i)
    for z in i:
        print(z)

# ========== next ===========#

"""
initializing a list to a fixed number of elements
"""
# immutable elements eg string literals and None

g_wagon = [None] * 10
print(g_wagon)





