# TFG-Implementaci-n_de_un_sistema_para_la_atencion_temprana_al_desgaste_psicologico

- modeloSentimientos se encuentra todo el codigo referente al entrenamiento del modelo y preprocesado de datos
- placa se encuentra todo el codigo codigo necesario para el funcionamiento del proyecto dentro de la placa Google Coral Dev
- marketplace-master contiene el codigo referente al marketplace.

## Parte Inteligencia Artificial

Los requisitos para esta parte serán los siguientes:

### Dentro del ordenador

- Base de Datos MySQL , recomendamos el uso de MySQL Workbech para su creacion
- Entorno de desarrollo de python, recomendamos PyCharm
- Las siguientes bibliotecas instaladas en el sistema:
Tensorflow,OpenCV,Pillow,Pandas y Keras.

### Dentro de la placa

- Instalacion de las siguientes bibliotecas dentro del sistema : pip3 y git.
- Instalacion de los siguientes paquetes de python : dlib,face-recognition,mysql-connector-python,OpenCV,Pillow,pycoral y numpy.

### modeloSentimientos

Para la separación de las imágenes entre datos de entrenamiento y datos de validación, ejecutaremos procesadoImagenes.py , que nos separará los sentimientos Happy, Neutral y Sad en diferentes carpetas. Una vez generados los datos, se genera el modelo, ya bien con la arquitectura propia con el archivo entrenarModeloPropio.py o con una arquitectura ya creada como mobilbet_v2 con el archivo entrenarModeloPropio. Dentro de estos dos archivos, hay que indicar la dirección donde se encuentran los datos tantos de validación como de entrenamiento. Una vez creados se deben transformar a tflite para su uso dentro de la placa con el archivo transformarTFLITE.py, donde indicaremos la ubicación de los modelos entrenador en formato .h5


### Placa

Se deben crear la carpeta porProcesar,faces y el archivo errores.txt para el correcto funcionamiento del código .

Dentro de la carpeta faces, se deben colocar las imágenes referentes a las persoans que van a ser predecidas por el sistema (en formato jpg o png). En la carpeta porProcesar se situarán las imágenes de manera temporal durante su procesamiento. Dentro del archivo proceso2.py se debe indicar el modelo de tflite que se va a usar dentro de la función deteccionDeSentimiento además de las credenciales de la base de datos dentro de la función envioBBDD. La gestión de errores de la función envioBBDD escribirá los datos que no se han podido enviar a la base de datos en el archivo errores.txt

Se ejecutara el proceso1.py para la generacion de imagenes para posteriormente ejecutar el proceso2.py para el procesado y elminacion de las mismas.

## marketplace-master

Requisitos:

- Instalacion de Ganache en el sistema
- Metamask instalado dentro del navegador
- Node.js instalado en el sistema

Se descargara el directorio y nos localizaremos dentro de el con la cmd. Ejecutamos las siguientes acciones:
- npm install
- Abrimos ganache
- npm migrate
- npm run start 

Con estos pasos tendremos el marketplace desplegado en el sistema.


