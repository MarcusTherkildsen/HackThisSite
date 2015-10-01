# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 01:31:41 2015

@author: Marcus Therkildsen
"""
from __future__ import division
import numpy as np
from PIL import Image

# Morse decryption from http://ken.friislarsen.net/blog/2007/09/19/morse-code-decoding-with-python-list-comprehensions/

letters = [('A',".-"),   ('B',"-..."), ('C',"-.-."), ('D',"-.."), ('E',"."),
           ('F',"..-."), ('G',"--."),  ('H',"...."), ('I',".."),  ('J',".---"),
           ('K',"-.-"),  ('L',".-.."), ('M',"--"),   ('N',"-."),  ('O',"---"),
           ('P',".--."), ('Q',"--.-"), ('R',".-."),  ('S',"..."), ('T',"-"),
           ('U',"..-"),  ('V',"...-"), ('W',".--"),  ('X',"-..-"),('Y',"-.--"),
           ('Z',"--.."),('0', "-----"),('1', ".----"),('2', "..---"),('3',"...--"),
           ('4',"....-"),('5', "....."),('6', "-...."),('7',"--..."),('8', "---.."),('9', "----.")]

def decode(input):
    if input == "" :
        return [""]
    else:
        return [ letter + remaining
                 for letter, code in letters if input.startswith(code)
                 for remaining in decode(input[len(code):]) ]

if __name__ == '__main__':

    img = np.array(Image.open('2.png'))

    n_col, n_row = img.shape

    # white pixels = 1
    test = []
    for jn in xrange(n_col):
        test_temp = 100*jn+np.where(img[jn,:]==1)[0]
        [test.append(test_temp[i]) for i in xrange(len(test_temp))]

    test = np.diff(np.array(test))

    test_chr = np.array([chr(test[i]) for i in xrange(len(test))])


    proper = str(test_chr)[1:-1].replace("'","").replace("\n","   space  ").replace("   ",",").replace(" ","").split(',')

    print proper
    for i in xrange(len(proper)):

        temp_decode = decode(proper[i])

        if len(temp_decode)>0:
            print min(temp_decode,key=len)
        else:
            print ' '


