import matplotlib.pyplot as plt


def plot_error(error_plot):
    plt.plot([i for i in range(len(error_plot))], error_plot)
    plt.ylabel('Error')
    plt.xlabel('Epochs')
    plt.show()


def plot_validate(validate_plot):
    plt.plot([i for i in range(len(validate_plot))], validate_plot)
    plt.ylabel('Accuracy')
    plt.xlabel('Epochs')
    plt.show()


