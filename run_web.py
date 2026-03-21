import sys
import os

# Add src to python path to make neurochip importable
sys.path.append(os.path.join(os.path.dirname(__file__), 'neurochip/src'))

from neurochip.web.app import app

if __name__ == '__main__':
    print("Starting Neurochip AI Dashboard at http://localhost:5000")
    app.run(host='0.0.0.0', port=5000)
