
from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world() -> str: 
    return "<p style=\"text-align: center; font-size: 100px\">Flask Text Test!😭</p>"

if __name__ == "__main__": 
    app.run(debug=True)
