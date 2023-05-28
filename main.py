import pandas as pd
import yfinance as yf
import streamlit as st
import warnings
warnings.filterwarnings('ignore')


st.sidebar.write("""
# PROVIDE INFORMATION ABOUT YOUR STOCK
""")
selected_stock_ticker = st.sidebar.text_input('Enter Your Ticker(for eg: google -> GOOGL):', "AAPL")
ticker = selected_stock_ticker.upper()
selected_years = st.sidebar.slider("Select the year", 2010, 2020, 2010)
st.sidebar.write('you selected:', selected_years)
st.title(f"STOCKS OF {ticker} FOR THE YEAR {selected_years}")
start_date = str(selected_years) + "-1-1"
end_date = str(selected_years) + '-12-31'
Ticker_data = yf.Ticker(ticker).history(period='1d', start=start_date, end=end_date)
st.write('### Closing Price')

st.line_chart(Ticker_data.Close)

st.write('### Volume')

st.line_chart(Ticker_data.Volume)

stocks_bought = int(st.sidebar.text_input("Enter The Number Of Stocks", "10"))
buy_yr = str(st.sidebar.slider("Select the year of buying", 2010, 2020, 2010))
sell_yr = str(st.sidebar.slider("Select the year of selling", 2010, 2020, 2010))
try:
    ticker_data_return = yf.Ticker(ticker).history(ticker, start=buy_yr + "-1-1", end=sell_yr + "-12-31")
    Open_price = ticker_data_return['Open'].values[0]
    Close_price = int(ticker_data_return['Close'].values[0])
    return_of_stock = ((Close_price - Open_price) * stocks_bought) + Open_price
    st.sidebar.write(f"your returns: {return_of_stock}")
    print(Open_price, Close_price)
except IndexError:
    st.sidebar.write("Sorry no data available for the selected time")