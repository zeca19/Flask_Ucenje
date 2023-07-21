from flask import Flask


app = Flask(__name__)

# Ovo predstavlja rutu u koju ulazimo


@app.route("/")
def hello():
    return "<h2>Zdravo</h2>"
