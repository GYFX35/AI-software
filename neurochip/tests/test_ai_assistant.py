import unittest
from neurochip.microchip.ai_assistant import generate_microchip_code

class TestAIAssistant(unittest.TestCase):

    def test_generate_led_blink_code(self):
        prompt = "Blink an LED"
        code = generate_microchip_code(prompt)
        self.assertIn("LED_PIN", code)
        self.assertIn("digitalWrite", code)
        self.assertIn("delay(1000)", code)

    def test_generate_temperature_sensor_code(self):
        prompt = "Read a temperature sensor"
        code = generate_microchip_code(prompt)
        self.assertIn("SENSOR_PIN", code)
        self.assertIn("analogRead", code)
        self.assertIn("Serial.println", code)

    def test_generate_heart_rate_code(self):
        prompt = "Measure heart rate"
        code = generate_microchip_code(prompt)
        self.assertIn("HEART_PIN", code)
        self.assertIn("Heartbeat detected!", code)

    def test_generate_seizure_alert_code(self):
        prompt = "Seizure alert system"
        code = generate_microchip_code(prompt)
        self.assertIn("NEURAL_PIN", code)
        self.assertIn("MEDICAL ALERT", code)

    def test_generate_unknown_code(self):
        prompt = "Do something else"
        code = generate_microchip_code(prompt)
        self.assertEqual(code, "// Sorry, I can't generate code for that prompt yet.")

if __name__ == '__main__':
    unittest.main()
