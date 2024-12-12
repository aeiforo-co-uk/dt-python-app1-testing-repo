from flask import Flask, request, jsonify
from flasgger import Swagger
import uuid

app = Flask(__name__)
swagger = Swagger(app)

# Simulate a simple in-memory database for the book requests
book_requests_db = {}

@app.route('/api/greet', methods=['GET'])
def greet_user():
    """
    A simple greeting API.
    ---
    tags:
      - Greeting Service
    responses:
      200:
        description: A greeting message
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: 'Hello, User!'
    """
    return {"message": "Hello, User!"}

@app.route('/api/data', methods=['POST'])
def post_data():
    """
    An API endpoint to post some data.
    ---
    tags:
      - Data Service
    parameters:
      - name: name
        in: query
        type: string
        required: true
        description: The name of the user
    responses:
      200:
        description: Data received successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                status:
                  type: string
                  example: 'Data received'
    """
    name = request.args.get('name')
    return {"status": "Data received", "name": name}

@app.route('/api/data', methods=['PUT'])
def put_data():
    """
    An API endpoint to update some data.
    ---
    tags:
      - Data Service
    parameters:
      - name: name
        in: query
        type: string
        required: true
        description: The name of the user to update
      - name: new_name
        in: query
        type: string
        required: true
        description: The new name of the user
    responses:
      200:
        description: Data updated successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                status:
                  type: string
                  example: 'Data updated'
                old_name:
                  type: string
                  example: 'Old Name'
                new_name:
                  type: string
                  example: 'New Name'
    """
    old_name = request.args.get('name')
    new_name = request.args.get('new_name')
    return {"status": "Data updated", "old_name": old_name, "new_name": new_name}

@app.route('/api/data', methods=['DELETE'])
def delete_data():
    """
    An API endpoint to delete some data.
    ---
    tags:
      - Data Service
    parameters:
      - name: name
        in: query
        type: string
        required: true
        description: The name of the user to delete
    responses:
      200:
        description: Data deleted successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                status:
                  type: string
                  example: 'Data deleted'
                name:
                  type: string
                  example: 'Name'
    """
    name = request.args.get('name')
    return {"status": "Data deleted", "name": name}

@app.route('/api/bookrequests', methods=['POST'])
def create_book_request():
    """
    An API endpoint to create a new book request.
    ---
    tags:
      - Book Request Service
    requestBody:
      description: Request body for creating a new book request
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              title:
                type: string
                example: 'The Great Gatsby'
              author:
                type: string
                example: 'F. Scott Fitzgerald'
              user_id:
                type: string
                example: '123e4567-e89b-12d3-a456-426614174000'
            required:
              - title
              - author
              - user_id
    responses:
      200:
        description: Book request created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                status:
                  type: string
                  example: 'Book request created'
                book_request_id:
                  type: string
                  example: '123e4567-e89b-12d3-a456-426614174001'
    """
    data = request.get_json()
    book_request_id = str(uuid.uuid4())
    book_requests_db[book_request_id] = data
    return jsonify({
        "status": "Book request created",
        "book_request_id": book_request_id
    }), 200

@app.route('/api/bookrequests/<book_request_id>', methods=['GET'])
def get_book_request(book_request_id):
    """
    Get a book request by its ID.
    ---
    tags:
      - Book Request Service
    parameters:
      - name: book_request_id
        in: path
        required: true
        description: The ID of the book request
        schema:
          type: string
    responses:
      200:
        description: A book request
        content:
          application/json:
            schema:
              type: object
              properties:
                book_request_id:
                  type: string
                  example: '123e4567-e89b-12d3-a456-426614174001'
                title:
                  type: string
                  example: 'The Great Gatsby'
                author:
                  type: string
                  example: 'F. Scott Fitzgerald'
                user_id:
                  type: string
                  example: '123e4567-e89b-12d3-a456-426614174000'
      404:
        description: Book request not found
    """
    book_request = book_requests_db.get(book_request_id)
    if book_request:
        return jsonify(book_request), 200
    return jsonify({"status": "Book request not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
