from flask import Flask, request, redirect, url_for, render_template
from backend import popup,info
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method=='POST':
        c=request.form.get('choice')
        open,close,dayl,dayh,weekl,weekh,date=popup(c)
        return render_template('mainpage.html', choice=c,open=open,close= close,dayl=dayl,dayh=dayh,weekl=weekl,weekh=weekh,date=date)   
    else:
        open,close,dayl,dayh,weekl,weekh,date=popup("NIFTY 50")
        return render_template('mainpage.html', choice="NIFTY 50",open=open,close= close,dayl=dayl,dayh=dayh,weekl=weekl,weekh=weekh,date=date)
@app.route('/company', methods=['GET', 'POST'])
def company():
    if request.method=='POST':
        company=request.form.get('company')
        clow,chigh=info(company)
        c="static/{}.png".format(company)
        return render_template('company.html', clow=clow,chigh=chigh,company=c)
    company='ASHOKLEY.NS'
    clow,chigh=info(company)
    c="static/{}.png".format(company)
    return render_template('company.html', clow=clow,chigh=chigh,company=c)

if __name__ == '__main__':
    app.run(debug=True)
    