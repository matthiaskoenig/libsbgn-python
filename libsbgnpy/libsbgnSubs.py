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

import sys
from lxml import etree as etree_

import ??? as supermod


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

#
# Data representation classes
#


class SBGNBaseSub(supermod.SBGNBase):
    def __init__(self, notes=None, extension=None, extensiontype_=None):
        super(SBGNBaseSub, self).__init__(notes, extension, extensiontype_, )
supermod.SBGNBase.subclass = SBGNBaseSub
# end class SBGNBaseSub


class pointSub(supermod.point):
    def __init__(self, notes=None, extension=None, x=None, y=None):
        super(pointSub, self).__init__(notes, extension, x, y, )
supermod.point.subclass = pointSub
# end class pointSub


class bboxSub(supermod.bbox):
    def __init__(self, notes=None, extension=None, w=None, h=None, x=None, y=None):
        super(bboxSub, self).__init__(notes, extension, w, h, x, y, )
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
    def __init__(self, notes=None, extension=None, id=None, x=None, y=None):
        super(portSub, self).__init__(notes, extension, id, x, y, )
supermod.port.subclass = portSub
# end class portSub


class glyphSub(supermod.glyph):
    def __init__(self, notes=None, extension=None, class_=None, orientation='horizontal', id=None, compartmentRef=None, compartmentOrder=None, label=None, state=None, clone=None, callout=None, entity=None, bbox=None, glyph_member=None, port=None):
        super(glyphSub, self).__init__(notes, extension, class_, orientation, id, compartmentRef, compartmentOrder, label, state, clone, callout, entity, bbox, glyph_member, port, )
supermod.glyph.subclass = glyphSub
# end class glyphSub


class arcgroupSub(supermod.arcgroup):
    def __init__(self, notes=None, extension=None, class_=None, glyph=None, arc=None):
        super(arcgroupSub, self).__init__(notes, extension, class_, glyph, arc, )
supermod.arcgroup.subclass = arcgroupSub
# end class arcgroupSub


class arcSub(supermod.arc):
    def __init__(self, notes=None, extension=None, class_=None, id=None, source=None, target=None, glyph=None, port=None, start=None, next=None, end=None):
        super(arcSub, self).__init__(notes, extension, class_, id, source, target, glyph, port, start, next, end, )
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
    def __init__(self, value=None, variable=None):
        super(stateTypeSub, self).__init__(value, variable, )
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
    def __init__(self, x=None, y=None):
        super(startTypeSub, self).__init__(x, y, )
supermod.startType.subclass = startTypeSub
# end class startTypeSub


class nextTypeSub(supermod.nextType):
    def __init__(self, x=None, y=None, point=None):
        super(nextTypeSub, self).__init__(x, y, point, )
supermod.nextType.subclass = nextTypeSub
# end class nextTypeSub


class endTypeSub(supermod.endType):
    def __init__(self, x=None, y=None, point=None):
        super(endTypeSub, self).__init__(x, y, point, )
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
