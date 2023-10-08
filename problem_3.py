'''
([4, 3, 5, 7, 8], 12) => [0, 2]
([1, 2, 3, 4], 15) => [-1, -1]
'''

def solution(l, t):
    '''
    If sum of all numbers < t, immediately return default answer [-1,-1]

    I feel like you can cache/precompute ranges e.g.
    {'0-1': 10, '1-2': 11, '2-3': 2, etc}

    What should I cache from the moving window?
    Window moves from left to right and increases in size.
    So if it shifts, instead of summing all the time, I could just
    cache values from sublist 0 to n, and subtract from window when
    necessary

    Ofc, if window sum becomes > than t, reset the window then slide.

    The window starts off as 1 element, so if the current 1-element window is immediately t,
    answer should be the left and right indexes of the window being the same.

    Remember: endWindowIndex depends on startWindowIndex; always reset it
    (prolly dont want to assign it to the startWindowIndex variable but
    copy instead so references don't mess up)

    [4, 3, 5, 7, 8], t=12
    [4]             | {0-0: 4}
    [4, 3]          | {0-0: 4, 0-1: 7}
    [4, 3, 5]       | {0-0: 4, 0-1: 7, 0-2: 12}

    [4, 3, 5, 7, 8], t=20
    [4]             | {0-0: 4}
    [4, 3]          | {0-0: 4, 0-1: 7}
    [4, 3, 5]       | {0-0: 4, 0-1: 7, 0-2: 12}
    [4, 3, 5, 7]    | {0-0: 4, 0-1: 7, 0-2: 12, 0-3: 19}
    [4, 3, 5, 7, 8] | {0-0: 4, 0-1: 7, 0-2: 12, 0-3: 19, 0-4: 27}

    [3]             | {0-0: 4, 0-1: 7, 0-2: 12, 0-3: 19, 0-4: 27} | windowSum = 3 from l[1]
    [3, 5]          | {0-0: 4, 0-1: 7, 0-2: 12, 0-3: 19, 0-4: 27} | windowSum = 12 - 4 = 8  from cache[0-2] - cache[0-0]
    [3, 5, 7]       | {0-0: 4, 0-1: 7, 0-2: 12, 0-3: 19, 0-4: 27} | windowSum = 19 - 4 = 15 from cache[0-3] - cache[0-0]
    [3, 5, 7, 8]    | {0-0: 4, 0-1: 7, 0-2: 12, 0-3: 19, 0-4: 27} | windowSum = 27 - 4 = 23 from cache[0-4] - cache[0-0]

    [5]             | {0-0: 4, 0-1: 7, 0-2: 12, 0-3: 19, 0-4: 27} | windowSum = 5 from l[2]
    [5, 7]          | {0-0: 4, 0-1: 7, 0-2: 12, 0-3: 19, 0-4: 27} | windowSum = 19 - 7 = 12 from cache[0-3] - cache[0-1]
    [5, 7, 8]       | {0-0: 4, 0-1: 7, 0-2: 12, 0-3: 19, 0-4: 27} | windowSum = 27 - 7 = 20 from cache[0-4] - cache[0-1]
    '''

    cache = {}
    startWindowIndex = 0
    endWindowIndex = 0
    listSize = len(l)
    windowSum = 0

    answer = [-1, -1]

    # Some guard checks
    if sum(l) < t:
        return answer

    if listSize == 1 and l[startWindowIndex] != t:
        return answer

    # Preprocessing step: generate some caches:
    for i in range(listSize):
        key = '{}-{}'.format(0, i)
        cache[key] = sum(l[0:i + 1])

    # Worst case is the first contiguous window is the last element. While-loop should end there.
    while startWindowIndex < listSize:
        keyWindowMinuend = '{}-{}'.format(0, endWindowIndex)
        keyWindowSubtrahend = '{}-{}'.format(0, startWindowIndex - 1)

        if startWindowIndex > 0:
            windowSum = cache[keyWindowMinuend] - cache[keyWindowSubtrahend]
        else:
            windowSum = cache[keyWindowMinuend]

        # if window sum is immediately t, that's the answer
        if windowSum == t:
            answer = [startWindowIndex, endWindowIndex]
            break

        # if windowSum immediately exceeds t, reset the window then slide
        elif windowSum > t:
            startWindowIndex = startWindowIndex + 1
            endWindowIndex = startWindowIndex

        # if windowSum is small, keep on increasing the window size
        else:
            endWindowIndex = endWindowIndex + 1

    return answer
