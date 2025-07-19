# Exploring h5 files


## Quick start

```bash
pip install h5manager
```

### Convert
```bash
h5manager convert example_img_dir/seefood/test/hot_dog \
               --output tmp/hotdog_64 --dim 64
```

```bash
h5manager convert example_img_dir/seefood/test/not_hot_dog \
               --output tmp/nothotdog_64 --dim 64
```

### Merge
```bash
h5manager merge --inputs tmp/hotdog_64.h5,tmp/nothotdog_64.h5 \
                --output tmp/merged
```

### Browse
```bash
h5manager visualize tmp/merged.h5
```


## Background
I started this project because I felt there were several things about h5 files I didn't understand.
- What are h5 files?
- Why can't we just use normal directories? What are the benefits of h5 over directories. 
- How to make a h5 from a directory?

I went into a rabbit hole of translating dirs<->h5s frequently, learning/forgetting information on each iteration. So I got frustrated, and created this repo to formalize the code/information.

Here are my answers to the above questions: 
- HDF5 is a machine-independent data format and software library for representing scientific data. The HDF5 software was developed at the National Center for Supercomputing Applications, by the Software Development Group, the same group that developed the Mosaic browser, at the University of Illinois at Champaign-Urbana. The HDF5 is also an open source file format. It supports large, complex, heterogeneous data. HDF5 uses a "file directory" like structure that allows you to organize data within the file in many different structured ways, as you might do with files on your computer. The HDF5 format also allows for embedding of metadata making it self-describing. 
- Normal directories take up more space, are ineffient for iteration, doesn't support parallel I/O, random Access, are non-heterogeneous (for eg: images in hot-dog-not-hot-dog project have different dimentions and hence data can't be directly fed to a neural network)
- One way to accomplish this is to read each image in dir, feed it to a preprocessing function for dimentional standardization, then parsed to a global numpy array which could then be used to create a h5 file


I tried to implement the above approach in the h5manager.


##Credits
- Here's an interesting article discussing the hdf5 in detail. I used it to read up on the theory: https://www.neonscience.org/about-hdf5
- TomaczGolan for the mergeh5.py file