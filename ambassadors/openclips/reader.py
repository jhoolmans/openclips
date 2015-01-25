import openclips

from xml.dom import minidom
from xml.parsers.expat import ExpatError
import os

class Reader(object):
    """
    Reader object that handles the parsing of .clip files.
    """
    # constructor
    def __init__(self, path):
        self._dom = self.read_dom(path)
        self._clip = self.to_clip()
    #end __init__
    
    def read_dom(self, filepath):
        """
        Returns a Document object based on file.
        """
        if not os.path.exists( os.path.abspath(filepath) ):
            raise IOError("file does not exist.")
        
        return minidom.parse(filepath)
    #end read_dom

    def clip(self):
        """
        Returns the clip object.
        """
        return self._clip
    # end clip
    
    def to_clip(self):
        """ 
        Reads the dom tree and creates a Clip object 
        """
        dom = self._dom
        
        clip = openclips.Clip()
        clip.versions = self.read_versions()
        
        return clip
    #end to_clip
    
    def read_versions(self):
        """
        Reads the versions from the DOM object.
        """
        root = self._dom.documentElement
        versionsEl = root.getElementsByTagName("versions")[0]
        
        versions = []
        # Loop through version elements
        for version in versionsEl.getElementsByTagName("version"):
            versions.append(openclips.Version())
        
        return versions
    
    #end read_versions
    
    @staticmethod
    def from_file(path):
        """
        Reads a .clip file and returns a clip object.
        """
        if not os.path.exists( os.path.abspath(path) ):
            raise IOError("file does not exist.")
        
        try:
            reader = Reader(path)
            return reader.clip()
        except ExpatError:
            return None
    #end from_file
#end Reader