# -*- coding: utf-8 -*-
'''
Python 3.8.6
[MSC v.1916 64 bit (AMD64)]
17 / 11 / 2020
@author: z_tjona
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

from math import log10, floor
from collections import Counter

''' Solution to the problem Digit Pairs
################################################### '''


def calculateBitScore(number):
    ''' Returns the bit score calculated as follows:
    From the 3-digit number,
    1. extract largest digit and multiply by 11 then
    2. extract smallest digit multiply by 7 then
    3. add both the result for getting bit pairs.

    Note: - Bit score should be of 2-digits, if above results in a 3-digit bit score, simply ignore most significant digit.

    It converts the number to string to do the calculations.
    ############################################### '''
    num_str = str(number)
    minDigit = int(min(num_str))
    maxDigit = int(max(num_str))

    bitScore = minDigit*7 + maxDigit*11
    bitScore %= 100  # to "ignore" the most significant bit.
    return bitScore


def getMostSignificantDigit(x):
    ''' Returns the most significant digit of a number.

    Example:
        getMostSignificantDigit(529)
        5
    ############################################### '''

    return x // (10**floor(log10(x)))


def countPairs(vectorA, vectorB):
    ''' Given a vector find the pairs from the following conditions:
    1. Both bit scores should be in either odd position or even position to be eligible to form a pair.
    2. Pairs can be only made if most significant digit are same and at most two pair can be made for a given significant digit.
    ############################################### '''
    significants = [getMostSignificantDigit(x) for x in vectorA]
    significantsB = [getMostSignificantDigit(x) for x in vectorB]
    significants_counter = Counter(significants)
    significantsB_counter = Counter(significantsB)

    pairs = 0  # result

    # vector
    for digit, appearances in significants_counter.most_common():
        # if digit in significantsB_counter:
        #     if significantsB_counter[digit] > 1:
        #         continue

        if appearances >= 2:
            pairs += appearances - 1
        # elif appearances == 2:
        #     pairs += 1
        else:
            # no more pairs, as the loop is over descending sorted elements.
            break
    
    # other vector
    for digit, appearances in significantsB_counter.most_common():
        # if digit in significants_counter:
        #     if significants_counter[digit] > 1:
        #         continue
        if appearances >= 2:
            pairs += appearances - 1
        # elif appearances == 2:
        #     pairs += 1
        else:
            # no more pairs, as the loop is over descending sorted elements.
            break

    return pairs


def main():
    ''' Main of the ditig pair.
    ############################################### '''
    _ = input()
    numbers = map(int, input().split())

    scores = [calculateBitScore(x) for x in numbers]
    # separinting two lists depending on the numbers being in even or odd position
    numbers_odd_position = []
    numbers_even_position = []

    isOddPostion = True  # flag (to avoid calculting remainder)
    for ith_number in scores:
        if isOddPostion:
            numbers_odd_position.append(ith_number)
        else:
            numbers_even_position.append(ith_number)
        isOddPostion = not isOddPostion

    # finging paris
    result = countPairs(numbers_even_position, numbers_odd_position)
    print(result)
    return


if __name__ == "__main__":
    main()
