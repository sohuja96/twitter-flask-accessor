import os

FILENAME = "app.py"
run_command = "FLASK_APP="+FILENAME+" flask run"
os.system("pwd")
os.system(run_command + ">> out.txt")

