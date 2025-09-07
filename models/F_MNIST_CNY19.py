# from tensorflow_core.python.keras.models import Sequential  # Old tensorflow_core import was outdated
# from tensorflow_core.python.keras.layers import Convolution2D, Dense, MaxPooling2D, Flatten  # Old tensorflow_core import was outdated
from tensorflow.keras.models import Sequential  # Updated to modern TensorFlow import
from tensorflow.keras.layers import Convolution2D, Dense, MaxPooling2D, Flatten, Input  # Updated to modern TensorFlow import


# Note: 'weights' is ignored and just present for compatibility with other networks
def F_MNIST_CNY19(classes, input_shape, weights=None):
    model = Sequential()
        
    # Use Input layer instead of input_shape parameter to avoid deprecation warning
    model.add(Input(shape=input_shape))
    model.add(Convolution2D(40, (5, 5), strides=(1, 1), activation="relu")) # Removed input_shape parameter
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Convolution2D(20, (5, 5), strides=(1, 1), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(320, activation='relu'))
    model.add(Dense(160, activation='relu'))
    model.add(Dense(80, activation='relu'))
    model.add(Dense(40, activation='relu'))
    model.add(Dense(classes, activation='softmax'))

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    return model
