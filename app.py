
from flask import Flask 
import os

app = Flask(__name__)

@app.route('/')
def hello_world() -> str: 
    web_text:str = ""
    if "FLASK_ENV" and "FLASK_APP" in os.environ:
        web_text= f"\'FLASK_ENV\': {os.environ["FLASK_ENV"]} | \'FLASK_APP\': {os.environ["FLASK_APP"]}"
    if not web_text: 
        return f"<p style=\"text-align: center; font-size: 100px\">😭</p>"
    else: 
        return f"<p style=\"text-align: center; font-size: 100px\"> {web_text} 😭</p>"

if __name__ == "__main__": 
    app.run(debug=True)
