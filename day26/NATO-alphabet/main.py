# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index,row) in student_data_frame.iterrows():
#     print(row.student)
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
import pandas
result = {rows.letter: rows.code for (index, rows) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}
# print(result)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_nato():
    ask = input("Enter a word: ").upper()
    again = True
    try:
        output = [result[letter] for letter in ask]
        #output = {letter: word for (letter, word) in result.items() if letter in ask}
    except KeyError:
        print("Sorry! Only letters in alphabet phase...")
        generate_nato()
    else:
        print(output)

generate_nato()