import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np



url = 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action'



page = requests.get(url)
print(page)


action = BeautifulSoup(page.content, 'html.parser')

title50 = action.find_all('div', class_= "lister-item-content")
movie_title = []

for i in title50:
    mo_title = i.a.text
    movie_title.append(mo_title)


print(movie_title)


# title100 = action.find_all('div', class_= "lister-item-content" )
# movie_title = []

# for i in title100:
#     mo_title = i.a.text
#     movie_title.append(mo_title)


# print(len(movie_title))





# description = action.find_all('p', class_= "text-muted")

# movie_des = []

# for i in description:
#     mo_desc = i.text
#     mo_desc = mo_desc.strip()
#     movie_des.append(mo_desc)

# print(len(movie_des))


# release_date = action.find_all('span', class_= "lister-item-year text-muted unbold")

# r_date = []

# for i in release_date:
#     r_dt = i.text
#     r_date.append(r_dt)

# print(len(r_date))
