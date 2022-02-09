import requests 
import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup

######################################################################################################################

url1 = 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&view=advanced'
page1 = requests.get(url1)
soup1 = BeautifulSoup(page1.content, 'html.parser')
genreList_1st_50 = []
starList_1st_50 = []
dateList_1st_50 = []

########################################################################################################################

url2 = 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&start=51&ref_=adv_nxt'
page2 = requests.get(url2)
soup2 = BeautifulSoup(page2.content, 'html.parser')
genreList_2nd_50 = []
starList_2nd_50 = []
dateList_2nd_50 = []

###########################################################################################################################

genres_1st_50 = soup1.find_all('span', class_="genre")
for genre_1st_50 in genres_1st_50:
    genreName_1st_50 = genre_1st_50.text
    genreName_1st_50 = genreName_1st_50.strip()
    genreList_1st_50.append(genreName_1st_50)


genres_2nd_50 = soup2.find_all('span', class_="genre")
for genre_2nd_50 in genres_2nd_50:
    genreName_2nd_50 = genre_2nd_50.text
    genreName_2nd_50 = genreName_2nd_50.strip()
    genreList_2nd_50.append(genreName_2nd_50)


##########################################################################################################################

stars_1st_50 = soup1.find_all('p', class_="")
for star1 in stars_1st_50:
    starsName1 = star1
    starsName1 = starsName1.text
    starsName1 = starsName1.strip()
    starsName1 = starsName1.replace('\n', '')
    starsName1 = starsName1.split('Stars:')[1]
    starList_1st_50.append(starsName1)


stars_2nd_50 = soup2.find_all('p', class_="")
for star2 in stars_2nd_50:
    starsName2 = star2
    starsName2 = starsName2.text
    starsName2 = starsName2.strip()
    starsName2 = starsName2.replace('\n', '')
    starsName2 = starsName2.split('Stars:')[1]
    starList_1st_50.append(starsName2)

##########################################################################################################################

genreListFinal = genreList_1st_50 + genreList_2nd_50
starListFinal = starList_1st_50 + starList_2nd_50

##########################################################################################################################

data = {'GENRE' : genreListFinal, 'STARS' : starListFinal}


table = pd.DataFrame(data)
print(table)






