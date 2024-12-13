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
        return jsonify({"error": "Input should be a list of book requests"}), 400

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


if __name__ == '__main__':
    app.run(debug=True)
