import numpy as np
import pandas as pd 
import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import plotly.express as px

# Function to fetch historical data
def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Function to calculate moving averages
def calculate_moving_averages(df, days):
    return df['Close'].rolling(window=days).mean()

# Function to get stock data for sectorial comparision
def get_data(tickers):
    data = yf.download(tickers, period=time_frame)
    return data['Close']

def get_data_change(tickers, time_frame):
    data = yf.download(tickers, period=time_frame)['Close']
    # Calculate percent return
    percent_return = data.pct_change().fillna(0)
    return percent_return

# Streamlit page configuration
st.set_page_config(page_title="US Market Analysis: Dow Jones Index", layout="wide", initial_sidebar_state="collapsed")

# Header
st.header("US Stock Market Analysis: Dow Jones Index")
#st.write(" ")
st.write(" ")
st.markdown('<div style="text-align: justify; text-justify: inter-word;">Welcome to the thrilling world of the Dow Jones Industrial Average, where finance meets excitement and Wall Street is the stage! Picture this: a venerable index with a history dating back to 1896, born from the minds of Charles Dow and Edward Jones, titans of the financial realm.</div>', unsafe_allow_html=True)

st.write(" ")
st.subheader('The Dow Dancefloor: Grooving with the Big 30')
st.markdown('<div style="text-align: justify; text-justify: inter-word;">So, what\'s the Dow all about? It\'s like assembling the Avengers of the stock market - 30 powerhouse companies, flexing their financial muscles in the limelight. These giants, spanning sectors from industrials to healthcare, are the A-listers, the rockstars, and the trendsetters of the U.S. stock market. Their moves? Well, they dictate the rhythm of the market, painting a vivid picture of its overall health and vigor.</div>', unsafe_allow_html=True)

st.write(" ")
st.subheader('Behind the Scenes: Dow\'s Unique Beat')
st.markdown('<div style="text-align: justify; text-justify: inter-word;">Now, here\'s where it gets interesting. The Dow Jones Industrial Average isn\'t your run-of-the-mill index; it\'s a maverick. While others play the market cap game, the Dow prefers a different tune. It\'s a "price-weighted" index, meaning the big shots are judged by their stock prices, not their market cap. Imagine a musical where the lead actor\'s salary determines their stage time - that\'s the Dow\'s world. And oh, does it add a dash of suspense to the market saga!</div>', unsafe_allow_html=True)

st.write(" ")
st.subheader('Curtain Call: Meet the Dow Jones\'s Star-Studded Cast')
st.markdown('<div style="text-align: justify; text-justify: inter-word;">Let\'s dim the lights and present to you the headliners, the Dow Jones\'s elite ensemble:</div>', unsafe_allow_html=True)
st.write(" ")
st.markdown("1. MMM - 3M Company (Industrial)\n 2. AXP - American Express Company (Finance)\n 3. AMGN - Amgen Inc. (Healthcare)\n 4. AAPL - Apple Inc. (Information Technology)\n 5. BA - Boeing Company (Industrial)\n 6. CAT - Caterpillar Inc. (Industrial)\n 7. CVX - Chevron Corporation (Energy)\n 8. CSCO - Cisco Systems, Inc. (Information Technolgy)\n 9. KO - Coca-Cola Company (Consumer)\n 10. DOW - Dow Inc. (Industrial)\n 11. GS - Goldman Sachs Group, Inc. (Finance)\n 12. HD - The Home Depot, Inc. (Consumer)\n 13. HON - Honeywell International Inc. (Industrial)\n 14. IBM - International Business Machines Corporation (Information Technolgy)\n 15. INTC - Intel Corporation (Information Technology)\n 16. JNJ - Johnson & Johnson (Finance)\n 17. JPM - JPMorgan Chase & Co. (Finance)\n 18. MCD - McDonald's Corporation (Consumer)\n 19. MRK - Merck & Co., Inc. (Healthcare)\n 20. MSFT - Microsoft Corporation (Information Technology)\n 21. NKE - Nike, Inc. (Consumer)\n 22. PG - Procter & Gamble Company (Consumer)\n 23. CRM - Salesforce.com, Inc. (Information Technology)\n 24. TRV - The Travelers Companies, Inc. (Finance)\n 25. UHN - UnitedHealth Group Incorporated (Healthcare)\n 26. VZ - Verizon Communications Inc. (Communication)\n 27. V - Visa Inc. (Information Technology)\n 28. WBA - Walgreens Boots Alliance, Inc. (Consumer)\n 29. WMT - Walmart Inc. (Consumer)\n 30. DIS - The Walt Disney Company (Entertainment)")

