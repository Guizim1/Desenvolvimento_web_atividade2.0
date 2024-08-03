import sqlite3
from model2 import *

# Classe Tabela (superclasse):
class Tabela:
    def __init__(self) -> None:
        self.module = sqlite3
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()

# Classe PersonGrupo:
class PersonGrupo(Tabela):
    def __init__(self) -> None:
        super().__init__()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS PersonGrupo(
            id_perso INTEGER,
            id_grup INTEGER,
            PRIMARY KEY (id_perso, id_grup),
            FOREIGN KEY (id_perso) REFERENCES Personagem(id_person) ON DELETE CASCADE,
            FOREIGN KEY (id_grup) REFERENCES Grupos(id_Grupo) ON DELETE CASCADE
        );
        """)
        self.conn.close()

    def add_person_grupo(self, id_perso: int, id_grup: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO PersonGrupo(id_perso, id_grup)
            VALUES(?, ?);
        """, (id_perso, id_grup))
        self.conn.commit()
        self.conn.close()

    def select_associacao_person_grupo(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM PersonGrupo;")
        associacoes = []
        for associacao in self.cursor.fetchall():
            associacoes.append({
                'id_perso': associacao[0],
                'id_grup': associacao[1]
            })
        self.conn.close()
        return associacoes

    def select_registro_person_grupo(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        SELECT P.*, G.*
        FROM Personagem AS P
        INNER JOIN PersonGrupo AS PG ON P.id_person = PG.id_perso
        INNER JOIN Grupos AS G ON G.id_Grupo = PG.id_grup;
        """)
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                "id_person": registro[0],
                "nome_person": registro[1],
                "poder_person": registro[2],
                "arma_person": registro[3],
                "forca_person": registro[4],
                "agilidade_person": registro[5],
                "nivel_person": registro[6],
                "id_grup": registro[7],
                "nome_Grupo": registro[8],
                "quant_membros": registro[9]
            })
        self.conn.close()
        return registros

# Classe PersonMiss:
class PersonMiss(Tabela):
    def __init__(self) -> None:
        super().__init__()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS PersonMiss(
            id_perso INTEGER,
            id_miss INTEGER,
            PRIMARY KEY (id_perso, id_miss),
            FOREIGN KEY (id_perso) REFERENCES Personagem(id_person) ON DELETE CASCADE,
            FOREIGN KEY (id_miss) REFERENCES Missoes(id_mis) ON DELETE CASCADE
        );
        """)
        self.conn.close()

    def add_person_miss(self, id_perso: int, id_miss: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO PersonMiss(id_perso, id_miss)
            VALUES(?, ?);
        """, (id_perso, id_miss))
        self.conn.commit()
        self.conn.close()

    def select_associacao_person_miss(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM PersonMiss;")
        associacoes = []
        for associacao in self.cursor.fetchall():
            associacoes.append({
                'id_perso': associacao[0],
                'id_miss': associacao[1]
            })
        self.conn.close()
        return associacoes

    def select_registro_person_miss(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        SELECT P.*, M.*
        FROM Personagem AS P
        INNER JOIN PersonMiss AS PM ON P.id_person = PM.id_perso
        INNER JOIN Missoes AS M ON M.id_mis = PM.id_miss;
        """)
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                "id_person": registro[0],
                "nome_person": registro[1],
                "poder_person": registro[2],
                "arma_person": registro[3],
                "forca_person": registro[4],
                "agilidade_person": registro[5],
                "nivel_person": registro[6],
                "id_miss": registro[7],
                "objetivo_mis": registro[8],
                "descricao_mis": registro[9],
                "recompensa": registro[10]
            })
        self.conn.close()
        return registros

# Classe PersonGene:
class PersonGene(Tabela):
    def __init__(self) -> None:
        super().__init__()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS PersonGene(
            id_perso INTEGER,
            id_gene INTEGER,
            PRIMARY KEY (id_perso, id_gene),
            FOREIGN KEY (id_perso) REFERENCES Personagem(id_person) ON DELETE CASCADE,
            FOREIGN KEY (id_gene) REFERENCES Genero(id_gene) ON DELETE CASCADE
        );
        """)
        self.conn.close()

    def add_person_gene(self, id_perso: int, id_gene: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO PersonGene(id_perso, id_gene)
            VALUES(?, ?);
        """, (id_perso, id_gene))
        self.conn.commit()
        self.conn.close()

    def select_associacao_person_gene(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM PersonGene;")
        associacoes = []
        for associacao in self.cursor.fetchall():
            associacoes.append({
                'id_perso': associacao[0],
                'id_gene': associacao[1]
            })
        self.conn.close()
        return associacoes

    def select_registro_person_gene(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        SELECT P.*, G.*
        FROM Personagem AS P
        INNER JOIN PersonGene AS PG ON P.id_person = PG.id_perso
        INNER JOIN Genero AS G ON G.id_gene = PG.id_gene;
        """)
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                "id_person": registro[0],
                "nome_person": registro[1],
                "poder_person": registro[2],
                "arma_person": registro[3],
                "forca_person": registro[4],
                "agilidade_person": registro[5],
                "nivel_person": registro[6],
                "id_gene": registro[7],
                "tipo_gene": registro[8]
            })
        self.conn.close()
        return registros

# Objetos de cada tabela:
obj_person_grupo = PersonGrupo()
obj_person_miss = PersonMiss()
obj_person_gene = PersonGene()
