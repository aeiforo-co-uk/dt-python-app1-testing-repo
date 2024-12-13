from flask import Flask, request, jsonify
from flasgger import Swagger
import uuid

app = Flask(__name__)
swagger = Swagger(app)

# Simulate a simple in-memory database for the book requests
book_requests_db = {}

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

@app.route('/api/bookrequests', methods=['GET'])
def get_all_book_requests():
    """
    Get all book requests.
    ---
    tags:
      - Book Request Service
    responses:
      200:
        description: List of all book requests
        content:
          application/json:
            schema:
              type: array
              items:
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
    """
    all_requests = [
        {"book_request_id": book_request_id, **data}
        for book_request_id, data in book_requests_db.items()
    ]
    return jsonify(all_requests), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
