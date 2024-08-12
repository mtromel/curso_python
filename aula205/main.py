# video aula 388 - 397
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# DELETE mais cuidadoso
# faz o id zerar a sequencia e começar novamente do 1
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

connection.commit()

# Registrar valores nas colunas das tabelas
# CUIDADO: sql injection
# dessa forma é possivel que o hacker consiga inserir comandos sql no lugar
# dos valores se fosse um formulário web por exemplo
# cursor.execute(
#     f'INSERT INTO {TABLE_NAME} (id, name, weight) '
#     'VALUES (NULL, "Helena", 4), (NULL, "Eduardo", 10)'
# )

# dessa forma o sqlite entende que só vai receber valores e não comandos sql
# nesse bloco estou inserindo um ou vários registros usando tupla ou lista
# sql = (f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)')
# cursor.execute(sql, ['Joana', 4]) # insere apenas um comando
# cursor.executemany(sql, (('Joana', 4,), ('Marcos', 5)))

# nesse bloco usando dicionario
sql = (f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (:name, :weight)')
# cursor.execute(sql, {'name': 'Joana', 'weight': 4})
cursor.executemany(sql, (
    {'name': 'Joãozinho', 'weight': 3},
    {'name': 'Maria', 'weight': 3},
    {'name': 'Helena', 'weight': 4},
    {'name': 'Joana', 'weight': 5},
))
connection.commit()

if __name__ == '__main__':
    print(sql)

    cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = "3"')
    connection.commit()
    
    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="Marcos", weight=67.89 '
        'WHERE id = 1'
    )
    connection.commit()

    cursor.execute(f'SELECT * FROM {TABLE_NAME}')

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)
    
    cursor.close()
    connection.close()