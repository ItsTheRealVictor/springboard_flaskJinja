from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is just a demo'
app.debug = True
toolbar = DebugToolbarExtension(app)


@app.route('/')
def mainPage():
    return 'Its the main page'

@app.route('/form')
def show_form():
    return render_template('form.html')

@app.route('/greet')
def show_greeting():
    name = request.args['username']
    return render_template('greet.html', username=name)


if __name__ == '__main__':
    app.run(debug=True)