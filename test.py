import pandas as pd
import numpy as np

# Import csv and set encoding to avoid encoding errors 
df_residential_property = pd.read_csv("PPR-2020.csv", encoding= "iso-8859-15")

# Rename columns to make it easier to work with
df_residential_property = df_residential_property.rename(columns={
    "Date of Sale (dd/mm/yyyy)": "Date of Sale",
    "Price ()": "Price"
})

# Ensure that date column is in datetime
df_residential_property["Date of Sale"] = pd.to_datetime(df_residential_property["Date of Sale"], format="%d/%m/%Y")

# Convert the 'Price' column to numeric type
df_residential_property['Price'] = df_residential_property['Price'].replace({'': '', ',': ''}, regex=True).astype(float)

# Review if column "Property Size Description" is all null, and if not, how many are filled as a percent of total rows
df_size_not_null = df_residential_property.loc[df_residential_property["Property Size Description"].notnull(), "Property Size Description"]

total_count = df_size_not_null.count()
print("Total non-null values:", total_count)

percentage = (total_count / len(df_residential_property)) * 100
print("Percentage of non null values: {:.2f}%".format(percentage))

# If percent of rows with data is less than 1%, drop column 
if percentage < 1:
    df_residential_property = df_residential_property.drop("Property Size Description", axis=1)
    print("Dropped column: ", "Property Size Description")