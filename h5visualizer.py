#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 22:49:14 2020

@author: shivanshsuhane
"""

# modules we need

import numpy as np  
import matplotlib.pyplot as plt  
import h5py
import sys, getopt


def visualize(full_file_path):

    # Load h5py file
    example_dt = h5py.File(full_file_path,'r')
    
    # see what is inside that h5 file
    print(example_dt.keys())
    
    images = example_dt['images']
    print(images.shape)
    
    plt.subplots(3,4,figsize = (20,20))
    
    for i in range(12):
        img_np = images[i]
        plt.subplot(3,4,1+i)
        plt.imshow(img_np)
    plt.show()


def get_params():
    
    if len(sys.argv) > 2:
        print('You have specified too many arguments')
        sys.exit()

    if len(sys.argv) < 2:
        print('You need to specify the input dir path and output file path to be listed')
        sys.exit()
        
    h5FileName = sys.argv[1]
    
    fullPath = "/Users/shivanshsuhane/Desktop/code/ml_gitRepo/side_projects/hot-dog-not-hot-dog/Assignment/" + h5FileName
    
    print ('Full file path is: ', fullPath)
    return fullPath

    
if __name__ == "__main__":
   h5FileName = get_params()
   
   
   visualize(h5FileName)
   print ('Completed.')