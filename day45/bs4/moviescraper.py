from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.timeout.com/newyork/movies/best-movies-of-all-time")
response = response.text

soup = BeautifulSoup(response, "html.parser")
links = soup.find_all(name="a", class_="xs-text-charcoal decoration-none")

lists = [i.getText() for i in links]
rank = [int(i.split("\n                    ")[1].split(".\xa0")[0]) for i in lists[0:-1]]
movies = [i.split(".\xa0")[1].split("\n")[0] for i in lists[0:-1]]

with open("movies.txt",mode="w") as file:
    for i in range(len(lists) - 1):
        file.write(f"{rank[i]}, {movies[i]}\n")
