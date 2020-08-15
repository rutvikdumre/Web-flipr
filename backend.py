import pandas as pd
nse= pd.read_csv('Data/NSE (Nifty).csv')
bse= pd.read_csv('Data/BSE (Sensex).csv')
nse_today=nse.loc[nse['Date'] == '2020-08-13']
bse_today=bse.loc[bse['Date'] == '2020-08-13']
print(nse_today)
print(bse_today)