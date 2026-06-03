from flask import Flask, request, jsonify
from classes.mycar import Car

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from your flask API!'})

@app.route('api/car', methods=['POST'])
def handle_car_request():
    data = request.json
    try:
        make = data.get('make')
        model = data.get('model')
        year = data.get('year')

        if not all([make, model, year]):
            return jsonify({'Error: Missing required fields'}), 400 # 400 status code is passed
        
        car = Car(make, model, year)
        return jsonify({'car': car.__dict__}), 201
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)