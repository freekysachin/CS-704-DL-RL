from keras.models import Sequential
import tensorflow as tf
from keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import keras
from tensorflow.keras.callbacks import LearningRateScheduler, Callback
import matplotlib.pyplot as plt

iris = load_iris()
X, y = iris.data, iris.target
encoder = OneHotEncoder(sparse_output=False)
y = encoder.fit_transform(y.reshape(-1, 1))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

class EpochLearningRateTracker(Callback):
    def __init__(self):
        self.learning_rates = []
        self.epochs = []

    def on_epoch_end(self, epoch, logs=None):
        lr = self.model.optimizer.learning_rate
        if isinstance(lr, tf.keras.optimizers.schedules.LearningRateSchedule):
            lr = lr(epoch).numpy()
        else:
            lr = lr.numpy()
        
        self.learning_rates.append(lr)
        self.epochs.append(epoch + 1)
        print(f"Epoch {epoch + 1}: Learning rate is {lr:.6f}")
        
def scheduler(epoch, lr):
    return lr * 0.90
    
lr_scheduler = LearningRateScheduler(scheduler)
lr_tracker = EpochLearningRateTracker()

model = Sequential()
model.add(Dense(10, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))   

model.compile(optimizer=keras.optimizers.Adam() ,loss='categorical_crossentropy', metrics=['accuracy'])
print(model.summary())
model.fit(X_train, y_train, epochs=35, batch_size=10, callbacks =[lr_tracker , lr_scheduler] , validation_data=(X_test, y_test))

plt.figure(figsize=(10, 6))
plt.plot(lr_tracker.epochs, lr_tracker.learning_rates, marker='o')
plt.title('Learning Rate vs. Epochs')
plt.xlabel('Epochs')
plt.ylabel('Learning Rate')
plt.grid(True)
plt.show()

test_loss, test_acc = model.evaluate(X_test, y_test)

print('Test accuracy:', test_acc)

model.save('01model.h5')

