from flask import Flask, jsonify, request
# Html Escaping
from markupsafe import escape
# HTTP Method
from flask import request
# URL Building
from flask import url_for
# Rendering Templates
from flask import render_template

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


@app.route("/users", methods=['GET'])
def get_user():
    return {
        "user": "John Doe",
    }

@app.route('/fdoo', methods=['GET'])
def index_page():
    response = jsonify('Hello World!!!')
    response.status_code = 200

    return response


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
    app.run(debug=True)