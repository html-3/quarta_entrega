from app.extensions import db
from ..association.alunos_turmas_tabela import alunos_turmas_tabela

class Matéria(db.Model):
    __tablename__="matérias"
    código=db.Column(db.String(6),primary_key=True)       # código da matéria se torna chave principal
    nome_matéria=db.Column(db.String(60),nullable=False)  # Bastante espaco para nomes das matérias

    turmas=db.relationship("Turma",backref="matéria")     # referência para a Matéria de cada Turma

    docentes=db.relationship("Professor",secondary=professores_matérias_tabela,backref="matéria") 
    # cria referência para a associacao entre professores e matérias

    
