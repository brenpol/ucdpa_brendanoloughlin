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


# Show top 10 results to review dataframe 
def display_dataframe():
    print("\n=== Display head of DF to complete initial review of data ===\n")
    df_residential_property_top_10 = df_residential_property.head(10)
    print(df_residential_property_top_10)
    print()
    return df_residential_property_top_10


def review_columns_not_null():
    global df_residential_property

    # Get a list of all column names
    column_names = df_residential_property.columns.values.tolist()

    # Loop through column names and drop if NOT_NULL values make up less than 1% the total
    for i in range(len(column_names)):

        # Review if columns is all null, and if not, how many are filled as a percent of total rows
        df_not_null = df_residential_property.loc[df_residential_property[column_names[i]].notnull(), column_names[i]]

        print("\n=== Review of '{}' column ===\n".format(column_names[i]))

        total_count = df_not_null.count()
        print("Total non-null values:", total_count)

        percentage = (total_count / len(df_residential_property)) * 100
        print("Percentage of non null values: {:.2f}%".format(percentage))

        # If percent of rows with data is less than 1%, drop column 
        if percentage < 1:
            df_residential_property = df_residential_property.drop(column_names[i], axis=1)
            print("Dropped column: ", "{}\n".format(column_names[i]))  
        else:
            print("{} column not dropped\n".format(column_names[i]))

    return df_residential_property


def average_price_by_county():
    global df_residential_property
    
    # Get list of counties and sort them for later use 
    county_list = df_residential_property["County"].unique()
    county_list = sorted(county_list)

    # Create a new dataframe with only wanted data
    price_by_county = df_residential_property[["County", "Price"]]
    price_by_county = price_by_county.sort_values("County")

    # loop through county list, and grab mean value of price for each df by county before storing in a dict
    county_average_price = {}

    for i in range(len(county_list)):
        df_select_county = price_by_county[price_by_county["County"] == county_list[i]]
        grab_mean_price = df_select_county["Price"].mean()
        county_average_price["{0}".format(county_list[i])] = round(grab_mean_price, 2)

    return county_average_price

def main():
    df_residential_property= display_dataframe()
    df_residential_property = review_columns_not_null()
    county_average_price = average_price_by_county()
    print(df_residential_property)

if __name__ == "__main__":
    main()