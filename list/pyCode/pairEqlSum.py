# -*- coding: utf-8 -*-
'''
Created on Thu Nov 11 19:49:05 2021

@author: Senkar
'''

#sum of pair of elements equal to given number

def method1(a,x):
    start=0
    end=1
    n=len(a)
    count=0
    while start<n-1:
        count+=1
        if a[start]+a[end]==x:
            print(f'pair is {a[start]} {a[end]} ')
        end+=1
        if end==n:
            start+=1
            end=start+1
    print(f'number of iterations are {count}')

#by using 2 pointer technique
def method2(a,x):
    n=len(a)
    start=0
    end=n-1
    count=0

    while start<end:
        count+=1
        sum=a[start]+a[end]
        if sum==x:
            print(f'pair is {a[start]} {a[end]}')
            break
        elif sum<x:
            start+=1
        else:
            end-=1
    print(f'number of iterations are {count}')

a=[10, 20, 35, 50, 75, 80]
x=155

method1(a,x)
method2(a,x)