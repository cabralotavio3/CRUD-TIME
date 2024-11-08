from database import db

class Times(db.Model):
    __tablename__ = 'time'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade

    def __repr__(self):
        return '<Times {}>'.format(self.nome)


    
class Jogos(db.Model):
    __tablename__ = 'jogo'
    id = db.Column(db.Integer, primary_key = True)
    time_id = db.Column(db.Integer, db.ForeignKey('time.id'))
    adversario = db.Column(db.String(100))
    data = db.Column(db.Date)

    time = db.relationship('Times', foreign_keys = time_id)

    def __init__(self, time_id, adversario, data):
        self.time_id = time_id
        self.adversario = adversario
        self.data = data

    def __repr__(self):
        return '<Jogos {} X {} - {}>'.format(self.time.nome, self.adversario, self.data)
    