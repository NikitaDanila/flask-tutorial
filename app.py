from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Nikita',
        'title': 'title 1',
        'content': 'First 1',
        'date': 'April 1'
    },
    {
        'author': 'Nikita',
        'title': 'title 2',
        'content': 'First 2',
        'date': 'April 2'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')
