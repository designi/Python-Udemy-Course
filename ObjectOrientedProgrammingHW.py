# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:03:09 2019
@author: ngarcia
Problem set:
https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/05-Object%20Oriented%20Programming/02-Object%20Oriented%20Programming%20Homework.ipynb
"""

#Problem 1
#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

import numpy as np
import pandas as pd


class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        
    def distance(self):
        x = (self.coor2[0]-self.coor1[0])**2
        y = (self.coor2[1]-self.coor1[1])**2
        return (x+y)**0.5

    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])


#Problem 2
class Cylinder:
    
    pi = np.pi #defined as a Class Object Attribute since PI won't be changing in the methods.
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
    
    def volume(self):
        return Cylinder.pi*self.height*self.radius**2
    
    def surface_area(self):
        return 2*Cylinder.pi*self.radius*(self.radius+self.height)
    
    
        