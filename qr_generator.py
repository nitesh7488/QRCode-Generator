# -*- coding: utf-8 -*-
# Generate QR Code of any type.
# It's based on PyQRCode Library.

from flask import Flask, send_file, render_template
import pyqrcode
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate/<text>')
def generate_qr(text):
    qr = pyqrcode.create(text)
    qr.png('static/generator.png', scale=10)

    return render_template('qr_display.html', text=text)


if __name__ == '__main__':
    app.run(debug=True)
