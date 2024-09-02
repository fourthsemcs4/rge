import pandas as pd
data=pd.read_csv(r"C:\Users\TRISHA MAITHRI\Documents\Dataset\Dataset\auto-mpg.csv")
df=pd.DataFrame(data)
print(df)
hp=df['Horsepower'].mean()
print(hp)