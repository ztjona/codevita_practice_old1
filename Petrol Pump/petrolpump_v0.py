# -*- coding: utf-8 -*-
'''
Python 3.8.6
[MSC v.1916 64 bit (AMD64)]
23 / 11 / 2020
@author: z_tjona
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

from collections import deque

''' Uses Karmarkar_Karp algorithm.

################################################### '''


def splitList(nums):
    ''' Returns two lists l1,l2 that minimizes mean(sum(l1), sum(l2)).
    It tries to balance the elements in both lists.
    ############################################### '''
    
    # the list is sorted and values are poped from the 
    nums.sort()
    avgVal = round(sum(nums)/2) # ideal target value, the rounding is because odd numbers

    # prealloc
    l1 = list()
    sum1 = 0
    l2 = list()
    sum2 = 0

    # I put the max value in l1
    n0 = nums.pop() 
    l1.append(n0)
    sum1 = n0

    while nums:
        n = nums.pop()

        # falla xq asume q los primeros números van en diferentes buckets
        if sum1 < sum2:
            # I can add n to l1 and be still below or in the target
            l1.append(n)
            sum1 += n
        else:
            # no, I have to add it to the second list
            l2.append(n)
            sum2 += n

        # falla xq asume q los primeros números van en el primer bucket
        # if n + sum1 <= avgVal:
        #     # I can add n to l1 and be still below or in the target
        #     l1.append(n)
        #     sum1 += n
        # else:
        #     # no, I have to add it to the second list
        #     l2.append(n)
        #     sum2 += n

            
    return l1, l2, sum1, sum2



def  Karmarkar_Karp(nums):
    ''' Retorna la diferencia mInima 
    ############################################### '''
    nums.sort()
    
    while True:
        if len(nums) > 1:
            n0 = nums.pop()
            n1 = nums.pop()

            nums.append(n0 - n1)
            nums.sort()
        
        elif len(nums) == 1:
            resp = nums[0]
            break
        else:
            resp = 0
            break
    

    return resp


def main():
    ''' 
    
    ############################################### '''
    vals = list(map(int, input().split()))
    
    # l1, l2, sum1, sum2 = splitList(vals)
    # print(max(sum1, sum2), end='')
    # print(max(sum1, sum2))#, end='')
    suma = sum(vals)

    dif = Karmarkar_Karp(vals)
    resp = (suma - dif) //2 + dif
    print(resp, end='')
    return 


if __name__ == "__main__":
    main()
