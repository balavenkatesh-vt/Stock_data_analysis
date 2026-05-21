import pandas as pd

returns_df = pd.read_csv("yearly_stock_returns_1.csv")
sector_df = pd.read_csv("cleaned_sector_data.csv")

# clean ticker values
sector_df['ticker'] = sector_df['ticker'].str.split(':').str[-1]

returns_df['ticker'] = returns_df['ticker'].str.strip().str.lower()
sector_df['ticker'] = sector_df['ticker'].str.strip().str.lower()

# merge datasets
merged_df = pd.merge(returns_df,sector_df,on='ticker')

# sector performance
sector_performance = merged_df.groupby('sector')['yearly_return_percent'].mean().reset_index()

# sort values
sector_performance = sector_performance.sort_values(by='yearly_return_percent',ascending=False)

# print output
print("\nSECTOR PERFORMANCE")
print(sector_performance)

# save csv
sector_performance.to_csv("sector_performance.csv",index=False)

print("\nSector Analysis Completed Successfully")