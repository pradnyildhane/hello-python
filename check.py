from nsepython import *
from pymongo import MongoClient
print(indices)

import numpy as np
import pandas as pd

today = pd.Timestamp("today").strftime("%d/%m/%Y")
print(today)


positions = nsefetch('http://localhost:3000/nse/get_quote_info?companyName=TCS')
df = pd.DataFrame(positions['data'])
df['Date'] = today
df.to_csv(r'/Users/pradnyilkumardhane/Downloads/dftocsv2.csv', mode='a', index=False, header=True)

df.reset_index(inplace=True)
data_dict =df.to_dict("records")
print(data_dict)



LTpositions = nsefetch('http://localhost:3000/nse/get_quote_info?companyName=LT')
df1 = pd.DataFrame(LTpositions['data'])
df1['Date'] = today
print(df1)
df1.to_csv(r'/Users/pradnyilkumardhane/Downloads/dftocsv2.csv', mode='a', index=False, header=False)
#df.to_csv(r'/Users/pradnyilkumardhane/Downloads/dftocsv.csv',encoding='utf-8', index=False)

# # Select the ones you want
# df2 = df[['closePrice','lastPrice']]
# df2.to_csv(r'/Users/pradnyilkumardhane/Downloads/dftocsv2.csv', mode='a', index=False, header=False)
# df2['Date'] = today
# print(df2)

import certifi
ca = certifi.where()

client = MongoClient("mongodb+srv://XXX/?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.myFirstDatabase

collection = db.myFirstDatabase

collection.insert_many(data_dict)

data = collection.find({'symbol':'TCS'})

for i in data:
    print(i)
    break

