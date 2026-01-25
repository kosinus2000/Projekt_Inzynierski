import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras.models import Model


class Encoder_conv(Model):
    def __init__(self):
        super().__init__()

        self.encoder = tf.keras.Sequential([
            layers.InputLayer(shape=(128, 128, 3)),

            layers.Conv2D(16, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=0.2),
            layers.MaxPooling2D((2, 2)),

            layers.Conv2D(32, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=0.2),
            layers.MaxPooling2D((2, 2)),

            layers.Conv2D(64, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=0.2),
            layers.MaxPooling2D((2, 2)),

            layers.Conv2D(128, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=0.2)
        ])

        self.decoder = tf.keras.Sequential([
            layers.InputLayer(shape=(16, 16, 128)),

            layers.Conv2D(128, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=0.2),
            layers.UpSampling2D((2, 2)),

            layers.Conv2D(64, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=0.2),
            layers.UpSampling2D((2, 2)),

            layers.Conv2D(32, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=0.2),
            layers.UpSampling2D((2, 2)),

            layers.Conv2D(16, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=0.2),

            layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same')
        ])

    def call(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded







