def get_pattern_construc(pattern):
    x_count = y_count = 0
    for value in pattern:
        if value == 'x':
            x_count += 1
        if value == 'y':
            y_count += 1
    return (x_count, y_count)

def count_word(string, start, b_slice):
    count = 0
    b_idx = 0
    i = start
    while i < len(string):
        if string[i] == b_slice[b_idx]:
            b_idx += 1
        else:
            b_idx = 0
            if b_slice[b_idx] == string[i]:
                b_idx += 1
        if b_idx == len(b_slice):
            count += 1
            b_idx = 0
        i += 1
    return count

def adjust_overlap(short_str, long_str, long_str_count):
    if len(short_str) < len(long_str) and short_str in long_str:
        return long_str_count
    else:
        return 0

def find_word_block(string, x_count, y_count, pattern):
    start = 0
    x_word = ''
    y_word = ''
    if y_count > 0:
        first_y = pattern.index('y')
    else:
        first_y = -1
    for end in range(start + 1, len(string) + 1 - start):
        b_slice = string[start:end]
        b_slice_count = count_word(string, start, b_slice)
        if first_y != -1:
            y_start = len(b_slice) * first_y
            if y_start < string.index(b_slice) + len(b_slice):
                continue
            y_len = (len(string) - len(b_slice) * x_count) // y_count
            if y_len <= 0:
                break
            y_slice = string[y_start: y_start + y_len]

            if count_word(string, y_start, y_slice) - adjust_overlap(y_slice, b_slice, x_count) == y_count and b_slice_count - adjust_overlap(b_slice, y_slice, y_count) == x_count:
                if len(b_slice) > len(x_word):
                    x_word = b_slice
                    y_word = y_slice
        elif b_slice_count == x_count and len(b_slice) > len(x_word):
            x_word = b_slice

    if x_word == '' and y_word == '':
        return []
    return [x_word, y_word]



def patternMatcher(pattern, string):
    # Write your code here.
    matched_word = []
    x_count, y_count = get_pattern_construc(pattern)
    matched_word = find_word_block(string, x_count, y_count, pattern)
    return matched_word


if __name__ == "__main__":
    print(patternMatcher('yy', 'abab'))
    print(patternMatcher('xyxxyx','yesnoyesyesnoyes'))
    print(patternMatcher('xyxy', 'abab'))
    print(patternMatcher('xyxxxyyx', 'yesnoyesyesyesnonoyes'))
    print(patternMatcher('xxyxxy', 'abababcabababc'))
    print(patternMatcher('xyxxxyyx', 'ababcababababcabcab'))