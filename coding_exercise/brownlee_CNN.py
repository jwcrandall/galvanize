'''
This is an exercise found on Machine Learning Mastery:
How to develop convolutional nueral network.
https://machinelearningmastery.com/how-to-develop-convolutional-neural-network-models-for-time-series-forecasting/?__s=j7zzzgjjjh5sd9m3cfd8

Model Description:
The model is fit using the efficient Adam version of stochastic gradient descent
and optimized using the mean squared error, or ‘mse‘, loss function.
'''
from numpy import array
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
# split a univariate sequence into samples
def split_sequence(sequence, n_steps):
    X, y = list(), list()
    for i in range(len(sequence)):
        #find the end of this pattern
        end_ix = i + n_steps
        # check if we are beyond the split_sequence
        if end_ix > len(sequence)-1:
            break
        #gather input and output parts of the pattern
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return array(X), array(y)

# define input split_sequence
raw_seq = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# choose number of time n_steps
n_steps = 3
# Split into samples
X, y = split_sequence((X.shape[0], X.shape[1], n_features))
# reshape from [samples, timesteps] into [samples, timesteps, features]
n_features = 1
X = X.reshape((X.shape[0], X.shape[1], n_features))
# define model
model = Sequential()
model.add(Conv1D(filters = 64, kernel_size=2, activation='relu', input_shape=(n_steps, n_features)))
model.add(MaxPooling1D(pool_size=2))
# A flatten layer is used between the convolutional layers and the dense layer
# to reduce the feature maps to a single one-dimensional vector.
model.add(Flatten())
model.add(Dense(50, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam',loss='mse')
# fit model
model.fit(X, y, epochs = 1000, verbose=0)
# demonstrate predictions
x_input = array([70, 80, 90])
x_input = x_input.reshape((1, n_steps, n_features))
yhat = model.predict(x_input, verbose = 0)
print(yhat)


if __name__ == '__main__':

    # define input sequence
    raw_seq = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    # choose a number of time steps
    n_steps = 3
    # split into samples
    X, y = split_sequence(raw_seq, n_steps)
    # summarize the data
    for i in range(len(X)):
        print(X[i], y[i])
