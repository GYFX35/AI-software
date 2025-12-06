import unittest
from neurochip.microchip.cyber_security import analyze_security

class TestCyberSecurity(unittest.TestCase):

    def test_analyze_security_with_vulnerabilities(self):
        code = """
        void vulnerable_function() {
            char buffer[10];
            strcpy(buffer, "This is a very long string that will overflow the buffer");
            sprintf(buffer, "Value: %d", 1234567890);
            gets(buffer);
        }
        """
        report = analyze_security(code)
        self.assertIn("strcpy", report)
        self.assertIn("sprintf", report)
        self.assertIn("gets", report)

    def test_analyze_security_with_no_vulnerabilities(self):
        code = """
        void secure_function() {
            char buffer[50];
            strncpy(buffer, "This is a safe string", sizeof(buffer) - 1);
            snprintf(buffer, sizeof(buffer), "Value: %d", 123);
            fgets(buffer, sizeof(buffer), stdin);
        }
        """
        report = analyze_security(code)
        self.assertIn("No major security vulnerabilities found.", report)

    def test_analyze_security_with_delay(self):
        code = """
        void loop() {
            delay(1000);
        }
        """
        report = analyze_security(code)
        self.assertIn("delay", report)

if __name__ == '__main__':
    unittest.main()
