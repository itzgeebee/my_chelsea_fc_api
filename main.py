from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from tinydb import TinyDB
import os
# from raw_data import RawData

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL', "sqlite:///testing.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


small_db = TinyDB("small_db.json")
auth = HTTPBasicAuth()
get_usr_data = small_db.all()
user_data = get_usr_data[0]


@auth.verify_password
def verify_password(username, password):
    if username in user_data and \
            check_password_hash(user_data.get(username), password):
        return username


##CONFIGURE TABLES
class Players(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(250), nullable=False)
    nationality = db.Column(db.String(250), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    career_years = db.Column(db.String(30), nullable=False)
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
    scored = db.Column(db.String(20), nullable=False)
    result = db.Column(db.String(20), nullable=False)
    stadium = db.Column(db.String(250), nullable=False)
    competition = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Captains(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(250), nullable=False)
    years = db.Column(db.String(30), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class FWA_Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(250), nullable=False)
    year = db.Column(db.String(30), nullable=False)

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
    year = db.Column(db.String(30), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class GoldenGlove(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(250), nullable=False)
    year = db.Column(db.String(30), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# db.create_all()
# try:
#     num_rows_deleted = db.session.query(Players).delete()
#     db.session.commit()
# except:
#     db.session.rollback()
# data_upload = RawData()
# data_upload.transfer_to_db(pl=Players, po=POTY, go=GOTY, cp=Captains, fw=FWA_Player,
#                             gdb=GoldenBoot, gdg=GoldenGlove, db=db, ti=Titles)

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
            )

    elif ploty:
        query_result = db.session.query(POTY).filter(
            POTY.player_name.like(f"{ploty}%"))

    elif goalty:
        query_result = db.session.query(GOTY).filter(
            GOTY.player_name.like(f"{goalty}%")
            | GOTY.against.like(f"{goalty}%")
            | GOTY.stadium.like(f"{goalty}%") |
            GOTY.competition.like(f"{goalty}%")
        )

    elif skipper:
        query_result = db.session.query(Captains).filter(
            Captains.player_name.like(f"{skipper}%"))

    elif epl_player_year:
        query_result = db.session.query(FWA_Player).filter(
            FWA_Player.player_name.like(f"{epl_player_year}%"))

    elif title_wins:
        query_result = db.session.query(Titles).filter(
            Titles.honour.like(f"{titles}%"))

    elif gb:
        query_result = db.session.query(GoldenBoot).filter(
            GoldenBoot.player_name.like(f"{gb}%"))

    elif gg:
        query_result = db.session.query(GoldenGlove).filter(
            GoldenGlove.player_name.like(f"{gg}%"))

    else:
        return jsonify({"error": {
            "Not found": "Sorry, page not found, check that the url is correct"
        }}), 404

    result_list = []
    for i in query_result:
        rez = i.to_dict()
        result_list.append(rez)

    if not result_list:
        return jsonify({"error": {
            "Not found": "Sorry, nothing in our database matches your search"
        }}), 404
    else:
        query_result_json = jsonify(results=result_list).json
        return query_result_json


@app.route("/add-new-player", methods=["POST"])
def add_new_player():
    new_player = Players(
        player_name=request.form.get("player-name"),
        nationality=request.form.get("nationality"),
        position=request.form.get("position"),
        career_years=request.form.get("career_years"),
        appearance=request.form.get("appearance"),
        goals=request.form.get("goals"),
        wikipedia_article=request.form.get("wikipedia-link")
    )
    db.session.add(new_player)
    db.session.commit()

    return jsonify({"response:": {"success": "new player added"}})


@app.route("/add-new-poty", methods=["POST"])
def add_new_poty():
    new_poty = POTY(
        player_name=request.form.get("player-name"),
        win_year=request.form.get("win-year")
    )
    db.session.add(new_poty)
    db.session.commit()

    return jsonify({"response:": {"success": "new player added"}})


@app.route("/add-new-captain", methods=["POST"])
def add_new_captain():
    new_goty = Captains(
        player_name=request.form.get("player-name"),
        years=request.form.get("years")
    )
    db.session.add(new_goty)
    db.session.commit()

    return jsonify({"response:": {"success": "new player added"}})


@app.route("/add-new-goty", methods=["POST"])
def add_new_goty():
    new_goty = GOTY(
        player_name=request.form.get("player-name"),
        win_year=request.form.get("win-year"),
        against=request.form.get("opponent"),
        scored=request.form.get("scoreline"),
        result=request.form.get("game-result"),
        stadium=request.form.get("stadium"),
        competition=request.form.get("competition")
    )
    db.session.add(new_goty)
    db.session.commit()

    return jsonify({"response:": {"success": "new player added"}})


@app.route("/add-new-eplpoty", methods=["POST"])
def add_new_eplpoty():
    new_eplpoty = FWA_Player(
        player_name=request.form.get("player-name"),
        year=request.form.get("win-year")
    )
    db.session.add(new_eplpoty)
    db.session.commit()

    return jsonify({"response:": {"success": "new player added"}})


@app.route("/add-new-title", methods=["POST"])
def add_new_title():
    new_title = Titles(
        honour=request.form.get("player-name"),
        years=request.form.get("win-year"),
    )
    db.session.add(new_title)
    db.session.commit()

    return jsonify({"response:": {"success": "new player added"}})


@app.route("/add-new-gbwinner", methods=["POST"])
def add_new_gb():
    new_gb = GoldenBoot(
        player_name=request.form.get("player-name"),
        win_year=request.form.get("win-year"),
    )
    db.session.add(new_gb)
    db.session.commit()

    return jsonify({"response:": {"success": "new player added"}})


@app.route("/add-new-ggwinner", methods=["POST"])
def add_new_gg():
    new_gg = GoldenGlove(
        player_name=request.form.get("player-name"),
        win_year=request.form.get("win-year"),
    )
    db.session.add(new_gg)
    db.session.commit()

    return jsonify({"response:": {"success": "new player added"}})


@app.route("/update-player-profile/<int:player_id>", methods=["GET", "PUT"])
def update_player(player_id):
    player_to_update = Players.query.get(player_id)
    if player_to_update:
        total_goals = request.args.get("goals")
        total_appearances = request.args.get("appearances")
        career = request.args.get("career")
        if total_goals:
            player_to_update.goals = total_goals
        elif total_appearances:
            player_to_update.appearance = total_appearances
        elif career:
            player_to_update.career_years = career
        else:
            return jsonify({"error": {
                "Not a valid url": "Kindly check the url and try again"
            }}), 404
    else:
        return jsonify({"error": {
            "Not found": "Sorry, a player with that id was not found in the database"
        }}), 404
    return jsonify({"success": "Successfully updated the price"})


@app.route("/delete", methods=["GET", "DELETE"])
@auth.login_required()
def delete_entry():
    del_ = None

    player_to_delete = request.args.get("player_id")
    poty_to_delete = request.args.get("poty_id")
    goty_to_delete = request.args.get("goty_id")
    captain_to_delete = request.args.get("captain_id")
    eplplayer_to_delete = request.args.get("eplplayer_id")
    title_to_delete = request.args.get("title_id")
    gb_to_delete = request.args.get("gb_id")
    gg_to_delete = request.args.get("gg_id")

    if player_to_delete:
        del_= Players.query.get(player_to_delete)

    elif poty_to_delete:
        del_= Players.query.get(poty_to_delete)

    elif goty_to_delete:
        del_= Players.query.get(goty_to_delete)

    elif player_to_delete:
        del_= Players.query.get(player_to_delete)

    elif captain_to_delete:
        del_= Players.query.get(captain_to_delete)

    elif eplplayer_to_delete:
        del_= Players.query.get(eplplayer_to_delete)

    elif title_to_delete:
        del_= Players.query.get(title_to_delete)

    elif gb_to_delete:
        del_= Players.query.get(gb_to_delete)

    elif gg_to_delete:
        del_= Players.query.get(gg_to_delete)

    else:
        return jsonify({"error": {
            "Not found": "Sorry, nothing with that id was not found in the database"
        }}), 404

    if del_:
        db.session.delete(del_)
        db.session.commit()
        return jsonify({"success":"deleted successfully"})
    else:
        return jsonify({"error": {
            "Not found": "Sorry, nothing with that id was not found in the database"
        }}), 404


if __name__ == "__main__":
    app.run(debug=True)
