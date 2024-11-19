from database import db

class Times(db.Model):
    __tablename__ = 'time'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    cidade = db.Column(db.String(50))

    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade

    def __repr__(self):
        return "<Time {}>".format(self.nome)

class Jogos(db.Model):
    __tablename__ = 'jogo'
    id = db.Column(db.Integer, primary_key = True)
    adversario = db.Column(db.String(100))
    data = db.Column(db.Date)
    id_time = db.Column(db.Integer, db.ForeignKey('time.id'))
    
    time = db.relationship('Times', foreign_keys=id_time)

    def __init__(self, adversario, data, id_time):
        self.adversario = adversario
        self.data = data
        self.id_time = id_time

    def __repr__(self):
        return "<Jogos {}>".format(self.adversario)