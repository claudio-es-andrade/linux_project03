import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='meubanco',
                                         user='mysql',
                                         password='123')

    mySql_Create_Table_Query = """CREATE TABLE dados ( 
                             AlunoId     int(15)       NOT NULL,
                             Nome        varchar(50)   NOT NULL,
			     Sobrenome   varchar(50)   NOT NULL,
			     Endereco    varchar(50)   NOT NULL,
			     Cidade      varchar(50)   NOT NULL,
			     Host        varchar(50)   NOT NULL,
                             PRIMARY KEY (Id)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Tabela dos Alunos criada com sucesso")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
