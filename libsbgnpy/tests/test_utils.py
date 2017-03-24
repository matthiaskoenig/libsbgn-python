"""
Tests the SBGN utility functions.
"""
from __future__ import print_function, absolute_import
import pytest
import os
import tempfile

from libsbgnpy import libsbgnUtils as utils
from libsbgnpy.libsbgnTypes import Language


@pytest.fixture
def f_adh():
    directory = os.path.dirname(os.path.realpath(__file__))
    f = os.path.join(directory, '../examples/sbgn/adh.sbgn')
    return f


def test_read_from_file(f_adh):
    sbgn = utils.read_from_file(f_adh)
    assert sbgn is not None


def test_write_to_file(f_adh):
    sbgn = utils.read_from_file(f_adh)
    f_out = tempfile.NamedTemporaryFile(suffix='.sbgn')
    utils.write_to_file(sbgn, f_out.name)
    sbgn2 = utils.read_from_file(f_out)
    assert sbgn2 is not None


def test_get_version(f_adh):
    version = utils.get_version(f_adh)
    assert version == 2


def test_get_language(f_adh):
    language = utils.get_language(f_adh)
    assert language == Language.PD
