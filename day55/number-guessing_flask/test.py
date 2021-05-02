import requests

# age = requests.get(url=f"https://api.agify.io/?name=ak")
# gender = requests.get(url=f"https://api.genderize.io/?name=akash")
# age = age.json()
# gender = gender.json()['gender']
# print(age,gender)


response = requests.get(url="https://api.npoint.io/5abcca6f4e39b4955965")
