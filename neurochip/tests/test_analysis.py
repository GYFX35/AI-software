import unittest
from neurochip.neuroscience.analysis import analyze_spike_train

class TestAnalysis(unittest.TestCase):

    def test_analyze_spike_train_empty(self):
        self.assertEqual(analyze_spike_train([]), {"firing_rate": 0})

    def test_analyze_spike_train_simple(self):
        spike_train = [0.1, 0.2, 0.3, 0.4, 0.5]
        result = analyze_spike_train(spike_train)
        self.assertAlmostEqual(result["firing_rate"], 10.0)

if __name__ == '__main__':
    unittest.main()
