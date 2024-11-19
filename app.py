from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/times"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLACHEMY_TRACK_MODIFICATIOS'] = False
from database import db
from flask_migrate import Migrate
from models import Jogos, Times
db.init_app(app)
migrate = Migrate(app, db)
from modulos.times.times import bp_time
app.register_blueprint(bp_time, url_prefix='/times')
from modulos.jogos.jogos import bp_jogo
app.register_blueprint(bp_jogo, url_prefix='/jogos')

@app.route('/')
def index():
    return render_template("index.html")


