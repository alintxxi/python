# # 001 Day 45 Goals what you will make by the end of the day
# # 002 Parsing HTML and Making Soup

# from bs4 import BeautifulSoup
# import lxml

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.p)

# # 003 Finding and Selecting Particular Elements with BeautifulSoup

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)

# # 004 Scraping a Live Website
# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
# articles = soup.find_all(name="a", rel="noreferrer")
# article_texts = []
# article_links = []
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_links.append(link)
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#
# largest_number = max(article_upvotes)
# largest_index = article_upvotes.index(largest_number)
#
# print(article_texts[largest_index])
# print(article_links[largest_index])

# # 005 Is Web Scraping Legal
# linkedin.com/robots.txt

# # 006 100 Movies that You Must Watch
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w", encoding='UTF-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")
