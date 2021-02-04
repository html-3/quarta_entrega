from app.extensions import db

class Boletim(db.Model):
    __tablename__="boletins"
    id=db.Column(db.Integer,primary_key=True)
    notas=db.Column(db.Float,nullable=False)

    boletim_aluno=db.relationship("Aluno",uselist=False,back_populates="boletins")
    # relacao 1-to-1 com alunos, espero que esteja certo
