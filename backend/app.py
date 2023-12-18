from flask import Flask, request

app = Flask(__name__)

@app.route('/api/endpoint', methods=['POST'])
def handle_post_request():
    data = request.get_json()
    # Faça algo com os dados do POST
    return {'message': 'POST recebido com sucesso'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
