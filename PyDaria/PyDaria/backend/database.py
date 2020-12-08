import mysql.connector
from flask import make_response

# Conencta no banco de dados
db = mysql.connector.connect(host="localhost", user="root",password="mp2020@@", database="clientes")

# Gera um cursos que será responsável por realizar as ações
cursor = db.cursor()

# Cria o banco de dados caso não exista
cursor.execute("CREATE DATABASE IF NOT EXISTS clientes;")

# Cria a tabela de clientes
cursor.execute("CREATE TABLE IF NOT EXISTS `Clients` ( \
  `ID` int(11) NOT NULL AUTO_INCREMENT, \
  `Name` varchar(45) NOT NULL, \
  `Email` varchar(45) NOT NULL, \
  `Telephone` varchar(45) NOT NULL, \
  `Cpf` varchar(45) NOT NULL, \
  `isAdmin` tinyint(4) NOT NULL, \
  `Password` varchar(45) NOT NULL, \
  PRIMARY KEY (`ID`) \
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;")

# Cria a tabela de produtos
cursor.execute("CREATE TABLE IF NOT EXISTS `Products` ( \
  `ID_Products` int(11) NOT NULL AUTO_INCREMENT, \
  `Price` float NOT NULL, \
  `Name` varchar(45) NOT NULL, \
  `Picture` varchar(255) NOT NULL, \
  `Quantity` int(11) NOT NULL, \
  PRIMARY KEY (`ID_Products`) \
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;")


# Adiciona um cliente no banco de dados apartir do cpf, email, nome e telefone
def add_client(cpf: str, name: str, email: str, telephone: str, password: str, isAdmin = False):

    # Comando SQL a ser executado
    query = ("INSERT INTO Clients (Cpf, Name, Email, Telephone, Password, isAdmin) VALUES (%s, %s, %s, %s, %s, %s);")
    
    # Valores a serem adicionados
    val = (cpf, name, email, telephone, password, isAdmin)

    # Executa o comando
    cursor.execute(query, val)

    # Faz com que as mudanças sejam salvas
    db.commit()
    
    # Verifica, pelo número de linhas modificadas, se a operação foi bem sucedida
    if( cursor.rowcount < 1):
        print("Failed to add 'Cliente: {}' to database!".format(name))
    return print("Added 'Cliente: {}' to database!".format(name))

# Retorna uma lista de tuplas com todos os dados de todos clientes
def show_all_clients():

    # Comando SQL a ser executado
    query = ("SELECT * FROM Clients")

    # Executa o comando
    cursor.execute(query)

    # Agrupa o resultado em tuplas
    result = cursor.fetchall()
    
    # Imprime o resultado em um terminal
    for i in result:
        print(i)
    
    # Retorna as tuplas
    return result

# Retorna os dados de um cliente de acordo com seu cpf
def show_client(cpf: str):

    # Comando SQL a ser executado
    query = ("SELECT * FROM Clients WHERE Cpf = '{}';".format(cpf))
    
    # Executa o comando
    cursor.execute(query)

    # Agrupa os dados em uma tupla
    result = cursor.fetchall()

    # Imprime o resulado em um terminal
    for i in result:
        print(i)

    # Retorna a tupla
    return result
    
# Remove um cliente do banco de dados
def rmv_client(cpf: str):

    # Comando SQL a ser executado
    query = ("DELETE FROM Clients WHERE Cpf = '{}';".format(cpf))

    # Executa o comando
    cursor.execute(query)

    # Salva as alterações
    db.commit()

    # Verifica, pelo número de linhas modificadas, se a operação foi bem sucedida 
    if( cursor.rowcount < 1):
        print("Failed to remove 'Cliente: {}' from database!".format(cpf))
    return print("Removed 'Cliente: {}' from databse!".format(cpf))

# Atualiza a senha de um cliente
def update_p_client(cpf: str, new_val: str):

    # Comando SQL a ser executado
    query = ("UPDATE Clients SET Password = '{}' WHERE Cpf = {};".format(new_val, cpf))

    # Executa o comando
    cursor.execute(query)

    # Salva as mudanças
    db.commit()

    if(cursor.rowcount < 1):
        print("Failed to update password")
        return False
    print("Password updated!")
    return True

