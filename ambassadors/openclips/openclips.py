#
# VFX Clip reader/writer etc
#

class Clip(object):
    # constant properties as defined here:
    # http://docs.autodesk.com/flamepremium2015/index.html?url=files/
    #   GUID-B718793C-1227-44D7-ACB1-BBB7702E1CFC.htm,topicNumber=d30e161574
    __VERSION   = 3
    __TYPE      = "clip"

    # constructor
    def __init__(self):
        # private properties
        self._document  = None
        # self._filepath  = None # dont really need to keep track of this since we will use a xml-document.
        self._opened    = False
        self._stream    = None

        # public properties
        self.name       = ""

    # Opens and reads an existing clip. Also keeps it open for additional changes.
    # The user is responsible for closing
    def open(self, path):
        self.name = "TestClip"

    # Closes any existing (file)streams
    def close(self):
        pass


class Track(object):
    pass

class Feed(object):
    pass

class Version(object):
    pass

class Span(object):
    pass
