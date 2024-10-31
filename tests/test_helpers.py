import unittest
from pathlib import Path

from utils.helpers import get_image_metadata


class TestImageMetadata(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # Setup so tests run from anywhere succesfully
        cls.test_dir = Path(__file__).parent
        cls.jpeg_path = cls.test_dir / "data" / "cave.jpg"
        cls.png_path = cls.test_dir / "data" / "oxygen.png"
        cls.gif_path = cls.test_dir / "data" / "mozart.gif"

    def test_jpeg_metadata(self):
        metadata = get_image_metadata(self.jpeg_path)
        self.assertEqual(metadata['format'], 'JPEG')
        self.assertIn('size', metadata)
        self.assertIn('mode', metadata)
        # self.assertIn('exif', metadata)
        # self.assertIsInstance(metadata['exif'], dict)

    def test_png_metadata(self):
        metadata = get_image_metadata(self.png_path)
        self.assertEqual(metadata['format'], 'PNG')
        self.assertIn('size', metadata)
        self.assertIn('mode', metadata)
        self.assertIn('gamma', metadata)
        self.assertIn('icc_profile', metadata)
        self.assertIn('text', metadata)

    def test_gif_metadata(self):
        metadata = get_image_metadata(self.gif_path)
        self.assertEqual(metadata['format'], 'GIF')
        self.assertIn('size', metadata)
        self.assertIn('mode', metadata)
        self.assertIn('background', metadata)
        self.assertIn('loop', metadata)
        self.assertIn('duration', metadata)


if __name__ == "__main__":
    unittest.main()
