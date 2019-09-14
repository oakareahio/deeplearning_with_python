from keras.datasets import imdb
from keras import preprocessing

max_features = 10000  # vocab
maxlen = 20

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

from IPython import embed; embed()

x_train = preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = preprocessing.sequence.pad_sequences(x_test, maxlen=maxlen)

from IPython import embed; embed()

from keras.models import Sequential
from keras.layers import Flatten, Dense, Embedding

model = Sequential()
# Embedding(vocab, output_shape, input_length=input vector dims)
model.add(Embedding(10000, 8, input_length=maxlen))

model.add(Flatten())

model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['acc'])

print(model.summary())

history = model.fit(x_train, y_train,
                    epochs=10,
                    batch_size=32,
                    validation_split=0.2)

