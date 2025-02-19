# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 18:18:05 2019

@author: amitabh.gunjan
"""

from PIL import Image
import numpy as np

w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[256, 256] = [255, 0, 0]
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()