from ambassadors.openclips import openclips as am  # am stands for Ambassadors

import unittest

class AMClipTest(unittest.TestCase):
    def test_read_clip(self):
        # Instanciate a Clip instance
        clip = am.Clip()
        clip.open("../examples/simple.clip")

        self.assertEqual("TestClip", clip.name)

        clip.close()

        self.assertTrue(False)
    # end test_read_clip
# end AMClipTest
