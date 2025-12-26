import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, losses
from tensorflow.keras.models import Model


from src.data_generation.data_generator import set_generator
from visualization.visualize_output import visualize_output


def load_data():
    (x_train)  = set_generator(5000)
    (x_test) = set_generator(1000)
    x_train = np.array(x_train, dtype='float32') / 255.
    x_test = np.array(x_test, dtype='float32') / 255.

    return x_train, x_test

latent_dim = 64

class Autoencoder(Model):
  def __init__(self, latent_dim):
    super().__init__()
    self.latent_dim = latent_dim

    self.encoder = tf.keras.Sequential([
      layers.Flatten(),
      layers.Dense(latent_dim, activation='relu'), #encoder
    ])
    self.decoder = tf.keras.Sequential([
      layers.Dense(2352, activation='sigmoid'),
      layers.Reshape((28, 28, 3))
    ])

  def call(self, x):
    encoded = self.encoder(x)
    decoded = self.decoder(encoded)
    return decoded



# Utworzenie instancji enkodera
autoencoder = Autoencoder(latent_dim)

autoencoder.compile(optimizer="adam", loss=losses.MeanSquaredError())

x_train, x_test = load_data()
autoencoder.fit(x_train, x_train,
                epochs=10,
                shuffle=True,
                validation_data=(x_test, x_test))

encoded_imgs = autoencoder.encoder(x_test).numpy()
decoded_imgs = autoencoder.decoder(encoded_imgs).numpy()


n = 10
visualize_output(x_test, decoded_imgs, n)