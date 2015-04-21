# -*- coding: utf-8 -*-
"""
Some helper functions to work with SBGN.

@author: Matthias Koenig
Created on Tue Apr 21 14:50:30 2015
"""
# import libsbgnpy.libsbgn as libsbgn

from __future__ import print_function
import libsbgnpy.libsbgn as libsbgn


def read_from_file(f):
    ''' Read an sbgn file (without validating against the schema).'''
    sbgn = libsbgn.parse(f)
    return sbgn

def write_to_file(sbgn, f):
    ''' Write sbgn to a file. '''
    sbgn.write_file(f)    



	

def print_bbox(b):
    ''' Print bounding box representation. '''
    print('x, y, w, h : ', b.get_x(), b.get_y(), b.get_w(), b.get_h())
