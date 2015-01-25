"""
OpenClip Objects and Components.
"""
import os

import reader

class Clip(object):
    # constant properties as defined here:
    # http://docs.autodesk.com/flamepremium2015/index.html?url=files/
    #   GUID-B718793C-1227-44D7-ACB1-BBB7702E1CFC.htm,topicNumber=d30e161574
    __VERSION = 3
    __TYPE = "clip"

    # constructor
    def __init__(self):
        # public properties
        self.name = ""
        
        self.currentVersion = 0

        self.versions = []
        self.tracks = []
    # end __init__

    @staticmethod
    def from_file(path):
        """
        Wrapper for the Reader.from_file method.
        """
        return reader.Reader.from_file(path)
        
    # end from_file
# end Clip


class Track(object):
    pass
# end Track


class Feed(object):
    pass
# end Feed


class Version(object):
    pass
# end Version


class Span(object):
    pass
# end Span
