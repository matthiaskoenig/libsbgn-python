# -*- coding: utf-8 -*-
"""
Helper functions for rendering SBGN.

Currently uses the webservice provided at "http://sysbioapps.dyndns.org/Layout/GenerateImage".
For documentation see
    http://sysbioapps.dyndns.org/Home/Services
"""

from __future__ import absolute_import, print_function
from libsbgnpy import utils
import requests
import tempfile


def render_sbgn(sbgn, image_file, file_format="png"):
    """ Render given sbgn object to image.
     
    Currently supports the following file_formats:
        - "png"
    The image file must end in .file_format, e.g. in '.png'
    
    Performs a request analogue to:
    curl -X POST -F file=@".\BorisEJB.xml" http://sysbioapps.dyndns.org/Layout/GenerateImage -o out.png
    
    :param sbgn: 
    :type sbgn: 
    :param out_file: 
    :type out_file: 
    :return: 
    :rtype: 
    """
    if file_format is not "png":
        raise ValueError("Only png rendering supported.")
    if not image_file.endswith('.{}'.format(file_format)):
        raise ValueError("The filename must end in <.file_format>, e.g. for png it must end in <.png>.")

    # Create temporary file
    f_in = tempfile.NamedTemporaryFile(suffix=".sbgn")
    utils.write_to_file(sbgn, f_in.name)

    # Call webservice for rendering
    files = [
        ('file', open(f_in.name, 'rb')),
    ]

    r = requests.post('http://sysbioapps.dyndns.org/Layout/GenerateImage', files=files)
    r.raise_for_status()

    with open(image_file, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
    print('SBGN rendered:', image_file)
