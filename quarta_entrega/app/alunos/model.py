from app.extensions import db
from ..association.alunos_turmas_tabela import alunos_turmas_tabela

class Aluno(db.Model):
    __tablename__="alunos"
    cpf_aluno=db.Column(db.Integer,primary_key=True)         # cpf torna-se a chave principal
    nome_aluno=db.Column(db.String(40),nullable=False)       # bstante espaco para nomes longos
    data_nascimento=db.Column(db.Date,nullable=False)        # nao tenho certeza se isso funciona
    sexo=db.Column(db.String(6),nullable=False)              # Homem (length=5) ou Mulher (length=6)
    período_ingresso=db.Column(db.String(6),nullable=False)  # 20XX.Y XX=[15,16,17...] Y=[1,2,3,4]
    curso=db.Column(db.String(40),nullable=False)

    lista_matérias_aluno=db.relationship("Turma",secondary=alunos_turmas_tabela,backref="alunos") 
    # cria referência para a associacao entre alunos e turmas
    
    boletim_aluno=db.relationship("Boletin",uselist=False,back_populates="alunos")
    # relacao 1-to-1 com boletins