from flask import Flask, render_template

# Initialize Flask app for the "goodguy" server
goodguy_app = Flask(__name__)


@goodguy_app.route('/')
def home():
    """Render the home page that uses resources from server.py"""
    return render_template('goodguy.html')

if __name__ == '__main__':
    print("Starting Goodguy Flask server on port 5002...")
    print("Home page: http://goodguy.local:5002/")
    print("Using resources from server.py at http://server.local:5000/")
    print("\nMake sure server.py is running on port 5000!")
    goodguy_app.run(debug=True, port=5002)

