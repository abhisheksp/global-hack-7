from flask import Flask, request
from broadcast import broadcast

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '<h1>Works!</h1>'


@app.route('/broadcast', methods=['POST'])
def broadcast_handler():
    request_body = request.get_json()
    message = request_body['message']
    status = broadcast(message)
    return status


@app.route('/messagecallback', methods=['POST'])
def message_callback_handler():
    message = request.values.get('Body', None)
    status = broadcast(message)
    return status

if __name__ == '__main__':
    app.run()
