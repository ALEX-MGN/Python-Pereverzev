from flask import Flask
import os

app = Flask(__name__)

@app.route("/hello/<username>")
def hello(username):
    return f"Hello, {username}!"

@app.route("/even/<int:number>")
def even(number) -> str:
    if number % 2 == 0:
        result = "чётное"
    else:
        result = "нечётное"
    return f"Число {number} <b>{result}</b>"

@app.route("/check_exists/<string:file_path>")
def check_exists(file_path):
    file_exists = os.path.exists(file_path)
    response_code = 200 if file_exists else 404
    result = "exists" if file_exists else "not exists"
    return f"File <h3>{file_path}</h3> {result}.", response_code

if __name__ == "__main__":
    app.run(debug=True)