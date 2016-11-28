"""
Test the example scripts in the examples folder.
"""
import unittest
import os
from libsbgnpy.examples.ReadExample import read_sbgn
from libsbgnpy.examples.WriteExample import write_sbgn
from libsbgnpy.examples.WriteExampleAnnotation import write_annotation_sbgn

dir = os.path.dirname(os.path.realpath(__file__))

class ExampleTestCase(unittest.TestCase):

    def test_read_example(self):
        f_in = 'sbgn/adh.sbgn'
        f = os.path.join(dir, '../examples/{}'.format(f_in))
        sbgn = read_sbgn(f)
        self.assertTrue(sbgn is not None)

    def test_write_example(self):
        f_out = "sbgn/test-output.sbgn"
        f = os.path.join(dir, '../examples/{}'.format(f_out))
        write_sbgn(f)

    def test_write_annotation_example(self):
        f_out = "sbgn/test-output-annotation.sbgn"
        f = os.path.join(dir, '../examples/{}'.format(f_out))
        write_annotation_sbgn(f)

    def test_write_read_example(self):
        f_out = "sbgn/test-output.sbgn"
        f = os.path.join(dir, '../examples/{}'.format(f_out))
        write_sbgn(f)
        sbgn = read_sbgn(f)
        self.assertTrue(sbgn is not None)


if __name__ == '__main__':
    unittest.main()
