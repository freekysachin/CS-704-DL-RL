import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Input
from keras.utils import to_categorical

data = pd.read_csv('./asset/Almond.csv')
print(data.head)
print(data.isnull().sum())

data.loc[:, 'Length (major axis)'] = data['Length (major axis)'].fillna(data['Length (major axis)'].mean())
data.loc[:, 'Width (minor axis)'] = data['Width (minor axis)'].fillna(data['Width (minor axis)'].mean())
data.loc[:, 'Thickness (depth)'] = data['Thickness (depth)'].fillna(data['Thickness (depth)'].mean())
data.loc[:, 'Roundness'] = data['Roundness'].fillna(data['Roundness'].mean())
data.loc[:, 'Aspect Ratio'] = data['Aspect Ratio'].fillna(data['Aspect Ratio'].mean())
data.loc[:, 'Eccentricity'] = data['Eccentricity'].fillna(data['Eccentricity'].mean())

print(data.isnull().sum())

x = data.drop("Type", axis=1)
y = data["Type"]
scalar = StandardScaler()
x_scaled = scalar.fit_transform(x)
print(x_scaled)

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
y_encoded=to_categorical(y_encoded)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y_encoded, test_size = 0.3)
print(x_train.shape)

model= Sequential()
model.add(Input(shape=(x_train.shape[1],)))
model.add(Dense(32, input_shape=(10,), activation='relu'))  
model.add(Dense(16, activation='relu'))                     
model.add(Dense(8, activation='relu'))                      
model.add(Dense(3, activation='softmax')) 
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
print(model.summary())

model.fit(x_train,y_train,epochs=50)

loss,accuracy=model.evaluate(x_test,y_test)
print('loss: ',loss)
print('accuracy',accuracy)
