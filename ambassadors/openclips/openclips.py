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
    def __init__(self, document):
        # private properties
        self._document = None
        
        # public properties
        self.name = ""
    # end __init__

    @staticmethod
    def from_file(path):
        #return reade
        pass
        
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
