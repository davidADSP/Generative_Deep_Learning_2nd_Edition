import tensorflow.keras.backend as K

def root_mean_squared_error(y_true, y_pred, axis):
    return K.sqrt(K.mean(K.square(y_pred - y_true), axis = axis))
