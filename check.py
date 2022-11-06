from nsepython import *
print(indices)

import numpy as np
import pandas as pd

positions = nsefetch('http://localhost:3000/nse/get_quote_info?companyName=TCS')
df = pd.DataFrame(positions['data'])
LTpositions = nsefetch('http://localhost:3000/nse/get_quote_info?companyName=LT')
df1 = pd.DataFrame(LTpositions['data'])
df.to_csv(r'/Users/pradnyilkumardhane/Downloads/dftocsv.csv', mode='a', index=False, header=False)
#df.to_csv(r'/Users/pradnyilkumardhane/Downloads/dftocsv.csv',encoding='utf-8', index=False)

# Select the ones you want
df2 = df[['closePrice','lastPrice']]
df2.to_csv(r'/Users/pradnyilkumardhane/Downloads/dftocsv.csv', mode='a', index=False, header=False)
print(df2)

