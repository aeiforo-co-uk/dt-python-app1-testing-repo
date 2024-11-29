from flask_swagger import swagger
from app import app

with app.test_request_context():
    swagger_spec = swagger(app)
    with open("swagger/swagger.json", "w") as f:
        f.write(str(swagger_spec))
    print("Swagger documentation generated at swagger/swagger.json")
