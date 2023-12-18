import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from werkzeug.utils import url_quote  # Importe a função correta

app = Flask(__name__)
CORS(app)  


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/endpoint', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'GET':
        # Lógica para lidar com solicitações GET
        return {'message': 'GET recebido com sucesso'}
    elif request.method == 'POST':
        data = request.get_json()
        # Lógica para lidar com solicitações POST
        return {'message': 'POST recebido com sucesso'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
