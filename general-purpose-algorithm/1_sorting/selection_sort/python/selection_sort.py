from typing import List

def selection_sort(array: List[int]) -> List[int]:
    '''
    This method will sort the pass-in array in asceding order
    '''
    for i in range(len(array)-1):
        min_value = float('inf')
        min_position = -1
        for j in range(i, len(array)):
            if array[j] < min_value:
                min_value = array[j]
                min_position = j

        if min_position is not -1:
            array[min_position] = array[i]
            array[i] = min_value
    return array



if __name__ == "__main__":
    print(selection_sort([3,4,2,1,6]))




