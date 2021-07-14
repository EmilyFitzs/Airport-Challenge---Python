from plane import Plane
import unittest


class TestPlane(unittest.TestCase):
    def test_new_plane(self):
        test_plane = Plane("test plane")
        self.assertIsInstance(test_plane, Plane)

    def test_take_off(self):
        test_plane = Plane("test plane")
        with self.assertRaises(Exception):
            test_plane.take_off()

    def test_land(self):
        test_plane = Plane("test plane")
        test_plane.flying = False
        with self.assertRaises(Exception):
            test_plane.land()
