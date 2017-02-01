# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 15:12:34 2017

@author: nandankirnesh
"""
import os
import re


filenames=[] #list of all files in the directory
def recdirfn(dirname): #recursive directory traversal#
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isdir(path): #if it is a directory apply recursive function#
            recdirfn(path)
        else:
            if os.path.isfile(path): #if it is a file append it in the list#
                filenames.append(path)
    return filenames

cwd=os.getcwd()                
flnames=recdirfn(os.path.join(cwd,'test_files'))

#regular expression for checking indian mobile number and its variants# 
regex="(?:(?:\+|0{0,2})91(\s*[\\-]\s*)?|[0]?)?[789]\d{2}\s*\d{3}\s*\d{4}"
for file in flnames:
    if file.endswith(".txt"): #check whether it is a text file#
        with open(file) as f:
            lines=f.read()
            mobilenos=re.finditer(regex,lines) #returning list of numbers by checking regular expression#
            for telno in mobilenos:
                print ("{telno}".format(telno=telno.group()))
