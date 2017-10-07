#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 23:17:39 2017

@author: viktorija
"""

import matplotlib.pyplot as plt
from skimage import io

e = io.imread('images/eyebrow-right.png')

from scipy import ndimage

#rotation angle in degree
rotated = ndimage.rotate(e, -45)
plt.figure()
plt.imshow(e)

#%%
import numpy as np
from cv2 import warpAffine, getRotationMatrix2D
import cv2.cv as cv
#image = io.imread('images/background.png')
image_l = io.imread('images/eyebrow-left.jpg')
image_l[:,:,0] -= 255
image_l[:,:,1] -= 231
image_l[:,:,2] -= 169
image_r = io.imread('images/eyebrow-right.jpg')
image_r[:,:,0] -= 255
image_r[:,:,1] -= 231
image_r[:,:,2] -= 169
eye_left = io.imread('images/eye-left.jpg')
eye_left[:,:,0] -= 255
eye_left[:,:,1] -= 231
eye_left[:,:,2] -= 169
eye_right = io.imread('images/eye-right.jpg')
eye_right[:,:,0] -= 255
eye_right[:,:,1] -= 231
eye_right[:,:,2] -= 169
mouth_sad = io.imread('images/mouth-sad.jpg')
mouth_sad[:,:,0] -= 255
mouth_sad[:,:,1] -= 231
mouth_sad[:,:,2] -= 169
(h, w) = image_l.shape[:2]
y = 200
#%%
from skvideo.io import vwriter
vid = vwriter("normal2sad.avi", image_l.shape[:2])
vid.open("normal2sad.avi")
#print cv2.VideoCapture.isOpened()
#%
for i in range(200):
    angle_r = -i/10
    angle_l = i/10
    center_left = (275,y)
    center_right = (340,y)
    # Perform the rotation
    M_l = getRotationMatrix2D(center_left, angle_l, 1)
    M_r = getRotationMatrix2D(center_right, angle_r, 1)
    rotated_left = warpAffine(image_l, M_l, (w, h))
    rotated_right = warpAffine(image_r, M_r, (w, h))
    image = rotated_left + rotated_right + eye_left + eye_right + mouth_sad
    image[:,:,0] += 255
    image[:,:,1] += 231
    image[:,:,2] += 169
    vid.write(image)
#    plt.imshow(image)
#vid.release()
    #    cv2.imwrite("images/eyebrow-left-%d.png" % i, rotated_left)
#    cv2.imwrite("images/eyebrow-right-%d.png" % i, rotated_right)
#    plt.figure()
#    plt.imshow(rotated)