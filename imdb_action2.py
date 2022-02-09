import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action'
url2 = 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&start=51&ref_=adv_nxt'

# page2 = requests.get(url2)
# print(page2)


# action2 = BeautifulSoup(page2.content, 'html.parser')

# title100 = action2.find_all('div', class_= "lister-item-content")
# movie_title = []

# for i in title100:
#     mo_title = i.a.text
#     movie_title.append(mo_title)


# print(movie_title)



def url_getter(url):
    page_all = requests.get(url)
    action = BeautifulSoup(page_all.content, "html.parser")
    return action
    

page2 = url_getter(url2)
page1 = url_getter(url)
#print(t1)


def title(action):
    title100 = action.find_all('div', class_= "lister-item-content")
    movie_title = []

    for i in title100:
        mo_title = i.a.text
        movie_title.append(mo_title)
    return movie_title




def description(action):
    desc100 = action.find_all('p', class_= "text-muted")
    des1 = desc100
    movies_desc = []

    for i in desc100:
        mo_desc = i.text.replace('\n', " ")                   #strip()                          
        movies_desc.append(mo_desc)
    return movies_desc



def release_date(action): 
    rdate100 = action.find_all('span', class_= "lister-item-year text-muted unbold")
    r_date = []
    
    for i in rdate100:
        r_dt = i.text
        r_date.append(r_dt)
    return r_date

<<<<<<< Updated upstream
first_50_titles = title(page1)
#print(first_50_titles)
second_50_titles = title(page2)
#print(second_50_titles)
all_titles = first_50_titles + second_50_titles
print(all_titles)
=======
# first_50_titles = title(page1)
# print(first_50_titles)
# second_50_titles = title(page2)
# print(second_50_titles)
>>>>>>> Stashed changes

# first_50_description = description(page1)
# print(first_50_description)
# second_50_description = description(page2)
# print(second_50_description)

<<<<<<< Updated upstream
# first_50_reldate = release_date(page1)
# #print(first_50_reldate)
# second_50_reldate = release_date(page2)
# #print(second_50_reldate)

# all_release_date = first_50_reldate + second_50_reldate
# print(all_release_date)
=======
first_50_reldate = release_date(page1)
print(first_50_reldate)
second_50_reldate = release_date(page2)
print(second_50_reldate)

>>>>>>> Stashed changes


