import pandas as pd

# load cleaned data
df = pd.read_csv("cleaned_master_stock_data.csv")

# create pivot table
pivot_df = df.pivot(index='date',columns='ticker',values='close')

# calculate correlation
correlation_matrix = pivot_df.corr()

# print output
print("\nCORRELATION MATRIX")
print(correlation_matrix)

# save csv
correlation_matrix.to_csv("stock_correlation_matrix.csv")

print("\nCorrelation Analysis Completed Successfully")