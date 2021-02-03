from app.extensions import db
from ..association.alunos_turmas_tabela import professores_matérias_tabela

class Professor(db.Model):
    __tablename__="professores"
    cpf_professor=db.Column(db.Integer,primary_key=True)        # CPF torna-se a chave principal
    nome_professor=db.Column(db.String(40),nullable=False)      # bastante espaco para nomes longos
    formacao=db.Column(db.String(60),nullable=False)            # bastante espaco para formacao acadêmica

    turmas_docente=db.relationship("Turma",backref="docente")  # referência para as turmas do Professor ou docente

    lista_matérias_docente=db.relationship("Matéria",secondary=professores_matérias_tabela,backref="docente") 
    # cria referência para a associacao entre professores e matérias


