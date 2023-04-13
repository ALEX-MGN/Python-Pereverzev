from flask import Flask

app = Flask(__name__)
host = '0.0.0.0'
port = 5000

@app.route('/hello/<user>')
def hello_user(user):
    return f'hello, {user}!'

if __name__ == '__main__':
    app.run(host=host, port=port)