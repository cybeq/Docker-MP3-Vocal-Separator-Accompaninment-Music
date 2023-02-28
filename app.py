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
#
# MIT License
#
# Copyright (c) 2019-present, Deezer SA.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
