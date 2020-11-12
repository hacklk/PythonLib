numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]
print(numbers)

def sort_list(anylist):
    length = len(anylist)

    for counter in range(length - 1):
        for index in range(length - 1):
            if anylist[index + 1] < anylist[index]:
                temp = anylist[index]
                anylist[index] = anylist[index + 1]
                anylist[index + 1] = temp

    print(anylist)


sort_list(numbers)
