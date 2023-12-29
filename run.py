from app import application
from views import blue

application.register_blueprint(blue)

application.run(debug=True)
