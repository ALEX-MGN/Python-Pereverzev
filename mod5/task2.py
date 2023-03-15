import shlex
import subprocess
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)
app.config["WTF_CSRF_ENABLED"] = False

class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(default=10, validators=[NumberRange(min=0, max=30)])

def run_code_in_subprocess(code, timeout):
    command = f'python3 -c "{code}"'
    command = shlex.split(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    kill_timeout = False
    try:
        outs, errors = process.communicate(timeout=timeout)
    except:
        process.kill()
        outs, errors = process.communicate()
        kill_timeout = True
    return outs.decode(), errors.decode(), kill_timeout

@app.route("/run_code", methods=["POST"])
def run_code():
    form = CodeForm()
    if form.validate_on_submit():
        stdout, stderr, killed = run_code_in_subprocess(code=form.code.data, timeout=form.timeout.data)
        return f"Stdout: {stdout}, stderr: {stderr}, process was killed by timeout: {killed}"
    return f"Bad request. Error = {form.errors}", 400

if __name__ == "__main__":
    app.run(debug=True)