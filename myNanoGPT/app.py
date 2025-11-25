from flask import Flask, jsonify, send_from_directory 
import subprocess
import random

app = Flask(__name__)

@app.route('/')
def index ():
    return send_from_directory('.', 'index.html')

@app.route('/generate', methods=['GET'])
def generate_text ():
    # Generate random seed for variety
    seed = random.randint(0, 100000) # type: ignore

    # Run sample.py with default settings, adjust as needed for your checkpoints
    result = subprocess.run(
        [
            "python", "sample.py", "--out_dir=out-movies",
            f"--seed={seed}"
        ],
        capture_output=True, text=True
    )
    return jsonify({"output": result.stdout})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)