
import requests
from bs4 import BeautifulSoup, NavigableString, Tag

def plantFinder(scientific_name):
    try:
        a,b = scientific_name.split(' ')
        url = "https://www.missouribotanicalgarden.org/PlantFinder/PlantFinderProfileResults.aspx?basic={}%20{}".format(a,b)
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        div = soup.find('table', {'class': 'results'})
        res  = div.find('div',{'class':'row'})
        out = res.text.split(':')[1].strip()
        print(out)
        return out
    except:
        return "Not Found"

# print(plantFinder("abies concolor"))