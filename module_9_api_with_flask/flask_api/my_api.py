from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from your flask API!'})

if __name__ == '__main__':
    app.run(debug=True)

### In Terminal, verified that app is running ###
# kenny@Kennys-MacBook-Air flask_api % python3 my_api.py
#  * Serving Flask app 'my_api'
#  * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 356-233-617

### In Postman, created a new collection and new request: http://127.0.0.1:5000/api which returned JSON payload.