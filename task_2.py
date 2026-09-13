import pandas as pd
data=pd.read_json('airports.json')
df=pd.DataFrame(data)
print(df)