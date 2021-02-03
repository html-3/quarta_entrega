from app.extensions import db
from ..association import association_table

class Torneio(db.Model):
    __tablename__="torneios"
    id=db.Column(db.Integer,primary_key=True)
    modalidade=db.Column(db.String(20),nullable=False)

    lutadores=db.relationship("Lutadores",secondary=association_table,backref="torneios")
    #referencia essa classe para a tabela de associacao.