from bs4 import BeautifulSoup
import lxml
import requests

# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.find_all(name="li"))
# all_li = soup.find_all(name="li")
# for tag in all_li:
#     print(tag.getText())
# heading = soup.find(name="h1", id="name").getText()
# print(heading)
# company = soup.select_one(selector="p a")
# print(company.get("href"))

response = requests.get(url="https://news.ycombinator.com/news")
news = response.text

soup = BeautifulSoup(news, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append((article_tag.get("href")))
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

index = article_upvote.index(max(article_upvote))
print(f"text = {article_texts[index]}")
print(f"link = {article_links[index]}")
print(f"upvote = {article_upvote[index]}")
