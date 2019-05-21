from typing import List

def build_min_heap(array: List[int]):
    first_parent = (len(array) -2) // 2
    for current_parent in reversed(range(first_parent + 1)):
        sift_down(current_parent, len(array)-1, array)
    return array
        
def sift_down(current_parent:int, end_idx:int, array:List[int]):
    first_child = current_parent * 2 + 1
    while first_child <= end_idx:
        second_child = current_parent * 2 + 2 if current_parent * 2 + 2 <= end_idx else -1
        if second_child is not -1 and array[first_child] > array[second_child]:
            swap_idx = second_child
        else:
            swap_idx = first_child
        if array[current_parent] > array[swap_idx]:
            array[current_parent], array[swap_idx] = array[swap_idx], array[current_parent]
            current_parent = swap_idx
            first_child = current_parent * 2 + 1
        else:
            return
    
def min_heap_sort(array: List[int]):
    build_min_heap(array)
    for endI in reversed(range(1,len(array))):
        array[0], array[endI] = array[endI], array[0]
        sift_down(0, endI-1, array)
    return array[::-1]



if __name__ == "__main__":
    print(min_heap_sort([8,5,2,9,5,6,3]))

