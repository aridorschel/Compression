# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 19:16:06 2021

@author: User
"""

import os
import skimage
from skimage.external import tifffile

"""
for testing purposes:
tiflist = ['C:\\Users\\User\\Desktop\\movie.tif']
"""

# OPTIONAL: Deleting channel two images
def delete_channel2_tif(tiflist):
    tiflistnew = [x for x in tiflist if "channel2" not in x and "channel02" not in x 
               and "channel_2" not in x and "channel_02" not in x 
               and "channel__2" not in x and "channel__02" not in x]
    print("We have now deleted " + str(len(tiflist)-len(tiflistnew)) + " channel 2 tif images")
    return tiflistnew

# Creating paths for new tif file compressed with zlib
def tif_zlibcompressed_path(tiflist):
    compressionpaths_tif_zlib = []
    for i in range(len(tiflist)):
        
        # Change filename to indicate compression format
        x = list(os.path.split(tiflist[i]))
        filename_sep = os.path.splitext(x[-1])
        filename_zlib = filename_sep[0] + '_ZLIBcompressed' + filename_sep[-1]
        
        z = x.copy()
        z[-1] = filename_zlib

        compressionpath = os.path.join(*z)
        """
        CAREFUL: HARDCODED DIRECTORY NAME! 
        If you want to save your compressed file in a copy of your directory,
        simply replace with the root name.
        """
        compressionpath = compressionpath.replace("Locomot", "Locomot_compressed")
        #compressionpath = compressionpath.replace("Sample_directory", "Sample_directory_compressed")
        compressionpaths_tif_zlib.append(compressionpath)
    return compressionpaths_tif_zlib

"""
Performing zlib compression:
Values from 0 to 9 control the level of zlib compression.
If 0, data are written uncompressed (default). 

From my experience, 9 reduces file size to approximately half.
Problem: files with 2 colour channels are reduced into one

Regarding the compression algorithm (zlib), files compressed with the LZMA
compression don't open properly in ImageJ.
skimage.external.tifffile.imsave(compressionpath_lzma,tif_img,compress='lzma')

"""
# Performing zlib compression
def tif_zlib_compression(tiflist,compressionpaths,compression_level=9):
    for i in range(len(tiflist)):
        # Read file
        try:
            tif_img = tifffile.imread(tiflist[i])
            # Compress and save
            tifffile.imsave(compressionpaths[i],tif_img,compress=compression_level)
        except:
            print("Could not read or save tif file, corrupt input data")
        
        

        

