import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tidy_data_set_ppr_2020 as ppr2020

average_price_by_county = ppr2020.average_price_by_county()

df_average_price_by_county = pd.DataFrame.from_dict([average_price_by_county])
county_price_plot = sns.barplot(data=df_average_price_by_county)
county_price_plot.set_xlabel("County")
county_price_plot.set_ylabel("Price in €")
county_price_plot.set_xticklabels(county_price_plot.get_xticklabels(), rotation=90)
plt.savefig("Generated Graphs\\average_price_by_county_2020.png")
plt.show()