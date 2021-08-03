# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 15:19:57 2021

@author: User
"""

# Note 03.08.2021
# I unpacked everything that could be unpacked

from zipping import unpack
from inventory import collect_root, collect_sizes, bytesperfolder, directory_GB, totalfilecount
from filetypes import filetype_list, filetype_sum
from compression_tif import delete_channel2_tif, tif_zlibcompressed_path, tif_zlib_compression
from compression_avi import avicompression
from uncompressed import copy_remaining

#newdirectory = r'U:\Locomot_compressed\Jerry'
directory = r'U:\Locomot\Jerry'

# Test directories
#directory = r'Y:\Locomot\Jerry\j_physiology\ETL_Lick\animals\2012_09_01' 
#directory = r'Y:\AviFiles_TestBatch1'
#directory = r'U:\AlienwareCopy\Sample_directory'


#  Unpack zip and rar files
print("=====================================")
print("UNPACKING ZIP AND RAR FILES")
print("=====================================")
unpack(directory)

# Create dictionary that indicates storage space indicated by each subdirectory
print("=====================================")   
print("TAKING INVENTORY OF DIRECTORY")  
print("=====================================") 
rootlist = collect_root(directory)
sizelist = collect_sizes(directory)
folderbytes_dict = bytesperfolder(directory,rootlist,sizelist)

#print("The amount of storage space occupied by all subfolders of the current directory: ")
#print(folderbytes_dict)
#print("=====================================")

# Make lists for tif, txt, pdf, avi, mov, mp4, mat, png, jpg/jpeg
tiflist = filetype_list(directory,'.tif',5000,' tif files')
#tifflist = filetype_list(directory,'.tiff',5000,' tiff files')
txtlist = filetype_list(directory,'.txt',5000,' txt files')
pdflist = filetype_list(directory,'.pdf',5000,' pdf files')
avilist = filetype_list(directory,'.avi',5000,' avi files')
movlist = filetype_list(directory,'.mov',5000,' mov files')
mp4list = filetype_list(directory,'.mp4',5000,' mp4 files')
binlist = filetype_list(directory,'.bin',5000,' bin files')
matlist = filetype_list(directory,'.mat',5000,' mat files')
datlist = filetype_list(directory,'.dat',5000,' dat files')
nbflist = filetype_list(directory,'.nbf',5000,' nbf files')
pnglist = filetype_list(directory,'.png',5000,' png files')
jpglist = filetype_list(directory,'.jpg',5000,' jpg files')
jpeglist = filetype_list(directory,'.jpeg',5000,' jpeg files')

# Take inventory of which filetypes take up how much storage space
numberfiles = totalfilecount(directory)
totalsize_GB = directory_GB(directory)

tif_bytes = filetype_sum(tiflist)
avi_bytes = filetype_sum(avilist)
txt_bytes = filetype_sum(txtlist) # etc...
print("Overview of current directory: " + directory)
print("Number of files: " + str(numberfiles))
print("Total space occupied by directory: " + str(totalsize_GB) + " GB")
print("Number of bytes occupied by tif files: " + str(tif_bytes))
print("Number of bytes occupied by avi files: " + str(avi_bytes)) # etc...

# TIFF Compression
print("=====================================")
print("PERFORMING TIFF COMPRESSION")
print("=====================================")
print("Deleting channel 2 tif files")
tiflistnew = delete_channel2_tif(tiflist)
print("Done deleting channel 2 images")

print("Create new paths for compressed files")
compressionpaths_tif_zlib = tif_zlibcompressed_path(tiflistnew)

tif_zlib_compression(tiflistnew,compressionpaths_tif_zlib,compression_level=9)

# AVI COMPRESSION
print("=====================================")
print("PERFORMING AVI COMPRESSION")
print("=====================================")
returncodes = avicompression(avilist)

# If file is not tif or avi, copy and in its path just replace Locomot with Locomot_compressed
print("=====================================")
print("COPYING UNCOMPRESSED FILES INTO NEW DIRECTORY")
print("=====================================")
copy_remaining(directory,'.avi','.tif','.zip')