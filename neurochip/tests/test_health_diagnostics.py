import unittest
import numpy as np
from neurochip.neuroscience.health_diagnostics import analyze_heart_rate, detect_seizure_activity, diagnose_condition

class TestHealthDiagnostics(unittest.TestCase):

    def test_analyze_heart_rate(self):
        # Create a simulated signal with peaks at 100, 200, 300, 400, 500 samples
        # Sampling rate = 100 Hz, so peaks are every 1 second
        # BPM should be 60
        sampling_rate = 100
        ecg_signal = np.zeros(1000)
        ecg_signal[[100, 200, 300, 400, 500]] = 10.0

        hr = analyze_heart_rate(ecg_signal, sampling_rate)
        self.assertAlmostEqual(hr, 60.0)

    def test_analyze_heart_rate_empty(self):
        hr = analyze_heart_rate(np.array([]), 100)
        self.assertEqual(hr, 0.0)

    def test_detect_seizure_activity_positive(self):
        # Signal with a massive spike
        neural_signal = np.ones(100)
        neural_signal[50] = 100.0

        is_seizure = detect_seizure_activity(neural_signal)
        self.assertTrue(is_seizure)

    def test_detect_seizure_activity_negative(self):
        # Calm signal
        neural_signal = np.random.normal(0, 1, 100)

        is_seizure = detect_seizure_activity(neural_signal)
        self.assertFalse(is_seizure)

    def test_diagnose_condition_normal(self):
        summary = {'heart_rate': 75, 'seizure_detected': False}
        diagnosis = diagnose_condition(summary)
        self.assertIn("normal range", diagnosis)

    def test_diagnose_condition_seizure(self):
        summary = {'heart_rate': 75, 'seizure_detected': True}
        diagnosis = diagnose_condition(summary)
        self.assertIn("Warning: Potential seizure activity detected", diagnosis)

    def test_diagnose_condition_tachycardia(self):
        summary = {'heart_rate': 120, 'seizure_detected': False}
        diagnosis = diagnose_condition(summary)
        self.assertIn("Tachycardia", diagnosis)

    def test_diagnose_condition_bradycardia(self):
        summary = {'heart_rate': 45, 'seizure_detected': False}
        diagnosis = diagnose_condition(summary)
        self.assertIn("Bradycardia", diagnosis)

if __name__ == '__main__':
    unittest.main()
