import pandas as pd
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbhwanE


def load_list():
    house_list = []
    df = pd.read_csv("database.csv")
    for i in range(len(df)):
        house_list.append(df.iloc[i].tolist())
    print(house_list)
    return house_list

def load_naverMove():
    naver_move= []
    result = db.movies.find()

    for r in result:
        tmp = [r["ranking"],r["title"],r["point"]]
        naver_move.append(tmp)

    return naver_move

def load_kosipRank():
    kosip_list = []
    result = db.kospinews.find()

    for r in result:
        tmp = [r["KOSPI"],r["title"],r["capitalization"],r["comparison"],r["nowmoney"]]
        kosip_list.append(tmp)

    return kosip_list

def load_bugsMusic():
    music_list=[]
    result = db.music.find()

    for r in result:
        tmp = [r["ranking"], r["title"], r["artist"]]
        music_list.append(tmp)

    return music_list


def update_naverMove():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    movies = soup.select("#old_content > table > tbody > tr")

    for movie in movies:
        movie_name = movie.select_one("td.title > div > a")
        if movie_name is not None:
            movie_ranking = movie.select_one("td:nth-child(1) > img")["alt"]
            movie_title = movie_name.text
            movie_point = movie.select_one("td.point").text

            db.movies.update({"ranking": movie_ranking}, {"$set": {"title": movie_title}})
            db.movies.update({"ranking": movie_ranking}, {"$set": {"point" : movie_point}})



def update_kosipRank():
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?page=1"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    stock_list = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")

    for stock in stock_list:
         if len(stock) > 1 :
              tmp = stock.get_text().split()
              db.kospinews.update({"ranking": tmp[0]}, {"$set": {"title": tmp[1]}})
              db.kospinews.update({"ranking": tmp[0]}, {"$set": {"capitalization": tmp[6]}})
              db.kospinews.update({"ranking": tmp[0]}, {"$set": {"comparison": tmp[4]}})
              db.kospinews.update({"ranking": tmp[0]}, {"$set": {"nowmoney": tmp[2]}})


def update_bugsMusic():
    data = requests.get('https://music.bugs.co.kr/chart')
    soup = BeautifulSoup(data.text, 'html.parser')
    rank_lists = soup.select('.list > tbody > tr')

    for rank_list in rank_lists:
        ranking = rank_list.select_one('td > div.ranking > strong').text
        m_title = rank_list.select_one('th > .title > a').text
        m_artist = rank_list.select_one('td.left > .artist > a').text

        db.music.update({"ranking": ranking}, {"$set": {"title": m_title}})
        db.music.update({"ranking": ranking}, {"$set": {"artist": m_artist}})



def set_naverMove():
    result = db.movies.find()
    tmp = 0
    for r in result:
        tmp +=1

    if tmp < 2:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)

        soup = BeautifulSoup(data.text, 'html.parser')

        movies = soup.select("#old_content > table > tbody > tr")

        for movie in movies:
            movie_name = movie.select_one("td.title > div > a")
            if movie_name is not None:
                movie_ranking = movie.select_one("td:nth-child(1) > img")["alt"]
                movie_title = movie_name.text
                movie_point = movie.select_one("td.point").text

                put_data = {
                    'ranking': movie_ranking,
                    'title': movie_title,
                    'point': movie_point
                }
                db.movies.insert_one(put_data)


def set_kosipRank():
    result = db.kospinews.find()
    tmp = 0
    for r in result:
        tmp += 1
    if tmp < 2:
        url = "https://finance.naver.com/sise/sise_market_sum.nhn?page=1"

        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

        stock_list = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")

        for stock in stock_list:
             if len(stock) > 1 :
                  tmp = stock.get_text().split()
                  put_data = {
                      'KOSPI': tmp[0],
                      'title': tmp[1],
                      'capitalization': tmp[6],
                      'comparison' : tmp[4],
                      'nowmoney' : tmp[2]
                  }
                  db.kospinews.insert_one(put_data)

def set_bugsMusic():
    result = db.music.find()
    tmp = 0
    for r in result:
        tmp +=1

    if tmp < 2:
        data = requests.get('https://music.bugs.co.kr/chart')
        soup = BeautifulSoup(data.text, 'html.parser')
        rank_lists = soup.select('.list > tbody > tr')

        for rank_list in rank_lists:
            ranking = rank_list.select_one('td > div.ranking > strong').text
            m_title = rank_list.select_one('th > .title > a').text
            m_artist = rank_list.select_one('td.left > .artist > a').text

            put_data = {
                'ranking': ranking,
                'title': m_title,
                'artist': m_artist
            }
            db.music.insert_one(put_data)


if __name__ =="__main__":
    load_list()