import sqlite3 as sql 

#conectando com sqlite
conectar = sql.connect('db_web.db')

#criando uma conexão
cur = conectar.cursor()

#Excluir tabela de usuários se já existir.
cur.execute("DROP TABLE IF EXISTS users")

#Criar tabela de usuários no banco de dados db_web 
sql ='''CREATE TABLE "users" (
	"ID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"titulo"	TEXT,
	"detalhe"	TEXT
)'''

cur.execute(sql)

#comfirmar alterações
conectar.commit()

#fechar conexão
conectar.close()


