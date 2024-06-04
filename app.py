from flask import Flask
from flask_cors import CORS
from routes.data_routes import data_blueprint
from routes.genai_routes import genai_blueprint

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

app.register_blueprint(data_blueprint)
app.register_blueprint(genai_blueprint)

if __name__ == '__main__':
    app.run(debug=True)