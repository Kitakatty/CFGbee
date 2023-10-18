from flask import Flask, jsonify, request
from books_data import books
# from utils import search_flight, get_index

app = Flask(__name__)

@app.route('/')
def welcome():
    return """
       <html>
         <head>
           <title>Welcome to  <link>Cobb's Cosy Corner</link></title>
           <style>
             body {
               background-color: #E0D2C7;
               font-family: Poor Richard, sans-serif;
               margin: 0;
               padding: 50px;
               text-align: center;
             }
             h1 {
               color: #B38575;
               font-size: 32px;
               margin-bottom: 20px;
             }
             p {
               color: #9c5d41;
               font-size: 22px;
               margin-bottom: 20px;
             }
            
           </style>
         </head>
         <body>
           <h1>Welcome to  <link>Cobb's Cosy Corner</link>!</h1>
           <p>Explore our collection of books, search by genre or author, and place orders.</p>
           <p>Come in and explore the wonders of books.</p>
         </body>
       </html>
       """


# Endpoint to get all books
@app.route('/books', methods=['GET'])
def get_books():
    # Code to read the book information from the file

    # Return the book information as a JSON response
    return jsonify(books)


    # Return the book information as a JSON response
    return jsonify(books)

# Endpoint to get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({'message': 'Book not found'}), 404
    return jsonify({'book': book})

# Endpoint to create a new book
# @app.route('/books', methods=['POST'])
# def create_book():
#     data = request.get_json()
#     new_book = {
#         'id': len(books) + 1,
#         'title': data['title'],
#         'author': data['author']
#     }
#     books.append(new_book)
#     return jsonify({'message': 'Book created', 'book': new_book}), 201
#
# # Endpoint to update a book by ID
# @app.route('/books/<int:book_id>', methods=['PUT'])
# def update_book(book_id):
#     data = request.get_json()
#     book = next((book for book in books if book['id'] == book_id), None)
#     if book is None:
#         return jsonify({'message': 'Book not found'}), 404
#     book['title'] = data['title']
#     book['author'] = data['author']
#     return jsonify({'message': 'Book updated', 'book': book})
#
# # Endpoint to delete a book by ID
# @app.route('/books/<int:book_id>', methods=['DELETE'])
# def delete_book(book_id):
#     global books
#     books = [book for book in books if book['id'] != book_id]
#     return jsonify({'message': 'Book deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
