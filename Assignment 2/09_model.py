import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Input
from keras.utils import to_categorical

data = pd.read_csv('./asset/seattle-weather.csv')

print(data.isnull().sum())
x = data.drop('weather', axis = 1)
y = data['weather']

x['date'] = pd.to_datetime(x['date']).astype('int64') / 10**9  
sc = StandardScaler()
x_sc = sc.fit_transform(x)

label_encoder = LabelEncoder()
y_enoded = label_encoder.fit_transform(y)
y_enc = to_categorical(y_enoded)


x_train, x_test, y_train, y_test = train_test_split(x_sc, y_enc, test_size = 0.3)

model = Sequential()
model.add(Input(shape = (x_train.shape[1],)))
model.add(Dense(30, activation = 'relu'))
model.add(Dense(20, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(5, activation = 'softmax'))
model.compile(optimizer = 'SGD', loss = 'categorical_crossentropy', metrics = ['categorical_accuracy'])
print(model.summary())

model.fit(x_train, y_train, epochs = 100 ,  batch_size=20 , validation_split=0.1)
loss, accuracy = model.evaluate(x_test, y_test)

print('Test accuracy:', accuracy)