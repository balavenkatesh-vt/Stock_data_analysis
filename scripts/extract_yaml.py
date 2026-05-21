# traverse folders
# read yaml files
# convert to dataframe
# save csv

import os
import yaml
import pandas as pd

main_folder = r"C:\Users\welcome\PycharmProjects\PythonProject2\data"

all_data = []

for month_folder in os.listdir(main_folder):

    month_path = os.path.join(main_folder, month_folder)

    if os.path.isdir(month_path):

        for file in os.listdir(month_path):

            if file.endswith(".yaml"):

                file_path = os.path.join(month_path, file)

                with open(file_path, "r") as f:

                    data = yaml.safe_load(f)

                    all_data.extend(data)

df = pd.DataFrame(all_data)

df.to_csv("master_stock_data.csv", index=False)

print(df.head())
print(df.shape)
