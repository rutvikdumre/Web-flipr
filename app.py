from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method=='POST':
        c=request.form.get('choice')
        return render_template('mainpage.html', choice=c)
    else:
        return render_template('mainpage.html', choice="NIFTY")

if __name__ == '__main__':
    app.run(debug=True)
    