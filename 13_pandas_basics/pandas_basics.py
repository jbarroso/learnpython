import pandas as pd

# Create a DataFrame from a dictionary
dict = {
    "country": [
        "Brazil", "Russia", "India", "China", "South Africa"
    ],
    "capital": [
        "Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"
    ],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

brics = pd.DataFrame(dict)
print(brics)

# Custom key
# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)

# Create a DataFrame from a csv file
cars = pd.read_csv('cars.csv', index_col=0)

print(cars)

# Print out country column as Pandas Series
print(cars['cars_per_cap'])

# Print out country column as Pandas DataFrame
print(cars[['cars_per_cap']])

# Print out DataFrame with country and drives_right columns
print(cars[['cars_per_cap', 'country']])

# Print out first 4 observations
print(cars[0:4])

# Print out fifth, sixth, and seventh observation
print(cars[4:6])

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])
