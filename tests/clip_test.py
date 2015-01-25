from ambassadors.openclips import openclips

import unittest

class OCClipTest(unittest.TestCase):
    
    def test_read_clip(self):
        # Instanciate a Clip instance
        clip = openclips.Clip.from_file("../examples/simple.clip")

        self.assertEqual("NoVersionNoSetup", clip.name)
    # end test_read_clip
        
# end OCClipTest
