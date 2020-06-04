#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 16:55:12 2017

@author: rdelapp
"""
def remove_item(list_items, item_to_remove):
 ''' Remove *first* occurrence of item from list

 Parameters
 ----------_
 list_items: list
 item_to_remove: object
 The object to be removed form list_items

 Returns
 --------
 - if the item is in the list: list
 list with first occurrence of item removed
 - if the item is not in the list: str
 'The item is not in the list'

 Example
 --------
 >>>list_items = [1,3,7,8,0]
 >>>remove_item(list_items, 7)
 [1,3,8,0]
 '''
 
 if item_to_remove not in list_items:
     print('The item is not in the list')
     
 else: 
     remove_index = [i for i,x in enumerate(list_items) if x==item_to_remove]
         
 return([ y for x,y in enumerate(list_items) if x != remove_index[0]])
                             
 pass

#for n, i in enumerate(list_items):
#    if i == item_to_remove:
#        remove_index = n
#        return(remove_index)
#            break
        
