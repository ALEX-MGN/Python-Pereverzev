import os
import shlex
import signal
import subprocess
from flask import Flask

app = Flask(__name__)

def delete_active_processes(port):
    command_str = f"lsof -i :{port}"
    command = shlex.split(command_str)
    result_list = subprocess.run(command, capture_output=True).stdout.decode().split('\n')[1:-1]
    pid_list = []
    for line in result_list:
        pid_list.append(int(line.split()[1]))

    if not os.getpid() in pid_list:
        for pid in pid_list:
            os.kill(pid, signal.SIGKILL)
    app.run(debug=True, port=port)

if __name__ == "__main__":
    delete_active_processes(5000)
