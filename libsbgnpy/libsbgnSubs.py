#!/usr/bin/env python

#
# Generated Mon Nov 28 14:10:23 2016 by generateDS.py version 2.24a.
#
# Command line options:
#   ('-o', 'libsbgn.py')
#   ('-s', 'libsbgnSubs.py')
#
# Command line arguments:
#   SBGN.xsd
#
# Command line:
#   /usr/local/bin/generateDS.py -o "libsbgn.py" -s "libsbgnSubs.py" SBGN.xsd
#
# Current working directory (os.getcwd()):
#   schema
#
from __future__ import print_function, absolute_import

import sys
from lxml import etree as etree_

import libsbgnpy.libsbgn as supermod
from libsbgnpy.libsbgn import showIndent, Tag_pattern_


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'


class Notes(supermod.notesType):
    """ 
    The optional SBGN element named 'notes', present on every major SBGN
    component type, is intended as a place for storing optional
    information intended to be seen by humans.  An example use of the
    'notes' element would be to contain formatted user comments about the
    model element in which the 'notes' element is enclosed.  Every object
    derived directly or indirectly from type SBase can have a separate
    value for 'notes', allowing users considerable freedom when adding
    comments to their models.

    The format of 'notes' elements must be XHTML 1.0 (http://www.w3.org/1999/xhtml). 
    """
    def __init__(self, anytypeobjs_=None):
        super(Notes, self).__init__(anytypeobjs_, )

    def __str__(self):
        if len(self.anytypeobjs_) > 0:
            return self.anytypeobjs_[0]
        else:
            return None

    def hasContent_(self):
        return self.anytypeobjs_ is not None

    def export(self, outfile, level, namespace_='sbgn:', name_=None,
               namespacedef_='xmlns:sbgn="http://sbgn.org/libsbgn/0.2"', pretty_print=True):
        """ Custom export function. 
        
        Necessary to provide handling for the xsd:any. 
        """
        name_ = self.__class__.__name__.lower()
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''

        if self.hasContent_():
            # notes defined as sequence, so handle the normal case of just having string
            notes_items = self.anytypeobjs_
            if type(self.anytypeobjs_) not in [list, tuple]:
                notes_items = [notes_items]
            showIndent(outfile, level, pretty_print)
            outfile.write('<%s%s%s>%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', eol_))
            for obj_ in notes_items:
                showIndent(outfile, level, pretty_print)
                outfile.write('%s%s' % (obj_, eol_))
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s%s>%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', eol_))

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        """ Custom build function.
        
        Necessary to provide handling for the xsd:any.
        """
        # This is the lxml.etree._Element, in first version going via strings
        obj_ = etree_.tostring(child_, pretty_print=False)
        # print('obj_', obj_)
        if obj_ is not None:
            self.add_anytypeobjs_(obj_)

supermod.notesType.subclass = Notes
# end class Notes


class Extension(supermod.extensionType):
    """ SBGN Extension.
    
    Any well-formed XML content, and with each top-level element placed in a unique XML namespace; see text.
    Whereas Notes is a container for content to be shown directly to humans, Extension is a container for
    optional software-generated content not meant to be shown to humans. Every SBGN object can
    have its own Extension object instance. In XML, the Extension content type is any, allowing essentially
    arbitrary well-formed XML data content.

    """
    def __init__(self, anytypeobjs_=None):
        super(Extension, self).__init__(anytypeobjs_, )

    def __str__(self):
        return str(self.anytypeobjs_)

    def hasContent_(self):
        return self.anytypeobjs_ is not None

    def export(self, outfile, level, namespace_='sbgn:', name_=None,
               namespacedef_='xmlns:sbgn="http://sbgn.org/libsbgn/0.2"', pretty_print=True):

        name_ = self.__class__.__name__.lower()
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''

        if self.hasContent_():
            # notes defined as sequence, so handle the normal case of just having string
            notes_items = self.anytypeobjs_
            if type(self.anytypeobjs_) not in [list, tuple]:
                notes_items = [notes_items]
            showIndent(outfile, level, pretty_print)
            outfile.write('<%s%s%s>%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', eol_))
            for obj_ in notes_items:
                showIndent(outfile, level, pretty_print)
                outfile.write('%s%s' % (obj_, eol_))
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s%s>%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', eol_))

supermod.notesType.subclass = Notes
# end class Notes



def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'SBGNBase'
        rootClass = supermod.SBGNBase
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:sbgn="http://sbgn.org/libsbgn/0.2"',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'SBGNBase'
        rootClass = supermod.SBGNBase
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'SBGNBase'
        rootClass = supermod.SBGNBase
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:sbgn="http://sbgn.org/libsbgn/0.2"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'SBGNBase'
        rootClass = supermod.SBGNBase
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    # import pdb; pdb.set_trace()
    main()
