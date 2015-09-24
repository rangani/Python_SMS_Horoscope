import urllib.request
import requests
from bs4 import BeautifulSoup
# scraping http://www.littleastro.com/


def horoscope():
   soup = BeautifulSoup(requests.get("http://www.littleastro.com/").text)
   content = soup.find('ul')
   horoscopes = content.find_all('li')
   zodiacs = []
   predictions = []
   #todaypredictions = {}

   #for signs in horoscopes:
   #   todaypredictions[signs.h3.string.split()[1]] = signs.find('p').string

   for signs in horoscopes:
      sign = signs.h3.string.split()[1]
      zodiacs.append(sign)

   for signs in horoscopes:
      prediction = signs.find('p').string
      predictions.append(prediction)


   return dict(zip(zodiacs,predictions))


def main():
   zipup = horoscope()
   print (zipup)
   for k, v in zipup.items():
      print ("Sign: ", k)
      print ("Predictions: ", v)
      #print():

if __name__ == "__main__":
   main()