st.write(" ")
st.subheader('Market Capitalization by Sector')
df_tm = pd.read_excel('Dows_Jone_Companies_List.xlsx')
#df_tm['hover_text'] = df_tm.apply(lambda x: f"Ticker: {x['ticker']}<br>Sector: {x['sector']}<br>Price: ${x['price']}<br>Market Cap: ${x['marketcap']}", axis=1)

# Treemap Plot
fig = px.treemap(df_tm, path=['sector', 'ticker'], values='marketcap', 
                 color='marketcap', hover_data={'marketcap': False, 'delta': False},
                 custom_data=['ticker', 'sector', 'marketcap', 'delta'], 
                 color_continuous_scale='RdYlGn',
                 title="Treemap of Companies in the Dow Jones Index")
fig.update_traces(hovertemplate='Company: %{customdata[0]}<br>Sector: %{customdata[1]}<br>Market Cap: %{customdata[2]}<br>Delta: %{customdata[3]}')
# Display Treemap
st.plotly_chart(fig, use_container_width=True)
st.markdown('<div style="text-align: justify; text-justify: inter-word;">Welcome to our financial jungle! Picture a digital canopy where sectors are ecosystems. Each sector—IT, Consumer, Healthcare, Financials, Industrial, Energy, Entertainment, Communication—is a distinct realm.</div>', unsafe_allow_html=True)
st.write(" ")
st.markdown('<div style="text-align: justify; text-justify: inter-word;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>• IT Rainforest:</b> Apple, Cisco, Intel, Microsoft, Visa dominate, visually representing their weightage in tech.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify; text-justify: inter-word;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>• Consumer Meadows:</b> Coca-Cola, McDonald\'s, Nike, P&G, Walmart grace the landscape, their sizes mirroring market impact.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify; text-justify: inter-word;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>• Healthcare Heights:</b> Amgen, J&J, Merck, UnitedHealth tower with significance.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify; text-justify: inter-word;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>• Financial Foothills:</b> American Express, Goldman Sachs, JPMorgan stand tall, their rectangles illustrating economic influence.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify; text-justify: inter-word;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>• Industrial Valleys:</b> Boeing, Caterpillar, Dow Inc. shape the landscape with industrial strength.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify; text-justify: inter-word;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>• Energy Deserts:</b> Chevron stands tall, its rectangle reflecting energy sector significance.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify; text-justify: inter-word;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>• Entertainment Oasis:</b> Disney casts its magical spell in the oasis of entertainment.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify; text-justify: inter-word;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>• Communication Corners:</b> Verizon speaks volumes in the communication sector.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify; text-justify: inter-word;"></div>', unsafe_allow_html=True)
st.write(" ")
st.write(" ")
st.subheader("Moving Average Plot for Dow Jones Companies")

company_list = [
    "AAPL", "AXP", "AMGN", "BA", "CAT", "CSCO", "CVX", "CRM", "DIS", "DOW", "GS", "HD", 
    "HON", "IBM", "INTC", "JNJ", "JPM", "KO", "MCD", "MMM", "MRK", "MSFT", "NKE", 
    "PG", "TRV", "UNH", "V", "VZ", "WBA", "WMT"
]
selected_companies = st.multiselect('Select Companies', company_list, default=['AAPL'])
# Date range picker
start_date, end_date = st.select_slider(
    "Select Date Range",
    options=pd.date_range("2020-01-01", "2023-12-07", freq='D'),
    value=(pd.Timestamp("2022-01-01"), pd.Timestamp("2023-12-07"))
)
# Plotting
if selected_companies:
    fig = go.Figure()
    for ticker in selected_companies:
        stock_data = get_stock_data(ticker, start_date, end_date)
        ma20 = calculate_moving_averages(stock_data, 20)
        ma50 = calculate_moving_averages(stock_data, 50)
        ma100 = calculate_moving_averages(stock_data, 100)

        fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name=f'{ticker} Close'))
        fig.add_trace(go.Scatter(x=ma20.index, y=ma20, mode='lines', name=f'{ticker} 20-Day MA'))
        fig.add_trace(go.Scatter(x=ma50.index, y=ma50, mode='lines', name=f'{ticker} 50-Day MA'))
        fig.add_trace(go.Scatter(x=ma100.index, y=ma100, mode='lines', name=f'{ticker} 100-Day MA'))

    fig.update_layout(title='Stock Prices and Moving Averages', xaxis_title='Date', yaxis_title='Price')
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Sectorial Comparision")

