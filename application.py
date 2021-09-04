from flask import Flask, render_template, request, redirect, url_for
import sys
application = Flask(__name__)
import database

@application.route("/")
def hello():
    return render_template("rankView.html")

@application.route("/list")
def list():
    house_list = database.load_list()
    length = len(house_list)
    return render_template("list.html",house_list=house_list,length=length)

@application.route("/naverMovie")
def naverMovie():
    naver_movie_list = database.load_naverMove()
    return render_template("naverMovie.html",naver_movie_list=naver_movie_list)


@application.route("/kospinews")
def kospinews():
    kospi_list = database.load_kosipRank()
    return render_template("kospinews.html",kospi_list=kospi_list)


@application.route("/bugsMusic")
def bugsMusic():
    music_list = database.load_bugsMusic()
    return render_template("bugsMusic.html",music_list=music_list)


@application.route("/getRank")
def getRank():
    database.set_kosipRank()
    database.set_naverMove()
    database.set_bugsMusic()
    return redirect(url_for("hello"))

@application.route("/update")
def update():
    database.update_kosipRank()
    database.update_naverMove()
    database.update_bugsMusic()
    return redirect(url_for("hello"))

if __name__ == "__main__":
    application.run()