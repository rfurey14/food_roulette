from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "What are you craving?"

app.run(host = "0.0.0.0", port=80)