# Atualiza o email de um cliente
def update_e_client(cpf: str, new_val: str):

    # Comando SQL a ser executado
    query = ("UPDATE Clients SET Email = '{}' WHERE Cpf = {};".format(new_val, cpf))

    # Executa o comando
    cursor.execute(query)

    # Salva as mudanças
    db.commit()

    if(cursor.rowcount < 1):
        print("Failed to update email")
        return False
    print("Email updated!")
    return True

# Atualiza o telefone de um cliente
def update_t_client(cpf: str, new_val: str):

    # Comando SQL a ser executado
    query = ("UPDATE Clients SET Telephone = '{}' WHERE Cpf = {};".format(new_val, cpf))

    # Executa o comando
    cursor.execute(query)

    # Salva as mudanças
    db.commit()

    if(cursor.rowcount < 1):
        print("Failed to update telephone")
        return False
    print("Telephone updated!")
    return True

# Atualiza o nome de um cliente
def update_n_client(cpf: str, new_val: str):

    # Comando SQL a ser executado
    query = ("UPDATE Clients SET Name = '{}' WHERE Cpf = {};".format(new_val, cpf))

    # Executa o comando
    cursor.execute(query)

    # Salva as mudanças
    db.commit()

    if(cursor.rowcount < 1):
        print("Failed to update name")
        return False
    print("Name updated!")
    return True

# Adiciona produtos no banco de dados
def add_product(name: str, price: float, img: str, qtd: int):
       
    # Comando SQL a ser executado
    query = ("INSERT INTO Products (Name, Price, Picture, Quantity) VALUES (%s, %s, %s, %s);")
    
    # Valores a serem adicionados
    val = (name, price, img, qtd)

    # Executa o comando
    cursor.execute(query, val)

    # Faz com que as mudanças sejam salvas
    db.commit()
    
    # Verifica, pelo número de linhas modificadas, se a operação foi bem sucedida
    if( cursor.rowcount < 1):
        print("Failed to add 'Product: {}' to database!".format(name))
    return print("Added 'Product: {}' to databse!".format(name)) 

# Retorna todos os produtos
def show_all_products():

    # Comando SQL a ser executado
    query = ("SELECT * FROM Products")

    # Executa o comando
    cursor.execute(query)

    # Agrupa o resultado em tuplas
    result = cursor.fetchall()
    
    # Imprime o resultado em um terminal
    for i in result:
        print(i)
    
    # Retorna as tuplas
    return result

# Retorna um produto de acordo com o ID
def show_product(id_product: int):

    # Comando SQL a ser executado
    query = ("SELECT * FROM Products WHERE ID_Products = '{}';".format(id_product))
    
    # Executa o comando
    cursor.execute(query)

    # Agrupa os dados em uma tupla
    result = cursor.fetchall()

    # Imprime o resulado em um terminal
    for i in result:
        print(i)

    # Retorna a tupla
    return result

# Remove um produto do banco de dados
def rmv_product(id_product: int):

    # Comando SQL a ser executado
    query = ("DELETE FROM Products WHERE ID = '{}';".format(id_product))

    # Executa o comando
    cursor.execute(query)

    # Salva as alterações
    db.commit()

    # Verifica, pelo número de linhas modificadas, se a operação foi bem sucedida 
    if( cursor.rowcount < 1):
        print("Failed to remove 'Product: {}' from database!".format(id_product))
    return print("Removed 'Product: {}' from databse!".format(id_product))

# Atualiza o preço de um produto
def update_p_product(id_product: int, new_val: float):

    # Comando SQL a ser executado
    query = ("UPDATE Products SET Price = '{}' WHERE ID_Products = {};".format(new_val, id_product))

    # Executa o comando
    cursor.execute(query)

    # Salva as mudanças
    db.commit()

    if(cursor.rowcount < 1):
        print("Failed to update price")
        return False
    print("Price updated!")
    return True

# Atualiza a quantidade de um produto
def update_q_product(id_product: int, new_val: int):

    # Pega a quantidade antiga do produto
    query = ("SELECT Quantity FROM Products WHERE ID_Products = {};".format(id_product))
    cursor.execute(query)
    result = cursor.fetchall()
    resto = sum(result[0]) - new_val

    # Comando SQL a ser executado
    query = ("UPDATE Products SET Quantity = '{}' WHERE ID_Products = {};".format(resto, id_product))

    # Executa o comando
    cursor.execute(query)

    # Salva as mudanças
    db.commit()

    # Verifica se houveram mudanças
    if(cursor.rowcount < 1):
        print("Failed to update quantity")
        return False
    print("Quantity updated!")
    return True
