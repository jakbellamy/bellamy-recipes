from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'The Bellamy Recipe Page is Under Construction! 👷‍♂️'

if __name__ == '__main__':
    app.run()