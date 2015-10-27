# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 00:06:35 2015

@author: Marcus Therkildsen
"""
from __future__ import division
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

if __name__ == '__main__':

    # URL to the 11th prog mission
    url_data = 'https://www.hackthissite.org/missions/prog/11/'

    # Open in firefox
    driver = webdriver.Firefox()

    # Login
    log_pass_list = [('your_username', 'your_password')]

    # Load the page
    driver.get(url_data)

    # Username
    inputElement = driver.find_element_by_name('username')
    inputElement.send_keys(log_pass_list[0][0])

    # Password
    inputElement = driver.find_element_by_name('password')
    inputElement.send_keys(log_pass_list[0][1])

    # Enter
    inputElement.send_keys(Keys.ENTER)
    time.sleep(0.2)

    # Get the source code
    source = driver.page_source

    # Search for the generated string
    search_word = 'Generated String'
    start_loc = source.find(search_word)+len(search_word)+2

    dirty = source[start_loc:start_loc+100].split('<br')[0]

    # Find out which separator is used
    sep_used = dirty[2]

    # Clean it up
    clean = np.array(dirty.split(sep_used)[:-1]).astype(int)

    # Search for the shift statement
    search_word = 'Shift'
    start_loc = source.find(search_word)+len(search_word)+2
    num_shift = int(source[start_loc:start_loc+100].split('<br')[0])

    # Final array to decode
    gen_str = clean-num_shift

    # Decoding
    asci_str = []
    for i in xrange(len(gen_str)):
        asci_str.append(chr(gen_str[i]))

    to_submit = [str(asci_str)[1:-1].replace(",", "").replace("'", "")
                                    .replace(" ", "")]

    # Submit solution
    inputElement = driver.find_element_by_name('solution')
    inputElement.send_keys(to_submit)

    # Enter
    inputElement.send_keys(Keys.ENTER)
    time.sleep(0.2)

    # And that's it !
