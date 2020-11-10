a = int(input('Enter your first value number: '))
b = int(input('Enter your first value number: '))
print("\nOut of your two entered numbers: ")


def minimum(x, y):
    print("Minimuim is: ", "They are actually equal" if x == y else (x if x < y else y))


def maximum(x, y):
    print("Maximum is: ", "They are still equal" if x == y else (x if x > y else y))


def multiply(x,y):
    if y == 0:
        return 0
    elif y == 1:
        return x
    elif y < 0:
        return - multiply(x, -y)
    if y > 0:
        return x + multiply(x, y - 1)


def power(x, y):
    if (y == 0):
        return 1

    result = x
    increase = x

    for i in range(1, y):
        for j in range(1, x):
            result += increase
        increase = result
    return result


def divmodulo(x, y):
    if y == 0:
        print("You are silly to try dividing by Zero :-P ")
    dividend = 0
    modulo = 1

    dividend = int(x/y)
    modulo = x - (y * dividend)

    return (dividend, modulo)



minimum(a, b)
maximum(a, b)
print("x * y is: ", multiply(a, b))
print("x ^ y is: ", power(a, b))
print("x divmod y is: ", divmodulo(a, b))


def max(values_list):
    value = -1000
    for i in values_list:
        if i > value:
            value = i
    print("Maxim of the values: ", value)


def length(values_list):
    len = 0
    for i in values_list:
        len += 1
    print("Length of the list is: ", len)


values = [2, 5, 7, 99, 34, 67, 89]
print("\nList of Values: ", values)
max(values)
length(values)

