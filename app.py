from flask import Flask
from routes.data_routes import data_blueprint
from routes.genai_routes import genai_blueprint

app = Flask(__name__)
app.register_blueprint(data_blueprint)
app.register_blueprint(genai_blueprint)

if __name__ == '__main__':
    app.run(debug=True)