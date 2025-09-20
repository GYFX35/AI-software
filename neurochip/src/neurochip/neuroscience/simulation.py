"""
This module contains an AI-powered simulation tool to model and predict neural behavior.
"""
import numpy as np
from sklearn.neural_network import MLPRegressor

def generate_neural_activity(duration_s: int, sampling_rate_hz: int, freq_hz: float) -> np.ndarray:
    """
    Generates a simulated neural activity signal (e.g., an oscillation).

    Args:
        duration_s (int): The duration of the signal in seconds.
        sampling_rate_hz (int): The sampling rate in Hz.
        freq_hz (float): The frequency of the oscillation in Hz.

    Returns:
        np.ndarray: A 1D array representing the simulated neural activity.
    """
    num_samples = int(duration_s * sampling_rate_hz)
    time = np.linspace(0, duration_s, num_samples, endpoint=False)
    activity = np.sin(2 * np.pi * freq_hz * time)
    # Add some noise to make it more realistic
    noise = np.random.normal(0, 0.2, num_samples)
    return activity + noise

def _create_time_series_dataset(data: np.ndarray, window_size: int):
    """
    Creates a windowed dataset for time series prediction.
    Helper function.
    """
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:(i + window_size)])
        y.append(data[i + window_size])
    return np.array(X), np.array(y)

def train_activity_model(activity_data: np.ndarray, window_size: int = 10):
    """
    Trains a model to predict the next step in a neural activity time series.

    Args:
        activity_data (np.ndarray): The time series data of neural activity.
        window_size (int): The number of previous time steps to use as input.

    Returns:
        MLPRegressor: The trained prediction model.
    """
    X, y = _create_time_series_dataset(activity_data, window_size)
    if len(X) == 0:
        raise ValueError("Not enough data to create a single training window. Increase data length or decrease window_size.")

    # Using a simple MLP for prediction.
    # These parameters are not tuned and are for demonstration purposes.
    model = MLPRegressor(hidden_layer_sizes=(50,), max_iter=500, random_state=42)
    model.fit(X, y)
    return model

def predict_future_activity(model: MLPRegressor, current_activity_window: np.ndarray) -> float:
    """
    Predicts the next time step of neural activity.

    Args:
        model (MLPRegressor): The trained prediction model.
        current_activity_window (np.ndarray): The most recent window of activity.
                                            Should have shape (window_size,).

    Returns:
        float: The predicted value for the next time step.
    """
    if current_activity_window.ndim != 1:
        raise ValueError("Input window must be a 1D array.")

    # Reshape for single sample prediction
    X_new = current_activity_window.reshape(1, -1)
    prediction = model.predict(X_new)
    return prediction[0]
