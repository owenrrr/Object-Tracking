# MOSSE Tracking Algorithm
![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)   
This is the **python** implementation of the - [Visual object tracking using adaptive correlation filters](https://ieeexplore.ieee.org/document/5539960/).

## Requirements
- python - 3.5.2
- opencv-python

## How to use the code
### Step 0
prepare directory "datasets" on the same level of demo.py
datasets includes several sub-directory, every sub-directory includes numbers of pictures and only a "groundtruth.txt" includes ground-truth paramters
```
groundtruth.txt

x1,y1,x2,y2,x3,y3,x4,y4

x1,y1-----------x2,y2
|					|
|					|
|					|
|					|
x4,y4-----------x3,y3
```
accepts rectangles or other for vertex graph
### Step 1
```bash
python demo.py 

```
### Step2
Use mouse to select the object which needs to be tracked and Press **Enter** to start tracking.

## Demo
![demo](https://github.com/owenrrr/Object-Tracking/tree/master/examples/fish.mp4)

## Reference:
[1] [Visual object tracking using adaptive correlation filters](https://ieeexplore.ieee.org/document/5539960/)
