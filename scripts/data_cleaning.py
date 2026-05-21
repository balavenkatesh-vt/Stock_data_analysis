import pandas as pd
df = pd.read_csv("master_stock_data.csv")

print("Before Cleaning:")
print(df.shape)

# remove duplicates
# -----------------------------
duplicate_rows = df[df.duplicated()]

print("Total Duplicate Rows:", duplicate_rows.shape[0])
print(f"Rows before duplicate removal: {len(df)}")

df.drop_duplicates(inplace=True)

print(f"Rows after duplicate removal: {len(df)}")

# -----------------------------
# -----------------------------
print("Cleaning column : Ticker")
# -----------------------------
# -----------------------------
df.Ticker = df.Ticker.str.lower().str.strip()
df.Ticker = df.Ticker.str.lower().str.strip()
print(df.Ticker)
print("\nMissing Values:")
print(df.Ticker.isnull().sum())
print("\nData Types:")
print(df.Ticker.dtypes)
df = df.rename(columns = {'Ticker' : 'ticker'})
print(df.ticker)
# -----------------------------
# -----------------------------
print("\nCleaning column : close")
# -----------------------------
# -----------------------------
print("\nMissing Values:")
print(df.close.isnull().sum())
print("\nData Types:")
print(df.close.dtypes)
# -----------------------------
# -----------------------------
print("Cleaning column : date")
# -----------------------------
# -----------------------------
print("\nMissing Values:")
print(df.date.isnull().sum())
print("\nData Types:")
print(df.date.dtypes)
df.date = pd.to_datetime(df.date)
print(df.date.dtypes)
# -----------------------------
# -----------------------------
print("Cleaning column : high")
# -----------------------------
# -----------------------------
print(df.high.isnull().sum())
print("\nData Types:")
print(df.high.dtypes)
# -----------------------------
# -----------------------------
print("Cleaning column : low")
# -----------------------------
# -----------------------------
print("\nMissing Values:")
print(df.low.isnull().sum())
print("\nData Types:")
print(df.low.dtypes)
# -----------------------------
# -----------------------------
print("Cleaning column : month")
# -----------------------------
# -----------------------------
print("\nMissing Values:")
print(df.month.isnull().sum())
print("\nData Types:")
print(df.month.dtypes)
# -----------------------------
# -----------------------------
print("Cleaning column : open")
# -----------------------------
# -----------------------------
print("\nMissing Values:")
print(df.open.isnull().sum())
print("\nData Types:")
print(df.open.dtypes)
# -----------------------------
# -----------------------------
print("Cleaning column : volume")
# -----------------------------
# -----------------------------
print("Cleaning column : volume")
print("\nMissing Values:")
print(df.volume.isnull().sum())
print("\nData Types:")
print(df.volume.dtypes)
# -----------------------------
# -----------------------------
print("sorting both columns ticker and date")
# -----------------------------
# -----------------------------
df = df.sort_values(by=['ticker', 'date'])
# -----------------------------
# -----------------------------
print("reordering the index")
# -----------------------------
# -----------------------------
df.reset_index(drop=True, inplace=True)
# -----------------------------
# save cleaned data
# -----------------------------
df.to_csv("cleaned_master_stock_data.csv", index=False)
print("\nAfter Cleaning:")
print(df.shape)
print("\nCleaning Completed Successfully")