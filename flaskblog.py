from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config['SECRET_KEY'] = '93634a0c5bba68ecd50c3bcb2ef47bf9'

posts = [
    {
        'author': 'Mojo Dojo',
        'title': 'The Art of Code',
        'content': 'Coding is an artform as you put together different elements to build a website.',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Meila Feila',
        'title': 'The Sus Chronicles',
        'content': 'Did you vent? I saw you vent and lurk around medbay.',
        'date_posted': 'April 25, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
