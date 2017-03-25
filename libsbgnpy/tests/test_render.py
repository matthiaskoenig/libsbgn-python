"""
Tests the SBGN render functions.
"""
from __future__ import print_function, absolute_import
import pytest
import os
import tempfile

from libsbgnpy import utils
from libsbgnpy import render


@pytest.fixture
def f_adh():
    directory = os.path.dirname(os.path.realpath(__file__))
    f = os.path.join(directory, '../examples/sbgn/adh.sbgn')
    return f


def test_render_sbgn(f_adh):
    sbgn = utils.read_from_file(f_adh)
    tmp_file = tempfile.NamedTemporaryFile(suffix=".png")
    render.render_sbgn(sbgn, image_file=tmp_file.name, file_format="png")

