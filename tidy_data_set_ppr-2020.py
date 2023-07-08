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


def display_dataframe():
    print("\n=== Display head of DF to complete initial review of data ===\n")
    df_residential_property_top_10 = df_residential_property.head(10)
    print(df_residential_property_top_10)
    print()
    return df_residential_property_top_10


def display_county_price():
    print("\n=== Create and display dataframe of price by county ===\n")
    df_price_by_county = df_residential_property[["Price", "County"]]
    print(df_price_by_county)
    print()
    return df_price_by_county

def review_property_size_not_null():
    global df_residential_property

    # Review if column "Property Size Description" is all null, and if not, how many are filled as a percent of total rows
    df_size_not_null = df_residential_property.loc[df_residential_property["Property Size Description"].notnull(), "Property Size Description"]

    print("\n=== Review of 'Property Size Description' column ===\n")

    total_count = df_size_not_null.count()
    print("Total non-null values:", total_count)

    percentage = (total_count / len(df_residential_property)) * 100
    print("Percentage of non null values: {:.2f}%".format(percentage))

    # If percent of rows with data is less than 1%, drop column 
    if percentage < 1:
        df_residential_property = df_residential_property.drop("Property Size Description", axis=1)
        print("Dropped column: ", "Property Size Description\n")  
    else:
        print("No column dropped\n")

    return df_residential_property

def main():
    display_dataframe()
    display_county_price()
    review_property_size_not_null()

if __name__ == "__main__":
    main()