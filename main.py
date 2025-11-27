#!/usr/bin/env python3
"""
Malicious POC Application - Python
WARNING: This application uses known vulnerable/malicious dependencies
"""

import sys
import yaml  # Vulnerable PyYAML
import requests  # Vulnerable requests
from flask import Flask, request, render_template_string  # Vulnerable Flask
from jinja2 import Template  # Vulnerable Jinja2
from cryptography.fernet import Fernet  # Vulnerable cryptography
from PIL import Image  # Vulnerable Pillow
import urllib3  # Vulnerable urllib3

# Disable SSL warnings from vulnerable urllib3
urllib3.disable_warnings()

app = Flask(__name__)

# Insecure secret key
app.secret_key = "super-secret-key-123"


@app.route('/')
def index():
    return """
    <h1>⚠️ Malicious POC Application - Python</h1>
    <p>This application contains known vulnerable dependencies!</p>
    <p><strong>DO NOT USE IN PRODUCTION!</strong></p>
    """


@app.route('/yaml-load', methods=['POST'])
def yaml_load():
    """Vulnerable YAML loading (RCE risk)"""
    data = request.data
    try:
        # Unsafe YAML loading - allows arbitrary code execution
        result = yaml.load(data, Loader=yaml.Loader)
        return {'status': 'loaded', 'data': str(result)}
    except Exception as e:
        return {'error': str(e)}, 500


@app.route('/template', methods=['GET'])
def render_template():
    """SSTI vulnerability"""
    template_str = request.args.get('template', 'Hello World')
    # Vulnerable to Server-Side Template Injection
    template = Template(template_str)
    return template.render()


@app.route('/fetch', methods=['GET'])
def fetch_url():
    """Insecure URL fetching with vulnerable requests"""
    url = request.args.get('url', '')
    try:
        # No validation, vulnerable requests version
        response = requests.get(url, verify=False, timeout=5)
        return {'status': response.status_code, 'content': response.text[:200]}
    except Exception as e:
        return {'error': str(e)}, 500


@app.route('/encrypt', methods=['POST'])
def encrypt_data():
    """Using vulnerable cryptography library"""
    data = request.data
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(data)
    return {'encrypted': encrypted.decode(), 'key': key.decode()}


def vulnerable_image_processing(image_path):
    """Vulnerable Pillow usage"""
    try:
        img = Image.open(image_path)
        return img.size
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    print("⚠️  WARNING: Starting malicious POC application!")
    print("This application contains known vulnerable dependencies!")
    print("DO NOT USE IN PRODUCTION ENVIRONMENT!")
    app.run(debug=True, host='0.0.0.0', port=5000)
