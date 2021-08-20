from bs4 import BeautifulSoup
import requests

from csv import reader

def is_movie_streaming(movie_title, movie_year):
    movie_title = movie_title.replace(' ','-')
    movie_title = movie_title.replace(':','')
    movie_title = movie_title.lower()
    URL = "https://reelgood.com/movie/"+movie_title+"-"+movie_year
    
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    services = ["Disney+", "Tubi", "PlutoTV", "Vudu", "Prime Video", "Peacock", "Hoopla", "Plex", "Crackle"]

    for a in soup.findAll('div', title=lambda title: title and title.startswith("Stream on")):
        title = soup.findAll('title')[0]
        #print(title)
        for s in services:
            if s in str(title):
                return s, URL
        return "None",False
    return "None","Not Found"

dir = "icheckmovies_070621/"

#movie_list = "imdbs+top+250.csv"
#movie_list = "jennifer+eisss+500+essential+cult+movies.csv"
#movie_list = "time+out+london+50+essential+sci-fi+films.csv"

#standup
#TODO: merge these all into a single dict
#movie_list = "flavorwires+the+50+funniest+stand-up+specials+of+all+time.csv"
#movie_list = "stand-up+comedy+101+essential+specials+for+the+comedy+nerd.csv"
#movie_list = "splitsider+the+20+greatest+standup+specials+of+all+time.csv"
movie_list = "stand-up+comedy.csv"

title_col = 2
year_col = 3
checked_col = 12

with open(dir+movie_list, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        movie_title = row[title_col]
        movie_year = row[year_col]
        movie_checked = row[checked_col]

        if movie_checked == 'no':
            s,URL = is_movie_streaming(movie_title,movie_year)
            if URL is not False:
                if URL != "Not Found":
                    print(movie_title, s, URL)