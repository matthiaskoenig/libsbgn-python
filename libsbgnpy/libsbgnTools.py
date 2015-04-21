# -*- coding: utf-8 -*-
"""
Some helper functions to work with SBGN.

@author: Matthias Koenig
Created on Tue Apr 21 14:50:30 2015
"""
# import libsbgnpy.libsbgn as libsbgn

def print_bbox(b):
    print('x, y, w, h : ', b.get_x(), b.get_y(), b.get_w(), b.get_h())