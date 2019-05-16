from typing import List

def quick_sort(array:List[int], start:int, end:int) -> None:
    '''
    Complexity:
        Best: O(nlog(n)) time | O(log(n)) space
        Avg: O(nlog(n)) time | O(log(n)) space
        Worst: O(n^2) time | O(log(n)) space 
     
    '''
    if start >= end:
        return
    else:
        pivot:int = array[start]
        left:int = start +1
        right:int = end
        while left <= right:
            if array[left] > pivot and array[right] < pivot:
                array[left], array[right] = array[right], array[left]
            if array[left] <= pivot:
                left += 1
            if array[right] >= pivot:
                right -= 1

        array[start] = array[right]
        array[right] = pivot
        quick_sort(array, start, right-1)
        quick_sort(array, right+1, end)


if __name__ == "__main__":
    array = [5,6,1,3,2,4,7]
    quick_sort(array,0,len(array)-1)
    print(array)