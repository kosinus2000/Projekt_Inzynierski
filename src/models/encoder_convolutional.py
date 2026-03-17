import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras.models import Model

solope = 0.2

class Encoder_conv(Model):
    def __init__(self):
        super().__init__()

        self.encoder = tf.keras.Sequential([
            layers.InputLayer(shape=(128, 128, 3)), # wymiary zdjęcia i 3 kolory RGB

            layers.Conv2D(16, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=solope),
            layers.MaxPooling2D((2, 2)),

            layers.Conv2D(32, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=solope),
            layers.MaxPooling2D((2, 2)),

            layers.Conv2D(64, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=solope),
            layers.MaxPooling2D((2, 2)),

            # layers.Conv2D(96, (3,3), padding='same'),
            # layers.BatchNormalization(),
            # layers.LeakyReLU(negative_slope=solope),
            # layers.UpSampling2D((2, 2)),

            layers.Conv2D(128, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=solope)
        ])

        self.decoder = tf.keras.Sequential([
            layers.InputLayer(shape=(16, 16, 128)),

            layers.Conv2D(128, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=0.2),
            layers.UpSampling2D((2, 2)),

            # layers.Conv2D(96, (3, 3), padding='same'),
            # layers.BatchNormalization(),
            # layers.LeakyReLU(negative_slope=solope),
            # layers.UpSampling2D((2, 2)),

            layers.Conv2D(64, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=0.2),
            layers.UpSampling2D((2, 2)),

            layers.Conv2D(32, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=0),
            layers.UpSampling2D((2, 2)),

            layers.Conv2D(16, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=solope),

            layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same')
        ])

    def call(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded







