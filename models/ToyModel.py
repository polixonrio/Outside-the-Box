# from tensorflow_core.python.keras.models import Sequential  # Old tensorflow_core import was outdated
# from tensorflow_core.python.keras.layers import Dense  # Old tensorflow_core import was outdated
from tensorflow.keras.models import Sequential  # Updated to modern TensorFlow import
from tensorflow.keras.layers import Dense  # Updated to modern TensorFlow import
import numpy as np

from . import ManualModel


# Note: 'weights' is ignored and just present for compatibility with other networks
def ToyModel(classes=2, input_shape=(2,), weights=None):
    weights1 = np.matrix([[-0.2, 0.8], [0.3, 0.6]])
    weights2 = np.matrix([[1.0, 0.0], [0.0, 1.0]])

    # Tensorflow version (did not work)
    # model = Sequential()
    #
    # # hidden layer
    # layer1 = Dense(2, input_shape=input_shape, activation='relu')
    # model.add(layer1)
    # weights1 = [weights, np.array([0.0, 0.0])]
    # layer1.set_weights(weights1)
    #
    # # output layer
    # weights2 = [weights2, np.array([0.0, 0.0])]
    # layer2 = Dense(classes, activation='softmax')
    # model.add(layer2)
    # layer2.set_weights(weights2)
    #
    # model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    weights = [weights1, weights2]
    activations = ["relu", ""]
    model = ManualModel(weights, activations)

    return model
