import plotly as py
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime

#py.tools.set_credentials_file(username='hansenchan', api_key='pLrGADI5iTzoCQOpZFRp')


#top = tk.Tk()
#top.mainloop()
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

trace = go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])
data = [trace]

py.offline.init_notebook_mode(connected=True)

py.offline.plot(data, auto_open=True)
