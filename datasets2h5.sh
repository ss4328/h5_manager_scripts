#!/bin/sh

#1/4. Generate Training set -> hot dogs
python h5Converter.py /Users/shivanshsuhane/Desktop/code/ml_gitRepo/side_projects/hot-dog-not-hot-dog/Assignment/datasets/train/hot_dog train_hot_dogs
 
#2/4. Generate Training set -> NOT hot dogs
python h5Converter.py /Users/shivanshsuhane/Desktop/code/ml_gitRepo/side_projects/hot-dog-not-hot-dog/Assignment/datasets/train/not_hot_dog train_not_hot_dogs

#3/4. Generate Testing set -> hot dogs
python h5Converter.py /Users/shivanshsuhane/Desktop/code/ml_gitRepo/side_projects/hot-dog-not-hot-dog/Assignment/datasets/test/hot_dog test_hot_dogs

#4/4. Generate Testing set -> NOT hot dogs
python h5Converter.py /Users/shivanshsuhane/Desktop/code/ml_gitRepo/side_projects/hot-dog-not-hot-dog/Assignment/datasets/test/not_hot_dog test_not_hot_dogs

echo "All files translate. H4s generated @root dir location"