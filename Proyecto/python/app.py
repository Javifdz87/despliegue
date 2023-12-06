from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Hola, mundo! Esta es una aplicación Python en Flask.'

if __name__ == '__main__':
    app.run()