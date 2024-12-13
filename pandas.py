import pandas as pd

data = {'Name': ['Alvi', 'Emon'], 'Age': [22, 30]}
df = pd.DataFrame(data)
print(df)

# Filter rows
filtered = df[df['Age'] > 22]
print(filtered)
