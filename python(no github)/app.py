from flask import Flask, request, send_from_directory, render_template_string
import os
print("da")
app = Flask(__name__)

@app.route('/')
def index():
    files = os.listdir('.')
    return render_template_string('''
        <h1>File Browser</h1>
        <ul>
        {% for file in files %}
            <li><a href="/file/{{ file }}">{{ file }}</a></li>
        {% endfor %}
        </ul>
    ''', files=files)

@app.route('/file/<path:filename>')
def get_file(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True)
