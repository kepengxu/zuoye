# coding:utf-8


import random
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

random.seed(154)
import sys
sys.setrecursionlimit(10000000)
def get_list():
    L=[]
    number = int(input('please enter the num of number:  '))
 #   print number
    for i in xrange(number):
        tn=int(input(str(i+1)+'  :  '))
        L.append(tn)
 #   print 'origin array:  ',L
    return L



def bubble_sort(L):
    temp=0
    length=len(L)
    times=0
    for i in xrange(length):
        for j in xrange(i+1,length):
            times=times+1
            if L[i]>L[j]:
                temp=L[i]
                L[i]=L[j]
                L[j]=temp
 #   print 'after bubble sort :  ',L
    return times

def insert_sort(L):
    temp=0
    lenth=len(L)
    times=0
    for i in xrange(1,lenth):
        for j in xrange(0,i):
            times=times+1
            if L[i]<L[j]:
                temp=L[i]
                L[i]=L[j]
                L[j]=temp
#    print 'after insert sort array :  ',L
    return times

def check_sort(L):
    temp=0
    lenth=len(L)
    times=0

    for i in xrange(lenth):
        t=i
        for j in xrange(i+1,lenth):
            times=times+1
            if L[i]>L[j]:
                t=j
        temp=L[i]
        L[i]=L[t]
        L[t]=temp
#    print 'after check sort :  ',L
    return times

timesmerge=0
def merge(l,r):
    ll=len(l)
    lr=len(r)
    i,j=0,0
    global timesmerge
    result=[]
    while i<ll and j <lr:
        timesmerge=timesmerge+1
        if l[i]<r[j]:
            result.append(l[i])
            i=i+1
        else:
            result.append(r[j])
            j=j+1
    if i==ll:
        for t in r[j:]:
            result.append(t)
    if j==lr:
        for t in l[i:]:
            result.append(t)
    return result

def merge_sort(L):
    temp=0
    length=len(L)
    if length<=1:
        return L
    else:
        left=merge_sort(L[:length/2])
        right=merge_sort(L[length/2:])
        return merge(left,right)

timesquick=0
def quick_sort(array, left, right):
    global timesquick
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        timesquick=timesquick+1
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)
    return array

def quick(L):
    T=quick_sort(L,0,len(L)-1)
    #print 'quick sort : ',T

if __name__=='__main__':
    insert = []
    bubble = []
    check = []
    merges = []
    quicks = []
    global timesmerge,timesquick
    for j in tqdm(range(1,26)):
        timesquick=0
        timesmerge=0
    #L=get_list()
        L=[]
        for i in range(200*j):
            L.append(random.randint(0,100000))
        # print 'origin array :  ',L
        a1=insert_sort(L)
        a2=bubble_sort(L)
        a3=check_sort(L)
        re=merge_sort(L)
        # print 'after merge sort : ',re
        quick(L)

        insert.append(a1)
        bubble.append(a2)
        check.append(a3)
        merges.append(timesmerge)
        quicks.append(timesquick)
    print '\n'
    print insert
    print bubble
    print check
    print quicks
    print merges
# # result
# [19900, 79800, 179700, 319600, 499500, 719400, 979300, 1279200, 1619100, 1999000, 2418900, 2878800, 3378700, 3918600, 4498500, 5118400, 5778300, 6478200, 7218100, 7998000, 8817900, 9677800, 10577700, 11517600, 12497500, 13517400, 14577300, 15677200, 16817100, 17997000, 19216900, 20476800, 21776700, 23116600, 24496500, 25916400, 27376300, 28876200, 30416100, 31996000, 33615900, 35275800, 36975700, 38715600, 40495500, 42315400, 44175300, 46075200, 48015100, 49995000]
# [19900, 79800, 179700, 319600, 499500, 719400, 979300, 1279200, 1619100, 1999000, 2418900, 2878800, 3378700, 3918600, 4498500, 5118400, 5778300, 6478200, 7218100, 7998000, 8817900, 9677800, 10577700, 11517600, 12497500, 13517400, 14577300, 15677200, 16817100, 17997000, 19216900, 20476800, 21776700, 23116600, 24496500, 25916400, 27376300, 28876200, 30416100, 31996000, 33615900, 35275800, 36975700, 38715600, 40495500, 42315400, 44175300, 46075200, 48015100, 49995000]
# [19900, 79800, 179700, 319600, 499500, 719400, 979300, 1279200, 1619100, 1999000, 2418900, 2878800, 3378700, 3918600, 4498500, 5118400, 5778300, 6478200, 7218100, 7998000, 8817900, 9677800, 10577700, 11517600, 12497500, 13517400, 14577300, 15677200, 16817100, 17997000, 19216900, 20476800, 21776700, 23116600, 24496500, 25916400, 27376300, 28876200, 30416100, 31996000, 33615900, 35275800, 36975700, 38715600, 40495500, 42315400, 44175300, 46075200, 48015100, 49995000]
# [198, 399, 597, 797, 997, 1194, 1390, 1585, 1788, 1969, 2176, 2377, 2573, 2754, 2955, 3158, 3331, 3535, 3720, 3924, 4124, 4321, 4487, 4723, 4878, 5072, 5265, 5438, 5652, 5833, 6004, 6220, 6404, 6582, 6769, 6946, 7140, 7302, 7510, 7703, 7865, 8049, 8267, 8454, 8622, 8776, 8973, 9141, 9323, 9560]
# [733, 1664, 2660, 3729, 4933, 5923, 7051, 8261, 9512, 10877, 11954, 13053, 14282, 15515, 16857, 18137, 19418, 20848, 22236, 23772, 25051, 26124, 27390, 28524, 29886, 31193, 32467, 33880, 35253, 36773, 38287, 39539, 40886, 42287, 43772, 45379, 46798, 48350, 49941, 51611, 53447, 54404, 55524, 56768, 58049, 59488, 60658, 62024, 63447, 64875]

