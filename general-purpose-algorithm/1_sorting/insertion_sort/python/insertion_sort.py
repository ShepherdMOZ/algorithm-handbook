from typing import List

def insertion_sort(array:List[int]) -> List[int]:
    for i in range(1,len(array)):
        j = i
        while j > 0 and array[j] < array [j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1

    return array


if __name__ == "__main__":
    print(insertion_sort([1,4,2,3,6]))