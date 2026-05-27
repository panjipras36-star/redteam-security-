from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

SECRET_PIN_HASH = "81dc9bdb52d04dc20036dbd8313ed055" 
THE_FLAG = "CTF{pyth0n_num3r1c_brut3_f0rc3_l3g1t}"

@app.route('/api/auth', methods=['POST'])
def auth():
    data = request.json or {}
    input_pin = data.get("pin", "")

    if not input_pin.isdigit() or len(input_pin) != 4:
        return jsonify({"status": "error", "message": "PIN must be a 4-digit number"}), 400

    input_hash = hashlib.md5(input_pin.encode()).hexdigest()

    if input_hash == SECRET_PIN_HASH:
        return jsonify({"status": "access_granted", "flag": THE_FLAG})
    else:
        return jsonify({"status": "access_denied", "message": "Incorrect PIN!"}), 401

if __name__ == '__main__':
    app.run(port=5000)
