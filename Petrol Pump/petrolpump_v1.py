# -*- coding: utf-8 -*-
'''
Python 3.8.6
[MSC v.1916 64 bit (AMD64)]
27 / 11 / 2020
@author: z_tjona
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

from copy import deepcopy
from bisect import insort

''' Uses Complete Karmarkar_Karp algorithm.

################################################### '''


def cKK(nums=[]):
    ''' 
    
    ############################################### '''
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 0:
        return 0

    # else more than 1 element+
    # is assuemd the array is sorted
    # nums.sort()

    Bigger = nums.pop()
    secondBiger = nums.pop()

    lRight = deepcopy(nums)
    lRight.append(Bigger + secondBiger)

    lLeft = deepcopy(nums)
    insort(lLeft, Bigger - secondBiger)

    resp = min(cKK(lLeft), cKK(lRight))

    return resp


def main():
    ''' 
    
    ############################################### '''
    # a = [25,30,35,20,90,110,45,70,80,12,30,35,85]

    vals = list(map(int, input().split()))

    vals.sort()
    suma = sum(vals)

    dif = cKK(vals)

    resp = (suma - dif) // 2 + dif

    print(resp)
    return


if __name__ == "__main__":
    main()
