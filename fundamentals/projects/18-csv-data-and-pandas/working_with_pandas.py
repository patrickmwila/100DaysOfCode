# working with the pandas library
# Things to note:
# A DataFrame in pandas is equivalent to an Excel work sheet
# A DataSeries is equivalent to a single column of an Excel work sheet

# import pandas
import pandas as pd

data = pd.read_csv("weather_data.csv") # extract a panda DataFrame
print(data)
temp_values = data["temp"].to_list() # convert the temp series to a list

# display the mean temperature of the temp series
print(temp_values)
print(sum(temp_values) / len(temp_values))
print(data["temp"].mean())
print(data["temp"].max())

# extract a row from a DataFrame by filtering the column with a condition
monday_row = data[data.day == "Monday"]
print(type(monday_row))
print(monday_row)

# display row of data with maximum temp
print(data[data.temp == data.temp.max()])

# working with extracted rows
deg_temp = int(monday_row.temp)

fah_temp = (deg_temp * 9 / 5) + 32
print(fah_temp)

# creating a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
# create DataFrame
student_results = pd.DataFrame(data_dict)
print(student_results)

# export the student_results DataFrame to a csv file
student_results.to_csv("student_results.csv", index=False)
