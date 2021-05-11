import requests

apikey="a763dbadfd51b5c2576d9ea0426b7d6e"
api_read_access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNzYzZGJhZGZkNTFiNWMyNTc2ZDllYTA0MjZiN2Q2ZSIsInN1YiI6IjYwOWE0Zjk3MjgzZWQ5MDAzZjZlYzVkMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Qxj3EYXkQFU80Iyu7XScm8OO9m701gs0puWsuW3ysos"

url = f"https://api.themoviedb.org/3/search/movie"
params = {
    "api_key": apikey,
    "query": "The Matrix"
}

response = requests.get(url, params=params)
movies= response.json()['results']
movie_lists = []
movies_data = []
for i in movies:
    movie_lists.append(i["title"])
    movies_data.append([i["title"], i["release_date"], i["overview"], i["poster_path"]])


params = {
    "api_key": apikey,
    # "movie_id": 603
}
response = requests.get("https://api.themoviedb.org/3/movie/603", params=params)
print(response.json())

print(movie_lists)
print(movies_data)
