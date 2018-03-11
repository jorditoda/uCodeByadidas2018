#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flaskext.mysql import MySQL
from json import dumps
import numpy as np
import pickle
 

# Set up the database and the Flask app

app = Flask("medtech-iot")
mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'R6i8e5m3a5n3n361*'
app.config['MYSQL_DATABASE_DB'] = 'adidas_experience'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

#Starting MySQL
mysql.init_app(app)

# Set up the REST API
api = Api(app)

@app.route('/')
def hello_world():
    return 'Bienvenido a la API de Adidas Experience.'

@app.route('/POST/USER', methods=['POST'])
def create_user():
    dictValues = request.form
    username = dictValues['username']
    age = dictValues['age']
    gender = dictValues['gender']
    height = dictValues['height']
    postal_code = dictValues['postal_code']
    statusOp = createUser(username, age, gender, height, postal_code)
    message = 'Todo correcto' if statusOp else 'Error'
    return message

@app.route('/POST/INTUSER', methods=['POST'])
def create_rel_interest_user():
    dictValues = request.form
    idInterest = dictValues['idInterest']
    username = dictValues['username']
    statusOp =createRelInterestUser(idInterest, username)
    message = 'Todo correcto' if statusOp else 'Error'
    return message

@app.route('/POST/ADQPRODUCTS', methods=['POST'])
def create_adquired_products():
    dictValues = request.form
    idProduct = dictValues['idProduct']
    username = dictValues['username']
    statusOp =createAdquiredProducts(idProduct, username)
    message = 'Todo correcto' if statusOp else 'Error'
    return message


@app.route('/POST/PRODUCT',methods=['POST'])
def create_product():
    dictValues = request.form
    idProduct = dictValues['idProduct']
    urlPhoto = dictValues['urlPhoto']
    price = dictValues['price']
    statusOp = createProduct(idProduct, urlPhoto, price)
    message = 'Todo correcto' if statusOp else 'Error'
    return message

@app.route('/POST/EXPERIENCE',methods=['POST'])
def create_experience():
    dictValues = request.form
    idExperience = dictValues['idExperience']
    expDescription = dictValues['expDescription']
    statusOp = createExperience(idExperience, expDescription)
    message = 'Todo correcto' if statusOp else 'Error'
    return message

@app.route('/POST/INTEREST',methods=['POST'])
def create_interest():
    dictValues = request.form
    idInterest = dictValues['idInterest']
    nameOfInterest = dictValues['nameOfInterest']
    statusOp = createInterest(idInterest, nameOfInterest)
    message = 'Todo correcto' if statusOp else 'Error'
    return message

@app.route('/POST/EXP_HIST',methods=['POST'])
def create_experience_history():
    dictValues = request.form
    idExperience = dictValues['idExperience']
    username = dictValues['username']
    year = dictValues['year']
    month = dictValues['month']
    day = dictValues['day']
    statusOp = createExperiencesHistory(idExperience, username, year, month, day)
    message = 'Todo correcto' if statusOp else 'Error'
    return message

@app.route('/GET/INTEREST',methods=['GET'])
def get_recommended_interest():
    args = request.args
    username = args['username']
    prediction = predict(username)
    SQLSentence = "SELECT * FROM Products p WHERE (p.idProduct={0})".format(prediction)
    print(SQLSentence)
    result = get_sql(SQLSentence)
    return jsonify(idProduct=result[0][0], urlPhoto=result[0][1], price=result[0][2])

#######################################################
# Form functions
#######################################################

'''
Metodos para crear formularios para rellenar la BD. No sirven para nada
mas
'''
@app.route('/createUser',methods=['GET'])
def formCreateUser():
    return ('''
        <form action="http://46.101.12.106:5000/POST/USER" method="post">
        <label for="username">Username</label>
        <input type="text" id="username" name="username"><br/>
     
        <label for="age">age</label>
        <input type="text" id="age" name="age"><br/>

        <label for="gender">gender</label>
        <input type="text" id="gender" name="gender"><br/>

        <label for="height">height</label>
        <input type="text" id="height" name="height"><br/>

        <label for="postal_code">postal_code</label>
        <input type="text" id="postal_code" name="postal_code"><br/>

        <input type="submit" value="Enviar" />
    </form>
    ''')

@app.route('/createRelInterestUser',methods=['GET'])
def formCreateInterestUser():
    return ('''
        <form action="http://46.101.12.106:5000/POST/INTUSER" method="post">
        <label for="idInterest">idInterest</label>
        <input type="text" id="idInterest" name="idInterest"><br/>
     
        <label for="username">username</label>
        <input type="text" id="username" name="username"><br/>

        <input type="submit" value="Enviar" />
    </form>
    ''')

@app.route('/createAdquiredProducts',methods=['GET'])
def formCreateAdquiredProducts():
    return ('''
        <form action="http://46.101.12.106:5000/POST/ADQPRODUCTS" method="post">
        <label for="idProduct">idProduct</label>
        <input type="text" id="idProduct" name="idProduct"><br/>
     
        <label for="username">username</label>
        <input type="text" id="username" name="username"><br/>

        <input type="submit" value="Enviar" />
    </form>
    ''')

