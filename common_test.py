import pandas as pd
df= pd.DataFrame({"A":[1,2,3],"B":[3,6,7]})
df["C"] = df["A"] + df["B"]
print(df)
