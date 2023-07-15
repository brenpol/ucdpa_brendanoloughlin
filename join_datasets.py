import pandas as pd
import tidy_data_set_ppr_2020 as ppr2020
import tidy_data_set_ppr_2010_2021 as ppr2010

# Pull in mean price by month dataset from ppr2020
df_mean_price_month_2020 = ppr2020.average_price_by_month()

# Pull in mean price by month dataset from ppr2010
df_grab_2019_values = ppr2010.limit_to_2019_values()
df_mean_price_month_2019 = ppr2010.average_price_by_month(df_grab_2019_values)

# Pull in mean price by month by year from 2010 to 2019
df_2010_2019 = ppr2010.drop_2020_2021()
df_mean_price_by_month_decade = ppr2010.average_price_by_month_decade(df_2010_2019)

# Merge mean price by month values from 2019 and 2020 for comparison 
def merge_monthly_mean():
    global df_mean_price_month_2020
    global df_mean_price_month_2019
    
    df_merged_mean_price_by_month = pd.merge(df_mean_price_month_2019, df_mean_price_month_2020, on="Month")
    return df_merged_mean_price_by_month


# Merge mean price by month values from 2010 - 2019 with mean price from 2020 for comparison 
def merge_month_mean_decade():
    global df_mean_price_month_2020
    global df_mean_price_by_month_decade

    # Create local dfs to avoid messing with previous code
    df_local_mean_price_month_2020 = df_mean_price_month_2020
    df_local_mean_price_by_month_decade = df_mean_price_by_month_decade

    # Rename the df_mean_price_month_2020 column to match df_mean_price_by_month_decade
    df_local_mean_price_month_2020 = df_local_mean_price_month_2020.rename(columns={'Mean Price 2020': '2020'})

    # Merge data columns and return complete df
    df_merged_full_decade = pd.merge(df_local_mean_price_by_month_decade, df_local_mean_price_month_2020, on="Month")

    #print(df_merged_full_decade)

    return df_merged_full_decade