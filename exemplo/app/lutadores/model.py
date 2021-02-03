from app.extensions import db
from ..association import association_table

class Lutador(db.Model):
    __tablename__="lutadores"
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String(20),nullable=False)
    peso=db.Column(db.Integer,nullable=False)

    trofeu=db.relationship("Trofeu",backref="owner")
    #estabelece uma referencia de 1 lutador pode ter n trofeus

    torneios=db.relationship("Torneio",secondary=association_table,backref="lutadores")
    #referencia essa classe para a tabela de associacao.