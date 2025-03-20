from flask import Flask, request, jsonify
from flask_cors import CORS
from chatgpt import get_chatgpt_response

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return {'message': 'Hello, World!'}

@app.route('/submit', methods=['POST'])
def receive_data():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data received'}), 400
    
    response = get_chatgpt_response(data)

    return jsonify({'message': response})

if __name__ == '__main__':
    app.run(debug=True)