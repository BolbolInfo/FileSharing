from flask import Flask, request, render_template
from flask import send_from_directory
import os
import secrets
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16MB

# Function to generate a random filename

def generate_random_filename(filename):
    random_hex = secrets.token_hex(8)
    _, ext = os.path.splitext(filename)
    return secure_filename(random_hex + ext)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        # filename = generate_random_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return f'File uploaded successfully! Access it at: <a href="/download/{filename}">Download Link</a>'



@app.route('/download/<path:filename>')
def download_file(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    except Exception as e:
        print(e)  # Optional: Print the exception for further debugging
        return "File not found or an error occurred while retrieving the file."

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)# or change it to 192.168.43.1 to use it in the personpersonal hotspot
