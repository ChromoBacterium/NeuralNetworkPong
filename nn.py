import tensorflowjs as tfjs
import json
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout

with open('training_data-100k.json') as f:
    data = json.load(f)
    xs = np.array(data['xs'])
    ys = np.array(data['ys'])

x_train = xs[:-10000]
y_train = ys[:-10000]
x_test = xs[-10000:]
y_test = ys[-10000:]

model = Sequential()
model.add(Dense(48, activation='relu', input_dim=6))
model.add(Dropout(0.2))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(3, activation='softmax'))

adam = keras.optimizers.Adam(lr=0.001)

model.compile(optimizer=adam,
              loss='binary_crossentropy',
              metrics=['binary_accuracy'])

model.fit(x_train, y_train, epochs=20, batch_size=128)

score = model.evaluate(x_test, y_test, batch_size=128)
print(score)
model.save("KerasNN")

tfjs.converters.save_keras_model(model, "tfjsmodel")
