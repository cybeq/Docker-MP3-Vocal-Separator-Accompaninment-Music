from flask import Flask, send_file, request, render_template
import os
import subprocess
import zipfile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def download_file():
    if 'file' not in request.files:
        return 'No file uploaded.'

    file = request.files['file']
    if file.filename == '':
        return 'No file selected.'
    _, ext = os.path.splitext(file.filename)
    if ext != '.mp3':
        return 'Only MP3 files are allowed.'
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'file.mp3')
    file.save(filepath)

    subprocess.run(["spleeter", "separate", "-p", "spleeter:2stems", "-o", "output", "file.mp3"], check=True)

    zip_filename = 'vocals_and_accompaniment.zip'
    zip_filepath = os.path.join('output', 'file', zip_filename)
    filepaths = ['output/file/vocals.wav', 'output/file/accompaniment.wav']

    with zipfile.ZipFile(zip_filepath, 'w') as zip_file:
        for filepath in filepaths:
            if os.path.exists(filepath):
                zip_file.write(filepath)
            else:
                raise FileNotFoundError(f'File "{filepath}" not found.')

    return send_file(zip_filepath, as_attachment=True)



if __name__ == '__main__':
    app.run(host='0.0.0.0')
