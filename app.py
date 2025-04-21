from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Calculator API! Use POST /calculate with num1, num2, and operation."

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    try:
        num1 = float(data.get("num1"))
        num2 = float(data.get("num2"))
        operation = data.get("operation")

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
