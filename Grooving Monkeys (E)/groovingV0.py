# -*- coding: utf-8 -*-
'''
Python 3.8.6
[MSC v.1916 64 bit (AMD64)]
28 / 11 / 2020
@author: z_tjona
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

from math import gcd

''' 

################################################### '''

def findPeriods(rute=[]):
    ''' how the monkeys in pos i change seats. 1 indexed
    ############################################### '''
    groups = [] # list of sets
    usedVals = set()
    for i in range(1, len(rute) + 1):
        if i in usedVals:
            continue
        
        # search loop
        nextPos = i
        loop = [nextPos, ]
        
        while True:
            nextPos = rute[nextPos - 1]
            if nextPos in loop:
                break
            
            loop.append(nextPos)
        
        usedVals.update(loop)
        groups.append(loop)
    
    resp = [len(x) for x in groups]
    return resp, groups


def lcm(a, b):
    ''' 
    
    ############################################### '''
    
    return a*b // gcd(a, b)



def main():
    ''' 
    
    ############################################### '''
    T = int(input())
    for _ in range(T):
        _ = input()
        vals = list(map(int, input().split()))
        vals, _ = findPeriods(vals)
        resp = 1
        for i in vals:
            resp = lcm(resp, i)
        print(resp)
    return 


if __name__ == "__main__":
    main()
