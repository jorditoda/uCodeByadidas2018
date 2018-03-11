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

def createUser(username, age, gender, height, postal_code, interests):
    #Escapamos el valor del username
    username = MySQLdb.escape_string(username)
    #Comprobamos que todos los datos son correctos.
    correctAge = ((type(age) is int) and age > 0)
    correctGender = (gender ==1 or gender == 0)
    correctHeight = ((type(height) is int) and height > 0)
    correctPostalCode = ((type(postal_code) is int) and postal_code > 0)
    if(correctAge and correctGender and correctHeight and correctPostalCode):
        #Si todos los datos son correctos, creamos el objeto y
        #lo subimos a la bbdd.
        SQLSentence = "INSERT INTO Users (username, age, gender, height, postal_code, expenses) VALUES ({0}, {1}, {2}, {3}, '{4}', 0)".format(username, age, gender, height, postal_code)
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
    #Comprobamos que el id es correcto.
    correctId = ((type(idInterest) is int) and idInterest > 0)
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
Permite crear un producto a partir de los siguientes parámetros
idProduct: int Id del producto que queremos tratar
urlPhoto: string url de la fotografía asociada al producto
price: float Precio del producto 
'''
def createProduct(idProduct, urlPhoto, price):
    correctString = ((type(idProduct) is int) and isinstance(urlPhoto, str))
    correctPrice = ((type(price) is int) and price > 0) 
    idProduct = MySQLdb.escape_string(idProduct)
    urlPhoto = MySQLdb.escape_string(urlPhoto)
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
    correctId = (type(idExperience) is int) and  idExperience > 0
    correctDescription = isinstance(expDescription, str)
    if(correctId and correctDescription):
        idExperience = MySQLdb.escape_string(idExperience)
        expDescription = MySQLdb.escape_string(expDescription)
        SQLSentence = "INSERT INTO Experiences (idExperience, exDescription) VALUES({0},'{1}')".format(idExperience, expDescription)
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
    correctID = (type(idInterest) is int) and  idInterest > 0
    correctName = isinstance(nameOfInterest, str)
    if (correctID and correctName):
        idInterest = MySQLdb.escape_string(idInterest)
        nameOfInterest = MySQLdb.escape_string(nameOfInterest)
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
    correctID = (type(idExperience) is int) and idExperience > 0
    correctUsername = isinstance(username, str)
    correctDate = type(year) is type(month) and type(month)is type(day) and type(day) is int
    idExperience = MySQLdb.escape_string(idExperience)
    username = MySQLdb.escape_string(username)
    if (correctID and correctUsername and correctDate):
        SQLSentence = "INSERT INTO ExperiencesHistory (idExperience, username, dateOfShow) VALUES({0}, '{1}', {2}-{3}-{4})".format(idExperience, username, year, month, day)
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
        cursor.execute(SQLInstruction)
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
        row = cursor.fetchall()
        return row
    except:
        return []