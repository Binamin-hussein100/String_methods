c = [12,34,56,8,90,0,6,54]
d = [1,2,3,4,5]

c.extend(d)
print(c) # [12, 34, 56, 8, 90, 0, 6, 54, 1, 2, 3, 4, 5]

data = 'binamin hussein    22 2000'
name_slice = slice(0,19)
age_slice = slice(19,21)
salary_slice = slice(22,None)

print(data[name_slice])  # binamin hussein 
print(data[salary_slice]) # 22

lsty = ['data'] * 7
if not lsty:
    print('list is empty')
else:
    print(lsty) # ['data', 'data', 'data', 'data', 'data', 'data', 'data']


