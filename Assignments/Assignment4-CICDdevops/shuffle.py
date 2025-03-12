import os
from flask import Flask, jsonify, request 
import json
import random

app = Flask(__name__)

@app.route('/shuffle', methods=['GET'])
def shuffle():
    try:
        data = request.get_json()
        if 'list_of_ints' in data:
            input_list = data['list_of_ints']
            shuffled_list = random.sample(input_list, len(input_list))
            response = {'shuffled_list': shuffled_list}
            return jsonify(response)
        else:
            return jsonify({'error': 'Missing list_of_ints in request'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    