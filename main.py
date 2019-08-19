import plotly as py
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime



#API control
#py.tools.set_credentials_file(username='hansenchan', api_key='pLrGADI5iTzoCQOpZFRp')

#Data feed needed
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

trace = go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])
data = [trace]

fig=go.Figure(data)

fig.layout.update(
    title='Backtest Result',
    yaxis_title='AAPL Stock',
    shapes = [dict(
        x0='2016-12-09', x1='2016-12-09', y0=0, y1=1, xref='x', yref='paper',
        line_width=2),
        dict(
        x0='2017-02-02', x1='2017-02-02', y0=0, y1=1, xref='x', yref='paper',
        line_width=2)
    ],
    annotations=[dict(
        x='2016-12-09', y=0.05, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Buy Close Price'),
        dict(
        x='2017-02-02', y=0.05, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Sell Close Price')
    ]
)


py.offline.init_notebook_mode(connected=True)

#html file rename needed
py.offline.plot(fig, auto_open=True)
