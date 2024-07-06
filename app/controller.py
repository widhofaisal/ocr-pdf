from flask import jsonify, request
import subprocess
import os
import uuid

def hello_world():
    responseSuccess = {
        "name": "endpoint hello world",
        "message": "success",
        "err_code": 200,
        "data": ""
    }
    return responseSuccess

def ocr_pdf():
    # Get the input PDF file from the request
    file = request.files['file']
    
    # Generate a unique UUID for the input and output files
    unique_id = str(uuid.uuid4())
    input_dir = 'input/'
    output_pdf_dir = 'output/pdf/'
    output_txt_dir = 'output/txt/'
    input_pdf = os.path.join(input_dir, f'input_{unique_id}.pdf')
    output_pdf = os.path.join(output_pdf_dir, f'output_{unique_id}.pdf')
    sidecar_file = os.path.join(output_txt_dir, f'output_{unique_id}.txt')

    # Ensure output directories exist
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_pdf_dir, exist_ok=True)
    os.makedirs(output_txt_dir, exist_ok=True)

    # Save the uploaded PDF file
    file.save(input_pdf)

    # Run the OCRmyPDF command
    try:
        subprocess.run(['ocrmypdf', '--sidecar', sidecar_file, '--force-ocr',input_pdf, output_pdf], check=True)
    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e)}), 500

    # Read the contents of the sidecar file
    if os.path.exists(sidecar_file):
        with open(sidecar_file, 'r') as f:
            ocr_text = f.read()
    else:
        return jsonify({'error': 'Sidecar file not found'}), 500

    # Return the OCR text as JSON and paths to the input and output files
    return jsonify({
        'ocr_text': ocr_text,
        'input_pdf': input_pdf,
        'output_pdf': output_pdf,
        'output_txt': sidecar_file
    })