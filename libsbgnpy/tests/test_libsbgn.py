"""
Example tests.
"""
import unittest
import libsbgnpy.libsbgn as libsbgn
from libsbgnpy.libsbgnTypes import Language, GlyphClass, ArcClass, Orientation


class TestLibSBGN(unittest.TestCase):

    def setUp(self):
        # create empty sbgn
        self.sbgn = libsbgn.sbgn()
        # create map, set language and set in sbgn
        sbgn_map = libsbgn.map()
        sbgn_map.set_language(Language.PD)
        self.sbgn.set_map(sbgn_map)

        # create a bounding box for map
        box = libsbgn.bbox(x=0, y=0, w=363, h=253)
        sbgn_map.set_bbox(box)

        # create some glyphs
        # class attribute is named 'class_' ! in glyphs and arcs

        # glyphs with labels
        g = libsbgn.glyph(class_=GlyphClass.SIMPLE_CHEMICAL, id='glyph1')
        g.set_label(libsbgn.label(text='Ethanol'))
        g.set_bbox(libsbgn.bbox(x=40, y=120, w=60, h=60))
        sbgn_map.add_glyph(g)

        # glyph with ports (process)
        g = libsbgn.glyph(class_=GlyphClass.PROCESS, id='pn1', 
                          orientation=Orientation.HORIZONTAL)
        g.set_bbox(libsbgn.bbox(x=148, y=168, w=24, h=24))
        g.add_port(libsbgn.port(x=136, y=180, id="pn1.1"))
        g.add_port(libsbgn.port(x=184, y=180, id="pn1.2"))
        sbgn_map.add_glyph(g)

        # arcs
        # create arcs and set the start and end points
        a = libsbgn.arc(class_=ArcClass.CONSUMPTION, source="glyph1", target="pn1.1", id="a01")
        a.set_start(libsbgn.startType(x=98, y=160))
        a.set_end(libsbgn.endType(x=136, y=180))
        sbgn_map.add_arc(a)
      
    def tearDown(self):
        self.sbgn = None
        
    def test_sbgn_exists(self):
        self.assertTrue(self.sbgn is not None, 'sbgn created')
        
    def test_map_exists(self):
        self.assertTrue(self.sbgn.get_map() is not None, 'map created')
        
    def test_map_language(self):
        sbgn_map = self.sbgn.get_map()
        self.assertEqual(sbgn_map.get_language(), Language.PD, 'language is process diagram')
        
    def test_map_box_exists(self):
        self.assertTrue(self.sbgn.get_map().get_bbox() is not None, 'bbox created')
    
    def test_map_box_x(self):
        bbox = self.sbgn.get_map().get_bbox()
        self.assertEqual(bbox.get_x(), 0, 'bbox.get_x()')
    
    def test_map_box_y(self):
        bbox = self.sbgn.get_map().get_bbox()
        self.assertEqual(bbox.get_y(), 0, 'bbox.get_y()')
    
    def test_map_box_w(self):
        bbox = self.sbgn.get_map().get_bbox()
        self.assertEqual(bbox.get_w(), 363, 'bbox.get_w()')
        
    def test_map_box_h(self):
        bbox = self.sbgn.get_map().get_bbox()
        self.assertEqual(bbox.get_h(), 253, 'bbox.get_h()')
            
    def test_glyph_exists(self):
        glyphs = self.sbgn.get_map().get_glyph()
        self.assertEqual(len(glyphs), 2, '2 glyphs were created')
        
    def test_glyph_ids(self):
        glyphs = self.sbgn.get_map().get_glyph()
        self.assertEqual(glyphs[0].get_id(), "glyph1", 'glyph id')
        self.assertEqual(glyphs[1].get_id(), "pn1", 'glyph id')
    
    def test_glyph_classes(self):
        glyphs = self.sbgn.get_map().get_glyph()
        print(glyphs[0].class_)
        self.assertEqual(glyphs[0].get_class(), GlyphClass.SIMPLE_CHEMICAL, 'glyph class')
        self.assertEqual(glyphs[1].get_class(), GlyphClass.PROCESS, 'glyph class')
    
    def test_glyph_labels(self):
        glyphs = self.sbgn.get_map().get_glyph()
        self.assertEqual(glyphs[0].get_label().get_text(), 'Ethanol', 'glyph text')
        
    def test_glyph_bboxes(self):
        glyphs = self.sbgn.get_map().get_glyph()
        bbox = glyphs[0].get_bbox()
        self.assertEqual(bbox.get_x(), 40, 'glyph bbox coordinates')
        self.assertEqual(bbox.get_y(), 120, 'glyph bbox coordinates')
        self.assertEqual(bbox.get_w(), 60, 'glyph bbox coordinates')
        self.assertEqual(bbox.get_h(), 60, 'glyph bbox coordinates')
        
        bbox = glyphs[1].get_bbox()
        self.assertEqual(bbox.get_x(), 148, 'glyph bbox coordinates')
        self.assertEqual(bbox.get_y(), 168, 'glyph bbox coordinates')
        self.assertEqual(bbox.get_w(), 24, 'glyph bbox coordinates')
        self.assertEqual(bbox.get_h(), 24, 'glyph bbox coordinates')
        
    def test_glyph_ports(self):
        g = self.sbgn.get_map().get_glyph()[1]
        glyphs = self.sbgn.get_map().get_glyph()
        ports = glyphs[1].get_port()
        self.assertEqual(ports[0].get_x(), 136, 'glyph port x')
        self.assertEqual(ports[0].get_y(), 180, 'glyph port y')
        self.assertEqual(ports[0].get_id(), 'pn1.1', 'glyph port id')
        
        self.assertEqual(ports[1].get_x(), 184, 'glyph port x')
        self.assertEqual(ports[1].get_y(), 180, 'glyph port y')
        self.assertEqual(ports[1].get_id(), 'pn1.2', 'glyph port id')
        
    def test_arc_exists(self):
        arcs = self.sbgn.get_map().get_arc()
        self.assertEqual(len(arcs), 1, '1 arc was created')
        
    def test_arc_start(self):
        start = self.sbgn.get_map().get_arc()[0].get_start()
        self.assertTrue(start is not None, 'start of arc exists')
        self.assertEqual(start.get_x(), 98, 'arc start x coordinate')
        self.assertEqual(start.get_y(), 160, 'arc start y coordinate')
        
    def test_arc_end(self):
        end = self.sbgn.get_map().get_arc()[0].get_end()
        self.assertTrue(end is not None, 'end of arc exists')
        self.assertEqual(end.get_x(), 136, 'arc start x coordinate')
        self.assertEqual(end.get_y(), 180, 'arc start y coordinate')

    def test_glyph_class(self):
        g1 = libsbgn.glyph(class_=GlyphClass.SIMPLE_CHEMICAL, id='glyph1')
        self.assertEqual(g1.get_id(), 'glyph1')
        self.assertEqual(g1.get_class(), GlyphClass.SIMPLE_CHEMICAL)

        g2 = libsbgn.glyph(id='glyph1')
        g2.set_class(GlyphClass.SIMPLE_CHEMICAL)
        self.assertEqual(g2.get_id(), 'glyph1')
        self.assertEqual(g2.get_class(), GlyphClass.SIMPLE_CHEMICAL)

if __name__ == '__main__':
    unittest.main()
