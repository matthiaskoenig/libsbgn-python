# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:25:49 2015

@author: mkoenig
"""
from enum import Enum

class Severity(Enum):
    WARNING = 1 
    ERROR = 2
        
class Issue(object):
    '''
    Describes one issue found during schematron validation.
    One validation run may produce multiple issues.
    '''
    def __init__(self, role, rule_id, diagnostic_id, message):
        self.message = message.strip();
        self.diagnostic_id = diagnostic_id;
        self.rule_id = rule_id;
        if role.lower() == "error":
            self.severity = Severity.ERROR
        else:
            self.severity = Severity.WARNING
	
    def get_severity(self):
        ''' Severity of the issue, i.e.: is it an error, or a warning? '''
        return self.severity
	
    def get_message(self):
        ''' Human readable description of the issue. '''
        return self.message

    def get_diagnostic_id(self):
        ''' Identifier of the element that this issue is about. '''
        return self.diagnostic_id
	
    def get_rule_id(self):
        ''' Identifier of the issue '''
        return self.rule_id
	
    def __str__(self):
        return "{} at diagnosticId={}; ruleId={} Message: {}".format(self.severity, 
                                    self.diagnostic_id, self.rule_id, self.message)
