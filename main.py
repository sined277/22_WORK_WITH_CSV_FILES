# import csv
#
#
# with open("../22 WORK WITH CSV FILES/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
import csv

# IMPORT PANDA
import pandas

# READING DATA
# data = pandas.read_csv('weather_data.csv')
# print(data['temp'])

# DATA TO DICT
# data_dict = data.to_dict()
# print(data_dict)

# DATA TO LIST
# temp_list = data['temp'].to_list()
# print(max(temp_list))


#GET DATA IN ROW
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# monday_temp = monday.temp
# monday_temp_f = (monday_temp * 9/5) + 32
# print(monday_temp_f)



#CREATE A DATAFRAME FROM SCRATH
# data_dict = {
#     'students': ['Ammy', 'Dennis', 'Mila'],
#     'scores': [60, 50, 74],
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv('new_data_csv')



data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])

# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)


data_dict = {
    'Fur color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

sqrl_data = pandas.DataFrame(data_dict)
print(sqrl_data)
sqrl_data.to_csv("data_about_sqrl_in_park.csv")