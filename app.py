# app.py
from flask import Flask, render_template, request
from models import Dictionary
import os
import ast

def get_dictionary() -> Dictionary:
    current_directory = os.getcwd()
    relative_file_path = os.path.join(current_directory, 'data', 'words.txt')
    with open(relative_file_path, 'r', encoding='utf-8') as file:
        words = ast.literal_eval(file.readline().strip())
        return Dictionary(words)

app = Flask(__name__)
dictionary = get_dictionary()
curr_page = 1

@app.route('/', methods=['GET', 'POST'])
def index():
    global curr_page
    word_list = []
    if request.method == 'POST':
        request_num = int(request.form['number'])
        if dictionary.is_valid_page(request_num):
            curr_page = request_num
    elif request.method == 'GET':
        x = request.args.get('page', type=int, default=0)
        if x == 1:
            if dictionary.is_valid_page(curr_page - 1):
                curr_page -= 1
        if x == 2:
            if dictionary.is_valid_page(curr_page + 1):
                curr_page += 1
    word_list = dictionary.get_page(curr_page)
    return render_template('index.html', words=word_list, curr_page=curr_page)

if __name__ == '__main__':
    get_dictionary()
    app.run(debug=True)
