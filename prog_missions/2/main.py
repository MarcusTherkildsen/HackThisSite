# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 01:31:41 2015

@author: Marcus Therkildsen
"""
from __future__ import division
import numpy as np
from PIL import Image

'''
Morse decryption from
http://ken.friislarsen.net/blog/2007/09/19/
morse-code-decoding-with-python-list-comprehensions/
'''

letters = [('A', ".-"), ('B', "-..."), ('C', "-.-."), ('D', "-.."),
           ('E', "."), ('F', "..-."), ('G', "--."),  ('H', "...."),
           ('I', ".."), ('J', ".---"), ('K', "-.-"), ('L', ".-.."),
           ('M', "--"), ('N', "-."), ('O', "---"), ('P', ".--."),
           ('Q', "--.-"), ('R', ".-."),  ('S', "..."), ('T', "-"),
           ('U', "..-"),  ('V', "...-"), ('W', ".--"),  ('X', "-..-"),
           ('Y', "-.--"), ('Z', "--.."), ('0', "-----"), ('1', ".----"),
           ('2', "..---"), ('3', "...--"), ('4', "....-"), ('5', "....."),
           ('6', "-...."), ('7', "--..."), ('8', "---.."), ('9', "----.")]


def decode(input):
    if input == "":
        return [""]
    else:
        return [letter + remaining
                for letter, code in letters if input.startswith(code)
                for remaining in decode(input[len(code):])]

if __name__ == '__main__':

    img = np.array(Image.open('www.hackthissite.png'))

    n_col, n_row = img.shape

    # Flatten to a single string
    img_flat = np.reshape(img, n_col*n_row)

    # White pixels == 1
    wp_index = np.where(img_flat == 1)[0]

    # As stated at the website, the first character should remain the same
    # then the second should be wp_index[1]-wp_index[0]

    wp_dist = [wp_index[0]]
    for i in np.arange(len(wp_index)-1)+1:
        wp_dist.append(wp_index[i]-wp_index[i-1])

    # Convert into morse code
    morse_code = []
    for i in xrange(len(wp_dist)):
        morse_code.append(chr(wp_dist[i]))

    morse_final = ("".join(morse_code)).split(" ")

    # Now we solve the morse code
    morse_solved = []
    for i in xrange(len(morse_final)):
        morse_solved.append(min(decode(morse_final[i]), key=len))

    # Print the solved morse code
    print "".join(morse_solved)
