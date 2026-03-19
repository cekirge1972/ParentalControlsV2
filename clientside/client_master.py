import subprocess
import sys

# Start api.py and main.py as separate processes
api_process = subprocess.Popen([sys.executable, 'api.py'])
main_process = subprocess.Popen([sys.executable, 'client_engine.py'])

# Exit the current script immediately
sys.exit()