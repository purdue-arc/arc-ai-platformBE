import flask
import gemini_test
import os

arcApp = flask.Flask(__name__)
temp_path = './gemini_test.py'
file_path = './arc_wiki.py'
@arcApp.route("/ideation_generate")
def ideation_generate():
    try:
        print("Endpoint Success")
        os.system(f'python {temp_path}')
    except FileNotFoundError:
        print(f"Error: Could not execute '{temp_path}'. Please check the directory")

@arcApp.route("/arc_wiki")
def arc_wiki():
    try:
        print("Endpoint Success")
        os.system(f'python {file_path}')
    except FileNotFoundError:
        print(f"Error: Could not execute '{file_path}'. Please check the directory")
