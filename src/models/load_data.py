def load_data():
    (x_train)  = set_generator_with_random_aligment(5000)
    (x_test) = set_generator_with_random_aligment(1000)
    x_train = np.array(x_train, dtype='float32') / 255.
    x_test = np.array(x_test, dtype='float32') / 255.

    return x_train, x_test