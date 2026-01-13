import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras.models import Model


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
history = autoencoder_conv.fit(x_train, x_train,
                               epochs=15,
                               shuffle=True,
                               callbacks=[callback],
                               validation_data=(x_test, x_test))
len(history.history['loss'])
autoencoder_conv.evaluate(x_test, x_test, verbose=2)
encoded_imgs = autoencoder_conv(x_test).numpy()
decoded_imgs =autoencoder_conv(encoded_imgs).numpy()





