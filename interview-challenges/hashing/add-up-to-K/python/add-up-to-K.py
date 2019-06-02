from typing import Set,List

def find_pairs(array:List[int], k:int) -> bool:
    
    # init an empty set to store the diff between k and array elements
    diff_set:Set = set()

    for number in array:
        if number in diff_set:
            return True
        diff_set.add(k-number)

    return False


if __name__ == "__main__":
    print(find_pairs([10, 15, 3, 7], 17))

