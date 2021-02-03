from app.extensions import db
from ..association.alunos_turmas_tabela import alunos_turmas_tabela

class Turma(db.Model):
    __tablename__="turmas"
    id=db.Column(db.Integer,primary_key=True)                      # id qualquer para identificar a Turma
    horário=db.Column(db.String(40),nullable=False)                # horário escrito, como otimizar?
    
    docente=db.Column(db.String(40),ForeignKey("docente.cpf"))     # recebe o nome do Professor usando a chave cpf
    matéria=db.Column(db.String(60),ForeignKey("matéria.código"))  # recebe o nome da Matéria usando a chave código

    lista_alunos=db.relationship("Aluno",secondary=alunos_turmas_tabela,backref="turmas") 
    # referência para a associacao entre alunos e turmas

    
