from __future__ import print_function
from keras.preprocessing.image import ImageDataGenerator
from keras.applications import mobilenet_v2

num_classes = 3
img_rows, img_cols = 48, 48
batch_size = 512
train_data_dir = 'datos'
validation_data_dir = 'validacion'
val_datagen = ImageDataGenerator(rescale=1./255)
train_datagen = ImageDataGenerator(
        rescale=1./255,
      rotation_range=30,
      shear_range=0.3,
      zoom_range=0.3,
      horizontal_flip=True,
      fill_mode='nearest')
train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(48,48),
        batch_size=batch_size,
        color_mode="grayscale",
        class_mode='categorical')

validation_generator = val_datagen.flow_from_directory(
        validation_data_dir,
        target_size=(48,48),
        batch_size=batch_size,
        color_mode="grayscale",
        class_mode='categorical')

print(validation_generator.class_indices)

model = mobilenet_v2.MobileNetV2(include_top=True, weights=None, input_tensor=None, input_shape=(48,48,1), pooling=None, classes=3)
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['acc', 'mse'])
model.summary()

nb_train_samples = 13630
nb_validation_samples = 3380
epochs = 150
model_info = model.fit(
            train_generator,
            steps_per_epoch=nb_train_samples // batch_size,
            epochs=epochs,
            validation_data=validation_generator,
            validation_steps=nb_validation_samples // batch_size)

model.save("modelopropio.h5")


