import pandas as pd

df = pd.read_csv("cleaned_master_stock_data.csv")

# convert date
df['date'] = pd.to_datetime(df['date'])

# calculate daily returns
df['daily_return'] = df.groupby('ticker')['close'].pct_change()

# calculate cumulative return
df['cumulative_return'] = (1 + df['daily_return']).groupby(df['ticker']).cumprod() - 1

# latest cumulative return for each stock
latest_returns = df.groupby('ticker').last().reset_index()

# top 5 performing stocks
top_5 = latest_returns.sort_values(by='cumulative_return',ascending=False).head(5)

print("\nTOP 5 CUMULATIVE RETURN STOCKS")
print(top_5[['ticker', 'cumulative_return']])

df.to_csv("cumulative_return_data.csv", index=False)

top_5.to_csv("top_5_cumulative_return.csv", index=False)

print("\nCumulative Return Analysis Completed Successfully")