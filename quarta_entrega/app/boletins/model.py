from app.extensions import db

class Boletim(db.Model):
    __tablename__="boletins"
    
    cpf_aluno=db.Column(db.Interger,ForeignKey("alunos.cpf"))
    boletim_aluno=db.relationship("Aluno",uselist=False,back_populates="boletins")
    # relacao 1-to-1 com alunos, espero que esteja certo
