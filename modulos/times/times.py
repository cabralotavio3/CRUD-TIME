from flask import Blueprint, render_template, request, redirect, flash
from models import Times
from database import db

bp_time = Blueprint('times', __name__, template_folder="templates")

@bp_time.route('/')
def index():
    dados = Times.query.all()
    return render_template('time.html', times = dados)
    
@bp_time.route('/add')
def add():
    return render_template('time_add.html')

@bp_time.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    cidade = request.form.get('cidade')
    if nome and cidade:
        bd_time = Times(nome, cidade)
        db.session.add(bd_time)
        db.session.commit()
        flash('Time salvo com sucesso!!!')
        return redirect('/times')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/times/add')
    
@bp_time.route("/remove/<int:id>")
def remove(id):
    dados = Times.query.get(id)
    if id > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Paciente removido com sucesso!')
        return redirect("/times")
    else:
        flash("Caminho incorreto!")
        return redirect("/times")

@bp_time.route("/edita/<int:id>")
def edita(id):
    time = Times.query.get(id)
    return render_template("time_edita.html", dados=time)

@bp_time.route("/editasave", methods=['POST'])
def editasave():
    id = request.form.get('id')
    nome = request.form.get('nome')
    cidade = request.form.get('cidade')
    if id and nome and cidade:
        jogo = Times.query.get(id)
        jogo.nome = nome
        jogo.cidade = cidade
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/times')
    else:
        flash('Dados incompletos.')
        return redirect("/times")