import pandas as pd
import numpy as np
import matplotlib as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('core/data/cow_data.csv')
df.fillna(-1, inplace=True)

X = df.drop(['price'], axis = 1)
y = df['price']

X_test, X_train, y_test, y_train = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluation
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2:", r2_score(y_test, y_pred))

# Coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)