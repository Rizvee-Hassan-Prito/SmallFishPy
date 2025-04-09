# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 23:52:02 2025

@author: User
"""

import os
from PIL import Image, ImageOps

input_folder = 'input folder path....'
output_folder = 'output folder path...'


target_size = (320, 320)


os.makedirs(output_folder, exist_ok=True)


supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

for filename in os.listdir(input_folder):
    if filename.lower().endswith(supported_formats):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with Image.open(input_path) as img:

            img = img.convert("RGB")

            original_width, original_height = img.size

            
            top_padding = (target_size[1] - original_height) // 2
            bottom_padding = target_size[1] - original_height - top_padding

            left_padding = (target_size[0] - original_width) // 2
            right_padding = target_size[0] - original_width - left_padding

           
            padded_img = ImageOps.expand(
                img, 
                border=(left_padding, top_padding, right_padding, bottom_padding), 
                fill=(0, 0, 0)
            )

            
            padded_img.save(output_path)

            print(f"Saved: {output_path}")
