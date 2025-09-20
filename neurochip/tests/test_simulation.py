import unittest
import numpy as np
from neurochip.neuroscience.simulation import (
    generate_neural_activity,
    train_activity_model,
    predict_future_activity
)

class TestSimulation(unittest.TestCase):

    def test_generate_neural_activity(self):
        activity = generate_neural_activity(duration_s=1, sampling_rate_hz=100, freq_hz=10)
        self.assertIsInstance(activity, np.ndarray)
        self.assertEqual(activity.shape, (100,))

    def test_train_and_predict(self):
        # Generate some data
        activity = generate_neural_activity(duration_s=5, sampling_rate_hz=100, freq_hz=5)

        # Train the model
        window_size = 10
        model = train_activity_model(activity, window_size=window_size)

        # Check that the model is trained (has coefficients)
        self.assertTrue(hasattr(model, "coefs_"))

        # Make a prediction
        current_window = activity[-window_size:]
        prediction = predict_future_activity(model, current_window)

        # Check the prediction type and shape
        self.assertIsInstance(prediction, float)

    def test_train_with_insufficient_data(self):
        # Test that training raises an error if data is too short
        activity = np.array([1, 2, 3])
        with self.assertRaises(ValueError):
            train_activity_model(activity, window_size=5)

if __name__ == '__main__':
    unittest.main()
