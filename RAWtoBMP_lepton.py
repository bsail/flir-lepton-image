#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 15:50:31 2018

@author: dmitry
"""
data=(open('111.ir','rb').read())
image = []
for x in range (0,59):
    for y in range (0,79):
        high = data[x*164 + 4 + y*2]
        low = data[x*164 + 5 + y*2]
        image.append((high&(~(3<<14)))+low)
from PIL import Image
im=Image.new("RGB",(80,60),0)
k=0
for j in range (0,59):
    for i in range (0,79):
        im.putpixel((i,j),(image[k],image[k],image[k]))
        k+=1
im.show()
im.save("1.bmp")
