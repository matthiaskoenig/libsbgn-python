# Generate python bindings


The python language bindings were created from the XML schema using
generateDS and than adapted to include GlyphClasses and ArcClasses.

The latest versions support py2 and py3 (>0.24a0)
```
sudo pip install generateDS
```

```
/usr/local/bin/generateDS.py -o "libsbgn.py" -s "libsbgnSubs.py" SBGN.xsd
```

Additional changes to the mapping after creation:

**Adding write function**
```{python}
class SBGNBase ->

def write_file(self, outfile):
    """ Write SBGN to file
    :param outfile:
    :type outfile:
    :return:
    """
    f = open(outfile, 'w')
    f.write('<?xml version="1.0" encoding="UTF-8"?>')
    self.export(f, level=0, namespace_='sbgn', name_='', namespacedef_='xmlns="http://sbgn.org/libsbgn/0.2"')    
    f.close()
```

**Adding type checks**
```{python}
class map ->

def get_language(self):
    """ Get the Language.
    :return: Language instance.
    """
    return Language(self.language)

def set_language(self, language):
    """ Sets the language and checks that within allowed values.
    :param language:
    :return:
    """
    if language and not isinstance(language, Language):
        raise TypeError('language must be of type Language')
    if language:
        self.language = _cast(None, language.value)
    else:
        self.language = _cast(None, language)


class glyph ->

def get_class(self):
    """ Returns the GlyphClass."""
    return GlyphClass(self.class_)
    
def set_class(self, class_):
    """ Sets the class and checks that in allowed GlyphClasses
    :param class_:
    :return:
    """
    if class_ and not isinstance(class_, GlyphClass):
        raise TypeError('class must be of type GlyphClass')
    if class_:
        self.class_ = _cast(None, class_.value)
    else:
        self.class_ = _cast(None, class_)
        
class arc ->

def get_class(self):
    """ Get the ArcClass. """
    return ArcClass(self.class_)

def set_class(self, class_):
    """ Set the ArcClass.
    :param class_:
    :return:
    """
    if class_ and not isinstance(class_, ArcClass):
        raise TypeError('class must be of type ArcClass')
    if class_:
        self.class_ = _cast(None, class_.value)
    else:
        self.class_ = _cast(None, class_)
        
class bbox ->
-> change order of arguments for backwards compatibility
    def __init__(self, x=None, y=None, w=None,  h=None, notes=None, extension=None):

class calloutType ->

    def set_target(self, target):
        if isinstance(target, glyph):
            self.target = target.get_id()
        else:
            self.target = target

```