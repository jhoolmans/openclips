from ambassadors.openclips import reader, openclips

import unittest

class OCReaderTest(unittest.TestCase):
    
    def test_reader_exceptions(self):
        # Test to make sure a wrong path would raise an IOError
        self.assertRaises(IOError, reader.Reader.from_file, "../examples/no_file.clip")
    # end test_reader_exceptions
    
    def test_reader_returns_clip_when_exists(self):
        # Test return type of clip
        clip = reader.Reader.from_file("../examples/simple.clip")
        
        self.assertIsInstance(clip, openclips.Clip)
    # end test_reader_returns_clip
    
    def test_reader_returns_none_when_invalid(self):
        # Test return type of clip
        clip = reader.Reader.from_file("../examples/broken.clip")
        
        self.assertIsNone(clip, "Invalid clip file is None")
    # end test_reader_returns_none_when_invalid
    
# end OCReaderTest