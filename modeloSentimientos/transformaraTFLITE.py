import tensorflow as tf

new_model = tf.keras.models.load_model('--')
converter = tf.lite.TFLiteConverter.from_keras_model(new_model)
tflite_model = converter.convert()
open("--.tflite", "wb").write(tflite_model)
print("Todo acabado")