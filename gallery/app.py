from flask import Flask, render_template, request, send_from_directory
from gallery.upload import upload_file, UPLOADS_DIR
from gallery.db import get_images
import os


app = Flask(__name__)

app.config.update(
    SECRET_KEY='abc123',
    TEMPLATES_AUTO_RELOAD=True
)


@app.route('/', methods=['POST', 'GET'])
def show():
    if request.method == 'POST' and 'file' in request.files:
        fileitem = request.files['file']
        title = request.form.get('title')
        upload_file(fileitem, title)
    return render_template('home.html', images=get_images())


@app.route('/uploads/<path>')
def send_uploads(path):
    print('-----------------------', path)
    return send_from_directory(os.path.join(os.getcwd(), UPLOADS_DIR), path)
