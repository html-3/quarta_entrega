from .extensions import db

association_table=db.Table("association",db.Model.metadata,
    db.Column("torneio",
              db.Integer,
              db.ForeignKey("torneio.id"))
    db.Column("lutadores",
              db.Integer
              db.ForeignKey("lutadores.id"))
              )