import pandas as pd

df = pd.read_csv("cleaned_master_stock_data.csv")
# convert date // because whatever we cleaned it in previous importing csv again the date will show str
df['date'] = pd.to_datetime(df['date'])
stock_returns = []

grouped = df.groupby('ticker')

for ticker, stock_data in grouped:

    first_close = stock_data.iloc[0]['close']

    last_close = stock_data.iloc[-1]['close']

    yearly_return = ((last_close - first_close) / first_close) * 100

    stock_returns.append({
        'ticker': ticker,
        'first_close': first_close,
        'last_close': last_close,
        'yearly_return_percent': yearly_return
    })


returns_df = pd.DataFrame(stock_returns)

# top gainers
top_gainers = returns_df.sort_values(by='yearly_return_percent',ascending=False).head(10)

# top losers
top_losers = returns_df.sort_values(by='yearly_return_percent').head(10)

# market summary
green_stocks = (returns_df['yearly_return_percent'] > 0).sum()
red_stocks = (returns_df['yearly_return_percent'] < 0).sum()
average_close_price = df['close'].mean()
average_volume = df['volume'].mean()

print("\nTOP 10 GAINERS")
print(top_gainers)

print("\nTOP 10 LOSERS")
print(top_losers)

print("\nMARKET SUMMARY")
print(f"Green Stocks : {green_stocks}")
print(f"Red Stocks   : {red_stocks}")
print(f"Average Close Price : {average_close_price:.2f}")
print(f"Average Volume : {average_volume:.2f}")

returns_df.to_csv("yearly_stock_returns_1.csv", index=False)

top_gainers.to_csv("top_10_gainers.csv_1", index=False)

top_losers.to_csv("top_10_losers.csv_1", index=False)
