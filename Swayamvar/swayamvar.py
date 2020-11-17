# -*- coding: utf-8 -*-
'''
Python 3.8.6
[MSC v.1916 64 bit (AMD64)]
17 / 11 / 2020
@author: z_tjona
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

from collections import Counter

''' Solving problem Swayamvar of TCS Code Vita practice

################################################### '''


def main():
    ''' 
    ############################################### '''

    N = int(input())

    # strings of r's (rum) or m's (mojito)
    brides_to_be = input()
    grooms_to_be = input()

    # how many grooms went for rum or mojito
    grooms_counter = Counter(grooms_to_be)

    result = N  # assumming everybody got married
    for ith_bride_choice in brides_to_be:

        if grooms_counter[ith_bride_choice] > 0:
            # There is still a groom who matches the bride

            # remove the groom from the counter
            grooms_counter.subtract(ith_bride_choice)

            # registering the new couple
            result -= 1
        else:
            break
    print(result)


if __name__ == "__main__":
    main()
