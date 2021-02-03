from ..extensions import db

alunos_turmas_tabela=db.Table("Alunos_Turmas",db.Model.metadata,
    db.Column("aluno",
              de.String(40),
              db.ForeignKey("aluno.cpf")),
    db.Column("turma",
               db.Integer,
               db.ForeignKey("turma.id"))
               )