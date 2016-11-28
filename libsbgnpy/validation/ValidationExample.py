# -*- coding: utf-8 -*-
"""
This is an example that shows both low-level validation using XML Schema,
and high-level validation using schematron.
"""
# TODO: Implement validation against schema
#    find the python package for import org.sbgn.schematron.SchematronValidator

from __future__ import print_function


def lowLevelExample(f):
    """
    Low level validation using XML Schema.
    This will check if the XML is properly structured.
    """
    is_valid = libsbgnUtil.is_valid(f);
    if is_valid:
        print("Validation succeeded")
    else:
        print("Validation failed")


def highLevelExample(f):
    """
    High-level validation using schematron.
    This will check if the drawing rules of SBGN are fulfilled. 
    """

    # Export validation reports to file for debugging
    # TODO: how to handle the schematron ?
    SchematronValidator.setSvrlDump(true)

    # validation will result in a list of issues
    issues = SchematronValidator.validate(f)

    # print each issue individually.
    print ("There are " + issues.size() + " validation problems")
    for issue in issues:
        print (issue)

if __name__ == "__main__":
    print("LOW LEVEL VALIDATION")
    f = "./test-files/PD/adh.sbgn"
    lowLevelExample(f)

    print("HIGH LEVEL VALIDATION")
    f2 = "./test-files/PD/multimer2.sbgn"
    highLevelExample(f2)