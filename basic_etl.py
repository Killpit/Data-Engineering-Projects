import tensorflow.keras as keras
(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()

x_train.shape

y_train.shape

x_test.shape

y_test.shape

import numpy as np

x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

x_train = np.reshape(x_train, (x_train.shape[0], 28, 28, 1))
x_test = np.reshape(x_test, (x_test.shape[0], 28, 28, 1))

x_train.shape

y_train.shape

x_test.shape

y_test.shape

import sqlite3

conn = sqlite3.connect('fashion_mnist.db')

conn.execute('''CREATE TABLE IF NOT EXISTS images
(id INTEGER PRIMARY KEY AUTOINCREMENT, image BLOB NOT NULL,
label INTEGER NOT NULL);''')

for i in range(x_train.shape[0]):
  conn.execute('INSERT INTO images (image, label) VALUES (?, ?)',
               [sqlite3.Binary(x_train[i]), y_train[i]])

conn.commit()

for i in range(x_test.shape[0]):
  conn.execute('INSERT INTO images (image, label) VALUES (?, ?)',
               [sqlite3.Binary(x_test[i]), y_test[i]])

conn.commit()

conn.close()

conn = sqlite3.connect('fashion_mnist.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM images')
rows = cursor.fetchall()

import pandas as pd

data = pd.read_sql_query('SELECT * FROM images', conn)
