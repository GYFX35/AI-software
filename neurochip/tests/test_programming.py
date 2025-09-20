import unittest
from neurochip.microchip.programming import program_microchip

class TestProgramming(unittest.TestCase):

    def test_program_microchip(self):
        firmware = b"\x01\x02\x03"
        self.assertTrue(program_microchip("test_chip", firmware))

if __name__ == '__main__':
    unittest.main()
