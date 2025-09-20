"""
This module contains functions for neuroscience data analysis.
"""

def analyze_spike_train(spike_train):
    """
    Analyzes a spike train.

    Args:
        spike_train (list): A list of spike times.

    Returns:
        dict: A dictionary of analysis results.
    """
    if len(spike_train) < 2:
        return {"firing_rate": 0}

    duration = spike_train[-1] - spike_train[0]
    if duration == 0:
        return {"firing_rate": float('inf')}

    firing_rate = (len(spike_train) - 1) / duration
    return {"firing_rate": firing_rate}
