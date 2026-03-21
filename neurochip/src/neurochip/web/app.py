from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import numpy as np
import sys

# Add src to python path if not already there
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if src_path not in sys.path:
    sys.path.append(src_path)

from neurochip.microchip.ai_assistant import generate_microchip_code
from neurochip.microchip.cyber_security import analyze_security
from neurochip.neuroscience.health_diagnostics import analyze_heart_rate, detect_seizure_activity, diagnose_condition

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/generate_code', methods=['POST'])
def api_generate_code():
    data = request.json
    prompt = data.get('prompt', '')
    code = generate_microchip_code(prompt)
    return jsonify({'code': code})

@app.route('/api/analyze_security', methods=['POST'])
def api_analyze_security():
    data = request.json
    code = data.get('code', '')
    report = analyze_security(code)
    return jsonify({'report': report})

@app.route('/api/diagnose', methods=['POST'])
def api_diagnose():
    data = request.json
    # Expected format for data: {'ecg_signal': [...], 'sampling_rate': 100, 'neural_signal': [...]}
    ecg_signal = np.array(data.get('ecg_signal', []))
    sampling_rate = data.get('sampling_rate', 100)
    neural_signal = np.array(data.get('neural_signal', []))

    hr = analyze_heart_rate(ecg_signal, sampling_rate)
    seizure = detect_seizure_activity(neural_signal)
    diagnosis = diagnose_condition({'heart_rate': hr, 'seizure_detected': seizure})

    return jsonify({
        'heart_rate': hr,
        'seizure_detected': bool(seizure),
        'diagnosis': diagnosis
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
