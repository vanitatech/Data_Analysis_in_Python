# Squirrel Census Data Analysis

This project uses **Pandas** to analyse the 2018 Central Park Squirrel Census dataset and count the number of squirrels by their primary fur colour.

## Project Overview

The program:

1. Loads the squirrel census CSV file using Pandas.
2. Selects the `Primary Fur Color` column.
3. Uses Pandas `value_counts()` to count squirrels by fur colour.
4. Creates a new DataFrame containing the fur colour and squirrel count.
5. Exports the results to a new CSV file called `squirrel_count.csv`.

## Technologies Used

* Python
* Pandas
* CSV data
* DataFrames

## Project Files

```text
Day 25/
│
├── main.py
├── 2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20261006.csv
├── squirrel_count.csv
└── README.md
```

## Example Code

```python
import pandas

fur_color = pandas.read_csv(
    "2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20261006.csv"
)

data_dict = {
    "Fur Color": fur_color["Primary Fur Color"].value_counts().index,
    "Count": fur_color["Primary Fur Color"].value_counts().values
}

pandas.DataFrame(data_dict).to_csv("squirrel_count.csv", index=False)
```

## Output

The program creates a `squirrel_count.csv` file containing the number of squirrels for each fur colour.

Example:

```text
Fur Color,Count
Gray,2473
Cinnamon,392
Black,103
```

## What I Learned

This project helped me practise:

* Reading CSV files with Pandas
* Selecting columns from a DataFrame
* Using `value_counts()`
* Working with `.index` and `.values`
* Creating a DataFrame from a dictionary
* Exporting DataFrames to CSV
* Understanding how Pandas handles indexes
