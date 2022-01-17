#flask
from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def Home():
    return render_template('index.html')

#root vers about.html
@app.route('/about')
def About():
    return render_template('about.html')

#root vers contact.html
@app.route('/contact')
def Contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
