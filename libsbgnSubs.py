#!/usr/bin/env python

#
# Generated Mon Apr 20 18:58:07 2015 by generateDS.py version 2.15a.
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
#   generateDS
#

import sys
from lxml import etree as etree_

import libsbgn as supermod

def parsexml_(*args, **kwargs):
    if 'parser' not in kwargs:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class SBGNBaseSub(supermod.SBGNBase):
    def __init__(self, notes=None, extension=None, extensiontype_=None):
        super(SBGNBaseSub, self).__init__(notes, extension, extensiontype_, )
supermod.SBGNBase.subclass = SBGNBaseSub
# end class SBGNBaseSub


class pointSub(supermod.point):
    def __init__(self, notes=None, extension=None, y=None, x=None):
        super(pointSub, self).__init__(notes, extension, y, x, )
supermod.point.subclass = pointSub
# end class pointSub


class bboxSub(supermod.bbox):
    def __init__(self, notes=None, extension=None, y=None, h=None, w=None, x=None):
        super(bboxSub, self).__init__(notes, extension, y, h, w, x, )
supermod.bbox.subclass = bboxSub
# end class bboxSub


class labelSub(supermod.label):
    def __init__(self, notes=None, extension=None, text=None, bbox=None):
        super(labelSub, self).__init__(notes, extension, text, bbox, )
supermod.label.subclass = labelSub
# end class labelSub


class sbgnSub(supermod.sbgn):
    def __init__(self, notes=None, extension=None, map=None):
        super(sbgnSub, self).__init__(notes, extension, map, )
supermod.sbgn.subclass = sbgnSub
# end class sbgnSub


class mapSub(supermod.map):
    def __init__(self, notes=None, extension=None, language=None, bbox=None, glyph=None, arc=None, arcgroup=None):
        super(mapSub, self).__init__(notes, extension, language, bbox, glyph, arc, arcgroup, )
supermod.map.subclass = mapSub
# end class mapSub


class portSub(supermod.port):
    def __init__(self, notes=None, extension=None, y=None, x=None, id=None):
        super(portSub, self).__init__(notes, extension, y, x, id, )
supermod.port.subclass = portSub
# end class portSub


class glyphSub(supermod.glyph):
    def __init__(self, notes=None, extension=None, id=None, compartmentRef=None, class_=None, compartmentOrder=None, orientation='horizontal', label=None, state=None, clone=None, callout=None, entity=None, bbox=None, glyph_member=None, port=None):
        super(glyphSub, self).__init__(notes, extension, id, compartmentRef, class_, compartmentOrder, orientation, label, state, clone, callout, entity, bbox, glyph_member, port, )
supermod.glyph.subclass = glyphSub
# end class glyphSub


class arcgroupSub(supermod.arcgroup):
    def __init__(self, notes=None, extension=None, class_=None, glyph=None, arc=None):
        super(arcgroupSub, self).__init__(notes, extension, class_, glyph, arc, )
supermod.arcgroup.subclass = arcgroupSub
# end class arcgroupSub


class arcSub(supermod.arc):
    def __init__(self, notes=None, extension=None, source=None, target=None, class_=None, id=None, glyph=None, port=None, start=None, next=None, end=None):
        super(arcSub, self).__init__(notes, extension, source, target, class_, id, glyph, port, start, next, end, )
supermod.arc.subclass = arcSub
# end class arcSub


class notesTypeSub(supermod.notesType):
    def __init__(self, anytypeobjs_=None):
        super(notesTypeSub, self).__init__(anytypeobjs_, )
supermod.notesType.subclass = notesTypeSub
# end class notesTypeSub


class extensionTypeSub(supermod.extensionType):
    def __init__(self, anytypeobjs_=None):
        super(extensionTypeSub, self).__init__(anytypeobjs_, )
supermod.extensionType.subclass = extensionTypeSub
# end class extensionTypeSub


class stateTypeSub(supermod.stateType):
    def __init__(self, variable=None, value=None):
        super(stateTypeSub, self).__init__(variable, value, )
supermod.stateType.subclass = stateTypeSub
# end class stateTypeSub


class cloneTypeSub(supermod.cloneType):
    def __init__(self, label=None):
        super(cloneTypeSub, self).__init__(label, )
supermod.cloneType.subclass = cloneTypeSub
# end class cloneTypeSub


class calloutTypeSub(supermod.calloutType):
    def __init__(self, target=None, point=None):
        super(calloutTypeSub, self).__init__(target, point, )
supermod.calloutType.subclass = calloutTypeSub
# end class calloutTypeSub


class entityTypeSub(supermod.entityType):
    def __init__(self, name=None):
        super(entityTypeSub, self).__init__(name, )
supermod.entityType.subclass = entityTypeSub
# end class entityTypeSub


class startTypeSub(supermod.startType):
    def __init__(self, y=None, x=None):
        super(startTypeSub, self).__init__(y, x, )
supermod.startType.subclass = startTypeSub
# end class startTypeSub


class nextTypeSub(supermod.nextType):
    def __init__(self, y=None, x=None, point=None):
        super(nextTypeSub, self).__init__(y, x, point, )
supermod.nextType.subclass = nextTypeSub
# end class nextTypeSub


class endTypeSub(supermod.endType):
    def __init__(self, y=None, x=None, point=None):
        super(endTypeSub, self).__init__(y, x, point, )
supermod.endType.subclass = endTypeSub
# end class endTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    doc = parsexml_(inFilename)
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
    doc = parsexml_(inFilename)
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
    doc = parsexml_(StringIO(inString))
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
    doc = parsexml_(inFilename)
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
    #import pdb; pdb.set_trace()
    main()
