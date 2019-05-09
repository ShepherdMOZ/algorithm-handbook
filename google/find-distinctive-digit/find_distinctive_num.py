
def find_distinctive_number(array):
    once = 0
    twice = 0 
    for number in array:
        twice = twice | (once & number)
        once = once ^ number
        bit_mask = ~(twice & once)
        once &= bit_mask
        twice &= bit_mask

    return once

print(find_distinctive_number([6, 1, 3, 3, 3, 6, 6]))
print(find_distinctive_number([13, 19, 13, 13]))
print(find_distinctive_number([1,2,3,4,1,2,3,1,2,3]))