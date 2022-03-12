# reading data from a csv file
# with open("weather_data.csv") as input_file:
#     data = input_file.readlines()
#     print(data)

# using the csv library
import csv
with open("weather_data.csv") as input_file:
    data = csv.reader(input_file)
    temperatures = []

    # extract temperature values from the data as integers
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)
