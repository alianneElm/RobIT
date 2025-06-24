import unittest
from models.direction import Direction

class TestDirection(unittest.TestCase):

    def test_left_turns(self):
        self.assertEqual(Direction.N.left(), Direction.W)
        self.assertEqual(Direction.W.left(), Direction.S)
        self.assertEqual(Direction.S.left(), Direction.E)
        self.assertEqual(Direction.E.left(), Direction.N)

    def test_right_turns(self):
        self.assertEqual(Direction.N.right(), Direction.E)
        self.assertEqual(Direction.E.right(), Direction.S)
        self.assertEqual(Direction.S.right(), Direction.W)
        self.assertEqual(Direction.W.right(), Direction.N)

    def test_from_letter(self):
        self.assertEqual(Direction.from_letter("N"), Direction.N)
        self.assertEqual(Direction.from_letter("e"), Direction.E)

    def test_invalid_letter(self):
        with self.assertRaises(ValueError):
            Direction.from_letter("?")

    def test_to_letter(self):
        self.assertEqual(Direction.S.to_letter(), "S")

    def test_str_representation(self):
        self.assertEqual(str(Direction.N), "N")
    
