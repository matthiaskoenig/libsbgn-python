# -*- coding: utf-8 -*-
"""
Definition of Language, GlyphClass and ArcClass types.
Created manually from schema file.
"""
from __future__ import absolute_import, print_function
from enum import Enum, unique


@unique
class Language(Enum):
    """
    Enum representing the three languages of SBGN.
    """
    AF = "activity flow"
    ER = "entity relationship"
    PD = "process description"


@unique
class Orientation(Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"


@unique
class GlyphClass(Enum):
    """
    Enumeration with all possible values for the class attribute of Glyphs in SBGN-ML.
    This includes both top-level glyphs and sub-glyphs.
    """
    # glyphs
    UNSPECIFIED_ENTITY = "unspecified entity"
    SIMPLE_CHEMICAL = "simple chemical"
    MACROMOLECULE = "macromolecule"
    NUCLEIC_ACID_FEATURE = "nucleic acid feature"
    SIMPLE_CHEMICAL_MULTIMER = "simple chemical multimer"
    MACROMOLECULE_MULTIMER = "macromolecule multimer"
    NUCLEIC_ACID_FEATURE_MULTIMER = "nucleic acid feature multimer"
    COMPLEX = "complex"
    COMPLEX_MULTIMER = "complex multimer"
    SOURCE_AND_SINK = "source and sink"
    PERTURBATION = "perturbation"
    BIOLOGICAL_ACTIVITY = "biological activity"
    PERTURBING_AGENT = "perturbing agent"
    COMPARTMENT = "compartment"
    SUBMAP = "submap"
    TAG = "tag"
    TERMINAL = "terminal"
    PROCESS = "process"
    OMITTED_PROCESS = "omitted process"
    UNCERTAIN_PROCESS = "uncertain process"
    ASSOCIATION = "association"
    DISSOCIATION = "dissociation"
    PHENOTYPE = "phenotype"
    AND = "and"
    OR = "or"
    NOT = "not"
    STATE_VARIABLE = "state variable"
    UNIT_OF_INFORMATION = "unit of information"

    # @deprecated
    # By mistake, we used STOICHIOMETRY in instead of {@link CARDINALITY} in LibSBGN M1.
    # We keep this constant here to support reading old documents.
    # This constant will be removed in LibSBGN M3.
    STOICHIOMETRY = "stoichiometry"
    ENTITY = "entity"
    OUTCOME = "outcome"

    # @deprecated
    # Observable was used in old versions of SBGN, but has been replaced with {@link PHENOTYPE}.
    # However, because older versions of SBGN are supported by LibSBGN, this constant will never be removed.
    OBSERVABLE = "observable"
    INTERACTION = "interaction"
    ANNOTATION = "annotation"
    VARIABLE_VALUE = "variable value"
    IMPLICIT_XOR = "implicit xor"
    DELAY = "delay"
    EXISTENCE = "existence"
    LOCATION = "location"
    CARDINALITY = "cardinality"


@unique
class ArcClass(Enum):
    """
    Enumeration with all possible values for the class attribute of Arcs in SBGN-ML.
    """
    # arcs
    PRODUCTION = "production"
    CONSUMPTION = "consumption"
    CATALYSIS = "catalysis"
    MODULATION = "modulation"
    STIMULATION = "stimulation"
    INHIBITION = "inhibition"
    ASSIGNMENT = "assignment"
    INTERACTION = "interaction"
    ABSOLUTE_INHIBITION = "absolute inhibition"
    ABSOLUTE_STIMULATION = "absolute stimulation"
    POSITIVE_INFLUENCE = "positive influence"
    NEGATIVE_INFLUENCE = "negative influence"
    UNKNOWN_INFLUENCE = "unknown influence"
    EQUIVALENCE_ARC = "equivalence arc"
    NECESSARY_STIMULATION = "necessary stimulation"
    LOGIC_ARC = "logic arc"


'''
import libsbml
libsbml.SBase.setNotes()
libsbml.SBase.getNotesString()
libsbml.SBase.getAnnotation()
libsbml.SBase.getAnnotationString()
'''


class Information(object):
    """ Parent class for Extension and Notes.
    """
    name_ = None

    def __init__(self):
        """
        Parameter 'notes' is an XML string that is to be used as the content
        of the 'notes' subelement of this object. The <notes></notes> tag should
        not be part of the xml string.

        :param notes_str: 
        """
        self.xml_string = None

    def set_xml_string(self, xml_string):
        """ Set given xml string as information.
        
        :param notes_str: 
        :return: 
        """
        self.xml_string = xml_string

    def __str__(self):
        return self.xml_string


    def hasContent_(self):
        return self.xml_string is not None

    def export(self, outfile, level, namespace_='sbgn:', name_=None,
               namespacedef_='xmlns:sbgn="http://sbgn.org/libsbgn/0.2"', pretty_print=True):
        name_ = self.__class__.__name__.lower()
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        Information.showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        if self.hasContent_():
            outfile.write('>%s' % (eol_,))
            Information.showIndent(outfile, level, pretty_print)
            outfile.write('%s%s' % (self.xml_string, eol_))
            Information.showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    @staticmethod
    def showIndent(outfile, level, pretty_print=True):
        if pretty_print:
            for idx in range(level):
                outfile.write('    ')

    def build(self, node):
        print("Building Informations")
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self

    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('x', node)
        if value is not None and 'x' not in already_processed:
            already_processed.add('x')
            try:
                self.x = float(value)
            except ValueError as exp:
                raise ValueError('Bad float/double attribute (x): %s' % exp)
        value = find_attr_value_('y', node)
        if value is not None and 'y' not in already_processed:
            already_processed.add('y')
            try:
                self.y = float(value)
            except ValueError as exp:
                raise ValueError('Bad float/double attribute (y): %s' % exp)
        super(point, self).buildAttributes(node, attrs, already_processed)

    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(point, self).buildChildren(child_, node, nodeName_, True)
        pass




class Extension(Information):
    """
    Any well-formed XML content, and with each top-level element placed in a unique XML namespace; see text.
    Whereas Notes is a container for content to be shown directly to humans, Extension is a container for
    optional software-generated content not meant to be shown to humans. Every SBGN object can
    have its own Extension object instance. In XML, the Extension content type is any, allowing essentially
    arbitrary well-formed XML data content.

    """
    name_ = "extension"


class Notes(Information):
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
    name_ = 'notes'



# --------------------------------------------------------------------

# xml_node = XMLNode.convertStringToXMLNode(notes)
# if xml_node is None:
#    raise ValueError("XMLNode could not be generated for:\n{}".format(notes))