sectors = {
    'Information Technology': ['AAPL', 'CRM', 'CSCO', 'IBM', 'INTC', 'MSFT', 'V'],
    'Healthcare': ['AMGN', 'JNJ', 'MRK', 'UNH'],
    'Financials': ['AXP', 'GS', 'JPM', 'TRV'],
    'Industrial': ['MMM', 'BA', 'CAT', 'DOW', 'HON', 'RTX'],
    'Consumer': ['KO', 'HD', 'MCD', 'NKE', 'PG', 'WBA', 'WMT'],
    'Energy': ['CVX'],
    'Communication': ['VZ'],
    'Entertainment': ['DIS']
}
# Dropdown to select the sector
sector = st.selectbox('Select a sector:', list(sectors.keys()))
time_frame = st.selectbox('Select Time Frame', ['7d', '1d', '3d', '7d', '1mo', '3mo', '6mo', '1y', '3y', '5y'])

# Get ticker symbols for the selected sector
tickers = sectors[sector]

# Fetch data
data = get_data(tickers)
data_change = get_data_change(tickers, time_frame)

# Plotting the line chart
if sector == 'Energy' or sector == 'Communication' or sector == 'Entertainment':
    fig = px.line(data, x=data.index, y='Close', labels={'value': 'Stock Price', 'variable': 'Company'})
    fig.update_layout(title=f'{sector} Sector Comparison')
    st.plotly_chart(fig, use_container_width=True)
else:
    fig = px.line(data, x=data.index, y=data.columns, labels={'value': 'Stock Price', 'variable': 'Company'})
    fig.update_layout(title=f'{sector} Sector Comparison')
    st.plotly_chart(fig, use_container_width=True)
    fig2 = px.line(data_change, x=data.index, y=data.columns, labels={'value': 'Percent Return', 'variable': 'Company'})
    fig2.update_layout(title=f'{sector} Sector % Return Comparison', xaxis_title='Date')
    st.plotly_chart(fig2, use_container_width=True)

#stock market dashboard
st.subheader("Stock Market Dashboard")
with st.sidebar:
    st.title('Dashboard')
    selected_sector = st.sidebar.selectbox('Select Sector', list(sectors.keys()))  # Placeholder for sectors
    selected_company = st.sidebar.selectbox('Select Company', sectors[selected_sector])  # List of Dow Jones companies
    chart_type = st.selectbox('Select Chart Type', ['Candlestick Chart', 'Line Chart', 'OHLC Chart'])
    time_frame = st.selectbox('Select Time Frame', ['1y', '1d', '7d', '1mo', '3mo', '6mo', '1y', '3y', '5y'])

# Fetch historical data from yfinance
data = yf.download(selected_company, period=time_frame)

# Plotting
if chart_type == 'Line Chart':
    fig = go.Figure(data=[go.Scatter(x=data.index, y=data['Close'])])
elif chart_type == 'Candlestick Chart':
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                         open=data['Open'],
                                         high=data['High'],
                                         low=data['Low'],
                                         close=data['Close'])])
elif chart_type == 'OHLC Chart':
    fig = go.Figure(data=[go.Ohlc(x=data.index,
                                  open=data['Open'],
                                  high=data['High'],
                                  low=data['Low'],
                                  close=data['Close'],
                                  name='OHLC')])

# Update layout of the chart
fig.update_layout(
    title=f'{selected_company} Share Price ({chart_type})',
    xaxis_title='Date',
    yaxis_title='Price (USD)',
    xaxis_rangeslider_visible=False
)

# Streamlit - Display the chart
st.plotly_chart(fig, use_container_width=True)
