numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]


def sort_list(user_list):
    i = 0
    N = len(user_list)
    while i < N - 1:
        j = 0
        while j < N - i - 1:
            if user_list[j] > user_list[j + 1]:
                temp = user_list[j + 1]
                user_list[j + 1] = user_list[j]
                user_list[j] = temp
            j += 1
        i += 1
    print(user_list)


sort_list(numbers)
