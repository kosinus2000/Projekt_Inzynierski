import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras import losses

from tensorflow.keras import layers
from tensorflow.keras.models import Model

from src.data_generation.data_generator import set_generator_with_random_aligment


def load_data():
    (x_train)  = set_generator_with_random_aligment(5000)
    (x_test) = set_generator_with_random_aligment(1000)
    x_train = np.array(x_train, dtype='float32') / 255.
    x_test = np.array(x_test, dtype='float32') / 255.

    return x_train, x_test

class Encoder_conv(Model):
    def __init__(self):
        super().__init__()

        self.encoder = tf.keras.Sequential([
            layers.InputLayer(input_shape=(128, 128, 3)),

            layers.Conv2D(16, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(alpha=0.2),
            layers.MaxPooling2D((2, 2)),

            layers.Conv2D(32, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(alpha=0.2),
            layers.MaxPooling2D((2, 2)),

            layers.Conv2D(64, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(alpha=0.2),
            layers.MaxPooling2D((2, 2)),

            layers.Conv2D(128, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(alpha=0.2)
        ])

        self.decoder = tf.keras.Sequential([
            layers.InputLayer(input_shape=(16, 16, 128)),

            layers.Conv2D(128, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(alpha=0.2),
            layers.UpSampling2D((2, 2)),

            layers.Conv2D(64, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(alpha=0.2),
            layers.UpSampling2D((2, 2)),

            layers.Conv2D(32, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(alpha=0.2),
            layers.UpSampling2D((2, 2)),

            layers.Conv2D(16, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(alpha=0.2),

            layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same')
        ])

    def call(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded


autoencoder_conv = Encoder_conv()
autoencoder_conv.compile(optimizer='adam', loss='BinaryCrossentropy',metrics=['accuracy'])

x_train, x_test = load_data()
autoencoder_conv.fit(x_train, x_train,
                     epochs=15,
                     shuffle=True,
                     validation_data=(x_test, x_test))

encoded_imgs = autoencoder_conv.encoder(x_test).numpy()
decoded_imgs = autoencoder_conv.decoder(encoded_imgs).numpy()

print("--- DIAGNOSTYKA ---")
test_loss, test_acc = autoencoder_conv.evaluate(x_test, x_test, verbose=2)
print(f'Test accuracy: {test_acc*100:.2f}%')
print(f"Input Min: {x_test.min()}, Max: {x_test.max()}, Mean: {x_test.mean()}")
print(f"Output Min: {decoded_imgs.min()}, Max: {decoded_imgs.max()}, Mean: {decoded_imgs.mean()}")

n = 10
plt.figure(figsize=(20, 4))
for i in range(n):
      # display original
      ax = plt.subplot(2, n, i + 1)
      plt.imshow(x_test[i])
      plt.title("original")
      plt.gray()
      ax.get_xaxis().set_visible(False)
      ax.get_yaxis().set_visible(False)

      # display reconstruction
      ax = plt.subplot(2, n, i + 1 + n)
      plt.imshow(decoded_imgs[i])
      plt.title("reconstructed")
      plt.gray()
      ax.get_xaxis().set_visible(False)
      ax.get_yaxis().set_visible(False)
plt.show()

