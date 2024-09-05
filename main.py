from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_new_content')
def get_new_content():
    new_content = "This is new content from the backend!"
    return jsonify({'content': new_content})

if __name__ == '__main__':
    app.run(debug=True)