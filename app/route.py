from app.controller import hello_world, ocr_pdf
from app import app


@app.route("/hello", methods=['GET'])
def api_hello_world():
    return hello_world()
    # return "<p>Hello, World!</p>"
    
@app.route('/ocr-pdf', methods=['POST'])
def api_ocr_pdf():
    return ocr_pdf()
