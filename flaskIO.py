import flask
import gemini_test
import os

arcApp = flask.Flask(__name__)
file_path = './gemini_test.py'
@arcApp.route("/ideation_generate")
def ideation_generate():
    try:
        print("Endpoint Success")
        os.system(f'python {file_path}')
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
