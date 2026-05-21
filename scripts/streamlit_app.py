import streamlit as st
import pandas as pd
import mysql.connector


st.set_page_config(
    page_title="Stock Market Analysis",
    layout="wide"
)

# database connection
@st.cache_resource
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        password="",
        database="stock_market_analysis"
    )

connection = connect_db()

# sidebar navigation
st.sidebar.title("Page selector")

page = st.sidebar.selectbox("",["Market Overview","Volatility Analysis","Sector Analysis","SQL Analysis"])

# MARKET OVERVIEW PAGE
if page == "Market Overview":

    st.title("Market Overview")

    yearly_returns = pd.read_sql("SELECT * FROM yearly_returns",connection)

    stock_data = pd.read_sql("SELECT * FROM stock_data",connection)

    # top gainers
    top_gainers = yearly_returns.sort_values(by='yearly_return_percent',ascending=False).head(10)

    # top losers
    top_losers = yearly_returns.sort_values(by='yearly_return_percent',ascending=True).head(10)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top 10 Gainers")
        st.bar_chart(top_gainers.set_index('ticker')['yearly_return_percent'])

    with col2:
        st.subheader("Top 10 Losers")
        st.bar_chart(top_losers.set_index('ticker')['yearly_return_percent'])

    # KPI metrics
    avg_close = stock_data['close'].mean()
    avg_volume = stock_data['volume'].mean()

    green_stocks = len(yearly_returns[yearly_returns['yearly_return_percent'] > 0])

    red_stocks = len(yearly_returns[yearly_returns['yearly_return_percent'] < 0])

    st.subheader("Market Summary")

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    kpi1.metric("Green Stocks", green_stocks)
    kpi2.metric("Red Stocks", red_stocks)
    kpi3.metric("Average Close Price", f"{avg_close:.2f}")
    kpi4.metric("Average Volume", f"{avg_volume:.2f}")

# VOLATILITY ANALYSIS PAGE
elif page == "Volatility Analysis":

    st.title("Volatility Analysis")

    volatility_df = pd.read_sql("SELECT * FROM volatility_data",connection)

    top_volatile = volatility_df.sort_values(by='volatility',ascending=False).head(10)

    st.bar_chart(top_volatile.set_index('ticker')['volatility'])

# SECTOR ANALYSIS PAGE
elif page == "Sector Analysis":

    st.title("Sector Performance")

    sector_df = pd.read_sql("SELECT * FROM sector_performance",connection)

    st.bar_chart(sector_df.set_index('sector')['yearly_return_percent'])

# SQL ANALYSIS PAGE
elif page == "SQL Analysis":

    st.title("SQL Query Analysis")

    query_option = st.selectbox("Choose Query",["Top 5 Gainers","Top 5 Losers"])

    cursor = connection.cursor()

    if query_option == "Top 5 Gainers":

        query = """
        SELECT ticker, yearly_return_percent
        FROM yearly_returns
        ORDER BY yearly_return_percent DESC
        LIMIT 5
        """

        result = pd.read_sql(query, connection)

        st.dataframe(result)

    elif query_option == "Top 5 Losers":

        query = """
        SELECT ticker, yearly_return_percent
        FROM yearly_returns
        ORDER BY yearly_return_percent ASC
        LIMIT 5
        """

        result = pd.read_sql(query, connection)

        st.dataframe(result)