from datetime import timedelta
from flask import Flask


app = Flask(__name__)

@app.route("/uptime", methods=["GET"])
def uptime():
    with open('/proc/uptime', 'r') as f:
        seconds = float(f.readline().split(maxsplit=1)[0])
    return f"Current uptime is {str(timedelta(seconds=seconds)).split('.')[0]}"

if __name__ == '__main__':
    app.run(debug=True)