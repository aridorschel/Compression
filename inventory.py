# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 15:22:06 2021

@author: User
"""

import os 
from os.path import join, getsize
#from collections import Counter

"""
# Checks the byte size of each folder
def bytesperfolder(newlist,directory):
    for root, dirs, files in os.walk(directory):
        print(root, "consumes ", end="")
        print(sum([getsize(join(root, name)) for name in files]), end="")
        print(" bytes in", len(files), "non-directory files")
"""

# Collects the paths to each subfolder; we will then check how much storage space each of them occupies
def collect_root(directory):
    rootlist = []
    for root, dirs, files in os.walk(directory):
        rootlist.append(root)
    return rootlist

# Collects space occupied by files in each of the above paths in kilobytes
def collect_sizes(directory):
    sizelist = []
    for root, dirs, files in os.walk(directory):
        size = sum([getsize(join(root, name))/1000 for name in files]) # bytes to kB
        print(size)
        sizelist.append(round(size,3))
    return sizelist

# Combines the information stored in collect_root and collect_sizes in a dictionary
def bytesperfolder(directory,rootlist,sizelist):
    folderbytes_dict = {}
    for i in range(len(rootlist)):
        folderbytes_dict.update({rootlist[i]:sizelist[i]}) # size in kB
    return folderbytes_dict

# Calculates the total space occupied by all files in the directory we are cleaning up
def directory_GB(directory):
    from os.path import join, getsize
    sizelist = []
    for root, dirs, files in os.walk(directory):
        print(root, "consumes ", end="")
        print(sum([getsize(join(root, name)) for name in files]), end="")
        print(" bytes in", len(files), "non-directory files")
    
        sizevalue = (sum([getsize(join(root, name)) for name in files]))
        sizelist.append(sizevalue)
        
    totalsize_sum = sum(sizelist)/1000000000
    print("The sum of all the detectable data in our directory is " + str(totalsize_sum) + " GB")
    return totalsize_sum

# Calculates total number of files in the directory we are cleaning up
def totalfilecount(directory):
    file_count = sum(len(files) for _, _, files in os.walk(directory))
    print("The total number of files in " + directory + " is: " + str(file_count))
    return file_count
 
"""
# Additional functions that might be useful when doing inventory of your directory:

# Checking which element is most frequent in a list
def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

# Creating one long list where you collect the file's extensions
def extensions_list(directory):
    ext_list = []
    for dirpath, dirs, files in os.walk(directory):
        for filename in files:
            x = os.path.splitext(filename)
            ext_list.append(x[-1])
    return ext_list
    # then check most_frequent(ext_list)

# Manually excluding one data type and then checking for most frequent occurence:
def extensions_exclude(directory):
    new_ext_list = list(filter(lambda a: a != '.dat', extensions_list))
    return new_ext_list
    # then check most_frequent(new_ext_list)

# Excluding some files based on a specific substring from a typelist:
def remove_from_list(typelist,substring):
    res = len([i for i in typelist if substring in i])
    print ("Number of strings with given substring : " + str(res))
    
    unwanted_files = []
    for i in typelist:
        if substring in i:
            unwanted_files.append(i)
    for x in unwanted_files:
        typelist.pop(typelist.index(x))

"""
