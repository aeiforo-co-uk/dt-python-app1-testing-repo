from flask import Flask
from flasgger import Swagger
import json

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api')
def api():
    """
    This is the API endpoint
    ---
    responses:
      200:
        description: A successful response
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: 'Hello, World!'
    """
    return {'message': 'Hello, World!'}

if __name__ == "__main__":
    app.run(debug=True)
