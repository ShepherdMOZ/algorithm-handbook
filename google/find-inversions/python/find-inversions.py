from typing import List, Tuple, Any

def find_inversions(array: List[int]) -> List[Tuple[int,int]]:
    return merge_sort(array, [])[1]
     
 
def merge_sort(array: List[int], inverted:List[Tuple[int,int]]) -> Tuple[List[int], List[Tuple[int,int]]]:

    if len(array) == 1:
        return array, []
    else:
        mid_point:int = len(array) // 2
        left: Any = merge_sort(array[0:mid_point], inverted)[0]
        right: Any = merge_sort(array[mid_point:], inverted)[0]
        merged: List[int] = [] 
        i:int = 0
        j:int = 0
        #print("Left is", left)
        #print("Right is", right)

        while i < len(left) and j < len(right) :
            if left[i] <= right[j]:
                ### Normal order
                merged.append(left[i])
                i += 1
            else:
                ### Inverted order
                for number in left[i:]:
                    inverted.append((number,right[j]))
                merged.append(right[j])
                j += 1
            
        ## Append remaining part
        merged += left[i:]
        merged += right[j:]

    return merged, inverted


if __name__ == "__main__":
   print(find_inversions([5,4,3,2,1]))


