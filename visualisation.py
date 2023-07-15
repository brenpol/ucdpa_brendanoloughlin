import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tidy_data_set_ppr_2020 as ppr2020
import tidy_data_set_ppr_2010_2021 as ppr2010
import join_datasets as jd

average_price_by_county = ppr2020.average_price_by_county()

# Graph average price by county for 2020 dataset. 
def average_price_by_county_2020():
    df_average_price_by_county = pd.DataFrame.from_dict([average_price_by_county])
    plt.figure(figsize=(10, 6))
    county_price_plot = sns.barplot(data=df_average_price_by_county)
    county_price_plot.set_xlabel("County")
    county_price_plot.set_ylabel("Price in €")
    county_price_plot.set_xticklabels(county_price_plot.get_xticklabels(), rotation=90)
    plt.tight_layout()
    plt.savefig("Generated Graphs/average_price_by_county_2020.png")


# Graph average price by month for 2020 dataset.
def average_price_by_month_2020():
    average_price_by_month_2020 = ppr2020.average_price_by_month()
    plt.figure(figsize=(10, 6))
    price_by_month_plot_2020 = sns.barplot(data=average_price_by_month_2020, x="Month", y="Mean Price 2020")
    plt.tight_layout()
    plt.savefig("Generated Graphs/average_price_by_month_2020.png")


# Graph average price by month for 2019 dataset.
def average_price_by_month_2019():
    grab_2019_values = ppr2010.limit_to_2019_values()
    average_price_by_month_2019 = ppr2010.average_price_by_month(grab_2019_values)
    plt.figure(figsize=(10, 6))
    price_by_month_plot_2019 = sns.barplot(data=average_price_by_month_2019, x="Month", y="Mean Price 2019")
    plt.tight_layout()
    plt.savefig("Generated Graphs/average_price_by_month_2019.png")


# Graph line chart comparison on prices from 2019 to 2020
def line_chart_mean_price_merged_data():
    df_merged_average_price_by_month = jd.merge_monthly_mean()

    plt.figure(figsize=(10, 6))

    sns.lineplot(data=df_merged_average_price_by_month, x='Month', y='Mean Price 2019', label='2019')
    sns.lineplot(data=df_merged_average_price_by_month, x='Month', y='Mean Price 2020', label='2020')

    plt.xlabel('Month')
    plt.ylabel('Mean Price')
    plt.title('Comparison of Mean Prices between 2019 and 2020')
    plt.xticks(rotation=90)

    plt.tight_layout()
    plt.savefig("Generated Graphs/average_price_by_month_2019_2020.png")

# Plot new build v second hand houses sold
def line_chart_new_v_old_2020():
    df_new_v_old = ppr2020.df_residential_property
    df_new_v_old = df_new_v_old[["Description of Property", "Price"]]

    type_list = df_new_v_old["Description of Property"].unique()

    # loop through type list, and grab mean value of price for each df by type before storing in a dict
    type_average_price = {}

    for i in range(len(type_list)):
        df_select_type = df_new_v_old[df_new_v_old["Description of Property"] == type_list[i]]
        grab_mean_price = df_select_type["Price"].mean()
        type_average_price["{0}".format(type_list[i])] = round(grab_mean_price, 2)

    # Convert dictionary back to dataframe
    df_new_v_old = pd.DataFrame.from_dict([type_average_price])

    plt.figure(figsize=(10, 6))

    sns.barplot(data=df_new_v_old)

    plt.tight_layout()
    plt.savefig("Generated Graphs/new_v_old_2020.png")


def price_by_month_decade():

    # Pull in the right data
    df_mean_price_by_month_decade = jd.merge_month_mean_decade()

    # Set the figure size
    plt.figure(figsize=(10, 6))

    # Create the line plot
    sns.lineplot(data=df_mean_price_by_month_decade)

    # Set the title and labels
    plt.title('Average Price by Month')
    plt.xlabel('Month')
    plt.ylabel('Mean Price')
    plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

    # Update x-axis labesl with month names 
    month_names = df_mean_price_by_month_decade['Month']
    plt.xticks(range(len(month_names)), month_names, rotation=45)

    plt.tight_layout()
    plt.savefig("Generated Graphs/price_by_month_by_year.png")



def main():
    average_price_by_county_2020()
    average_price_by_month_2020()
    average_price_by_month_2019()
    line_chart_mean_price_merged_data()
    line_chart_new_v_old_2020()
    price_by_month_decade()


if __name__ == "__main__":
    main()