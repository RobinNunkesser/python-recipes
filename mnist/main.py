import tensorflow as tf
import numpy as np
#from keras.utils import plot_model
#import datetime
#import coremltools

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print(x_train[1], sep = ", ")
print(y_train[1])

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#log_dir="logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
#tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

model.fit(x_train, y_train, epochs=5)#,callbacks=[tensorboard_callback])

model.evaluate(x_test, y_test)

predictions = model.predict(x_test)
print(y_test[0])
print(predictions[0])
print(np.argmax(predictions[0]))

# Save the model in HDF5 format.
#keras_file = "keras_model.h5"
#model.save(keras_file)

# Convert to TensorFlow Lite model.
#converter = tf.lite.TFLiteConverter.from_keras_model(model)
#tflite_model = converter.convert()
#open("converted_model.tflite", "wb").write(tflite_model)

# Convert to CoreML model.
#coreml_model = coremltools.converters.keras.convert(model)
#coremltools.utils.save_spec(coreml_model, 'coverted_model.mlmodel')

#model.summary()
#tf.keras.utils.plot_model(model, to_file='model.png', show_shapes=True, dpi=180)

