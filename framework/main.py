from framework import Start

app = Start(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/index")
def index():
    return "This index"


if __name__ == "__main__":
    app.run()
