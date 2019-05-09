def get_power_sets(array):
    result = [[]]
    for x in array:
        for i in range(len(result)):
            new_set = result[i] + [x]
            result.append(new_set)
    return result

print(get_power_sets([1,2,3]))