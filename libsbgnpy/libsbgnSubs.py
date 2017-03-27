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
from libsbgnpy.libsbgn import showIndent


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
    def __init__(self, anytypeobjs_=None):

        super(Notes, self).__init__(anytypeobjs_, )

    def hasContent_(self):
        return self.anytypeobjs_ is not None

    def export(self, outfile, level, namespace_='sbgn:', name_='notes',
               namespacedef_='xmlns:sbgn="http://sbgn.org/libsbgn/0.2"', pretty_print=True):

        print("CUSTOM NOTES EXPORT CALLED")
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
# end class notesTypeSub


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
