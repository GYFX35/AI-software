"""
This module contains functions for health and medical diagnostics using neuroscience data.
"""

import numpy as np

def analyze_heart_rate(ecg_signal, sampling_rate):
    """
    Analyzes an ECG signal to calculate heart rate.

    Args:
        ecg_signal (np.ndarray): The ECG signal data.
        sampling_rate (int): The sampling rate of the signal in Hz.

    Returns:
        float: The calculated heart rate in beats per minute (BPM).
    """
    if len(ecg_signal) == 0:
        return 0.0

    # Simple peak detection: find peaks above a threshold
    threshold = np.mean(ecg_signal) + 2 * np.std(ecg_signal)
    above_threshold = np.where(ecg_signal > threshold)[0]

    if len(above_threshold) < 2:
        return 0.0

    # Identify distinct peaks by checking where the indices are not consecutive
    # A gap of at least 0.2 seconds (typical refractory period) is expected
    min_gap = int(0.2 * sampling_rate)
    peaks = [above_threshold[0]]
    for i in range(1, len(above_threshold)):
        if above_threshold[i] - peaks[-1] >= min_gap:
            peaks.append(above_threshold[i])

    if len(peaks) < 2:
        return 0.0

    # Calculate inter-beat intervals (IBIs)
    ibis = np.diff(peaks) / sampling_rate
    mean_ibi = np.mean(ibis)

    if mean_ibi == 0:
        return 0.0

    heart_rate = 60.0 / mean_ibi
    return heart_rate

def detect_seizure_activity(neural_signal, threshold=5.0):
    """
    Detects potential seizure activity in a neural signal.

    A simple detection based on signal amplitude exceeding a threshold
    relative to the mean signal.

    Args:
        neural_signal (np.ndarray): The neural signal data.
        threshold (float): The multiplier for the standard deviation.

    Returns:
        bool: True if potential seizure activity is detected, False otherwise.
    """
    if len(neural_signal) == 0:
        return False

    mean = np.mean(neural_signal)
    std = np.std(neural_signal)

    if std == 0:
        return False

    # Check for values significantly higher than the mean
    if np.any(np.abs(neural_signal - mean) > threshold * std):
        return True

    return False

def diagnose_condition(data_summary):
    """
    Provides a diagnostic suggestion based on analyzed data.

    Args:
        data_summary (dict): A dictionary containing analysis results.

    Returns:
        str: A diagnostic message.
    """
    hr = data_summary.get('heart_rate', 0)
    seizure_detected = data_summary.get('seizure_detected', False)

    if seizure_detected:
        return "Warning: Potential seizure activity detected. Immediate medical attention may be required."

    if hr > 100:
        return "Observation: Tachycardia (high heart rate) detected."
    elif 0 < hr < 60:
        return "Observation: Bradycardia (low heart rate) detected."
    elif hr == 0:
        return "Error: No heart rate could be determined."
    else:
        return "Diagnosis: Heart rate is within normal range."
