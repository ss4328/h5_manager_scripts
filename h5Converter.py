#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 18:21:52 2020

Library to facilitate the conversion of a jpg dataset directory to return a h5 file
args[1]->dataset dir
args[2]->output filename

@author: shivanshsuhane
"""

import sys, getopt
import h5py
import numpy as np
import os
import imageio
from PIL import Image
import argparse

def convert_create_file(input_dir, filename, output_file):
    filepath = input_dir + '/' + filename
    fin = open(filepath, 'rb')
    binary_data = fin.read()
    new_filepath = output_file + '/' + filename[:-4] + '.hdf5'
    f = h5py.File(new_filepath)
    dt = h5py.special_dtype(vlen=np.dtype('uint8'))
    dset = f.create_dataset('binary_data', (100, ), dtype=dt)
    dset[0] = np.fromstring(binary_data, dtype='uint8')
    
def get_h5(input_dir, filename, output_file):
    filepath = input_dir + '/' + filename
    fin = open(filepath, 'rb')
    binary_data = fin.read()
    new_filepath = output_file + '/' + filename[:-4] + '.hdf5'
    f = h5py.File(new_filepath)
    dt = h5py.special_dtype(vlen=np.dtype('uint8'))
    dset = f.create_dataset('binary_data', (100, ), dtype=dt)
    dset[0] = np.fromstring(binary_data, dtype='uint8')
    
    
'''Returns a resized num_px * num_px matrix by load img from input dir
'''
def preprocess(image_path, num_px):
    print()
    print("Preprocessing Image: ", image_path)
    image = Image.open(image_path)
    print("Image Size: ",image.size)
    print()
    
    resized_image = image.resize((num_px,num_px))
    print("Image Size: ",resized_image.size)
    image_arr = np.array(resized_image)
    return image_arr

    
'''Converts a directory full of different shaped images to a standard h5 file of parameterized dimention
'''
def convert_dir(input_dir, output_file_name, dimention):
    arr = os.listdir(input_dir)
    result_arr = np.empty([len(arr), dimention, dimention, 3],dtype='int16');
    
    for i in range(0,len(arr)):
        f_path = input_dir + '/' +arr[i]
        im_array=preprocess(f_path, dimention)
        result_arr[i]= im_array
        
    
    #convert to h5 file
    h5f = h5py.File(output_file_name + ".h5", 'w')
    h5f.create_dataset('dataset_1', data=result_arr)
        
    
        
'''Sanity checker: Makes sure that input dir, and output filename has been provided
''' 
def get_params():
   input_dir = ''
   output_file = ''
   
   #handling argument error exceptions
   
   parser = argparse.ArgumentParser(description='')
   parser.add_argument('--input_dir', dest='input_dir', type=str,
                    help='Input directory containing .jpg images')
   parser.add_argument('--output_dir', dest='output_dir', type=str,
                    help='Output directory containing .h5 images')
   args = parser.parse_args()
   if args.input_dir is None:
        raise Exception('Please declare an INPUT directory. Script Syntax: h5Converter input_dir_name output_file_name')
   if  args.output_dir is None:
        raise Exception('Please declare an OUTPUT directory. Script Syntax: h5Converter input_dir_name output_file_name')
       
        
    
   print ('Input directory is "', input_dir)
   print ('Output file is "', output_file)
   
   return (args.input_dir, args.output_dir)


'''Sanity checker v2: Makes sure that input dir, and output filename has been provided. Works better among two, albeit behaves a little more nonchalantly
''' 
def get_params2():
    
    if len(sys.argv) > 3:
        print('You have specified too many arguments')
        sys.exit()

    if len(sys.argv) < 2:
        print('You need to specify the input dir path and output file path to be listed')
        sys.exit()
        
    input_dir = sys.argv[1]
    output_file = sys.argv[2]
    
    print ('Input directory is: ', input_dir)
    print ('Output file is: ', output_file)
   
    return input_dir, output_file
   
   
    
if __name__ == "__main__":
   input_dir, output_file = get_params2()
   
   
   convert_dir(input_dir, output_file, 300)
   print ('Conversion successful. Output: ', output_file)




