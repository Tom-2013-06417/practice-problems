# abccbaabccba => abccba abccba
# a => a
# aa => a a
# aaa => a a a
# aaab => 0
# abab => ab ab
# abc => 0
# abcd
# m

def solution(s):
    for width in range(len(s)):
        window = s[0:width+1]
        splittedString = s.split(window)
        mappedPartitions = [partition == '' for partition in splittedString]
        count = len(mappedPartitions) - 1
        if (all(mappedPartitions)):
            return count if count > 1 else 0
    return 0
