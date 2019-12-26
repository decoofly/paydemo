from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

def deduct():
    pass



if __name__ == '__main__':
    app.run(debug=True)
