from typing import List

def build_heap(array:List[int]):
    first_parent_idx:int = (len(array) - 2) // 2
    for current_parent_node in reversed(range(first_parent_idx + 1)):
        sift_down(current_parent_node, len(array)-1, array)
    return array

def sift_down(current_idx:int, end:int, heap:List[int]) -> None:
    left_child_idx:int = current_idx * 2 + 1
    while left_child_idx <= end:
        right_child_idx:int = current_idx * 2 + 2 if current_idx * 2 + 2 <= end else -1
        if right_child_idx != -1 and heap[right_child_idx] > heap[left_child_idx]:
            swap_idx:int = right_child_idx
        else:
            swap_idx = left_child_idx

        if heap[current_idx] < heap[swap_idx]:
            heap[swap_idx], heap[current_idx] = heap[current_idx], heap[swap_idx]
            current_idx = swap_idx
            left_child_idx = current_idx * 2 + 1
        else:
            return None

def sift_up(current_idx:int, heap:List[int]) -> None:
    parent_idx:int = (current_idx - 1) // 2
    while parent_idx >= 0 and heap[current_idx] < heap[parent_idx]:
        heap[parent_idx], heap[current_idx] = heap[current_idx], heap[parent_idx]
        current_idx = parent_idx
        parent_idx = (current_idx - 1) // 2

def heap_sort(array:List[int]) -> List[int]:
    build_heap(array)
    for endI in reversed(range(1,len(array))):
        array[0], array[endI] = array[endI], array[0]
        sift_down(0, endI-1, array)

    return array 

if __name__ == "__main__":
    print(heap_sort([8,5,2,9,5,6,3]))