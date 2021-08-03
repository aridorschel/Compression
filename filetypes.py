# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:15:31 2021

@author: User
"""

import os 
from os.path import getsize

"""
Create filetype-specific lists; filter by extension and min. size
example parameters: tiflist = filetype_list(directory,'.tif',5000,' tif files')
Make lists e.g. for tif, txt, pdf, avi, mov, mp4, mat, png, jpg/jpeg
"""

def filetype_list(directory,extensiontype,minsize,typestr):
    typelist = []
    for dirpath, dirs, files in os.walk(directory):
        for filename in files:
            fname = os.path.join(dirpath,filename)
            if fname.endswith(extensiontype):
                if getsize(fname) > minsize: # getsize returns size in bytes
                    typelist.append(fname)
    print("There is " + str(len(typelist)) + typestr)
    return typelist
        
# Get total storage space occupied by each file type
def filetype_sum(files_list):
    files_size = 0
    for i in range(len(files_list)):
        files_size = files_size + getsize(files_list[i]) # maybe divide by 1000000000 to convert bytes to gigabytes
    return files_size 
   