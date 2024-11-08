from flask import Blueprint, render_template, request, redirect, flash
from database import db 
from models import Times

bp_time = Blueprint('times', __name__, template_folder='templates')

@bp_time.route('/')
def index():
    dados = Times.query.all()
    return render_template('time.html', dados=dados)

@bp_time.route('/add')
def add():
    return render_template('times_add.html')

@bp_time.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    cidade = request.form.get('cidade')
    if nome and cidade :
        objeto = Times(nome, cidade)
        db.session.add(objeto)
        db.session.commit()
        flash('Salvo!')
        return redirect('/times')
    else:
        flash('Preencha todos os campos!')
        return redirect('/times/add')