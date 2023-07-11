# Day 45 
# WebScraping using BeautifulSoup
# Day 45
from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.string)

print(soup.prettify())

print(soup.a)
# Gets hold of the first anchor tag that it finds

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())

for tag in all_anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a") #The anchor tag which is inside the paragraph tag
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)

response = requests.get("https://news.ycombinator.com/news")
# print(response.text)  # same as "view page source"

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

articles = soup.find_all(class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find("a")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)
print(article_upvotes)
print(article_upvotes.index(max(article_upvotes)))
print(article_links[0])
print(article_texts[0])

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
# print(soup.prettify())

all_movies = soup.find_all(name = "h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
# Reversing the list through slicing. (start:stop:step)
# Here, start is the beginning of the list, stop is end of the list, and step is -1

'''
# or can follow this step:
for n in range(len(movie_titles)-1, -1, -1):
    print(movie_titles[n])

# Here, the start is first element -1, because in python list starts from 0 
# Our stop is -1, because we want to get the 100th movie as well. 
'''

with open("movies.txt", mode="w", encoding="UTF-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")










