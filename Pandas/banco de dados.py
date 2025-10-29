import sqlite3

conn = sqlite3.connect('meubanco.db')
cursor = conn.cursor()

cursor.execute('select * from planilha')
dados = cursor.fetchall()
for linha in dados:
    print(linha)

cursor.execute('update planilha set PRECO = ? where ID = ?',   (109.99, 3))
conn.commit()
