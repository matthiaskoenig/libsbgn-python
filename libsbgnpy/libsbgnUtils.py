# -*- coding: utf-8 -*-
"""
Some helper functions to work with SBGN.

@author: Matthias Koenig
Created on Tue Apr 21 14:50:30 2015
"""
# import libsbgnpy.libsbgn as libsbgn

from __future__ import print_function
import libsbgnpy.libsbgn as libsbgn


def read_from_file(f):
    ''' Read an sbgn file (without validating against the schema).'''
    sbgn = libsbgn.parse(f)
    return sbgn

def write_to_file(sbgn, f):
    ''' Write sbgn to a file. '''
    sbgn.write_file(f)    


def is_valid(f):
    '''
    Check if a given file validates against the given xsd. If validation fails,
    an error message is printed to System.err.
    '''
    result = False;
    '''
			# TODO ??? - how to handle the validation
			// create a JAXB context and unmarshaller like usual
			JAXBContext context = JAXBContext.newInstance("org.sbgn.bindings");
			Unmarshaller unmarshaller = context.createUnmarshaller();
		
			// parse the schema.
			// If you call validate many times, 
			// it would be more efficient to do this step once of course.
			Schema schema;
			SchemaFactory schemaFactory = SchemaFactory.newInstance( XMLConstants.W3C_XML_SCHEMA_NS_URI );
			schema = schemaFactory.newSchema(new StreamSource(getResource("/SBGN.xsd")));

			// add the schema to the unmarshaller
			unmarshaller.setSchema(schema);
			
			// read the file. If there are problems, an UnmarshalException will be thrown here
			unmarshaller.unmarshal (f);
    '''
    return result;
	

def print_bbox(b):
    ''' Print bounding box representation. '''
    print('x, y, w, h : ', b.get_x(), b.get_y(), b.get_w(), b.get_h())