import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Input, Dropout
from keras.utils import to_categorical

df = pd.read_csv('./asset/lifestyle_sustainability_data.csv')
print(df.dtypes)

label_encodes = {}
for col in ['Location', 'DietType', 'LocalFoodFrequency', 'TransportationMode', 'EnergySource', 'HomeType', 'ClothingFrequency', 'SustainableBrands', 'CommunityInvolvement', 'Gender', 'UsingPlasticProducts', 'DisposalMethods', 'PhysicalActivities']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encodes[col] = le

x = df.drop('Rating', axis = 1)
scaler = StandardScaler()
x = scaler.fit_transform(x)
y = df['Rating']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train) 

model = Sequential()
model.add(Input(shape=(x_train.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))  # Dropout 
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(24, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(6, activation='softmax')) 

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print(model.summary())

model.fit(x_train, y_train, epochs=50, validation_split=0.2)

loss, accuracy = model.evaluate(x_test, y_test)
print(accuracy)