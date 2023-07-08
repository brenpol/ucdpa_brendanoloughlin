import pandas as pd
import numpy as np

# Import csv and set encoding to avoid encoding errors 
df_2010_property_price = pd.read_csv("Property_Price_Register_Ireland-28-05-2021.csv", encoding= "iso-8859-15")

# Ensure that date column is in datetime
df_2010_property_price["SALE_DATE"] = pd.to_datetime(df_2010_property_price["SALE_DATE"], format="mixed")

print(df_2010_property_price.head())

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

def main():
    review_columns_not_null()

if __name__ == "__main__":
    main()