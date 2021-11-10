from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        url = request.form['url']
        
        return render_template('home.html')

    if request.method == 'POST':
        return


if __name__ == "__main__":
    app.run(debug=True)