@app.route('/createProduct',methods=['GET'])
def formCreateProduct():
    return ('''
        <form action="http://46.101.12.106:5000/POST/PRODUCT" method="post">
        <label for="idProduct">idProduct</label>
        <input type="text" id="idProduct" name="idProduct"><br/>
     
        <label for="urlPhoto">urlPhoto</label>
        <input type="text" id="urlPhoto" name="urlPhoto"><br/>

        <label for="price">price</label>
        <input type="text" id="price" name="price"><br/>

        <input type="submit" value="Enviar" />
    </form>
    ''')

@app.route('/createExperience',methods=['GET'])
def formCreateExperience():
    return ('''
        <form action="http://46.101.12.106:5000/POST/EXPERIENCE" method="post">
        <label for="idExperience">idExperience</label>
        <input type="text" id="idExperience" name="idExperience"><br/>

        <label for="expDescription">expDescription</label>
        <input type="text" id="expDescription" name="expDescription"><br/>

        <input type="submit" value="Enviar" />
    </form>
    ''')

@app.route('/createInterest',methods=['GET'])
def formCreateInterest():
    return ('''
        <form action="http://46.101.12.106:5000/POST/INTEREST" method="post">
        <label for="idInterest">idInterest</label>
        <input type="text" id="idInterest" name="idInterest"><br/>
     
        <label for="nameOfInterest">nameOfInterest</label>
        <input type="text" id="nameOfInterest" name="nameOfInterest"><br/>

        <input type="submit" value="Enviar" />
    </form>
    ''')

@app.route('/createExperiencesHistory',methods=['GET'])
def formCreateExperiencesHistory():
    return ('''
        <form action="http://46.101.12.106:5000/POST/EXP_HIST" method="post">
        <label for="idExperience">idExperience</label>
        <input type="text" id="idExperience" name="idExperience"><br/>
     
        <label for="username">username</label>
        <input type="text" id="username" name="username"><br/>

        <label for="year">year</label>
        <input type="text" id="year" name="year"><br/>

        <label for="month">month</label>
        <input type="text" id="month" name="month"><br/>

        <label for="day">day</label>
        <input type="text" id="day" name="day"><br/>

        <input type="submit" value="Enviar" />
    </form>
    ''')

#### End of form functions #############################

#######################################################
# Auxiliar functions
#######################################################

import MySQLdb #Herramienta para escapar textos SQL


'''
Permite crear un usuario con los datos de usuario
proporcionados por parámetro.

username: String identificador único del usuario
age : int Edad del usuario proporcionada al registrarse.
gender: 0 o 1 : 0 Expresa mujer, 1 expresa hombre.
height: int: Altura del usuario en cms.
postal_code: int Código postal de la población del usuario.
interests: int[] : Lista con los id de los intereses de usuario.
'''

def createUser(username, age, gender, height, postal_code):
    print(username, age, gender, height, postal_code)
    #Escapamos el valor del username
    username = MySQLdb.escape_string(username)
    username = username.decode("utf-8")
    #Comprobamos que todos los datos son correctos.
    correctAge = age.isdigit()
    correctGender = (gender =='1' or gender == '0')
    correctHeight = height.isdigit()
    correctPostalCode = postal_code.isdigit()
    if(correctAge and correctGender and correctHeight and correctPostalCode):
        #Si todos los datos son correctos, creamos el objeto y
        #lo subimos a la bbdd.
        SQLSentence = "INSERT INTO Users (username, age, gender, height, postal_code, expenses) VALUES ('{0}', {1}, {2}, {3}, {4}, 0)".format(str(username), age, gender, height, postal_code)
        result = insert_sql(SQLSentence)
        return result
    else:
        return False
    return True
'''
Permite crear una relación de interés/usuario dados los siguientes parámetros
idInterest: int Identificador del interés en la base de datos.
username: string Identificador del usuario en la base de datos.
'''
def createRelInterestUser(idInterest, username):
    #Escapamos el valor del username
    username = MySQLdb.escape_string(username)
    username = username.decode("utf-8")
    #Comprobamos que el id es correcto.
    correctId = idInterest.isdigit()
    if(correctId):
        #Si el ID es correcto entonces creamos el objeto y lo subimos a
        #la bbdd
        SQLSentence = "INSERT INTO RelInterestUser (idInterest, username) VALUES ({0}, '{1}')".format(idInterest, username)
        result = insert_sql(SQLSentence)
        return result
    else:
        return False
    return True

