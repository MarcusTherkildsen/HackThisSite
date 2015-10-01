# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 01:14:58 2015

@author: Marcus Therkildsen
"""
from __future__ import division
import numpy as np
import random


if __name__ == '__main__':


    words2decrypt = np.genfromtxt('words2decrypt.txt', delimiter=',', dtype='str',autostrip = True)
    n_words2decrypt = len(words2decrypt)

    wordlist = np.genfromtxt('wordlist.txt', delimiter=',', dtype='str',autostrip = True)
    n_wordlist = len(wordlist)


    # Now go through each of the words in words2decrypt
    # randomize and check if in wordlist
    the_decrypted_words = []
    for item in words2decrypt:
        found = False
        while found == False:
            temp_perm = ''.join([str(w) for w in random.sample(item, len(item))])
            if temp_perm in wordlist:
                print temp_perm+','
                found = True

    # Copy the console output (except last ,)