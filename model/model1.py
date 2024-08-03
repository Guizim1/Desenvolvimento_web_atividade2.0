# Importando o módulo que fornece uma DB-API
import sqlite3

# Criando as classes:

# Classe Tabela (superclasse):
class Tabela:
    def __init__(self) -> None:
        self.module = sqlite3
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()

# Classe Personagem:
class Personagem(Tabela):
    def __init__(self) -> None:
        super().__init__()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Personagem(
            id_person INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_person VARCHAR(30) NOT NULL,
            poder_person VARCHAR(30) NOT NULL,
            arma_person VARCHAR(30) NOT NULL,
            forca_person INTEGER NOT NULL,
            agilidade_person INTEGER NOT NULL,
            nivel_person INTEGER NOT NULL
            );
        """)
        self.conn.close()

    def add_personagem(self, nome: str, poder: str, arma: str, forca: int, agilidade: int, nivel: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
        INSERT INTO Personagem(nome_person, poder_person, arma_person, forca_person, agilidade_person, nivel_person)
        VALUES('{nome}', '{poder}', '{arma}', {forca}, {agilidade}, {nivel});
        """)
        self.conn.commit()
        self.conn.close()

    def select_personagens(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Personagem;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_person': registro[1],
                'poder_person': registro[2],
                'arma_person': registro[3],
                'forca_person': registro[4],
                'agilidade_person': registro[5],
                'nivel_person': registro[6]
            })
        self.conn.close()
        return registros

    def del_personagem(self, id: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"DELETE FROM Personagem WHERE id_person = {id};")
        self.conn.commit()
        self.conn.close()

    def update_personagem(self, id: int, nome: str, poder: str, arma: str, forca: int, agilidade: int, nivel: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            UPDATE Personagem SET nome_person = '{nome}', poder_person = '{poder}', arma_person = '{arma}', forca_person = {forca}, agilidade_person = {agilidade}, nivel_person = {nivel}
            WHERE id_person = {id};
            """)
        self.conn.commit()
        self.conn.close()

# Classe Grupos:
class Grupos(Tabela):
    def __init__(self) -> None:
        super().__init__()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Grupos(
            id_Grupo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_Grupo VARCHAR(30) NOT NULL,
            quant_membros INTEGER NOT NULL
            );
        """)
        self.conn.close()

    def add_grupo(self, nome: str, quant_membros: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
        INSERT INTO Grupos(nome_Grupo, quant_membros)
        VALUES('{nome}', {quant_membros});
        """)
        self.conn.commit()
        self.conn.close()

    def select_grupos(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Grupos;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_Grupo': registro[1],
                'quant_membros': registro[2]
            })
        self.conn.close()
        return registros

    def del_grupo(self, id: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"DELETE FROM Grupos WHERE id_Grupo = {id};")
        self.conn.commit()
        self.conn.close()

    def update_grupo(self, id: int, nome: str, quant_membros: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            UPDATE Grupos SET nome_Grupo = '{nome}', quant_membros = {quant_membros}
            WHERE id_Grupo = {id};
            """)
        self.conn.commit()
        self.conn.close()

# Classe Missoes:
class Missoes(Tabela):
    def __init__(self) -> None:
        super().__init__()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Missoes(
            id_mis INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            objetivo_mis VARCHAR(30) NOT NULL,
            descricao_mis VARCHAR(30) NOT NULL,
            recompensa INTEGER NOT NULL
            );
        """)
        self.conn.close()

    def add_missao(self, objetivo: str, descricao: str, recompensa: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
        INSERT INTO Missoes(objetivo_mis, descricao_mis, recompensa)
        VALUES('{objetivo}', '{descricao}', {recompensa});
        """)
        self.conn.commit()
        self.conn.close()

    def select_missoes(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Missoes;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id': registro[0],
                'objetivo_mis': registro[1],
                'descricao_mis': registro[2],
                'recompensa': registro[3]
            })
        self.conn.close()
        return registros

    def del_missao(self, id: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"DELETE FROM Missoes WHERE id_mis = {id};")
        self.conn.commit()
        self.conn.close()

    def update_missao(self, id: int, objetivo: str, descricao: str, recompensa: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            UPDATE Missoes SET objetivo_mis = '{objetivo}', descricao_mis = '{descricao}', recompensa = {recompensa}
            WHERE id_mis = {id};
            """)
        self.conn.commit()
        self.conn.close()

# Classe Genero:
class Genero(Tabela):
    def __init__(self) -> None:
        super().__init__()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Genero(
            id_gene INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            tipo_gene VARCHAR(30) NOT NULL
            );
        """)
        self.conn.close()

    def add_genero(self, tipo: str) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
        INSERT INTO Genero(tipo_gene)
        VALUES('{tipo}');
        """)
        self.conn.commit()
        self.conn.close()

    def select_generos(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Genero;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id': registro[0],
                'tipo_gene': registro[1]
            })
        self.conn.close()
        return registros

    def del_genero(self, id: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"DELETE FROM Genero WHERE id_gene = {id};")
        self.conn.commit()
        self.conn.close()

    def update_genero(self, id: int, tipo: str) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            UPDATE Genero SET tipo_gene = '{tipo}'
            WHERE id_gene = {id};
            """)
        self.conn.commit()
        self.conn.close()

# Objetos de cada tabela:
Obj_Personagem = Personagem()
Obj_Grupo = Grupos()
Obj_Missao = Missoes()
Obj_Genero = Genero()

# Inserindo dados em cada tabela:
# Obj_Personagem.add_person
