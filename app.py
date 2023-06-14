# app.py
from flask import Flask, render_template
from models import Dictionary
import os
import ast

app = Flask(__name__)
# dictionary = Dictionary()

@app.route('/')
def index():
    return render_template('index.html')

def get_dictionary() -> Dictionary:
    current_directory = os.getcwd()
    relative_file_path = os.path.join(current_directory, 'data', 'words.txt')
    with open(relative_file_path, 'r') as file:
        words = ast.literal_eval(file.readline().strip())
        return Dictionary(words)

if __name__ == '__main__':
    get_dictionary()
    app.run(debug=True)
