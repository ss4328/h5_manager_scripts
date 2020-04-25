# Exploring h5 files

## About
I started this project because I felt there were several things about h5 files I didn't understand.
- What are h5 files?
- Why can't we just use normal directories? What are the benefits of h5 over directories. 
- How to make a h5 from a directory?

I went into a rabbit hole of translating dirs<->h5s frequently, learning/forgetting information on each iteration. So I got frustrated, and created this repo to formalize the code/information.

Here are my answers to the above questions: 
- HDF5 is a machine-independent data format and software library for representing scientific data. The HDF5 software was developed at the National Center for Supercomputing Applications, by the Software Development Group, the same group that developed the Mosaic browser, at the University of Illinois at Champaign-Urbana. The HDF5 is also an open source file format. It supports large, complex, heterogeneous data. HDF5 uses a "file directory" like structure that allows you to organize data within the file in many different structured ways, as you might do with files on your computer. The HDF5 format also allows for embedding of metadata making it self-describing. 
- Normal directories take up more space, are ineffient for iteration, doesn't support parallel I/O, random Access, are non-heterogeneous (for eg: images in hot-dog-not-hot-dog project have different dimentions and hence data can't be directly fed to a neural network)
- One way to accomplish this is to read each image in dir, feed it to a preprocessing function for dimentional standardization, then parsed to a global numpy array which could then be used to create a h5 file


I tried to implement the above ^approach in the h5Converter.py file. I also created a shell file to run h4Converter with ease.

## Code written
- h5converter.py : Converts dir of images to h5 format file
- dir2h5.sh: Shell script that automates h5converter.py for multiple runs
- h5cisualizer.py: Visualizes contents (images in this case) of h5 file

## MergeH5

Merge hdf5 files (requires the same datasets, with the same shapes,
in all input files):

```
usage: ./merge.py <options>

optional arguments:
  -h, --help            show this help message and exit

required arguments:
  --input [list of input files]
                        path to input hdf5 files to merge ('file1, file2,...'
                        will look for all files starts with file1 and file2
                        and ends with .hdf5)
  --output [path/to/filename]
                        path to output hdf5 file
```

## h5Visualizer
Visualize a h5 file with given name in dir.
- you have to change the path_to_file in the h5visualizer.py file first
:

```
usage: ./h5.py <options>

HDF5 MANIPULATOR (merge)

required arguments:
  --<FileName> [Just the filename + extension. Change the path to file in the source code itself]
```

## h5Converter
Convert a directory of images to a h5 file. The h5 will be created at default root.

```
usage: ./h5Converter.py <options>

HDF5 MANIPULATOR (merge)

required arguments:
  --<input_dir> [provide the input dir directly without dashes and quotes (i.e. no formal flag but a CLA here. Address it till the directory level of the directory you're trying to make to a h5 file]
  --<output_file_name> [provide the output file name directly without dashes and quotes (i.e. no formal flag but a CLA here. ]
```


##Credits
- Here's an interesting article discussing the hdf5 in detail. I used it to read up on the theory: https://www.neonscience.org/about-hdf5
- TomaczGolan for the mergeh5.py file