
# URL Categorization

**URL Categorization** is a machine learning project that categorizes URLs based on their content. This project can be utilized for applications such as cybersecurity, advertisement filtering, and parental controls.

## Features
- Machine learning-based URL classification.
- Dataset preprocessing and model training capabilities.
- Flask-based server for backend processing.
- React-based client interface to interact with the model.

## Installation

### 1. Clone the repository:
   ```bash
   git clone https://github.com/dogncankrkc/URL-Categorization.git
   ```

### 2. Backend Setup (Flask Server):
1. Navigate to the `flask-server` directory:
   ```bash
   cd flask-server
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask server:
   ```bash
   python app.py
   ```

### 3. Client Setup:
1. Navigate to the `client` directory:
   ```bash
   cd client
   ```
2. Start the client:
   ```bash
   npm install
   npm start
   ```

### 4. Usage:
Once both the Flask server and the client are running:
- Open the client interface and interact with the model to categorize URLs.
- The Flask server will handle the backend processing.

## License
This project is licensed under the MIT License.
