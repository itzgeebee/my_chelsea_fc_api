from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_bootstrap import Bootstrap
from datetime import date
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from raw_data import RawData

app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['SECRET_KEY'] = "secretkey"
Bootstrap(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///testing.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLES


class Players(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(250), nullable=False)
    nationality = db.Column(db.String(250), nullable=False)
    position = db.Column(db.String(3), nullable=False)
    career_years = db.Column(db.String(12), nullable=False)
    appearance = db.Column(db.Integer, nullable=False)
    goals = db.Column(db.Integer, nullable=False)
    wikipedia_article = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class POTY(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(250), nullable=False)
    win_year = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class GOTY(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(250), nullable=False)
    win_year = db.Column(db.Integer, nullable=False)
    against = db.Column(db.String(250), nullable=False)
    scored = db.Column(db.String(5), nullable=False)
    result = db.Column(db.String(5), nullable=False)
    stadium = db.Column(db.String(250), nullable=False)
    competition = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Captains(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(5), nullable=False)
    years = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class FWA_Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(5), nullable=False)
    year = db.Column(db.String(6), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Titles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    honour = db.Column(db.String(250), nullable=False)
    years = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class GoldenBoot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(250), nullable=False)
    year = db.Column(db.String(6), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class GoldenGlove(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(250), nullable=False)
    year = db.Column(db.String(6), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/all")
def all_players():
    players = Players.query.all()

    every_player = []
    for i in players:
        play = i.to_dict()
        every_player.append(play)

    every_player_json = jsonify(player=every_player).json
    return every_player_json


@app.route("/club-poty")
def poty_players():
    players = POTY.query.all()

    every_player = []
    for i in players:
        play = i.to_dict()
        every_player.append(play)

    every_player_json = jsonify(player=every_player).json
    return every_player_json


@app.route("/club-goty")
def goty():
    players = GOTY.query.all()

    every_goal = []
    for i in players:
        play = i.to_dict()
        every_goal.append(play)

    every_goal_json = jsonify(goals=every_goal).json
    return every_goal_json


@app.route("/captains")
def captain():
    players = Captains.query.all()

    every_player = []
    for i in players:
        play = i.to_dict()
        every_player.append(play)

    every_player_json = jsonify(player=every_player).json
    return every_player_json


@app.route("/epl-poty")
def epl_poty():
    players = FWA_Player.query.all()

    every_player = []
    for i in players:
        play = i.to_dict()
        every_player.append(play)

    every_player_json = jsonify(player=every_player).json
    return every_player_json


@app.route("/golden-boot")
def golden_boot():
    players = GoldenBoot.query.all()

    every_player = []
    for i in players:
        play = i.to_dict()
        every_player.append(play)

    every_player_json = jsonify(player=every_player).json
    return every_player_json


@app.route("/golden-glove")
def golden_glove():
    players = GoldenGlove.query.all()

    every_player = []
    for i in players:
        play = i.to_dict()
        every_player.append(play)

    every_player_json = jsonify(player=every_player).json
    return every_player_json


@app.route("/titles")
def titles():
    title = Titles.query.all()
    every_title = []
    for i in title:
        play = i.to_dict()
        every_title.append(play)

    every_title_json = jsonify(titles=every_title).json
    return every_title_json


@app.route("/search")
def search():
    player = request.args.get("player")
    ploty = request.args.get("poty")
    goalty = request.args.get("goty")
    skipper = request.args.get("captain")
    epl_player_year = request.args.get("epl-poty")
    title_wins = request.args.get("trophies")
    gb = request.args.get("golden-boot")
    gg = request.args.get("golden-gloves")

    if player:
        query_result = db.session.query(Players).filter(
            Players.player_name.like(f"{player}%") | Players.nationality.like(f"{player}%") | Players.position.like(
                f"{player}%")
            | Players.career_years.like(f"{player}%") | Players.appearance.like(f"{player}%")
            | Players.goals.like(f"{player}%"))

    elif ploty:
        query_result = db.session.query(POTY).filter(
            POTY.player_name.like(f"{ploty}%") | POTY.win_year.like(f"{ploty}%"))

    elif goalty:
        query_result = db.session.query(GOTY).filter(
            GOTY.player_name.like(f"{goalty}%") | GOTY.win_year.like(f"{goalty}%")
            | GOTY.against.like(f"{goalty}%") | GOTY.scored.like(f"{goalty}%") |
            GOTY.result.like(f"{goalty}%") | GOTY.stadium.like(f"{goalty}%") |
            GOTY.competition.like(f"{goalty}%")
        )

    elif skipper:
        query_result = db.session.query(Captains).filter(
            Captains.player_name.like(f"{skipper}%") | Captains.years.like(f"{skipper}%"))

    elif epl_player_year:
        query_result = db.session.query(FWA_Player).filter(
            FWA_Player.player_name.like(f"{epl_player_year}%") | FWA_Player.year.like(f"{epl_player_year}%"))

    elif title_wins:
        query_result = db.session.query(Titles).filter(
            Titles.honour.like(f"{titles}%") | Titles.years.like(f"{titles}%"))

    elif gb:
        query_result = db.session.query(GoldenBoot).filter(
            GoldenBoot.player_name.like(f"{gb}%") | GoldenBoot.year.like(f"{gb}%"))

    elif gg:
        query_result = db.session.query(GoldenGlove).filter(
            GoldenGlove.player_name.like(f"{gg}%") | GoldenGlove.year.like(f"{gg}%"))

    else:
        return jsonify({"error": {
            "Not found": "Sorry, page not found, check that the url is correct"
        }}), 404




    result_list = []
    for i in query_result:
        rez = i.to_dict()
        result_list.append(rez)
    print(result_list)

    if not result_list:
        return jsonify({"error": {
            "Not found": "Sorry, nothing in our database matches your search"
        }}), 404
    else:
        query_result_json = jsonify(results=result_list).json
        return query_result_json


@app.route("/add", methods=["POST"])
def add():
    new_player = request.args.get("new-player")
    print(new_player)
    return jsonify({"message": {"new player added"}})

if __name__ == "__main__":
    app.run(debug=True)
