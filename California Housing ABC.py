# imports DataSET
from matplotlib import pyplot as plt
from sklearn.datasets import fetch_california_housing
X, y = fetch_california_housing(return_X_y=True)

# Train Test Split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

print("xtrain shape : ", X_train.shape)
print("xtest shape  : ", X_test.shape)
print("ytrain shape : ", y_train.shape)
print("ytest shape  : ", y_test.shape)

#Normalize The DATA
from sklearn.preprocessing import MinMaxScaler
data = [[14448,8], [6192,8], [14448,0], [6192,0]]
scaler = MinMaxScaler()
print(scaler.fit(data))
print(scaler.data_max_)
print(scaler.transform(data))
print(scaler.transform([[2, 2]]))

# Linear regression model
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predicting the test set results
y_pred = regressor.predict(X_test)


# Scatter graph to show the prediction
plt.scatter(y_test, y_pred, c = 'green')
plt.xlabel("Price: in $1000's")
plt.ylabel("Predicted value")
plt.title("True value vs predicted value : Linear Regression")
plt.show()

# feature selection algorithm

cali = fetch_california_housing()
X, y = cali.data, cali.target
print(cali.DESCR)