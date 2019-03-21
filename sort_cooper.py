# coding:utf-8


import random
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

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
    for j in tqdm(range(1,51)):
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
        # print a1,a2,a3,timesmerge,timesquick
    # x=np.arange()
    #
    # print 'test--'
