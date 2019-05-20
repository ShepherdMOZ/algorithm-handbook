from typing import List, Dict

class MinHeap():

    def __init__(self, array:List[int]):
        self.heap: List[int] = self.build_heap(array)

    
    def build_heap(self, array:List[int]):
        first_parent_idx:int = (len(array) - 2) // 2
        for current_parent_node in reversed(range(first_parent_idx + 1)):
            self.sift_down(current_parent_node, len(array)-1, array)
        return array

    def sift_down(self, current_idx:int, end:int, heap:List[int]) -> None:
        left_child_idx:int = current_idx * 2 + 1
        while left_child_idx <= end:
            right_child_idx:int = current_idx * 2 + 2 if current_idx * 2 + 2 <= end else -1
            if right_child_idx != -1 and heap[right_child_idx] < heap[left_child_idx]:
                swap_idx:int = right_child_idx
            else:
                swap_idx = left_child_idx

            if heap[current_idx] > heap[swap_idx]:
                heap[swap_idx], heap[current_idx] = heap[current_idx], heap[swap_idx]
                current_idx = swap_idx
                left_child_idx = current_idx * 2 + 1
            else:
                return None

    def sift_up(self, current_idx:int, heap:List[int]) -> None:
        parent_idx:int = (current_idx - 1) // 2
        while parent_idx >= 0 and heap[current_idx] < heap[parent_idx]:
            heap[parent_idx], heap[current_idx] = heap[current_idx], heap[parent_idx]
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2


    def peek(self):
        return (self.heap[0])

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        removed_value:int = self.heap.pop()
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return removed_value

    def insert(self, number):
        self.heap.append(number)
        self.sift_up(len(self.heap) - 1, self.heap)



class MaxHeap():

    def __init__(self, array:List[int]):
        self.heap: List[int] = self.build_heap(array)

    
    def build_heap(self, array:List[int]):
        first_parent_idx:int = (len(array) - 2) // 2
        for current_parent_node in reversed(range(first_parent_idx + 1)):
            self.sift_down(current_parent_node, len(array)-1, array)
        return array

    def sift_down(self, current_idx:int, end:int, heap:List[int]) -> None:
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

    def sift_up(self, current_idx:int, heap:List[int]) -> None:
        parent_idx:int = (current_idx - 1) // 2
        while parent_idx >= 0 and heap[current_idx] < heap[parent_idx]:
            heap[parent_idx], heap[current_idx] = heap[current_idx], heap[parent_idx]
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2


    def peek(self):
        return (self.heap[0])

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        removed_value:int = self.heap.pop()
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return removed_value

    def insert(self, number):
        self.heap.append(number)
        self.sift_up(len(self.heap) - 1, self.heap)