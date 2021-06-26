import os
import face_recognition as fr
import mysql.connector
import cv2
import time
import numpy as np
from pycoral.adapters import classify
from pycoral.adapters import common
from pycoral.utils.dataset import read_label_file
from pycoral.utils.edgetpu import make_interpreter

# Carga de candidatos para predecir Caras
def get_encoded_faces():
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded



####Proceso de deteccion de personas
def deteccionDePersona(arrayCaras,im):
    faces = arrayCaras # array fotos
    faces_encoded = list(faces.values()) #puntos
    known_face_names = list(faces.keys()) #personas

    img = cv2.imread(im, 1)# 1 = cv2.IMREAD_COLOR (flag por defecto)
    face_locations = fr.face_locations(img) # localizacion cara
    unknown_face_encodings = fr.face_encodings(img, face_locations) # array de puntos
    face_names = ""
    for face_encoding in unknown_face_encodings: #para los puntos que tengo del array en los puntos del desconocido
        matches = fr.compare_faces(faces_encoded, face_encoding) #compara los puntos con una tolerancia alta para generar posibles candidatos
        name = "Unknown"
        face_distances = fr.face_distance(faces_encoded, face_encoding) #retorna la distancia euclidea de la cara desocnocida con el resto
        best_match_index = np.argmin(face_distances)  # retorna el indice del valor minimo
        if matches[best_match_index]: # compara si los posibles candidatos tambien contienen la menor distancia euclidea, en
            name = known_face_names[best_match_index]
        face_names=name
    return face_names


####Proceso de sentimiento
def deteccionDeSentimiento(img):
    labels = read_label_file("sentimientos.txt")
    interpreter = make_interpreter("--")
    interpreter.allocate_tensors()
    face_image = cv2.imread(img)
    face_image = cv2.resize(face_image, (48, 48))
    face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
    face_image = np.reshape(face_image, [1, face_image.shape[0], face_image.shape[1], 1])
    image = face_image
    common.set_input(interpreter, image)
    for _ in range(5):
        interpreter.invoke()
        classes = classify.get_classes(interpreter, 3)

    print('-------RESULTS--------')
    mejor=-10
    for c in classes:
        print('%s: %.5f' % (labels.get(c.id, c.id), c.score))
        if(c.score>mejor):
            resultado=str(labels.get(c.id, c.id))
            mejor=c.score

    return resultado


####Envio BBDD
def envioBBDD(identificador,sentimiento,num):
    try:
        cnx = mysql.connector.connect(user='--', password='--',
                                      host='--', database='--',
                                      auth_plugin='mysql_native_password')
        mycursor = cnx.cursor()
        mycursor.execute("INSERT INTO datos Values('"+identificador
                         +"','"+sentimiento+"')")
        cnx.commit()
    except:
        if num>0:
             envioBBDD(identificador,sentimiento,num-1)
        else:
             print("No se ha podido acceder a la base de datos tras 3 intentos\n")
             f=open("errores.txt","a")
             f.write(identificador+sentimiento+"\n")
             f.close()
             print("Datos guardados en el archivo errores")



arrayCaras=get_encoded_faces()

while True:
    for dirpath, dnames, fnames in os.walk("./porProcesar"):
        for f in fnames:
            face = "porProcesar/" + f
            identificador=deteccionDePersona(arrayCaras,face)
            sentimiento=deteccionDeSentimiento(face)
            envioBBDD(identificador,sentimiento,3)
            os.remove(face)
    time.sleep(30)