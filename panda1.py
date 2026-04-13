import pandas as pd
data = {
    "Name": ["Alice", "Bod","Charlie"],
    "Age": [25,30,35],
    "City":["New York","Leh","Chicago"]
}
df = pd.DataFrame(data)
print(df)