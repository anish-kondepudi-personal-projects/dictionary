# app.py
from flask import Flask, render_template, request
from models import Dictionary
import os
import ast

app = Flask(__name__)
# dictionary = Dictionary()

@app.route('/', methods=['GET', 'POST'])
def index():
    word_list = []
    if request.method == 'POST':
        num = int(request.form['number'])
        dictionary = get_dictionary()
        word_list = dictionary.get_page(num)
    return render_template('index.html', words=word_list)

def get_dictionary() -> Dictionary:
    current_directory = os.getcwd()
    relative_file_path = os.path.join(current_directory, 'data', 'words.txt')
    with open(relative_file_path, 'r', encoding='utf-8') as file:
        words = ast.literal_eval(file.readline().strip())
        return Dictionary(words)

if __name__ == '__main__':
    get_dictionary()
    app.run(debug=True)
