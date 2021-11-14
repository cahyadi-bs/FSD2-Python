from flask import Flask, jsonify, request
# Html Escaping
from markupsafe import escape
# HTTP Method
from flask import request
# URL Building
from flask import url_for
# Rendering Templates
from flask import render_template

from author_book import author_book

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# Html Escaping
# using escape()
# <name> in router capture a value from the URL
@app.route("/<name>")
def helloEscape(name):
    return f"Hello, {escape(name)}!"

# Routing
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

# Variable Rule
@app.route('/user/<username>')
def showUserProfile(username):
    # show the user profile for that user
    return f"User {escape(username)}"

@app.route('/post/<int:postId>')
def showPost(postId):
    # show the post with the given id, the id is an integer
    return f"Post {postId}"

@app.route('/path/<path:subpath>')
def showSubpath(subpath):
    # show the subpath after /path/
    return f"Subpath {escape(subpath)}"

'''
    <int:postId> ==> berarti menggunakan converter untuk menspesifikasikan variable tersebut hanya menerima tipe tertentu
    format = <converter:variableName>

    jenis konverter
    1. string => (default) text tanpa slash (path)
    2. int => integer positif
    3. float => positif floating point
    4. path => seperti string tapi termasuk slash
    5. uuid => menerima string UUID

    bila converter tidak terpenuhi maka akan masuk ke page 404
    Ex. converter yang digunakan int tapi memasukkan string/path ke URL maka akan diarahkan ke 404
'''

# HTTP Method
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


# Static File
# Static file seperti file CSS dan Javascript
# format : url_for('{NAMA_FOLDER}', filename='{NAMA_FILE}')
# url_for('static', filename='style.css')

# Rendering Template
# untuk render template dapat menggunakan render_template()
@app.route('/hello/')
@app.route('/hello/<name>')
def helloTemplate(name=None):
    return render_template('hello.html', name=name)

@app.route('/post/')
def getPost():
    data = [
        {
            "title" : "Title 1",
            "body" : "This is a Body"
        },
        {
            "title" : "Title 2",
            "body" : "This is a Body"
        },
        {
            "title" : "Title 3",
            "body" : "This is a Body"
        },
        {
            "title" : "Title 4",
            "body" : "This is a Body"
        }
    ]
    return render_template('hello.html', data = data)

@app.route('/home')
@app.route('/')
def home():
    # return 'Hello, World!'
    return render_template('index.html')

@app.route("/users", methods=['GET'])
def get_user():
    return {
        "user": "John Doe",
    }

@app.route('/foo', methods=['GET'])
def index_page():
    response = jsonify('Hello World!!!')
    response.status_code = 200

    return response


@app.route('/author', methods=['GET', 'POST'])
def author():
    if 'author_id' in request.form:
        author_book[request.form['author_id']] = []

    return render_template('author.html', author_book = author_book)

# @app.route('/books/<author_id>')
@app.route('/books/<int:author_id>')
def books(author_id):
    # html = f'List of Books authored by {author_id}:'
    # html += '<ul> <li>intro to lyfe</li> <li>intro to lyfe 2</li> <li>intro to lye3</li></ul>'
    # return html
    # return render_template('book.html', template_var_author=author_id)
    # if author_id != 400:
    if len(author_book[author_id]) == 0:
        return render_template('book.html', author_id=author_id)
    else:
        return render_template('book.html', author_id=author_id, book_list=author_book[author_id])
    
    # return render_template('book.html', author_id=author_id, book_list=author_book[author_id])
    # return render_template('book.html', author_id=author_id)

# Request
# @app.route('/api', methods = ['POST', 'GET'])
# def api():
#     if request.method == 'POST':
#         data = [
#             {
#                 'username': request.form['username'],
#                 'password': request.form['password']
#             }
#         ]
#         return data,200


if __name__ == '__main__':
    # webbrowser.open_new('http://127.0.0.1:5000/')
    app.run(debug=True)