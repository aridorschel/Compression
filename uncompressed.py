# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 11:30:37 2021

@author: User
"""
import shutil
import os

def copy_remaining(directory,extension_skip1='.avi',extension_skip2='.tif',extension_skip3='.zip'):
    for dirpath,dirs,files in os.walk(directory):
        for filename in files:
            fname = os.path.join(dirpath,filename)
            if fname.endswith(extension_skip1):
                print("Already compressed and copied " + extension_skip1 + " file")
            elif fname.endswith(extension_skip2):
                print("Already compressed and copied " + extension_skip2 + " file")
            elif fname.endswith(extension_skip3):
                print("Zip file that could not be unpacked; ignore")
                # Note: Once I change unpack, this should not happen as zip files that could not be unpacked are deleted and ideally the source zip of successfully unpacked files would also be deleted
            else:
                """
                CAREFUL: Hardcoded directory name!!!
                """
                newpath = fname.replace('Locomot','Locomot_compressed')
                #newpath = fname.replace('Sample_directory','Sample_directory_compressed')
                try:
                    shutil.copy(fname, newpath)
                    print("File copied successfully.")
                except shutil.SameFileError:
                    print("Source and destination represent the same file.")
                except PermissionError:
                    print("Permission denied.")
                except:
                    print("Error occured while copying file.")
