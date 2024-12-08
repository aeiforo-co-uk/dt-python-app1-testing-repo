from flasgger import Swagger
from flask import Flask

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api')
def api():
    """
    An example API endpoint.
    ---
    responses:
      200:
        description: Returns an example API response
    """
    return "Hello, World!"
