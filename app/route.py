from flask import Flask
from app.controller import hello_world, ocr_pdf

app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def api_hello_world():
    return hello_world()
    # return "<p>Hello, World!</p>"
    
@app.route('/ocr-pdf', methods=['POST'])
def api_ocr_pdf():
    return ocr_pdf()
