# Functions
# Re-utilization in modules
def Print(string):
    print(string)


Print('value')


def subtraction(a, b):
    print('a =', a, 'b =', b)
    print(a-b)


subtraction(10, 20)


def subtraction(a=None, b=None):
    if a is None and b is None:
        Print('Error!')  # use Print() inside another function
    else:
        print('a =', a, 'b =', b)
        print(a-b)


subtraction()
subtraction(10, 20)
var = 100
global another_var


def subtraction(a=None, b=None):
    global another_var  # bad code
    another_var = 10
    if a is None:
        return '-1'
    if b is None:
        return '-1'
    sub_f = a - b
    print('This is a function environment', var)
    return sub_f


diff = subtraction(10, b=50)
Print(diff)


def operations(a, b):
    add_val = a + b
    sub_val = a - b
    exp_val = a ** b
    return add_val, sub_val, exp_val


add, sub, exp = operations(5, 6)
operation_val = operations(7, 8)
print(add, sub, exp)
print(operation_val)
print('#' * 10 + ' keyword arguments ' + '#' * 10)


def my_new_function(*args):
    for arg in args:
        print(arg)


my_new_function('Adel', 'Adonis', 'Ajaz', 'Akos')


def my_new_function(**kwargs):
    print(kwargs)


my_new_function(var1="Hello World", var2=100, var3=[1, 2, 3, 4])
my_new_function(
    var1="Hello World",
    var2=100,
    var3=('Adel', 'Adonis', 'Ajaz', 'Akos')
)


def my_new_function(**kwargs):
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])


my_new_function(var1="Hello World", var2=100, var3=[1, 2, 3, 4])


def square_or_square_root(arr):
    new_array = []
    for a in arr:
        square_root = a**0.5
        if square_root.is_integer():
            v = int(square_root)
        else:
            v = a**2
        new_array.append(v)
    print(new_array)
    return new_array


array = [4, 3, 9, 7, 125, 1, 0, 625]
print(array)
square_or_square_root(array)
