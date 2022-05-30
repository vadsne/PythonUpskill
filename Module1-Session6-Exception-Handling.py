# try-except
# syntax error example
# while True print('Hello world')

# division by zero example
try:
    a = 1 / 0
    print(a)
except ZeroDivisionError:
    print('Invalid Operation')

# TypeError example
try:
    a = 1 + 'abc'
    print(a)
except ZeroDivisionError:
    print('Invalid Operation')
except TypeError:
    print('Type error')


def my_function(n, d):
    try:
        division = n / d
        return division
    except ZeroDivisionError:
        print('Invalid operation in my_function')
        return '-1'


number = my_function(1, 0)
print(number)
# raise TypeError('Message Error')
# raise OSError('OS Error')


def first_function(n, d):
    print("First Function")
    try:
        return n / d
    except Exception as error:
        error_message = "Error in my First Function: " + str(error)
        raise ValueError(error_message)


def second_function(s1, s2):
    print("Second Function")
    try:
        return s1 + s2
    except Exception as error:
        error_message = "Error in my Second Function: " + str(error)
        raise ValueError(error_message)


def main():
    try:
        num = first_function(1, 2)
        second_function(3, num)
    except Exception as error:
        print(error)
        return -1


main()


print('#' * 10 + ' catch exception and finally statement ' + '#' * 10)
try:
    print('Hi')
    raise ValueError
except Exception:
    print('error')
    pass
finally:
    print("Finally Statement")

print('#' * 10 + ' exception in the 1st function ' + '#' * 10)


def first_function(n, d):
    print("First Function")
    try:
        return n/d
    except Exception as error:
        error_message = "Error in my First Function: " + str(error)
        raise ValueError(error_message)


def second_function(s1, s2):
    print("Second Function")
    try:
        return s1 + s2
    except Exception as error:
        error_message = "Error in my Second Function: " + str(error)
        raise ValueError(error_message)


def main():
    try:
        num = first_function(1, 0)
        second_function(3, num)
    except Exception as error:
        print(error)
        return -1
    finally:
        print("Finally Statement:", 'close connection')


main()

print('#' * 10 + ' try/except/else ' + '#' * 10)
try:
    a = 1/2  # a = 1/0
    print('value: ', a)
except Exception:
    print("Exception block")
    pass
else:
    print("Else block")
