import sqlite3

conn = sqlite3.connect('inventario.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jogos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    genero TEXT NOT NULL,
    plataforma TEXT NOT NULL,
    preco REAL,
    estoque INTEGER DEFAULT 0
)
""")

conn.commit()
conn.close()

print("Banco de dados de jogos criado com sucesso!")