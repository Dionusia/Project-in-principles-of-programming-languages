import pandas as pd
import matplotlib.pyplot as plt
import csv
from urllib.request import urlretrieve as retrieve
import urllib.request


url ="https://data.buffalony.gov/api/views/2cjd-uvx7/rows.csv?accessType=DOWNLOAD"

retrieve(url,'RecyclingData.csv')

#read csv file
df = pd.read_csv("RecyclingData.csv")
###############################################################################
#1o erwtima
df["DATE"] = pd.to_datetime(df['DATE'])
year_total = df.groupby(df['DATE'].dt.year)['TOTAL (IN TONS)'].sum().reset_index()
my_dict1 =df.groupby(df['DATE'].dt.year)['TOTAL (IN TONS)'].sum().to_dict()
#print(my_dict1)


#2o erwtima
type_total =df.groupby(['TYPE'])['TOTAL (IN TONS)'].sum().reset_index()
my_dict2 = df.groupby(['TYPE'])['TOTAL (IN TONS)'].sum().to_dict()
#print(type_total)


#3o erwtima
monthly_max = df.groupby(['MONTH'], as_index=False)['TOTAL (IN TONS)'].sum()
top5 = monthly_max.sort_values(by=['TOTAL (IN TONS)'],ascending=False).head(5)
my_dict3 = df.groupby(['MONTH'])['TOTAL (IN TONS)'].sum().head(5).to_dict()
#print(my_dict3)
#print(top5)

################################################################################
#1 erwtima chart
plt.style.use('dark_background')
df_year= year_total
df_year.plot(x='DATE', y='TOTAL (IN TONS)',kind="bar")
plt.title("Each years total Recycling")
plt.show()

#2 erwtima chart
plt.style.use('dark_background')
df_type= type_total
df_type.plot(x='TYPE', y='TOTAL (IN TONS)',kind="bar")
plt.title("For each recycle type the total garbage")
plt.show()

#3 erwtima chart
plt.style.use('dark_background')
df_5 = top5
df_5.plot(x='MONTH', y='TOTAL (IN TONS)',kind="bar")
plt.title("Top5 Months with the highest tons of garbage")
plt.show()

