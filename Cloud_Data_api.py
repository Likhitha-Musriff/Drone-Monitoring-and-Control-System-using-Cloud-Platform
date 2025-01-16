from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to receive drone data
@app.route('/upload_drone_data', methods=['POST'])
def upload_drone_data():
    data = request.get_json()
    print(f"Received Data: {data}")
    # Here you would typically store the data in a database or cloud storage
    return jsonify({"message": "Data received successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
