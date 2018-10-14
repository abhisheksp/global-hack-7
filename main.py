import firebase
from flask import Flask, request
from broadcast import broadcast
from register import register_group, register_number

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


@app.route('/register', methods=['POST'])
def register_handler():
    request_body = request.get_json()
    platform = request_body['platform']
    identifier = request_body['identifier']
    if platform == 'facebook':
        print('calling FB')
        status = register_group(identifier)
    else:
        print('calling Number')
        status = register_number(identifier)
    return status


if __name__ == '__main__':
    app.run()
