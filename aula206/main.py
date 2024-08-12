'''
video aula 398 - 
PyMySql - um cliente MySQL feito em Python Puro
Doc: https://pymuysql.readthedocs.io/en/latest/
Pypy: https://pypi.org/project/pymysql/
GitHub: https://github.com/PyMySQL/PyMySQL
'''
import pymysql
import dotenv
import os
import pymysql.cursors

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    # Começo a manipular dados a partir daqui

    # Inserindo um valor usando placeholder e um iterável
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%s, %s) '
        )
        data = ('Luiz', 18)
        result = cursor.execute(sql, data)
        # print(sql, data)
        # print(result) # número de linhas afetadas
    connection.commit()

    # Inserindo um valor usando placeholder e um dicionário
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%(name)s, %(age)s) '
        )
        data2 = {
            "age": 37,
            "name": "Le",
        }
        result = cursor.execute(sql, data2)
        # print(sql, data2)
        # print(result) # número de linhas afetadas
    connection.commit()

    # Inserindo vários valores usando placeholder e uma tupla de dicionários
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%(nome)s, %(idade)s) '
        )
        data3 = (
            {"nome": "Sah", "idade": 33, },
            {"nome": "Julia", "idade": 74, },
            {"nome": "Rose", "idade": 53, },
        )
        result = cursor.executemany(sql, data3)
        # print(sql, data3)
        # print(result) # número de linhas afetadas
    connection.commit()

    # Inserindo vários valores usando placeholder e uma tupla de tuplas
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%s, %s) '
        )
        data4 = (
            ("Siri", 22),
            ("Helena", 15),
            ("Luiz", 18),
        )
        result = cursor.executemany(sql, data4)
        print(sql)
        print(data4)
        print(result) # número de linhas afetadas
    connection.commit()

    # Lendo os valores com SELECT
    with connection.cursor() as cursor:
        # menor_id = int(input('Digite o menor id: '))
        # maior_id = int(input('Digite o maior id: '))
        menor_id = 2
        maior_id = 4
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s '
        )
        result = cursor.execute(sql, (menor_id, maior_id))
        print(cursor.mogrify(sql, (menor_id, maior_id)))

        data5 = cursor.fetchall()

        for row in data5:
            print(row)

    # Apagando com DELETE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )
        print(cursor.execute(sql, (1,)))
        cursor.execute(sql, (1,))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        for row in cursor.fetchall():
            print(row)

     # Editando com UPDATE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome = %s, idade = %s '
            'WHERE id = %s'
        )
        print(cursor.execute(sql, ('Eleonor', 102, 4)))
        cursor.execute(sql, ('Eleonor', 102, 4))
        resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        # data6 = cursor.fetchall()

        # print('For 1: ')
        # for row in data6:
        #     print(row)

        # print()
        # print('For 2: ')
        # for row in data6:
        #     print(row)

        # para conseguir fazer outro for sem usar uma variavel
        # print('For 1: ')
        # for row in cursor.fetchall():
        #     print(row)

        # print()
        # print('For 2: ')
        # # cursor.scroll(-2) #  modo relativo
        # cursor.scroll(0, 'absolute')
        # for row in cursor.fetchall():
        #     print(row)
        
        # para usar com SSDictCursor para volumes grandes de dados
        # print('For 1: ')
        # for row in cursor.fetchall_unbuffered():
        #     print(row)

        # print()
        # print('For 2: ')
        # for row in cursor.fetchall_unbuffered():
        #     print(row)

        for row in cursor.fetchall():
            print(row)
        
        cursor.execute(
            f'SELECT id FROM {TABLE_NAME} ORDER BY id DESC LIMIT 1'
        )
        lastIdFromSelect = cursor.fetchone()
        
        print('resultFromSelect', resultFromSelect)
        print('rowcount', cursor.rowcount)

        # sql = (
        #     f'INSERT INTO {TABLE_NAME} '
        #     '(nome, idade) VALUES (%s, %s) '
        # )
        # data = ('Luiz', 18)
        # cursor.execute(sql, data)

        print('lastrowid', cursor.lastrowid)
        # lastrowid se usado depois de um executemany vai mostrar o primeiro
        # registro inserido e não o último

        print('lastrowid na mão', lastIdFromSelect['id'])
        print('rownumber', cursor.rownumber)


    connection.commit()    
