from typing import List

def merge_sort_sd(array:List[int]) -> List[int]:
    '''
    Complexity:
        Best: O(nlog(n)) time | O(nlog(n)) space
        Avg: O(nlog(n)) time | O(nlog(n)) space
        Worst: O(nlog(n)) time | O(nlog(n)) space 
    '''
    if len(array) == 1:
        return array
    else:
        mid:int = len(array) // 2
        left: List[int] = merge_sort_sd(array[:mid])
        right: List[int] = merge_sort_sd(array[mid:])
        
        left_idx:int = 0
        right_idx:int = 0
        merged: List[int] = []

        while left_idx < len(left) and right_idx < len(right):
            if right[right_idx] < left[left_idx]:
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


def merge_sort_opt(array:List[int], aux_array:List[int], start_idx:int, end_idx:int) -> None:
    '''
    Complexity:
        Best: O(nlog(n)) time | O(n) space
        Avg: O(nlog(n)) time | O(n) space
        Worst: O(nlog(n)) time | O(n) space 
    '''
    if start_idx >= end_idx:
        return
    else:
        mid_idx:int = (start_idx + end_idx) // 2
        merge_sort_opt(aux_array, array, start_idx, mid_idx)
        merge_sort_opt(aux_array, array, mid_idx+1, end_idx)

        do_merge(array, aux_array, start_idx, mid_idx, end_idx)

def do_merge(array:List[int], aux_array:List[int], left_limit:int, mid_idx:int, right_limit:int) -> None:
    array_ref: int = left_limit
    left_idx:int = left_limit
    right_idx:int = mid_idx + 1

    while left_idx <= mid_idx and right_idx <= right_limit:
        if aux_array[left_idx] >= aux_array[right_idx]:
            array[array_ref] = aux_array[right_idx]
            right_idx +=1
        else:
            array[array_ref] = aux_array[left_idx]
            left_idx += 1

        array_ref += 1

    while left_idx <= mid_idx:
        array[array_ref] = aux_array[left_idx]
        left_idx += 1
        array_ref += 1

    while right_idx <= right_limit:
        array[array_ref] = aux_array[right_idx]
        right_idx += 1
        array_ref += 1

    




if __name__ == "__main__":
    array: List[int] = [5,6,1,3,2,4,7]
    #print(merge_sort_sd(array))
    aux_array = array[:]
    merge_sort_opt(array, aux_array, 0, len(array)-1)
    print(array)