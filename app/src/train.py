import MySQLdb #Herramienta para escapar textos SQL
from scipy import *
import pickle
from sklearn import svm
import numpy as np



'''
Función preparada para realizar inserts en la bbdd con
sentencias SQL raw.
'''
def get_sql(SQLInstruction):
    try:
        db = MySQLdb.connect("localhost","root","R6i8e5m3a5n3n361*","adidas_experience")
        cursor = db.cursor()
        cursor.execute(SQLInstruction)
        db.commit()
        row = cursor.fetchall()
        return row
    except:
        return []



def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "_iter_") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result


def show_interests():
    SQLSentence4 = "SELECT username FROM Users"
    users = get_sql(SQLSentence4)
    
    SQLSentence1 = "SELECT u.username, rel.idInterest FROM Users u, RelInterestUser rel WHERE (u.username = rel.username)"
    tuplaUserInterest = get_sql(SQLSentence1)
    #tractar tupla
    print("tupla user interest")
    print(tuplaUserInterest)

    listDades= {}

    for u in users:
        if u[0] in listDades: 
            listDades[u[0]].extend(map(lambda x:x[1]/20.0, filter(lambda x: u[0] in x, tuplaUserInterest)))           #interesos
        else:
            listDades[u[0]]=list(map(lambda x:x[1]/20.0, filter(lambda x: u[0] in x, tuplaUserInterest)))

    print("listDades")
    print(listDades)
    SQLSentence2 = "SELECT username, age, gender, height, postal_code FROM Users"
    infoUser = get_sql(SQLSentence2)
    #tractar info user
    print("tupla info user")
    print(infoUser)

    for u in users:   
        if u[0] in listDades:
            listDades[u[0]].extend(map(lambda x: list( (x[1]/100.0,x[2],x[3]/250.0 , x[4]/99999.0)  ) , filter(lambda x: u[0] in x, infoUser ))) 
            listDades[u[0]] = flatten(listDades[u[0]])
            
            
        else:
            listDades[u[0]]=list(map(lambda x: list( (x[1]/100.0,x[2],x[3]/250.0 , x[4]/99999.0)  )) , filter(lambda x: u[0] in x, infoUser ))
            listDades[u[0]] = flatten(listDades[u[0]])
            
            

    print("listDades")
    print(listDades)

    SQLSentence5 = "SELECT count(*) FROM Products"
    countProd = get_sql(SQLSentence5)

    SQLSentence6 = "SELECT u.username FROM Users u,AdquiredProducts p WHERE (u.username = p.username)"
    diccionariProductes = get_sql(SQLSentence6)

    SQLSentence3 = "SELECT u.username, ap.idProduct FROM Users u, AdquiredProducts ap WHERE (u.username = ap.username)"
    productosUser = get_sql(SQLSentence3)
    #tractar productes per fer matriu
    print("tupla productos user")
    print(productosUser)

    for u in users:   
        if u[0] in listDades:
            listDades[u[0]].extend(map( lambda x: x[1] ,  filter(lambda x: u[0] in x, productosUser) ))  #ojo q las tuplas tienen 2 elementos
        else:
            listDades[u[0]]=list(map(lambda x: x[1] ) , filter(lambda x: u[0] in x, productosUser))

    print("listDades")
    print(listDades)

    objX=[]
    objY=[]
    for u in users:
        i=0
        n=len(list(filter(lambda x: u[0] in x, diccionariProductes )))
        for i in range((len(listDades[u[0]])-11)):
            objX.append(listDades[u[0]])
        for idx in range(11,len(listDades[u[0]])):
            objY.append(listDades[u[0]][idx])

    matrixX=np.array(objX)
    matrixAux = []
    for line in matrixX:
        lineAux = []
        for i in range(10):
            lineAux.append(line[i])
        lineAux.append(line[10][0])
        lineAux.append(line[10][1])
        lineAux.append(line[10][2])
        lineAux.append(line[10][3])
        matrixAux.append(lineAux)
    matrixX = matrixAux

    vectorY=np.array(objY)
    matrixX=np.array(matrixX)

    #Now we are going to train the model
    clf = svm.SVC()
    clf.fit(matrixX, vectorY)
    # save the model to disk
    filename = 'finalized_model.sav'
    pickle.dump(clf, open(filename, 'wb'))

 
def main():
    show_interests() 
 
if __name__ == '__main__':
    main()