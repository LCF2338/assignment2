
from app import flask_app
flask_app.run(host="0.0.0.0", port=5000) # Resolved issue where app would run by separating it from app.py.