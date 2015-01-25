from ambassadors.openclips import reader

import unittest

class OCReaderTest(unittest.TestCase):
    
    def test_reader_exceptions(self):
        # Test to make sure a wrong path would raise an IOError
        self.assertRaises(IOError, reader.Reader.from_file, "../examples/no_file.clip")
    # end test_reader_exceptions
    
# end OCReaderTest