import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import keras
from keras import models
from keras import layers

data = pd.read_csv('./asset/Salary_Data.csv')

x = data['YearsExperience'].values.reshape(-1, 1)
y = data['Salary'].values

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


model = models.Sequential()
model.add(layers.Dense(20, input_dim=1 ,activation=keras.activations.relu , use_bias=True))
model.add(layers.Dense(80 ,activation=keras.activations.relu , use_bias=True))
model.add(layers.Dense(1,activation=keras.activations.linear , use_bias=True))

model.compile(optimizer=keras.optimizers.RMSprop(learning_rate=0.008), loss=keras.losses.mean_squared_error, metrics=['mean_absolute_error'] )

print(model.summary())

# Fit the model
history = model.fit(X_train, y_train, epochs=550, validation_split=0.1)

loss, mae = model.evaluate(X_test, y_test)
print(f"Test Mean Absolute Error: {mae}")

# model.save('02model-lr.keras')