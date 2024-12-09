import os
from flasgger import Swagger
from flask import Flask

# Create Flask app
app = Flask(__name__)
Swagger(app)

@app.route('/api/example', methods=['GET'])
def example_endpoint():
    """
    Example Endpoint
    ---
    responses:
      200:
        description: A successful response
    """
    return {"message": "Success"}, 200

# Generate Swagger files
os.makedirs("swagger", exist_ok=True)
with open("swagger/swagger.json", "w") as f:
    f.write(app.openapi_json)
print("Swagger documentation generated!")
