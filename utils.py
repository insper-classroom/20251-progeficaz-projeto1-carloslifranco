import json 
import sqlite3 as sql 

def load_data( ):
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from users")
    data=cur.fetchall()
    return data 

def load_template(arquivo_template):
    with open(f'static/templates/{arquivo_template}') as file:
        texto = file.read()
    return texto  

def create_post (titulo, detalhes):
    con=sql.connect("db_web.db")
    cur=con.cursor()
    cur.execute("insert into users(titulo, detalhe) values (?,?)", (titulo, detalhes))
    con.commit()
    con.close()

def delete_note(id):
    con=sql.connect("db_web.db")
    cur=con.cursor()
    cur.execute('delete from users where ID=?',(id,))
    con.commit()
    con.close()


        