# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 22:45:46 2015

@author: Marcus Therkildsen
"""
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import hashlib

def md5(str_in):
    m = hashlib.md5()
    m.update(str_in)
    return m.digest()

def evalCrossTotal(strMD5):
    intTotal = 0
    arrMD5Chars = (strMD5).split()

    for j in arrMD5Chars:
        intTotal += '0x0'+j

    return intTotal

def encryptString(strString, strPassword):
    strPasswordMD5 = md5(strPassword)
    intMD5Total = evalCrossTotal(strPasswordMD5)
    arrEncryptedValues = np.array()
    intStrlen = len(strString)

    for i in xrange(intStrlen):

        arrEncryptedValues =  ord(strString[i]) + ('0x0' + str(strPasswordMD5)+ str(i%32)) - intMD5Total
        
        #intMD5Total = evalCrossTotal(substr(md5(substr($strString,0,$i+1)), 0, 16)
        #                       .  substr(md5($intMD5Total), 0, 16));

    return arrEncryptedValues#implode(' ' , $arrEncryptedValues);


if __name__ == '__main__':
    
    strString = '99Z-KH5-OEM-240-1.1'
    strPassword = '19'
    
    print encryptString(strString,strPassword)
    
    
    import re


#    <?php
#
#          //------------------------------------------------------------------------------------
#          function evalCrossTotal($strMD5)
#          {
#              $intTotal = 0;
#              $arrMD5Chars = str_split($strMD5, 1);
#              foreach ($arrMD5Chars as $value)
#              {
#                  $intTotal += '0x0'.$value;
#              }
#              return $intTotal;
#          }//-----------------------------------------------------------------------------------
#
#
#
#          //------------------------------------------------------------------------------------
#          function encryptString($strString, $strPassword)
#          {
#              // $strString is the content of the entire file with serials
#              $strPasswordMD5 = md5($strPassword);
#              $intMD5Total = evalCrossTotal($strPasswordMD5);
#              $arrEncryptedValues = array();
#              $intStrlen = strlen($strString);
#              for ($i=0; $i<$intStrlen; $i++)
#              {
#                  $arrEncryptedValues[] =  ord(substr($strString, $i, 1))
#                                           +  ('0x0' . substr($strPasswordMD5, $i%32, 1))
#                                           -  $intMD5Total;
#                  $intMD5Total = evalCrossTotal(substr(md5(substr($strString,0,$i+1)), 0, 16)
#                                           .  substr(md5($intMD5Total), 0, 16));
#              }
#              return implode(' ' , $arrEncryptedValues);
#          }//-----------------------------------------------------------------------------------
#
#        ?>

