from flask import Blueprint, render_template, request, redirect, flash
from models import Jogos, Times
from database import db

bp_jogo = Blueprint('jogos', __name__, template_folder="templates")

@bp_jogo.route('/')
def index():
    dados = Jogos.query.all()
    return render_template('jogo.html', jogos = dados)
    
@bp_jogo.route('/add')
def add():
    p = Times.query.all()
    return render_template('jogo_add.html', times = p)

@bp_jogo.route('/save', methods=['POST'])
def save():
    adversario = request.form.get('adversario')
    data = request.form.get('data')
    id_time = request.form.get('id_time')
    if adversario and data and id_time:
        bd_jogo = Jogos(adversario, data, id_time)
        db.session.add(bd_jogo)
        db.session.commit()
        flash('Projeto salvo com sucesso!!!')
        return redirect('/jogos')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/jogos/add')

@bp_jogo.route("/remove/<int:id>")
def remove(id):
    dados = Jogos.query.get(id)
    if id > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Jogos removido com sucesso!')
        return redirect("/jogos")
    else:
        flash("Caminho incorreto!")
        return redirect("/jogos")

@bp_jogo.route("/edita/<int:id>")
def edita(id):
    jogo = Jogos.query.get(id)
    time = Times.query.all()
    return render_template("jogo_edita.html", dados=jogo, time=time)

@bp_jogo.route("/editasave", methods=['POST'])
def editasave():
    id = request.form.get('id')
    adversario = request.form.get('adversario')
    data = request.form.get('data')
    id_time = request.form.get('id_time')
    if id and adversario and data and id_time:
        jogo = Jogos.query.get(id)
        jogo.adversario = adversario
        jogo.data = data
        jogo.id_time = id_time
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/jogos')
    else:
        flash('Dados incompletos.')
        return redirect("/jogos")