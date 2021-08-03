# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 19:14:12 2021

@author: User
"""

import subprocess
import os

"""
You might first want to copy the folder structure, rather than directly overwriting original files
Command prompt: xcopy source destination /t /e
source = path containing current folder hierarchy
destination = path that will store empty folder hierarchy

You can verify that the process went correctly e.g. by checking number of folders.
"""

"""
We are performing compression with constant rate factor, which from 
experience reduces the size by factors of ~ 400-1000
"""

def avicompression(avilist):
    resultcodes = []
    for i in range(len(avilist)):
        # path to original avi file
        original_path = avilist[i]
    
        # creating path for compressed file
        a = list(os.path.split(avilist[i]))
        filename_sep = os.path.splitext(a[-1])
        compressed_filename = filename_sep[0] + '_aviCRF20' + filename_sep[-1]
        a[-1] = compressed_filename
        compressed_path = os.path.join(*a)
        """
        !! CAREFUL: HARDCODED DIRECTORY NAME
        """
        compressed_path = compressed_path.replace("Locomot", "Locomot_compressed")
        #compressed_path = compressed_path.replace("Sample_directory", "Sample_directory_compressed")
        print(compressed_path)
         
        # ffmpeg installation path
        #appDir = r"C:\Program Files\ffmpeg\bin"
        appDir=r"C:\ffmpeg\bin" # (for alienware computer)
            
        #Change directory on the go
        os.chdir(appDir)

        result = subprocess.run("ffmpeg -i "+original_path+" -vcodec libx264 -crf 20 "+compressed_path)
        print(result)
        resultcodes.append(result)
    return resultcodes

"""
Note: Check the return code in the output. 0=successful, 1=unsuccessful
For more detailed info on the error run the compression command for that file directly in the commmand prompt
In rare cases ffmpeg might throw an error (returncode=1) because dims are not divisible by 2
To make width and height divisible by 2, an example command is:
ffmpeg -i avipath -vcodec libx264 -crf 20 -vf "crop=trunc(iw/2)*2:trunc(ih/2)*2" avinewpath
"""

"""
Section for other potentially useful functions
"""

# Replace all spaces with underscores, otherwise the inputs to the command line will fail
def underscore_replacing(directory):
    for path, folders, files in os.walk(directory):
        for f in files:
            os.rename(os.path.join(path, f), os.path.join(path, f.replace(' ', '_')))
        for i in range(len(folders)):
            new_name = folders[i].replace(' ', '_')
            os.rename(os.path.join(path, folders[i]), os.path.join(path, new_name))
            folders[i] = new_name

# Converting tif files to avi files is another way of saving storage space;
# When opened with Fiji/ImageJ, the .avi will be displayed again in frames.
def tif2avi(tif_path):
    
    # Change extension in the path
    avi_path = tif_path
    avi_path.replace('.tif', '.avi')
    
    # ffmpeg installation path
    appDir = r"C:\Program Files\ffmpeg\bin"
    #appDir=r"C:\ffmpeg\bin" # (for alienware computer)
    
    #Change directory on the go
    os.chdir(appDir)
            
    result = subprocess.run("ffmpeg -i "+tif_path + avi_path)
    print(result)


