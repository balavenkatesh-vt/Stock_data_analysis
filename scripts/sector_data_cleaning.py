import pandas as pd

# load sector data
df = pd.read_csv("sector_data.csv")

# view columns
print("Original Columns:")
print(df.columns)

# remove duplicates
df.drop_duplicates(inplace=True)

# check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# convert columns to lowercase
df.columns = df.columns.str.lower()
df.columns = df.columns.str.strip()

# lowering the text  column - company:
df.company = df.company.str.lower()
df.company = df.company.str.strip()

# lowering the text column - sector:
df.sector =  df.sector.str.lower()
df.sector = df.sector.str.strip()

# lowering the text column - symbols:
df.symbol =  df.symbol.str.lower()
df.symbol = df.symbol.str.strip()
#renaming symbols to ticker("for column mismatch problem solving")
df = df.rename(columns = {'symbol' : 'ticker'})

# reset index
df.reset_index(drop=True, inplace=True)

df.to_csv(r"C:\Users\welcome\PycharmProjects\PythonProject2\cleaned_sector_data.csv",index=False)

print("\nCleaned Sector Data Saved Successfully")

print("\nFinal Columns:")
print(df)