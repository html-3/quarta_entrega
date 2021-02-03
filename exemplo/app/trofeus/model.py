from ..extensions import db

class Trofeu(db.Model):
    __tablename__="trofeus"
    id=db.Column(db.Integer,primary_key=True)
    tipo=db.Column(db.String,nullable=False)

    lutador_id=db.Column(db.Integer,db.ForeignKey("lutadores.id"))
    #ForeignKey corresponde ao nome da tabela e a coluna a ser citada
    #entende-se como uma importacao de dados usando os ids dos lutadores

    #self.owner.name
    #referencia o nome do dono daquela linha trofeu pelo "owner"

    #def json():
    #    return{
    #        "owner":self.owner.json()
    #    }
    #o próprio valor do dicionário vai ter uma funcao para devolver determindo dado dum lutador