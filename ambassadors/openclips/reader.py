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
        """ Reads the dom tree and creates a Clip object"""
        dom = self._dom
        
        return openclips.Clip()
    #end to_clip
    
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