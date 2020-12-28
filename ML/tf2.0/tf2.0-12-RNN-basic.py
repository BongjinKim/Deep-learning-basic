#tf2.0 RNN basic
import numpy as np
import tensorflow as tf

def build_model(num_classes, sequence_length, input_dim):
    #cell = tf.keras.layers.LSTMCell(units=num_classes, input_shape=(sequence_length, input_dim))
    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(units=num_classes, input_shape=(sequence_length, input_dim), return_sequences=True),
        tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(units=num_classes, activation='softmax'))
    ])
    return model

sample = "I will be an AI engineer"
char2idx = {c : idx for idx, c  in enumerate(set(sample))}
idx2char = {idx : c for idx, c  in enumerate(set(sample))}
sample2idx = [ char2idx[idx] for idx in sample ]
#RNN hyperparameter
num_classes = len(char2idx)
input_dim = len(char2idx) #input one hot size
sequence_length = len(sample) - 1 #< will be an AI engineer>

#print(char2idx, sample2idx)
#one_hot(index, depth=squence의 길이)
x_data = tf.one_hot(sample2idx[:-1], input_dim)
x_data = tf.reshape(x_data,[1, sequence_length, input_dim])
y_data = tf.one_hot(sample2idx[1:], input_dim)
y_data = tf.reshape(y_data,[1, sequence_length, input_dim])

#print(x_data, y_data)
#final output size
model = build_model(num_classes=num_classes, sequence_length=sequence_length, input_dim=input_dim)
model.summary()
model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(lr=0.1),
                  metrics=['accuracy'])
model.fit(x_data, y_data, epochs=50)
predictions = model.predict(x_data)
for i, prediction in enumerate(predictions):
    #print(prediction)
    result_str = [idx2char[c] for c in np.argmax(prediction, axis=1)]
    print("\tPrediction string : ",''.join(result_str))
'''
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
lstm_18 (LSTM)               (None, 23, 12)            1200
_________________________________________________________________
time_distributed_29 (TimeDis (None, 23, 12)            156
=================================================================
Total params: 1,356
Trainable params: 1,356
Non-trainable params: 0

	Prediction string :   will be an AI engineer

'''
