import random
import time

#naive search. scan the entire a list and ask if its equal to the target
#if yes, return the index
#if no, then return -1

def naive_search(l,target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    else:
        return -1
    
#binary search uses divide and conquer
# we will leverage the fact that our list is sorted

def binary_search(l,target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if low > high:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l,target,low, midpoint-1)
    else:
        return binary_search(l,target,midpoint +1,high)

if __name__ =='__main__':

    length = 10000
    #builed a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-4*length,4*length))
    
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ",(end -start), "second")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ",(end -start), "second")