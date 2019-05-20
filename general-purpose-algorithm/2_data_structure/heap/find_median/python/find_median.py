from typing import List, Any

class LiveMedianHandler():
    def __init__(self,):
        self.lower_part_max_heap: Heap = Heap(MAX_HEAP_COMPARE_FUNC, [])
        self.upper_part_min_heap: Heap = Heap(MIN_HEAP_COMPARE_FUNC, [])
        self.median:int = 0
    
    def insert(self, value) -> None:
        if self.lower_part_max_heap.length == 0 or self.lower_part_max_heap.peek() > value:
            self.lower_part_max_heap.insert(value)
        else:
            self.upper_part_min_heap.insert(value)
        
        if self.lower_part_max_heap.length - self.upper_part_min_heap.length >= 2:
            self.balance_heaps(self.lower_part_max_heap, self.upper_part_min_heap)

        if self.upper_part_min_heap.length - self.lower_part_max_heap.length >= 2:
            self.balance_heaps(self.upper_part_min_heap, self.lower_part_max_heap)

        self.update_median()
            

    def balance_heaps(self, long_heap: Any, short_heap: Any) -> None:
        exceed_note = long_heap.remove()
        short_heap.insert(exceed_note)

    def update_median(self) -> None:
        total_length = self.lower_part_max_heap.length + self.upper_part_min_heap.length
        if total_length % 2 == 0:
            self.median = round((self.lower_part_max_heap.peek() + self.upper_part_min_heap.peek()) / 2, 2)
        elif self.lower_part_max_heap.length < self.upper_part_min_heap.length:
            self.median = self.upper_part_min_heap.peek()
        else:
            self.median = self.lower_part_max_heap.peek()
    
    def getMedian(self) -> int:
        return self.median

    

def MAX_HEAP_COMPARE_FUNC(a,b):
    return a < b

def MIN_HEAP_COMPARE_FUNC(a,b):
    return a > b    


class Heap():
    
    def __init__(self, compare_func:Any, array):
        self.heap:List[int] = self.build(array)
        self.compare_func = compare_func
        self.length:int = len(self.heap)
        

    def build(self,array) -> List[int]:
        # The first parent node index is different from subsidary parent node index, here you need -2,
        # because we considered that a heap trie is completed so first parrent node will have two children
        first_parrent_idx = (len(array) -2) // 2
        for current_idx in reversed(range(first_parrent_idx + 1)):
            self.sift_down(current_idx, len(array)-1, array)
        return array

    def sift_down(self, current_idx:int, heap_end_idx:int, heap:List[int]) -> None:
        first_child_idx = current_idx * 2 + 1
        while first_child_idx <= heap_end_idx:
            second_child_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= heap_end_idx else -1
            if second_child_idx is not -1:
                if self.compare_func(heap[first_child_idx], heap[second_child_idx]):
                    swap_target_idx = second_child_idx
                else:
                    swap_target_idx = first_child_idx
            else:
                swap_target_idx = first_child_idx
            if self.compare_func(heap[current_idx], heap[swap_target_idx]):
                heap[current_idx], heap[swap_target_idx] = heap[swap_target_idx], heap[current_idx]
                current_idx = swap_target_idx
                first_child_idx = current_idx * 2 + 1
            else:
                return

    def insert(self, value) -> None:
        self.heap.append(value)
        self.sift_up(len(self.heap)-1, self.heap)
        self.length += 1

    def remove(self) -> int:
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        removed_node = self.heap.pop()
        self.sift_down(0,len(self.heap)-1, self.heap)
        self.length -= 1
        return removed_node

    def sift_up(self, current_idx:int, heap:List[int]) -> None:
        parent_idx = (current_idx -1) // 2
        while current_idx >0 and self.compare_func(heap[parent_idx], heap[current_idx]):
            heap[current_idx], heap[parent_idx] = heap[parent_idx], heap[current_idx]
            current_idx = parent_idx
            parent_idx = (current_idx -1) // 2


    def peek(self):
        return self.heap[0]


if __name__ == "__main__":
    median_seq = LiveMedianHandler()
    median_seq.insert(5)
    median_seq.insert(10)
    print(median_seq.getMedian())
    median_seq.insert(100)
    print(median_seq.getMedian())
    median_seq.insert(200)
    median_seq.insert(6)
    median_seq.insert(13)
    median_seq.insert(14)
    print(median_seq.getMedian())
    median_seq.insert(50)
    print(median_seq.getMedian())