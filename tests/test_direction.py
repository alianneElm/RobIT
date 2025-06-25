import unittest
from models.direction import Direction

class TestDirection(unittest.TestCase):
    """
    Unit tests for the Direction enum in the RobIT project.

    These tests verify:
    - Correct behavior of directional turns (left and right)
    - Mapping from string letters to Direction enum instances
    - Handling of invalid direction letters
    - Conversion of Direction instances to string and letter representations

    This suite ensures the directional logic that guides RobIT's movement
    is robust and behaves as expected across all edge cases.
    """

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
    
