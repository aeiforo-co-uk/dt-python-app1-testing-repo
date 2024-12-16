from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# In-memory storage for book reques
book_requests = []

# Swagger UI setup
SWAGGER_URL = '/apidocs'
API_URL = '/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Swagger APaI Testing"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/swagger.json')
def swagger_spec():
    return jsonify({
        "swagger": "2.0",
        "info": {
            "title": "Swagger API 'Teting",
            "version": "v1.0.1"
        },
        "schemes": ["http", "https"],
        "paths": {
            "/api/bookrequests": {
                "post": {
                    "summary": "Create a new book request",
                    "description": "Add a book's request to the list.",
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
                            "description": "Book requests created successfully",
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
                },
                "put": {
                    "summary": "Update an existing book request",
                    "description": "Update a book request by ID.",
                    "parameters": [
                        {
                            "in": "body",
                            "name": "body",
                            "required": True,
                            "schema": {
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
                                "required": ["id"]
                            },
                            "description": "Book request data to update."
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Book request updated successfully",
                            "schema": {"type": "string"}
                        },
                        "404": {
                            "description": "Book request not found"
                        }
                    }
                },
                "delete": {
                    "summary": "Delete a book request",
                    "description": "Delete a book request by ID.",
                    "parameters": [
                        {
                            "in": "query",
                            "name": "id",
                            "type": "integer",
                            "required": True,
                            "description": "ID of the book request to delete"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Book request deleted successfully",
                            "schema": {"type": "string"}
                        },
                        "404": {
                            "description": "Book request not found"
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
    username_filter = request.args.get('username')
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


@app.route('/api/bookrequests', methods=['PUT'])
def update_book_request():
    """
    Handles PUT requests to update an existing book request.
    """
    data = request.get_json()
    if not isinstance(data, dict) or 'id' not in data:
        return jsonify({"error": "A valid book request with an 'id' is required."}), 400

    for book_request in book_requests:
        if book_request['id'] == data['id']:
            book_request.update(data)
            return jsonify({"message": "Book request updated successfully"}), 200

    return jsonify({"error": "Book request not found"}), 404


@app.route('/api/bookrequests', methods=['DELETE'])
def delete_book_request():
    """
    Handles DELETE requests to remove a book request by ID.
    """
    id_filter = request.args.get('id')
    if not id_filter:
        return jsonify({"error": "ID parameter is required."}), 400

    global book_requests
    book_requests = [br for br in book_requests if str(br.get('id')) != id_filter]

    return jsonify({"message": "Book request deleted successfully"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
