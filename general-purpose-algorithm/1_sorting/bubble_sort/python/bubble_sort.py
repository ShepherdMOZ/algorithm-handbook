from typing import List

def bubble_sort(array:List[int]) -> List[int]:
    for i in range(len(array)-1):
        for j in range(1,len(array)):
            if array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]

    return array


if __name__ == "__main__":
    print(bubble_sort([5,6,1,3,2,4]))
    print(bubble_sort([1,2,3,4,5,6]))