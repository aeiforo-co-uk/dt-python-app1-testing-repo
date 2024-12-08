from flasgger import Swagger
from flask import Flask

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/hello', methods=['GET'])
def hello():
    """
    A simple Hello World endpoint
    ---
    responses:
      200:
        description: Returns a Hello message
    """
    return "Hello World!"

if __name__ == '__main__':
    app.run()
