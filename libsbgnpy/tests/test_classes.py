import unittest

import libsbgnpy.libsbgn as libsbgn
from libsbgnpy.libsbgnTypes import Language, GlyphClass, ArcClass, Orientation

class MyTestCase(unittest.TestCase):
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
