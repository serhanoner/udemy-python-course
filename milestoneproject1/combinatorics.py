import pandas as pd

data = pd.read_excel(r"C:\Users\aksak\Desktop\405-Details.xlsx")
df=pd.DataFrame(data,columns=['6 best'])

print(df.describe())