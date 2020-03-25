import pandas as pd
df = pd.read_excel('trfile.xlsx')
print(df)
df['new']=[1,2,3]
print(df)
df.to_excel('trfile.xlsx')