# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 23:31:20 2020

@author: shimurai

Gets one letter, and checks if this letter is a musical note.

(check-expect IsMusicNote(D) true)
(check-expect IsMusicNote(P) False)
"""

def IsMusicNote(c):
    if type(c) != str and len(c) != 1:
        return "Wrong format"
    else:
        if c in "CDEFGABcdefgab":
            return True
        else:
            return False
print(IsMusicNote("C"))
print(IsMusicNote("a"))
print(IsMusicNote("S"))
print(IsMusicNote("123"))