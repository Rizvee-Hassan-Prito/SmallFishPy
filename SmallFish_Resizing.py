# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 23:49:06 2025

@author: User
"""

import os
from PIL import Image


input_folder = 'input folder path....'
output_folder = 'output folder path...'

new_size = (240, 320)


os.makedirs(output_folder, exist_ok=True)


supported_formats = ('.jpg', '.jpeg')


for filename in os.listdir(input_folder):
    if filename.lower().endswith(supported_formats):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with Image.open(input_path) as img:
            resized_img = img.resize(new_size)
            resized_img.save(output_path)

        print(f"Resized and saved: {output_path}")
