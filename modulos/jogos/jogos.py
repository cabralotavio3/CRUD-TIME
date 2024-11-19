from flask import Blueprint, render_template, request, redirect, flash
from database import db 
from models import Times, Jogos

bp_jogo = Blueprint('jogos', __name__, template_folder='templates')

@bp_jogo.route('/')
def index():
    j = Jogos.query.all()
    t = Times.query.all()
    return render_template('jogos.html', jogos=j, times=t)

@bp_jogo.route('/add')
def add():
    t = Times.query.all()
    return render_template('jogos_add.html', times=t)

@bp_jogo.route('/save', methods=['POST'])
def save():
    time_id = request.form.get('time_id')
    adversario = request.form.get('adversario')
    data = request.form.get('data')
    if time_id and adversario and data:
        objeto = Jogos(time_id, adversario ,data)
        db.session.add(objeto)
        db.session.commit()
        flash('Salvo!')
        return redirect('/jogos')
    else:
        flash('Preencha todos os campos!')
        return redirect('/jogos/add')
    

@bp_jogo.route("/remove/<int:id>")
def remove(id):
    dados = Jogos.query.get(id)
    if id > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Jogo removido com sucesso!')
        return redirect("/jogos")
    else:
        flash("Caminho incorreto!")
        return redirect("/jogos")

@bp_jogo.route("/edita/<int:id>")
def edita(id):
    j = Jogos.query.get(id)
    t = Times.query.all()
    return render_template("jogos_edita.html", jogo=j, time=t)

@bp_jogo.route("/editasave", methods=['POST'])
def editasave():
    id = request.form.get('id')
    adversario = request.form.get('adversario')
    data = request.form.get('data')
    id_time = request.form.get('id_paciente')
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