'''
Permite crear una relación de productos adquiridos dados los siguientes parámetros
idProduct: int Identificador del interés en la base de datos.
username: string Identificador del usuario en la base de datos.
'''
def createAdquiredProducts(idProduct, username):
    #Escapamos el valor del username
    username = MySQLdb.escape_string(username)
    username = username.decode("utf-8")
    #Comprobamos que el id es correcto.
    correctId = idProduct.isdigit()
    if(correctId):
        #Si el ID es correcto entonces creamos el objeto y lo subimos a
        #la bbdd
        SQLSentence = "INSERT INTO AdquiredProducts (idProduct, username) VALUES ({0}, '{1}')".format(idProduct, username)
        result = insert_sql(SQLSentence)
        return result
    else:
        return False
    return True
'''
Permite crear un producto a partir de los siguientes parámetros
idProduct: int Id del producto que queremos tratar
urlPhoto: string url de la fotografía asociada al producto
price: float Precio del producto 
'''
def createProduct(idProduct, urlPhoto, price):
    correctString = idProduct.isdigit()
    correctPrice = price.isdigit()
    urlPhoto = MySQLdb.escape_string(urlPhoto)
    urlPhoto = urlPhoto.decode("utf-8")
    if(correctString and correctPrice):
        SQLSentence = "INSERT INTO Products (idProduct, urlPhoto, price) VALUES({0}, '{1}', {2})".format(idProduct, urlPhoto, price)
        result = insert_sql(SQLSentence)
        return result
    else:
	    return False 
    return True
	  
'''
Permite crear una experiencia a partir de los parámetro siguientes:
idExperience: int Descriptor único de la experiencia.
expDescription: string Descripción de la experiencia para el usuario.
'''
def createExperience(idExperience, expDescription):
    correctId = idExperience.isdigit()
    if(correctId):
        expDescription = MySQLdb.escape_string(expDescription)
        expDescription = expDescription.decode("utf-8")
        SQLSentence = "INSERT INTO Experiences (idExperience, expDescription) VALUES({0},'{1}')".format(idExperience, expDescription)
        result = insert_sql(SQLSentence)
        return result
    else:
        return False
    return True
 	
'''
Permite crear un interés a partir de los parámetros siguientes:
idInterest: int Descriptor único del interés.
nameOfInterest: string Nombre del interés
'''
def createInterest(idInterest, nameOfInterest):
    correctID = idInterest.isdigit()
    if (correctID):
        nameOfInterest = MySQLdb.escape_string(nameOfInterest)
        nameOfInterest = nameOfInterest.decode("utf-8")
        SQLSentence = "INSERT INTO Interests (idInterest, nameOfInterest) VALUES({0},'{1}')".format(idInterest,nameOfInterest)
        result = insert_sql(SQLSentence)
        return result
    else:
        return False
    return True

'''
Permite crear una entrada del historial de experiencias vistas por el usuario 
a partir de los siguientes parámetros.

idExperience: int Identificador único de la experiencia
username: Nombre de usuario que compró el producto (identificador único)
==Fecha de compra==
year: int
month: int
day: int

'''
def createExperiencesHistory(idExperience, username, year, month, day):
    correctID = idExperience.isdigit()
    correctDate = year.isdigit() and month.isdigit() and day.isdigit()
    username = MySQLdb.escape_string(username)
    username = username.decode("utf-8")
    if (correctID and correctDate):
        SQLSentence = "INSERT INTO ExperiencesHistory (idExperience, username, dateOfShow) VALUES({0}, '{1}', '{2}-{3}-{4}')".format(idExperience, username, year, month, day)
        result = insert_sql(SQLSentence)
        return result
    else:
	    return False
    return True

'''
Función preparada para realizar inserts en la bbdd con
sentencias SQL raw.
'''
def insert_sql(SQLInstruction):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        print(SQLInstruction)
        cursor.execute(SQLInstruction)
        conn.commit()
        return True
    except:
        return False

'''
Función preparada para realizar get de información en la bbdd con
sentencias SQL Raw.

Devuelve una lista con todas las filas que cumplan la condición
impuesta en la instrucción SQL.

Si SQL falla devuelve una lista vacía
'''
def get_sql(SQLInstruction):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(SQLInstruction)
        conn.commit()
        row = cursor.fetchall()
        return row
    except:
        return []

#########################################

def predict(username):
    SQLSentence1 = "SELECT u.username, rel.idInterest FROM Users u, RelInterestUser rel WHERE (u.username = rel.username AND u.username='{0}')".format(username)
    tuplaUserInterest = get_sql(SQLSentence1)
    listaNormalizada = []
    for valor in range(len(tuplaUserInterest)):
        listaNormalizada.append(valor/20.)
    SQLSentence2 = "SELECT username, age, gender, height, postal_code FROM Users u WHERE (u.username='{0}')".format(username)
    infoUser = get_sql(SQLSentence2)
    ultimaParteLista = list(map(lambda x: list( (x[1]/100.0,x[2],x[3]/250.0 , x[4]/99999.0)  ) , infoUser)) 
    filename = 'finalized_model.sav'
    # load the model from disk
    clf = pickle.load(open(filename, 'rb'))
    for elem in ultimaParteLista[0]:
        listaNormalizada.append(elem)
    prediction = clf.predict(np.array([listaNormalizada]))
    return prediction.tolist()[0]


def main():
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()