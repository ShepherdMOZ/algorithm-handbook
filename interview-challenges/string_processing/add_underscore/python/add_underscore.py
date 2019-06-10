def backward_index(string, char):
    i = len(string) - 1
    while i >= 0:
        if string[i] == char:
            return i
        i -= 1
    return -1


def check_overlap(main_idx, string, substring):
    if string[main_idx] not in substring:
        return False
    offset_amount = backward_index(substring, string[main_idx])
    sub_idx = 0
    if main_idx - offset_amount < 0:
        return False
    while offset_amount > 0:
        if string[main_idx-offset_amount] != substring[sub_idx]:
            return False
        offset_amount -= 1
        sub_idx += 1
    return True

def resolve_overlap(main_idx, sub_idx, string, substring, pattern_match):
    offset_amount = backward_index(substring, string[main_idx])
    sub_idx = offset_amount
    j = main_idx
    while offset_amount > 0:
        pattern_match[j] = offset_amount
        j -= 1
        offset_amount -= 1

def underscorifySubstring(string, substring):
    # Write your code here.
    sub_idx = 0
    main_idx = 0
    pattern_match = [-1 for i in range(len(string))]
    while main_idx < len(string):
        if string[main_idx] == substring[sub_idx]:
            # if check_overlap(main_idx, string, substring):
            #     resolve_overlap(main_idx, sub_idx, string, substring, pattern_match)
            # else:
            pattern_match[main_idx] = sub_idx
            sub_idx += 1
        elif check_overlap(main_idx, string, substring):
            resolve_overlap(main_idx, sub_idx, string, substring, pattern_match)
        else:
            j = main_idx
            while pattern_match[j] != len(substring)-1 and j >= 0:
                pattern_match[j] = -1
                j -= 1
            sub_idx = 0
        if sub_idx == len(substring):
            sub_idx = 0
        main_idx += 1
    if sub_idx > 0:
        j = main_idx - 1
        sub_idx -= 1
        while sub_idx >= 0 and j >= 0:
            pattern_match[j] = -1
            j -= 1
            sub_idx -= 1

    comp_string = ''
    in_range = False
    for i in range(len(string)):
        if pattern_match[i] != -1:
            if not in_range:
                in_range = True
                comp_string += '_'
                comp_string += string[i]
                continue
        else:
            if in_range:
                in_range = False
                comp_string += '_'
                comp_string += string[i]
                continue

        comp_string += string[i]
    if in_range:
        comp_string += '_'
    print("Pattern", pattern_match)
    return comp_string

if __name__ == '__main__':
    # print(underscorifySubstring('aaaaaaaab', 'aaa'))
    # print(underscorifySubstring('aacaacaaab', 'aaca'))
    print(underscorifySubstring('ttesttest', 'ttest'))
    # print(underscorifySubstring('testthis is a testest to testestes it is work', 'test'))
    # print(underscorifySubstring('ttttttttttttttbtttttctatawtatttttastvb','ttt'))
