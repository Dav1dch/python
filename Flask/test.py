from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
name = ["David"]

@app.route('/')
def hello_world(name=name):
    return render_template("index.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
    pass