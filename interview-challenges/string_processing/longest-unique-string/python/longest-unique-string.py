def longestSubstringWithoutDuplication(string):
    # Write your code here.
    start_idx = 0
    end_idx = 1
    str_slice = []
    used_char = {}
    used_char[string[start_idx]] = start_idx
    while end_idx < len(string):
        if string[end_idx] not in used_char.keys():
            used_char[string[end_idx]] = end_idx
            end_idx += 1
        else:
            char = string[end_idx]
            str_slice.append(string[start_idx: used_char[char] + 1])
            start_idx = used_char[char] + 1
            used_char = {}
            used_char[string[start_idx]] = start_idx
            end_idx = start_idx + 1
    str_slice.append(string[start_idx:end_idx])
    max_string = ''
    for string in str_slice:
        if len(string) > len(max_string):
            max_string = string

    return max_string

if __name__ == "__main__":
    string = "clementisacap"
    longestSubstringWithoutDuplication(string)


