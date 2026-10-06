import pandas

fur_color = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20261006.csv")

data_dict = {
    "Fur Color": fur_color["Primary Fur Color"].value_counts().index,
    "Count": fur_color["Primary Fur Color"].value_counts().values
}

pandas.DataFrame(data_dict).to_csv("squirrel_count.csv", index=True)

