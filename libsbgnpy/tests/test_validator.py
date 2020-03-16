import os
from libsbgnpy.validation import validator

directory = os.path.dirname(os.path.realpath(__file__))


def test_validate_xsd_01():
    """ Test XSD validation. """
    f = os.path.join(directory, '../examples/sbgn/adh.sbgn')
    is_valid = validator.validate_xsd(f) is None
    assert is_valid


def test_validate_xsd_02():
    """ Test XSD validation. """
    f = os.path.join(directory, '../examples/sbgn/glycolysis.sbgn')
    is_valid = validator.validate_xsd(f) is None
    assert is_valid
