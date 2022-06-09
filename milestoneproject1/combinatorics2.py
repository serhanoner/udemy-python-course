import pandas as pd
data = pd.read_excel(r"C:\Users\aksak\Desktop\405-Details.xlsx")
data.to_excel("405-Details",index=0)
df=pd.DataFrame(data,columns=['6 best'],)

print(df)


sum = 0
tot_numbers = 0
for index in range(1,len(df)):
    index = int(index)
    sum += index
    tot_numbers +=1
print(sum/tot_numbers)