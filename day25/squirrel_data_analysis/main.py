import pandas as pd

data = pd.read_csv("squirrel_data.csv")
#print(data["Primary Fur Color"])

final = pd.DataFrame()
gray = 0
cinnamon = 0
black = 0

for i in data["Primary Fur Color"]:
    if i == "Gray":
        gray += 1
    elif i == "Black":
        black += 1
    else:
        cinnamon += 1

print(pd.DataFrame({
    "fur color": ["gray" , "black", "cinnamon"],
    "count": [gray, black, cinnamon]
}))

print(data["Primary Fur Color"].unique())