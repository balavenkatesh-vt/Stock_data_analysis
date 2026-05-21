import pandas as pd

df = pd.read_csv("cleaned_master_stock_data.csv")

# convert date // because whatever we cleaned it in previous importing csv again the date will show str
df['date'] = pd.to_datetime(df['date'])

df['daily_return'] = df.groupby('ticker')['close'].pct_change()

volatility_df = df.groupby('ticker')['daily_return'].std().reset_index()

volatility_df.rename(columns={'daily_return': 'volatility'}, inplace=True)

# top 10 volatile stocks
top_volatile = volatility_df.sort_values(by='volatility',ascending=False).head(10)

print("\nTOP 10 MOST VOLATILE STOCKS")
print(top_volatile)

volatility_df.to_csv("stock_volatility.csv", index=False)

top_volatile.to_csv("top_10_volatile_stocks.csv", index=False)

print("\nVolatility Analysis Completed Successfully")