from flask import Flask, render_template
# Initialize Flask app for the "badguy" server
badguy_app = Flask(__name__)


@badguy_app.route('/')
def home():
    """Render the home page that uses resources from server.py"""
    return render_template('badguy.html')

if __name__ == '__main__':
    print("Starting Badguy Flask server on port 5001...")
    print("Home page: http://badguy.local:5001/")
    print("Using resources from server.py at http://server.local:5000/")
    print("\nMake sure server.py is running on port 5000!")
    badguy_app.run(debug=True, port=5001)
