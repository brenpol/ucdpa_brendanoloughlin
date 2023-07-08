import pandas as pd
import numpy as np

# Import csv 
df_house_price_index = pd.read_csv("HPA13.20230708144949.csv")

# Narrow down results to year 2020 - relevant to other dataset
df_house_price_index = df_house_price_index[df_house_price_index["Year"] == 2020]
print(df_house_price_index, "\n")

# Drop "TLIST(A1)" column as all data is same as "Year" column 
df_house_price_index = df_house_price_index.drop("TLIST(A1)", axis=1)
print(df_house_price_index, "\n")

# Show unique values for "Type of Residential Property"
types_of_properties = df_house_price_index["Type of Residential Property"].unique()
print(types_of_properties, "\n")

# Separate the data based on each unique value of the statistic column
statistic_unique_values = df_house_price_index['STATISTIC'].unique()

print("\n=== New dataframes created ===\n")

for value in statistic_unique_values:
    filtered_df = df_house_price_index[df_house_price_index['STATISTIC'] == value]
    new_df_names = value
    globals()[new_df_names] = filtered_df
    print(new_df_names)

print()
print("New dataframe created: HPA13C01")
print(HPA13C01)
print()
print("New dataframe created: HPA13C02")
print(HPA13C02)