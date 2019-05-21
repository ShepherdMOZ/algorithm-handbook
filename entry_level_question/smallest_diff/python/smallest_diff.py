def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.

    arrayOne = merge_sort(arrayOne)
    arrayTwo = merge_sort(arrayTwo)
    smallest_diff = float('inf')
    diff = 0
    smallest_set = [None, None]
    array_one_idx = 0
    array_two_idx = 0
    while array_one_idx < len (arrayOne) and array_two_idx < len(arrayTwo):
        first_number  = arrayOne[array_one_idx]
        second_number = arrayTwo[array_two_idx]
        if first_number > second_number:
            diff = first_number - second_number
            array_two_idx += 1
        elif first_number < second_number:
            diff = second_number - first_number
            array_one_idx += 1
        else:
            return [arrayOne[array_one_idx], arrayTwo[array_two_idx]]

        if diff < smallest_diff:
            smallest_diff = diff
            smallest_set[0] = first_number
            smallest_set[1] = second_number

    return smallest_set        


def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        return do_merge(left, right)

def do_merge(left, right):
    left_idx = 0
    right_idx = 0
    merged = []
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] > right[right_idx]:
            merged.append(right[right_idx])
            right_idx += 1
        else:
            merged.append(left[left_idx])
            left_idx += 1
            
    while left_idx < len(left):
        merged.append(left[left_idx])
        left_idx += 1
    
    while right_idx < len(right):
        merged.append(right[right_idx])
        right_idx += 1
    
    return merged

if __name__ == "__main__":
    print(smallestDifference([-1,5,10,20,3],[26,134,135,15,17]))
        
    