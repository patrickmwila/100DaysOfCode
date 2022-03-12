import pandas as pd

# extract a squirrel DataFrame from data
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# count the number gray, cinnamon and black squirrels
find_gray = data[data["Primary Fur Color"] == "Gray"]
count_gray_squirrels = len(find_gray)

find_cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
count_cinnamon_squirrels = len(find_cinnamon)

find_black = data[data["Primary Fur Color"] == "Black"]
count_black_squirrels = len(find_black)

# create a DataFrame showcasing the total number of different squirrels
data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [count_gray_squirrels, count_cinnamon_squirrels, count_black_squirrels]
}

squirrels = pd.DataFrame(data_dict)
squirrels.to_csv("squirrel_count.csv")
