import sqlite3
from pathlib import Path

Path('Database').mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect('Database/usuarios.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
)''')

cursor.execute('INSERT OR IGNORE INTO usuarios (usuario, senha) VALUES (?, ?)', ("admin", "1234567890"))

conn.commit()
conn.close()

print("Banco de dados inicializado com sucesso.")