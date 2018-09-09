
import requests
import io
import zipfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def getAndExtractZip(url):
    # yields (filename, file-like object) pairs
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as thezip:
        for zipinfo in thezip.infolist():
            with thezip.open(zipinfo) as thefile:
                yield zipinfo.filename, thefile

url = "http://seanlahman.com/files/database/baseballdatabank-master_2018-03-28.zip"

df_salaries = pd.DataFrame()
df_teams = pd.DataFrame()
for name, content in getAndExtractZip(url):
    if name == 'baseballdatabank-master/core/Salaries.csv':
        df_salaries = pd.read_csv(content)
    if name == 'baseballdatabank-master/core/Teams.csv':
        df_teams = pd.read_csv(content)
print(df_salaries.head())
print(df_salaries.max())
print(df_salaries.pct_change)
#print(df_teams.head())

print(pd.merge(df_salaries,df_teams))

fig, axis = plt.subplots(1, 1)
df_salaries.plot()
plt.show()


