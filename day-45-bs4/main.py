# # 001 Day 45 Goals what you will make by the end of the day
# # 002 Parsing HTML and Making Soup

from bs4 import BeautifulSoup
# import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
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

