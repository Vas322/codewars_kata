def sort_array(source_array):
    odd_sort = sorted(([odd for odd in source_array if odd % 2 != 0]))
    result = []
    i = 0
    for item in source_array:
        if item % 2 != 0:
            result.append(odd_sort[i])
            i += 1
        else:
            result.append(item)
    return result


print(sort_array([5, 8, 6, 3, 4]))
