import pandas as pd
from PIL import Image
import random
#3 Happy
#4 Sad
#6 Neutral



documento = pd.read_csv('train.csv')

print(documento.shape[0])
longitud=documento.shape[0]
print(documento.iat[0,0])

print(documento.head())

for i in range(longitud):
    x = random.choice((1, 2, 3, 4, 5))
    pixels=documento.iat[i,1]
    b = bytes(int(p) for p in pixels.split())
    a = Image.frombuffer('L', (48, 48), b)
    if(i%1000==0):
        print(str(i)+" numero 1000")
    if(documento.iat[i,0]==3):
        path="datos/Happy/happy"+str(i)+".jpg"
        a.save(path)
    if(documento.iat[i,0]==6):
        path = "datos/Neutral/neutral" + str(i) + ".jpg"
        a.save(path)
    if(documento.iat[i,0]==4):
        path = "datos/Sad/sad" + str(i) + ".jpg"
        a.save(path)
    if (x == 1):
        if (documento.iat[i, 0] == 3):
            path = "validacion/Happy/happy" + str(i) + ".jpg"
            a.save(path)
        if (documento.iat[i, 0] == 6):
            path = "validacion/Neutral/neutral" + str(i) + ".jpg"
            a.save(path)
        if (documento.iat[i, 0] == 4):
            path = "validacion/Sad/sad" + str(i) + ".jpg"
            a.save(path)


