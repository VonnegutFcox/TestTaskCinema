import csv
import requests
from bs4 import BeautifulSoup
import json


class FilmSearch:
    URL = 'https://www.amediateka.ru/movies'
    PAGE = requests.get(URL)
    SOUP = BeautifulSoup(PAGE.text, 'html.parser')

    def json_return(self):
        all_movie_div_tags = self.SOUP.find_all('script')
        jsonData = json.loads(all_movie_div_tags[17].contents[0])
        jsonData = jsonData["props"]["pageProps"]["data"]["results"]
        return jsonData

    def to_cvs(self):
        with open("moviestats.csv", 'w', encoding='utf-8') as a_file:
            file_writer = csv.writer(
                a_file,
                delimiter=";",
                lineterminator="\r"
            )
            jsonData = self.json_return()
            for movie in jsonData:
                name = movie["title"]
                genres = ",".join(
                    [i["name"] for i in movie["genres"]]
                )
                file_writer.writerow([name, genres])


if __name__ == "__main__":
    a = FilmSearch()
    a.to_cvs()
