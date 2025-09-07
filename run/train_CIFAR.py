from utils import *
from trainers import *


def run_script():
    seed = 0
    data_name = "CIFAR10"
    model_name = "CIFAR"
    n_epochs = 200
    batch_size = 128
    plot_name = "!"  # None = no plots, "" = show plots, "!" = store plots

    for n_classes in range(2, 9+1):
        classes = [k for k in range(n_classes)]
        data_train_model = DataSpec(randomize=False, classes=classes)
        data_test_model = DataSpec(randomize=False, classes=classes)
        classes_string = classes2string(classes)
        # model_path = "CNY19id2_CIFAR_{}.h5".format(classes_string)  # Original repo's naming convention
        model_path = "CNY19id2_CIFAR_{}_New.h5".format(classes_string)  # Updated to match renamed model files with _New suffix
        if plot_name == "!":
            plot_name_current = classes_string
        else:
            plot_name_current = plot_name

        run_training(
            data_name=data_name, data_train_model=data_train_model, data_test_model=data_test_model,
            model_name=model_name, model_path=model_path, n_epochs=n_epochs, batch_size=batch_size,
            seed=seed, plot_name=plot_name_current)


if __name__ == "__main__":
    run_script()
