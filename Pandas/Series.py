import pandas as pd;
a=[1,2,3,4]
chars=pd.Series(a,index=["First","Second","Third","Fourth"])
print(chars)
print(chars["First"])
print(chars["Second"])
print(chars["Third"])
print(chars["Fourth"])

