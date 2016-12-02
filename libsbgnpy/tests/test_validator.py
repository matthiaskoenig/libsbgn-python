from __future__ import print_function
import unittest


import os
from libsbgnpy.validation import validator

dir = os.path.dirname(os.path.realpath(__file__))


class ValidatorTestCase(unittest.TestCase):

    def test_validate_xsd_01(self):
        """ Test XSD validation. """

        f = os.path.join(dir, '../examples/sbgn/adh.sbgn')
        is_valid = validator.validate_xsd(f) is None
        self.assertTrue(is_valid)

    def test_validate_xsd_02(self):
        """ Test XSD validation. """

        f = os.path.join(dir, '../examples/sbgn/glycolysis.sbgn')
        is_valid = validator.validate_xsd(f) is None
        self.assertTrue(is_valid)

if __name__ == '__main__':
    unittest.main()
