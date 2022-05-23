# lists, tuples, dictionaries, sets
print('#' * 10 + ' lists ' + '#' * 10)
list1 = [1, 2.5, 'Hi', True, [1, 2, 3]]
print(list1)

list1.append('Hello!')
print(list1)
print(list1[0])
print(list1[3])
print(list1[-1])
print(list1[-2])

# slicing
print('#' * 10 + ' list slicing ' + '#' * 10)
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list2[0:3])
print(list2[7:10])
print(list2[-3:-1])
print(list2[-3:])  # -3 to last index
print(list2[:5])  # 0..4 index

# some methods for list
print('#' * 10 + ' list methods ' + '#' * 10)
print(dir(list2))
list3 = list2[:5]
list3[-1] = 10
print(list3[:])
list3.remove(3)
print(list3[:])

list4 = list3.copy()
list4.sort(reverse=True)
print(list4[:])

# tuples
print('#' * 10 + ' tuples ' + '#' * 10)
tuple1 = (1, 2, 3, 4, 'str1')
print(dir(tuple1))
print(str(tuple1[-1]) + ' - tuples had less methods than lists: count, index')

# dictionaries
print('#' * 10 + 'dictionaries' + '#' * 10)
dict1 = {'key': 'value'}
print(dir(dict1))
print(dict1['key'])
dict2 = {'name': 'Peter'}
print(dict2['name'])
dict3 = dict(name="Peter", age=30, area='Optimization', other=[1, 2, 3, 4, 5], more={'info': 'Data'})  # json
print(dict3['more'])

# sets
print('#' * 10 + ' sets ' + '#' * 10)
set1 = {1, 2, 3, 4, 4, 4}
print(dir(set1))
print(str(set1) + ' - only unique values in set1 here')
set2: set[int] = {2, 4}
print(set1.intersection(set2))
print(set1 - set2)

# Conditions
print('#' * 10 + ' conditions ' + '#' * 10)
number = 10
if True:
    print(1+1)
if number > 5:
    print('Is great than 5')
else:
    print('Is less than 5')

age = 20
if 18 < age <= 30:
    print('cond1')
elif 30 < age <= 50:
    print('cond2')
elif 50 < age <= 60:
    print('cond3')
else:
    print('cond4')
