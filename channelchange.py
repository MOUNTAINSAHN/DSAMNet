# -*- coding:utf-8 -*-
"""
# @Author  :Shan Huang
# @Time    :2022/09/24 16:42 
# @File    :channelchange.py
"""
import cv2
import numpy as np
import os
from PIL import Image
image_dir="D:/ChageDetectData/train1/label"
image_list=[]
if os.path.isdir(image_dir):
    for filepath,dirpath,filenames in os.walk(image_dir):
        for filename in filenames:
            image_list.append(os.path.join(filepath,filename))
for image_path in image_list:
    im=np.array(Image.open(image_path)).astype(np.uint8)
    im[im == 1] = 255
    imc=Image.fromarray(im)
    imc.save(image_path)
    print(image_path.split("\\")[1],"complete")

