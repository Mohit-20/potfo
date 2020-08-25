from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


def database(data):
    with open('database.txt', mode = 'a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')
def database_csv(data):
    with open('database.csv', mode = 'a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_file = csv.writer(database2,  delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email, subject, message])

@app.route('/<string:post_id>')
def post(post_id):
    return render_template(post_id)



@app.route('/')
def my_home():
    return render_template('./index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def form_submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        database_csv(data)
        return redirect('./redirect.html')
    else:
        return 'Try again'



# @app.route('/index.html')
# def index():
#     return render_template('./index.html')

# @app.route('/about.html')
# def about():
#     return render_template('./about.html')

# @app.route('/works.html')
# def works():
#     return render_template('./works.html')

# @app.route('/work.html')
# def work():
#     return render_template('./work.html')

# @app.route('/components.html')
# def components():
#     return render_template('./components.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('./contact.html')



# @app.route('/main.html')
# def hello_world2():
#     return render_template('./main2.html')

# @app.route('/blog/dogs')
# def blog2():
#     return 'This is my first blog on DOGS!!!!'

# @app.route('/<username>')
# def username(username = None):
#     return render_template('./main.html', name = username)

# @app.route('/<int:post_id>')
# def post(post_id = None):
#     return render_template('./main.html',post = post_id)

# @app.route('/favicon.ico')
# def blog():
#     return 'This is my first blog'

# py -3 -m venv venv
# venv\Scripts\activate
# $env:FLASK_APP = "hello.py"
# venv\scripts\flask run