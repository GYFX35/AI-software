import unittest
import numpy as np
from neurochip.neuroscience.ml import train_classifier, predict_signal

class TestML(unittest.TestCase):

    def test_train_and_predict(self):
        # Create some dummy data
        X_train = np.array([[0, 0], [1, 1], [0, 1], [1, 0]])
        y_train = np.array([0, 1, 0, 1])

        # Train the model
        model = train_classifier(X_train, y_train)

        # Make a prediction
        X_new = np.array([[0, 0]])
        prediction = predict_signal(model, X_new)

        # Check the prediction
        self.assertEqual(prediction[0], 0)

        # Make another prediction
        X_new = np.array([[1, 1]])
        prediction = predict_signal(model, X_new)

        # Check the prediction
        self.assertEqual(prediction[0], 1)

if __name__ == '__main__':
    unittest.main()
