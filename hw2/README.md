# Flask Server with JavaScript and Image Routes

This is a Flask application that demonstrates serving different types of content through different routes.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Servers

### Main Server (server.py)

Start the main Flask server:

```bash
python server.py
```

The server will start on `http://localhost:5000`

### Badguy Server (badguy.py)

The badguy server uses resources exposed by server.py. First start server.py, then in a separate terminal:

```bash
python badguy.py
```

The badguy server will start on `http://localhost:5001`

### Goodguy Server (goodguy.py)

The goodguy server uses resources exposed by server.py. First start server.py, then in a separate terminal:

```bash
python goodguy.py
```

The goodguy server will start on `http://localhost:5002`

**Note:** You must have server.py running on port 5000 for badguy.py and goodguy.py to work properly.

## Routes

- `/` - Home page displaying the image and using the JavaScript
- `/js/app.js` - Serves the JavaScript file
- `/image/sample` - Serves the image file

## Project Structure

```
alexis-hw2/
├── server.py          # Main Flask application (port 5000)
├── badguy.py          # Badguy Flask application using external resources (port 5001)
├── goodguy.py         # Goodguy Flask application using external resources (port 5002)
├── requirements.txt   # Python dependencies
├── static/
│   ├── app.js        # JavaScript file
│   └── image.png     # Image file
└── templates/
    ├── index.html    # Main server home page template
    ├── badguy.html   # Badguy server home page template
    └── goodguy.html  # Goodguy server home page template
```

## Features

- **Home Page**: Modern, responsive design with gradient background
- **JavaScript Integration**: Interactive elements that respond to user clicks
- **Image Display**: Sample image loaded from Flask route with hover effects
- **Separate Routes**: JavaScript and images are served through different routes as requested
- **Cross-Server Resources**: badguy.py and goodguy.py demonstrate using resources from server.py on different ports

## Usage

1. Open your browser and navigate to `http://localhost:5000`
2. You'll see a welcome page with the image displayed
3. Click the image to test the JavaScript interaction
4. Click the "Test JavaScript Function" button to verify JavaScript functionality

