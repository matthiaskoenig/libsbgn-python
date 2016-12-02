"""
Tests the SBGN utility functions.
"""
from __future__ import print_function
import unittest
import os
from libsbgnpy import libsbgnUtils as utils
import tempfile
from libsbgnpy.libsbgnTypes import Language

dir = os.path.dirname(os.path.realpath(__file__))


class UtilTestCase(unittest.TestCase):
    """ Testing the utility functions. """

    def test_read_from_file(self):
        f = os.path.join(dir, '../examples/sbgn/adh.sbgn')
        sbgn = utils.read_from_file(f)
        self.assertTrue(sbgn is not None)

    def test_write_to_file(self):
        f = os.path.join(dir, '../examples/sbgn/adh.sbgn')
        sbgn = utils.read_from_file(f)
        f_out = tempfile.NamedTemporaryFile(suffix='.sbgn')
        utils.write_to_file(sbgn, f_out.name)
        sbgn2 = utils.read_from_file(f_out)
        self.assertTrue(sbgn2 is not None)

    def test_get_version(self):
        f = os.path.join(dir, '../examples/sbgn/adh.sbgn')
        version = utils.get_version(f)
        self.assertEqual(version, 2)

    def test_get_language(self):
        f = os.path.join(dir, '../examples/sbgn/adh.sbgn')
        language = utils.get_language(f)
        self.assertEqual(language, Language.PD)


if __name__ == '__main__':
    unittest.main()
