import pandas as pd
import random

data = pd.read_csv("data/french_words.csv")

data_list = [{"French": rows.French, "English": rows.English} for rows in data.iterrows()]

print(data_list)
#print(random.choice(data["French"]))

