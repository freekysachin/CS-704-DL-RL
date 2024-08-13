import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Input
from keras.utils import to_categorical

data = pd.read_excel("./asset/Pumpkin_Seeds_Dataset.xlsx")
x= data.drop('Class', axis = 1)
y = data['Class']

sc= StandardScaler()
x_scaled = sc.fit_transform(x)

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
y_encoded = to_categorical(y_encoded)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y_encoded, test_size = 0.3)

model = Sequential()
model.add(Input(shape=(x_train.shape[1],)))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(2, activation='softmax'))
model.compile(optimizer = 'Adam', loss='binary_crossentropy', metrics=['accuracy'])
print(model.summary())

model.fit(x_train, y_train, epochs = 100)

loss,accuracy=model.evaluate(x_test,y_test)
print('loss: ',loss)
print('accuracy',accuracy)