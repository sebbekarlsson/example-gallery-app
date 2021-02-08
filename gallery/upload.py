from gallery.db import create_image
import os

UPLOADS_DIR = './uploads'


def upload_file(fileitem, title):
    if not os.path.isdir(UPLOADS_DIR):
        os.makedirs(UPLOADS_DIR)
    fileitem.save(os.path.join(UPLOADS_DIR, fileitem.filename))

    create_image(fileitem.filename, title)
