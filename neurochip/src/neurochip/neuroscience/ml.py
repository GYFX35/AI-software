"""
This module contains machine learning models for neuroscience data.
"""

from sklearn.svm import SVC
import numpy as np

def train_classifier(X_train, y_train):
    """
    Trains a classifier on the given data.

    Args:
        X_train (np.ndarray): The training data.
        y_train (np.ndarray): The training labels.

    Returns:
        SVC: The trained classifier.
    """
    model = SVC()
    model.fit(X_train, y_train)
    return model

def predict_signal(model, X_new):
    """
    Predicts the class of a new signal.

    Args:
        model (SVC): The trained classifier.
        X_new (np.ndarray): The new data point.

    Returns:
        np.ndarray: The predicted class.
    """
    return model.predict(X_new)
