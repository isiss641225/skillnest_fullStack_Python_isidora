# ==========================================================
# SERVIDOR PRINCIPAL DE FLASK
# ==========================================================

from flask_app import app
from flask_app.controllers import estudiantes

if __name__ == "__main__":
    app.run(debug=True)