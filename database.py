import mysql.connector

conexao = mysql.connector.connect(
    user='root',
    password='password',
    host='127.0.0.1',
    database='db_mrcut',
    auth_plugin='mysql_native_password'
)
cursor = conexao.cursor()


def cadastrarColab(nome):
    inserir = f'INSERT INTO colaborador(nome) VALUES ("{nome}")'
    cursor.execute(inserir)
    conexao.commit()



def exibirColabs():
    exibir = f'SELECT * FROM colaborador'
    cursor.execute(exibir)
    resultado = cursor.fetchall()
    print(resultado)


def removerColab(nome):
    deletar = f'DELETE colaborador WHERE nome = "{nome}"'
    cursor.execute(deletar)
    conexao.commit()



