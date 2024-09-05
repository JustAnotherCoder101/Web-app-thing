from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit_data', methods=['POST'])
def submit_data():
  data = request.get_json()  # Get data from the request body
  name = data.get('name')
  message = data.get('message')

  # Process the data (e.g., store in a database)
  # ... 

  return jsonify({'message': f'Received data: Name: {name}, Message: {message}'})

if __name__ == '__main__':
  app.run(debug=True)