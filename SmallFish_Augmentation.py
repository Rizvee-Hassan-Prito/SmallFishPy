# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 23:54:17 2025

@author: User
"""

import os
import random
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter



input_folder = 'input folder path....'
output_folder = 'output folder path...'


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def flip_horizontal(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)

def flip_vertical(image):
    return image.transpose(Image.FLIP_TOP_BOTTOM)

def rotate_90_clockwise(image):
    return image.rotate(-90, expand=False)

def rotate_90_counterclockwise(image):
    return image.rotate(90, expand=False)

def rotate_180(image):
    return image.rotate(180, expand=False)

def rotate(image, angle):
    return image.rotate(angle, expand=False)

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def apply_blur(image, radius):
    return image.filter(ImageFilter.GaussianBlur(radius))

def add_noise(image, noise_factor):

    np_image = np.array(image)

    noise_pixels = int(noise_factor * np_image.size)

    for _ in range(noise_pixels):
        x = random.randint(0, np_image.shape[0] - 1)
        y = random.randint(0, np_image.shape[1] - 1)
        np_image[x, y] = random.randint(0, 255)  # Random grayscale noise
    return Image.fromarray(np_image)


augmentations = [
    flip_vertical,
    flip_horizontal,
    rotate_90_clockwise,
    rotate_90_counterclockwise,
    rotate_180,
    lambda img: rotate(img, -25),
    lambda img: rotate(img, 25),
    lambda img: adjust_brightness(img, 0.7), 
    lambda img: adjust_brightness(img, 1.3),
    lambda img: apply_blur(img, 2.5),  
    lambda img: add_noise(img, 0.02)
]

for filename in os.listdir(input_folder):
    
    if filename.endswith(('.png', '.jpg', '.jpeg')):

        
        image_path = os.path.join(input_folder, filename)
        
        image = Image.open(image_path)
        
        image.save(os.path.join(output_folder, filename))
        

        aug_image = image.copy()


        x=1
        selected_augmentations = augmentations
        for aug in selected_augmentations:
            aug_pic = aug(aug_image)
            aug_pic.save(os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_{x}.JPG"))
            x+=1

