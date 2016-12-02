# -*- coding: utf-8 -*-
"""
This is an example that shows both low-level validation against the XSD Schema,
and high-level validation using schematron.

At this point only the XSD validation is implemented.
see [#7](https://github.com/matthiaskoenig/libsbgn-python/issues/7)
"""

from __future__ import print_function
import sys
import os
from lxml import isoschematron
from lxml import etree

from enum import Enum

dir = os.path.dirname(os.path.realpath(__file__))
XSD_SCHEMA = os.path.join(dir, '../schema/SBGN.xsd')

class Severity(Enum):
    WARNING = 1
    ERROR = 2


class Issue(object):
    """
    Describes one issue found during schematron validation.
    One validation run may produce multiple issues.
    """

    def __init__(self, role, rule_id, diagnostic_id, message):
        self.message = message.strip()
        self.diagnostic_id = diagnostic_id
        self.rule_id = rule_id
        if role.lower() == "error":
            self.severity = Severity.ERROR
        else:
            self.severity = Severity.WARNING

    def get_severity(self):
        """ Severity of the issue, i.e.: is it an error, or a warning? """
        return self.severity

    def get_message(self):
        """ Human readable description of the issue. """
        return self.message

    def get_diagnostic_id(self):
        """ Identifier of the element that this issue is about. """
        return self.diagnostic_id

    def get_rule_id(self):
        """ Identifier of the issue """
        return self.rule_id

    def __str__(self):
        return "{} at diagnosticId={}; ruleId={} Message: {}".format(self.severity,
                                                                     self.diagnostic_id, self.rule_id, self.message)


def validate_xsd(f):
    """ Validate SBGN file against XSD schema.

    :param f: file to validate
    :return: Returns None if valid, the error log otherwise.
    """
    xmlschema_doc = etree.parse(XSD_SCHEMA)
    xmlschema = etree.XMLSchema(xmlschema_doc)
    doc = etree.parse(f)
    is_valid = xmlschema.validate(doc)
    if not is_valid:
        log = xmlschema.error_log
        error = log.last_error
        sys.stderr.write(str(log) + '\n')
        return log

    return None


def validate_schematron(f):
    """ Validate SBGN file with schematron.

    In Java this does the XSL Transformations on the ruleset and the exported Pathway Object
    and then invokes the SAX parser through "parseSVRL" method on the transformation's result.

    :param f: SBGN file
    :return:
    """
    # Example adapted from http://lxml.de/validation.html#id2

    # get the language of the SBGN file
    lang = SbgnVersionFinder.getLanguage(inputFile);
    String
    schema = SbgnUtil.getResource("/sbgn_" + lang.name().toLowerCase() + ".sch");



    xdoc = etree.parse(f)
    # Parse schema for validation
    sct_doc = etree.parse('./rules/sbgn_af.sch')
    # sct_doc = etree.parse('./rules/sbgn_er.sch')
    # sct_doc = etree.parse('./rules/sbgn_pd.sch')
    # Validate against schema
    schematron = isoschematron.Schematron(sct_doc, store_schematron=True, store_xslt=True, store_report=True)
    if schematron.validate(xdoc):
        print("ok")
    else:
        print("ko")
    report = schematron.validation_report

    print(type(report))
    print(report)




if __name__ == "__main__":
    # f = "../examples/sbgn/adh.sbgn"
    f = "../examples/sbgn/glycolysis.sbgn"

    xsd_valid = validate_xsd(f) is None
    print('XSD valid ({}): {}'.format(f, xsd_valid))

    # sct_valid = validate_schematron(f)
    # print('Schematron valid ({}): {}'.format(f, xsd_valid))

