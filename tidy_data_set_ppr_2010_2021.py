import pandas as pd
import numpy as np

# Import csv and set encoding to avoid encoding errors 
df_2010_property_price = pd.read_csv("Property_Price_Register_Ireland-28-05-2021.csv", encoding= "iso-8859-15")

print(df_2010_property_price.head())