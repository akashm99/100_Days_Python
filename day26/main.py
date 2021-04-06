# num = [1, 2, 3]
# new_list = [n+1 for n in num]
# print(new_list)
#
# name = "akash"
# new_name = [letter for letter in name]
# print(new_name)
#
# range_list = [number * 2 for number in range(1,10) if number%2 == 0]
# print(range_list)
# print(range_list.__len__())
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n**2 for n in numbers]
# print(squared_numbers)
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [n for n in numbers if n%2 == 0]
# print(result)
#
# with open("file1.txt") as file1:
#   file1_number=file1.readlines()
# print(file1_number)
#
# with open("file2.txt") as file2:
#     result = [int(num) for num in file2.readlines() if num in file1_number]
# print(result)
#
# names = ["alex", "beth", "akash", "maddy", "akshay"]
# import random
# student_score = {name:random.randint(1,100) for name in names}
# print(student_score)
# passed_dict = {name : score for (name, score) in student_score.items() if score >60}
# print(passed_dict)
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)
#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = { day: temp * 9/5 +32 for (day, temp) in weather_c.items() }
# print(weather_f)

