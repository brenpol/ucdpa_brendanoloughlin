import pandas as pd
import tidy_data_set_ppr_2020 as ppr2020
import tidy_data_set_ppr_2010_2021 as ppr2010

# Pull in mean price by month dataset from ppr2020
df_mean_price_month_2020 = ppr2020.average_price_by_month()

# Pull in mean price by month dataset from ppr2010
df_grab_2019_values = ppr2010.limit_to_2019_values()
df_mean_price_month_2019 = ppr2010.average_price_by_month(df_grab_2019_values)

# Merge mean price by month values for comparison 
def merge_monthly_mean():
    global df_mean_price_month_2020
    global df_mean_price_month_2019
    
    df_merged_mean_price_by_month = pd.merge(df_mean_price_month_2019, df_mean_price_month_2020, on="Month")
    return df_merged_mean_price_by_month