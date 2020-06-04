#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 18:30:17 2017

@author: rdelapp
"""

def cipher(text, cipher_alphabet, option='encipher'):
 ''' Run text through a particular cipher alphabet

 Parameters
 -----------
 text: str
 Either the plain text to encipher, or the cipher text to decrypt
 cipher_alphabet: dict
 Dictionary specifying {'original_letter': 'cipher_letter'}
 option: str (default 'encipher')
 'encipher' (accept plain text and output cipher text)
 'decipher' (accept cipher text and output plain text)

 Returns
 --------
 cipher text by default,
 plain text if option is set to decipher

 >>> d = dict(zip('abcdefghijklmnopqrstuvwxyz',
 'phqgiumeaylnofdxjkrcvstzwb'))
 >>> cipher('defend the east wall of the castle',
 d)
 'giuifg cei iprc tpnn du cei qprcni'
 >>> cipher('giuifg cei iprc tpnn du cei qprcni',
 d,
 option='decopher')
 'defend the east wall of the castle'
 '''
 result = ""
 if option == "encripher":
     for c in text:
            if c in cipher_alphabet:
                result = result + cipher_alphabet[c]
            else:
                result = result + c
     print (result)
     print(''.join(cipher_alphabet.get(c, c) for c in text))
    
 else:
     inv_map = {v: k for k, v in cipher_alphabet.items()}
     for c in text:
            if c in inv_map:
                result = result + inv_map[c]
            else:
                result = result + c
     print (result)
     print(''.join(inv_map.get(c, c) for c in text))
    
# else:
#     print("Options are only 'encripher' or 'decipher'.)
 
 pass