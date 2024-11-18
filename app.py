from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdt435t4654756h3q3464756y'
conexao = 'mysql+pymysql://alunos:cefetmg@127.0.0.1/time'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
db.init_app(app)
migrate = Migrate(app, db)
from models import Times, Jogos
from modulos.times.times import bp_time
from modulos.jogos.jogos import bp_jogo

app.register_blueprint(bp_time, url_prefix='/times')
app.register_blueprint(bp_jogo, url_prefix='/jogos')

@app.route('/')
def index():
    return render_template('ola.html')