def adding_list_elements(list1, list2):
    result = []

    if len(list1) >= len(list2):
        long_list = list1
        short_list = list2
    else:
        long_list = list2
        short_list = list1

    for i in range(len(short_list)):
        result.append(short_list[i] + long_list[i])

    result += long_list[len(short_list):]
    return result


first_list = [1, 2, 3, 4, 5]
second_list = [1, 2, 3, 4, 5, 6, 7, 8]
third_list = adding_list_elements(first_list, second_list)
print(third_list)