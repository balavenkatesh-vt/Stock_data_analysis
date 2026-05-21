import pandas as pd
import os
df = pd.read_csv("cleaned_master_stock_data.csv")
final_folder = "50_stock_csv_files"

os.makedirs(final_folder, exist_ok=True)

grouped = df.groupby("ticker")

for ticker, stock_data in grouped:

    file_name = f"{ticker}.csv"

    file_path = os.path.join(final_folder, file_name)

    stock_data.to_csv(file_path, index=False)

print("All stock CSV files created successfully")