import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&ref_=adv_prv")
#print(page)
soup = BeautifulSoup(page.content,'html.parser')
#print(soup)

#Scraping Director name.-page-1

m_name = soup.find_all('div', class_ = "lister-item-content")
movie_name = []
for name in m_name:
    mo_name = name.a.text
    movie_name.append(mo_name)
#print(movie_name)

# Description
des = soup.find_all('p',class_ = "text-muted")

description = []
for i in des:
    m_des = i.text.strip()
    description.append(m_des) 
only_description = description[1::2]
#print(only_description)

# 

# description = []
# # for i in des:
# #     des1 = i.text.strip()
# #     description.append(des1)
# # print(description)


# Duration of the movie.-page-1
# def film_duration():
#     d_time = soup.find_all('span', class_ = "runtime")
#     duration = []
#     for dt in d_time:
#         dur = dt.text
#         duration.append(dur)
#     return duration
# f_d = film_duration()
# print(f_d)
# print(film_duration())
# print(duration)

# # Rating - Imdb
# imdb_r = soup.find_all('div', class_ = "inline-block ratings-imdb-rating")
# imdb_rating = []
# for ir in imdb_r:
#     r_stars = ir.strong.text
#     imdb_rating.append(r_stars)
# #print(imdb_rating)

# #Rating - Metascore-page-1
# meta_r = soup.find_all('div', class_ = "inline-block ratings-metascore")
# meta_rating =[]
# for mr in meta_r:
#     meta_score = mr.span.text.strip()
#     meta_rating.append(meta_score)
# #print(len(meta_rating))

# # director-name-page1
# d_name = soup.find_all('p', class_ = "")
# director_name =[]
# for dn in d_name:
#     dir_name = dn.a.text.strip()
#     director_name.append(dir_name)
# #print(director_name)

# # page-2
# page2 = requests.get("https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&start=51&ref_=adv_nxt")
# soup2 = BeautifulSoup(page2.content, 'html.parser')

# # Duration of the movie.-page-2
# d_time2 = soup2.find_all('span', class_ = "runtime")
# duration2 = []
# for dt in d_time2:
#     dur = dt.text
#     duration2.append(dur)
# #print(duration2)

# # Rating - Imdb-page2
# imdb_r2 = soup2.find_all('div', class_ = "inline-block ratings-imdb-rating")
# imdb_rating2 = []
# for ir in imdb_r2:
#     r_stars = ir.strong.text
#     imdb_rating2.append(r_stars)
# #print(imdb_rating2)

# #Rating - Metascore-page-2
# meta_r2 = soup2.find_all('div', class_ = "inline-block ratings-metascore")
# meta_rating2 =[]
# for mr in meta_r2:
#     meta_score = mr.span.text.strip()
#     meta_rating2.append(meta_score)
# #print(len(meta_rating2))

# # director-name-page2
# d_name2 = soup2.find_all('p', class_ = "")
# director_name2 =[]
# for dn in d_name2:
#     dir_name = dn.a.text.strip()
#     director_name2.append(dir_name)
# #print(director_name2)

# # Intersection of two lists.

# director = director_name+director_name2
# imdbrating = imdb_rating+imdb_rating2
# metarating = meta_rating+meta_rating2
# film_duration = duration+duration2

# print(director[51])
# print(len(director))
# print(len(imdbrating))
# print(len(metarating)) # There was no meta score for pushpa movie.
# print(len(film_duration))

# pandas data frame.














