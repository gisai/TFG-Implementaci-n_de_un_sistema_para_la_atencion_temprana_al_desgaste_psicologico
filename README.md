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

Para la separacion de las imagenes entre datos de entrenamiento y datos de validacion ejecutaresmos procesadoImagenes.py , nos separara los sentimientos Happy Neutral y Sad en diferentes carpetas. Una vez generados los datos se genera el modelo ya bien con la arquitectura propia con el archivo entrenarModeloPropio.py o con una arquitectura ya creada como mobilbet_v2 con el archivo entrenarModeloPropio. Dentro de estos dos archivos hay que indicar la direccion donde se encuentran los datos tantos de validacion como de entrenamiento. Una vez creados se deben transformar a tflite para su uso dentro de la placa con el archivo transformarTFLITE.py donde indicaremos la ubicacion de los modelos entrenador en formato .h5


### Placa

Dentro de la carpeta faces se deben colocar las imagenes referentes a las persoans que van a ser predecidas por el sistema (en formato jpg o png).
En la carpeta porProcesar se situaran las imagenes de manera temporal durante su procesamiento.
Dentro del archivo proceso2.py se debe indicar el modelo de tflite que se va a usar dentro de la funcion deteccionDeSentimiento ademas de las credenciales de la base de datos dentro de la funcion envioBBDD. 
La gestion de errores de la funcion envioBBDD escribira los datos que no se han podido enviar a la base de datos en el archivo errores.txt

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


