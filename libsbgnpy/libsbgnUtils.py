# -*- coding: utf-8 -*-
"""
Some helper functions to work with SBGN.
"""

from __future__ import print_function
import libsbgnpy.libsbgn as libsbgn


def read_from_file(f):
    """ Read an sbgn file (without validating against the schema).

    :param f: file to read
    :return: parsed SBGN
    :rtype:
    """
    sbgn = libsbgn.parse(f)
    return sbgn


def write_to_file(sbgn, f):
    """ Write sbgn object to file.

    :param sbgn:
    :param f:
    :return:
    """
    sbgn.write_file(f)    


def print_bbox(b):
    """ Print bounding box representation.

    :param b:
    :type b:
    :return:
    :rtype:
    """
    print('x, y, w, h : ', b.get_x(), b.get_y(), b.get_w(), b.get_h())
