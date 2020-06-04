#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 19:50:56 2017

@author: rdelapp
"""
def count_isograms(list_of_words):
    list_of_words = list_of_words.lower()
    return([len(set(x)) == len(x) for x in list_of_words].count(True))
    pass

