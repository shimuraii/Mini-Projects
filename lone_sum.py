# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 17:54:52 2020

@author: shimuraii
"""

'''
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

'''
def lone_sum(a, b, c):
  sum = 0
  l = [b, c]
  if a != b and a != c and b != c:
    return a + b + c
  if b == c and a != c and a != b:
    return a
  for i in l:
    if a == i:
      sum += 0
    else:
      sum += i
  return sum