import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Input
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score
from keras.utils import to_categorical

data = pd.read_csv('./asset/Tulip-dataset.csv')
print(data.isnull().sum())

scalar = StandardScaler()
x= data.drop("species",axis=1)
y= data["species"]
x_scaled = scalar.fit_transform(x)

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
y_encoded=to_categorical(y_encoded)

x_train, x_test,y_train,y_test=train_test_split(x_scaled,y_encoded,test_size=0.2)
print(x_train.shape)

model=Sequential()
model.add(Input(shape=(x_train.shape[1],)))  # Using Input layer here
model.add(Dense(32, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(3, activation='softmax'))

model.compile(optimizer='Adam',loss='categorical_crossentropy',metrics=['accuracy'])
print(model.summary())

model.fit(x_train,y_train,epochs=50)
model.save('06model-tulipKaggle-dataset.keras')