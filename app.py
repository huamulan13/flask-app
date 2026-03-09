from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'hello word'

@app.route('/analisa-data')
def alena():
    return 'al'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)