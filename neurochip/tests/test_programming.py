import unittest
from unittest.mock import patch
from neurochip.microchip.programming import program_microchip

class TestProgramming(unittest.TestCase):

    def test_program_microchip(self):
        firmware = b"\x01\x02\x03"
        self.assertTrue(program_microchip("test_chip", firmware))

    @patch('neurochip.microchip.programming.analyze_security')
    def test_security_analysis_is_called(self, mock_analyze_security):
        firmware = b"vulnerable code with strcpy"
        program_microchip("test_chip", firmware)
        mock_analyze_security.assert_called_once_with(firmware.decode('utf-8', errors='ignore'))

if __name__ == '__main__':
    unittest.main()
