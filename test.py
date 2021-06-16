#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import glob
import shutil

# 生成标注文件
if __name__ == '__main__':
    dir_path = 'datasets/'
    dstpath = 'marked/'
    for frame in os.listdir(dir_path):
        sub_dir = os.path.join(dir_path, frame)
        ground_truth = glob.glob(os.path.join(sub_dir, '*.txt'))
        srcfile = ground_truth[0]
        fpath, fname = os.path.split(srcfile)
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        shutil.copy(srcfile, dstpath + frame + '.txt')  # 复制文件


