from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('mainpage.html')

if __name__ == '__main__':
    app.run()