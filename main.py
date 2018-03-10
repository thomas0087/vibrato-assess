from flask import Flask

app = Flask(__name__)

@app.route('/')
def root_method():
    return "This is a boring method"

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
