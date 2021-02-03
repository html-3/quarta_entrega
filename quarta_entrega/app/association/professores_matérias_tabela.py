from ..extensions import db

professores_matérias_tabela=db.Table("Professores_Matérias",db.Model.metadata,
    db.Column("professor",
              de.String(40),
              db.ForeignKey("docente.cpf")),
    db.Column("matéria",
               db.String(60),
               db.ForeignKey("matéria.código"))
               )