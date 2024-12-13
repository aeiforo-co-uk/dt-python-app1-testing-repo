from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# In-memory storage for book requests
book_requests = []

# Swagger UI setup
SWAGGER_URL = '/apidocs'
API_URL = '/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Book Request API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/swagger.json')
def swagger_spec():
    return jsonify({
        "swagger": "2.0",
        "info": {
            "title": "Book Request API",
            "version": "1.0"
        },
        "paths": {
            "/api/bookrequests": {
                "post": {
                    "summary": "Create a new book request",
                    "description": "Add a book request to the list.",
                    "parameters": [
                        {
                            "in": "body",
                            "name": "body",
                            "required": True,
                            "schema": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "integer"},
                                        "username": {"type": "string"},
                                        "firstName": {"type": "string"},
                                        "lastName": {"type": "string"},
                                        "email": {"type": "string"},
                                        "password": {"type": "string"},
                                        "phone": {"type": "string"},
                                        "userStatus": {"type": "integer"}
                                    },
                                    "required": ["id", "username", "email"]
                                }
                            },
                            "description": "List of book requests to be added."
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Book request created successfully",
                            "schema": {"type": "string"}
                        }
                    }
                },
                "get": {
                    "summary": "Get book requests",
                    "description": "Retrieve all book requests or filter by query parameters.",
                    "parameters": [
                        {
                            "in": "query",
                            "name": "id",
                            "type": "integer",
                            "description": "Filter by ID"
                        },
                        {
                            "in": "query",
                            "name": "username",
                            "type": "string",
                            "description": "Filter by username"
                        },
                        {
                            "in": "query",
                            "name": "email",
                            "type": "string",
                            "description": "Filter by email"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "List of book requests",
                            "schema": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "integer"},
                                        "username": {"type": "string"},
                                        "firstName": {"type": "string"},
                                        "lastName": {"type": "string"},
                                        "email": {"type": "string"},
                                        "password": {"type": "string"},
                                        "phone": {"type": "string"},
                                        "userStatus": {"type": "integer"}
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    })


@app.route('/api/bookrequests', methods=['POST'])
def create_book_requests():
    """
    Handles POST requests to create new book requests.
    """
    data = request.get_json()
    if not isinstance(data, list):
        return jsonify({"error": "Input should be a lists of book requests"}), 400

    for book_request in data:
        if 'id' not in book_request or 'username' not in book_request or 'email' not in book_request:
            return jsonify({"error": "id, username, and email are required"}), 400
        book_requests.append(book_request)

    return jsonify({"message": "Book requests created successfully"}), 200


@app.route('/api/bookrequests', methods=['GET'])
def get_book_requests():
    """
    Handles GET requests to retrieve book requests, with optional filters.
    """
    id_filter = request.args.get('id')
    username_filter = request.args.get('Username')
    email_filter = request.args.get('email')

    # Filter the book_requests based on query parameters
    filtered_requests = book_requests
    if id_filter:
        filtered_requests = [br for br in filtered_requests if str(br.get('id')) == id_filter]
    if username_filter:
        filtered_requests = [br for br in filtered_requests if br.get('username') == username_filter]
    if email_filter:
        filtered_requests = [br for br in filtered_requests if br.get('email') == email_filter]

    return jsonify(filtered_requests), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
