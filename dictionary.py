"""
DICTIONARY
"""
# key value store also known as mapping.
# dictionaries can be created in many ways.
# ONE
### literal syntax 
import builtins
from ctypes import DEFAULT_MODE


d = {} # empty dictionary
d = {'key': 'value'} # dict with initial values
# -- unpacking one or more dicts with a literal syntax is possible
otherdict = {}
# this makes a shallow copy of the dictionary
d = {**otherdict}
## also update he shallow content with the content of yetanotherdict
yetanotherdict = {}
d = {**otherdict,**yetanotherdict}

## dictionary comprehensions
d = {k:v for k,v in otherdict}

# TWO
# builtin class
d = dict() # empty
d = dict(key = 'value') # explicit keyword argument
d = dict([('key','key')])  # passing a list of key/value pairs
# makes a shallow copy of another dict (only possible if keys are only strings)
d = dict(**otherdict)


d['newkey'] = 42 # adding a new key with a value to a dictionary
print(d)

del d['newkey'] # deleting a key

### avoiding KeyError exception

mydict = {}
# print(mydict['not there'])  # KeyError: 'not there'

# ===>  the use dict.get method. This allows you to specify a default value to return in the case of an absent key

# syntax ==> mydict.get(key, default_value)
# this returns the dictionary[key] if it exists. otherwise it returns a default value

thedict = {}
print(thedict) # {}

print(mydict.get('foo','bar')) # bar => it prints bar since it cant find the foo

# ===> mydict.setdefault(key, default_value)
print(mydict.setdefault('zick','noor')) # noor => it will print out 'noor' since it cant find 'zick'

# ===> try and except method
try:
    value = thedict['foo']
except KeyError:
    value = 'note'

print(value) # note

# ===> you could also check if the key is in the dictionary

if 'zink' in thedict:
    the_value = thedict['foo']
else:
    the_value = 'binamin'

print(the_value) # binamin

"""
Iterating over a dictionary
"""
d = {'a': 1, 'b':2, 'c':3, 'd':4}
for x in d:
    print(x, d[x]) 
    # a 1
    # b 2
    # c 3
    # d 4
# also true when used in a comprehension
print([key for key in d]) # ['a', 'b', 'c', 'd']

# the items() method can be used to loop over both the key and the value simultaneously
print(d) #{'a': 1, 'b': 2, 'c': 3, 'd': 4}

for x,y in d.items():
    print(x,y) 
    # a 1
    # b 2
    # c 3
    # d 4

# the values() method can be used to iterate over only the values:
print(d) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# for key, value in d.values(): ## Call awadh
#     print(key, value) 


#Here, the methods keys() , values() and items() return lists, and there are the three extra methods iterkeys()
#itervalues() and iteritems() to return iterators.

"""
A dictionary with default values
"""
from collections import defaultdict
d = defaultdict(int)
print(d['key']) # 0

d_3 = d['key'] = 5
print(d_3) # 5

d = defaultdict(lambda: 'empty')

print(d['key']) #empty
d_5 = d['key'] = 'full'
print(d_5) # full

# alternatively. if you must use the built-in dict class, using dict.setdefault() will allow you to create a default whenever you access a key that doesnot exist

dot = {}

dot.setdefault('another_key',[]).append('This works')
print(dot) #{'another_key': ['This works']}

"""
Merging dictionaries
"""
fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}

# merging
fishdog = {**fish, **dog}
print(fishdog) # {'name': 'Clifford', 'hands': 'paws', 'special': 'gills', 'color': 'red'}

"""
Accessing keys and values
"""
mydicto = {
    'a':'1',
    'b':'2'
}
# getting a list of keys using the keys() method
print(mydicto.keys()) # dict_keys(['a', 'b'])

# getting a list of values using the values() method
print(mydicto.values()) # dict_values(['1', '2'])

# for both keys and values . use the items() method
print(mydicto.items()) #dict_items([('a', '1'), ('b', '2')])

## NOTE: Because a dict is unsorted, keys() , values() , and items() have no sort order. Use sort() , sorted() , or an
#OrderedDict if you care about the order that these methods return.

### python 3 returns a special iterable object and not a list.

"""
ACCESSING VALUES IN A DICTIONARY
"""
dictionary = {
    'Hello': 1234,
    'World':5678
}

print(dictionary['Hello']) # 1234
# Hello is a key is used to look up a value in the dict by placing the key in square brackets.

# the number 1234 is  a value that hello maps to in the dict.

# looking up a value that does not  exist will raise a keyError. to avoid this one should use the  dict.get() method. This method  supplies a default value for incase a the key doesnt exist.

w = dictionary.get('whatever')
print(w) # None
x = dictionary.get('whatever', 'uun hu')
print(x) # uun hu

"""
CREATING AN UNORDERED DICTIONARY
"""
# import the ordered dictionary (OrderedDict) from collection

from collections import OrderedDict
d = OrderedDict()
print(d) #OrderedDict()
d['first'] = 1
d['second'] = 2
d['third'] = 3
print(d)  # OrderedDict([('first', 1), ('second', 2), ('third', 3)])

for x in d:
    print(x, d[x])

    # first 1
    # second 2
    # third 3

"""
Unpacking dictionaries using the ** operator
"""
# used to deliver key-value pairs in a dictionary into a functions arguments. 

def parrot(voltage, state, action):
    print('This parrot wouldnt', action, end=' ')
    print('If you put', voltage, 'volts through it.', end=' ')
    print("E's", state,'!')

d = {'voltage':'four million','state':"bleedin' demises", 'action':'Voom' }

parrot(**d) # This parrot wouldnt Voom If you put four million volts through it. E's bleedin' demises !

### Can also be used to merge an arbitrary number of dict objects
 # CODE NO' 131

"""
 The Trailing Comma
 """
# trailing comma is a comma after the last

role = {
    'By day': 'a typical programmer',
    'by night': 'Still a typical programmer',
}
# NOTE THE COMMA at the end of the last element

"""
The dict()
"""
# can be used to create dictionaries from keyword arguments. or from a single iterable of key-pair values, or from a single dictionary 
print(dict(a=1,b=2,c=3)) # {'a': 1, 'b': 2, 'c': 3}
print(dict( [('d', 4), ('e', 5), ('f', 6)] )) # {'d': 4, 'e': 5, 'f': 6}
print(dict([('a', 1)], b=2, c=3)) # {'a': 1, 'b': 2, 'c': 3}
print(dict({'a' : 1, 'b' : 2}, c=3)) #{'a': 1, 'b': 2, 'c': 3}

"""
Dictionary examples
"""
car = {}




"""
Sorting key and values
"""
# create a function
# use sorted method to sort the dict

def sort_by(dictionary):
  srt = sorted(dictionary)
  print(srt)
  return srt
  
sort_by({1:'one',2:'two',3:'three'})

## for value

def sort_for_me(dic):
    select = dic.values()
    sot = sorted(select)
    print(sot)
    return sot

sort_for_me({1:'one',2:'two',3:'three'}) # ['one', 'three', 'two']