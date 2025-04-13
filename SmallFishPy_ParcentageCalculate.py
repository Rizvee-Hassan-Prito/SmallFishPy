# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 22:59:30 2025

@author: User
"""

def polygon_area(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    return 0.5 * abs(sum(x[i] * y[i+1] - x[i+1] * y[i] for i in range(-1, len(points)-1)))


ant = {
    "boxes": [
        {
            "points": [
                [...][...],
                [...][...],
                ...
            ]
        }
    ],
    "height": ...,
    "width": ...
}

image_area = ant["height"] * ant["width"]

polygon_pnts = ant["boxes"][0]["points"]

obj_area = polygon_area(polygon_pnts)

parcent = (obj_area / image_area) * 100

print(f"Object covers approximately {parcent:.2f}% of the image.")
