# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:19:37 2021

@author: User
"""

import os
import pyunpack
import zipfile
import fnmatch
import time
# import patoolib
# import tarfile

#patoolib.extract_archive("foo_bar.rar", outdir="path here")

"""
For zipping files
"""

"""
For unpacking .zip and .rar files:
"""

def unpack(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".rar"):
                print("RAR" + os.path.join(root,filename))
            elif filename.endswith(".zip"):
                print("ZIP" + os.path.join(root,filename))
            name = os.path.splitext(os.path.basename(filename))[0] # what is the purpose of this??
            if filename.endswith(".rar") or filename.endswith(".zip"):
                try:
                    arch = pyunpack.Archive(os.path.join(root,filename))
                    arch.extractall(directory=root)
                    print("Unzipping successful")
                    #time.sleep(2)
                    #print(os.path.join(root,filename))
                    #os.remove(os.path.join(root,filename)) # removes the zipped folder -> for this to work I need to open with .open and use close() 
                except Exception as e:
                    print("ERROR: BAD ARCHIVE "+os.path.join(root,filename))
                    print(e)
                    #os.remove(os.path.join(root,filename)) # removes the zipped folder
                    #print("Deleted folder that could not be unzipped")
                    
"""
Option 2 for zip files:
"""

def unzip(directory):
    pattern = '*.zip' 
    for root, dirs, files in os.walk(directory):
        for filename in fnmatch.filter(files,pattern):
            print(os.path.join(root,filename))
            zipfile.ZipFile(os.path.join(root,filename)).extractall(os.path.join(root,os.path.splitext(filename)[0]))
                    
"""
For re-zipping files:
"""

def retrieve_file_paths(directory):
    filepaths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath_single = os.path.join(root, filename)
            filepaths.append(filepath_single)
    return filepaths

def zippingfiles(directory):
    filepaths = retrieve_file_paths(directory)
    
    print("The following list of files will be zipped:")
    for filename in filepaths:
        print(filename)
    
    zip_file = zipfile.ZipFile(directory+'.zip', 'w')
    with zip_file:
        # zipping each file one by one
        for file in filepaths:
            newfile = zip_file.write(file)
            print(newfile)
            print(directory+'.zip file is created successfully!')  
            