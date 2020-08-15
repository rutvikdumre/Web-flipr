import pandas as pd
import matplotlib.pyplot as plt

def popup(choice):
    nse= pd.read_csv('Data/NSE (Nifty).csv')
    bse= pd.read_csv('Data/BSE (Sensex).csv')
    nse_today=nse.loc[nse['Date'] == '2020-08-13']
    
    if(choice=='SENSEX'):
        dates=list(bse['Date'])
        dates.sort()
        bse_today=bse.loc[bse['Date'] == bse['Date'].max()]
        yest=bse.loc[bse['Date'] == dates[-1]]
        open=("{:.2f}".format(float(bse_today['Open'])))
        close=("{:.2f}".format(float(yest['Close'])))
        
        dayl=("{:.2f}".format(float(bse_today['Low'])))
        dayh=("{:.2f}".format(float(bse_today['High'])))
        weekl=("{:.2f}".format(float(bse['Low'].min())))
        weekh=("{:.2f}".format(float(bse['High'].max())))
        date=nse['Date'].max()
        return [open,close,dayl,dayh,weekl,weekh,date]
    if(choice=='NIFTY 50'):
        dates=list(nse['Date'])
        dates.sort()
        nse_today=nse.loc[nse['Date'] == nse['Date'].max()]
        yest=bse.loc[bse['Date'] == dates[-1]]
        open=("{:.2f}".format(float(nse_today['Open'])))
        close=("{:.2f}".format(float(yest['Close'])))
        
        dayl=("{:.2f}".format(float(nse_today['Low'])))
        dayh=("{:.2f}".format(float(nse_today['High'])))
        weekl=("{:.2f}".format(float(nse['Low'].min())))
        weekh=("{:.2f}".format(float(nse['High'].max())))
        date=bse['Date'].max()
        return [open,close,dayl,dayh,weekl,weekh,date]
def plot(company):
    df= pd.read_csv("Data/"+company+".csv")
    plt.plot(df['Date'], df['Open'], df['Close'])
    plt.ylabel('Price')
    plt.xlabel('Time')
    plt.savefig('static/{}.png'.format(company), transparent=True)
    
    
def all():
    l=['ASHOKLEY.NS','CIPLA.NS','EICHERMOT.NS','RELIANCE.NS','TATASTEEL.NS']
    for i in l:
        plot(i)
def info(company):
    df= pd.read_csv("Data/"+company+".csv")
    today= df.loc[df['Date'] == df['Date'].max()]
    return ["{:.2f}".format(float(today['Low'])),"{:.2f}".format(float(today['High']))]