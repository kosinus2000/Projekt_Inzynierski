import keras

from src.models.load_data import load_data
from src.visualization.visualize_output import visualize_output
from src.models.encoder_convolutional import Encoder_conv

def run_experiment():
    x_train, x_test = load_data()

    autoencoder = Encoder_conv()
    autoencoder.compile(optimizer='adam', loss='BinaryCrossentropy', metrics=['accuracy'])

    early_stopping = keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=3,
        restore_best_weights=True
    )

    history = autoencoder.fit(
        x_train, x_train,
        epochs=15,
        shuffle=True,
        callbacks=[early_stopping],
        validation_data=(x_test, x_test)
    )

    decoded_imgs = autoencoder.predict(x_test)

    print(f"Trening zakończony po {len(history.history['loss'])} epokach.")
    autoencoder.evaluate(x_test, x_test, verbose=2)

    visualize_output(x_test, decoded_imgs, 10)