from matplotlib import pyplot as plt


def visualize_output ( test_data, decoded_data,quantity: int =10, figsize: tuple = (20, 4)):
    plt.figure(figsize=figsize)
    n = quantity
    x_test = test_data
    decoded_imgs = decoded_data
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