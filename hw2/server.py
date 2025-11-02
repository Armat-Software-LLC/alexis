from crypt import methods
from flask import Flask, render_template, send_file, send_from_directory, make_response, request
from flask_cors import CORS 
import os

from werkzeug.datastructures import headers
from policies import CSP_POLICY_ALLOW, CSP_POLICY_DENY

app = Flask(__name__)
CORS(app, origins="*", 
    allow_headers="*", methods=["OPTIONS", "GET"], max_age=3600);


# here, insert the function and the app lifecycle hook (ex: @app.before_request)
# to apply CSP policy sitewide. Use the policies.py file (provided)

# serves the home page here
@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')

# serves the JavaScript file here
@app.route('/js/<path:filename>', methods=['GET', 'OPTIONS'])
def serve_js(filename):
    """Serve the JavaScript file"""
    return send_from_directory('static', filename, mimetype='application/javascript')

# serves the image file here
@app.route('/image/<path:filename>', methods=['GET', 'OPTIONS'])
def serve_image(filename):
    """Serve the image file"""
    # handle_cors_headers(request)
    return send_from_directory('static', filename, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

