import pandas as pd
import numpy as np

global df_2010_property_price

# Import csv and set encoding to avoid encoding errors 
df_2010_property_price = pd.read_csv("Property_Price_Register_Ireland-28-05-2021.csv", encoding= "iso-8859-15")

# Ensure that date column is in datetime
df_2010_property_price["SALE_DATE"] = pd.to_datetime(df_2010_property_price["SALE_DATE"], format="mixed")

def review_columns_not_null():
    global df_2010_property_price

    # Get a list of all column names
    column_names = df_2010_property_price.columns.values.tolist()
    print(column_names)

    for i in range(len(column_names)):

        # Review if columns is all null, and if not, how many are filled as a percent of total rows
        df_not_null = df_2010_property_price.loc[df_2010_property_price[column_names[i]].notnull(), column_names[i]]

        print("\n=== Review of '{}' column ===\n".format(column_names[i]))

        total_count = df_not_null.count()
        print("Total non-null values:", total_count)

        percentage = (total_count / len(df_2010_property_price)) * 100
        print("Percentage of non null values: {:.2f}%".format(percentage))

        # If percent of rows with data is less than 1%, drop column 
        if percentage < 1:
            df_2010_property_price = df_2010_property_price.drop(column_names[i], axis=1)
            print("Dropped column: ", "{}\n".format(column_names[i]))  
        else:
            print("{} column not dropped\n".format(column_names[i]))

    return df_2010_property_price


def limit_to_2019_values():
    global df_2010_property_price

    df_2019_values = df_2010_property_price[df_2010_property_price["SALE_DATE"].dt.year == 2019]
    return df_2019_values


def average_price_by_month(df_2019_values):
    # Group dates by month and find the mean
    mean_price_by_month = round(df_2019_values.groupby(df_2019_values.SALE_DATE.dt.month)["SALE_PRICE"].mean(), 2)
    df_mean_price_by_month = mean_price_by_month.to_frame(name = "Mean Price 2019")
    
    # Change date from numeric to str
    df_mean_price_by_month.index = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # Reset index and rename it to date so that we can use the df for visualisation
    df_mean_price_by_month = df_mean_price_by_month.reset_index()
    df_mean_price_by_month = df_mean_price_by_month.rename(columns={"index": "Month"})

    return df_mean_price_by_month

# As we have data for 2020, we can drop all data from here. 
# We also do not have complete data from 2021 - this goes to May 2021, dropping this. 
# This will give us from 2010 to 2020 - rounding out a full 10 years from mid resession to middle of the pandemic
def drop_2020_2021():
    global df_2010_property_price

    #Create a dataframe that extracts year from date
    df_extract_year = pd.DataFrame()
    df_extract_year["Year"] = pd.to_datetime(df_2010_property_price["SALE_DATE"]).dt.year

    #Create a mask that will return a boolean value
    mask = (df_extract_year["Year"] != 2020) & (df_extract_year["Year"] != 2021)
    
    #Filter the data in df_2010_property_price down using the mask 
    df_2010_property_price = df_2010_property_price[mask]
    
    return df_2010_property_price

# We want to graph average price by month from 2010 to 2019. 
# We can reuse the previous code to get average price by month using the filtered DF created in drop_2020_2021() function

def average_price_by_month_decade(df_2010_property_price):
    # Extract year from SALE_DATE
    df_2010_property_price['Year'] = df_2010_property_price['SALE_DATE'].dt.year

    # Group dates by year and month, and find the mean price
    mean_price_by_month_decade = df_2010_property_price.groupby(['Year', df_2010_property_price['SALE_DATE'].dt.month])['SALE_PRICE'].mean().round(2)

    # Reshape the data and create a DataFrame
    df_mean_price_by_month_decade = mean_price_by_month_decade.unstack(level='Year')
    
    # Change date from numeric to str
    df_mean_price_by_month_decade.index = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # Reset index and rename it to date so that we can use the df for visualisation
    df_mean_price_by_month_decade = df_mean_price_by_month_decade.reset_index()
    df_mean_price_by_month_decade = df_mean_price_by_month_decade.rename(columns={"index": "Month"})

    #print(df_mean_price_by_month_decade)

    return df_mean_price_by_month_decade

def main():

    review_columns_not_null()
    df_2010_property_price = drop_2020_2021()
    df_2019_values = limit_to_2019_values()
    average_price_by_month(df_2019_values)
    average_price_by_month_decade(df_2010_property_price)
    

if __name__ == "__main__":
    main()