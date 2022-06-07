# IDE's: visual studio code/ pycharm/ spider
# IntelliSence is goode python plug-in for VScode
# there are package and subpackage to import below
import sys
import operations.operations as op
import operations.moreoperations.moreoperations as mop
sys.path.insert(1, 'C:\\Users\\esnevad\\PycharmProjects\\PythonUpskill')


print('#' * 10 + ' working with py-scripts ' + '#' * 10)
print('My 1st script', 'c')
s = op.add(1, 21)
print('the sum is:', s)
m = mop.mul(3, 6)
print('the mul is:', m)

print(sys.path)
