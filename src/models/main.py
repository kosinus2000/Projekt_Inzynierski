import keras
import numpy as np

from src.models.load_data import load_data
from src.visualization.visualize_output import visualize_output
from src.models.encoder_convolutional import Encoder_conv


def print_diag(model, x_test, decoded_imgs):
    print("--- DIAGNOSTYKA ---")
    test_loss, test_acc = model.evaluate(x_test, x_test, verbose=2)
    mse = np.mean(np.square(x_test - decoded_imgs))
    print(f'MSE: {mse:.5f}')
    print(f'Test loss: {test_loss:.4f}')
    print(f'Test accuracy: {test_acc*100:.2f}%')
    stats = [
        ("Min", x_test.min(), decoded_imgs.min()),
        ("Max", x_test.max(), decoded_imgs.max()),
        ("Mean", x_test.mean(), decoded_imgs.mean())
    ]

    print(f"{'Statystyka':<12} | {'Oryginał':<10} | {'Rekonstrukcja':<13} | {'Różnica'}")
    for name, orig, reco in stats:
        diff = orig - reco
        print(f"{name:<12} | {orig:<10.4f} | {reco:<13.4f} | {diff:+.4f}")

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
    print_diag(autoencoder, x_test, decoded_imgs)
    visualize_output(x_test, decoded_imgs, 10)





