from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello worlddd'
    dsfg
if __name__ == '__main__':

    app.run()