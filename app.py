from flask import Flask, request, jsonify
import calculator  # Assuming your artifact contains a `calculator` module

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    """Add two numbers"""
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify({"error": "Missing parameters a or b"}), 400
    result = calculator.add(a, b)  # Example usage of your artifact
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
