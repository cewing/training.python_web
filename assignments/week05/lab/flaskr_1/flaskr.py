from flask import Flask


# configuration goes here


app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)
