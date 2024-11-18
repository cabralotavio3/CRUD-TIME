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