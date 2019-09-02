from sklearn import datasets
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

# Load dataset
boston = datasets.load_boston()
# Convert to DataFrame
boston_df = DataFrame(boston.data)
# Set column name
boston_df.columns = boston.feature_names
# Add price
boston_df["Price"] = boston.target
# Print 10 records
print(boston_df[:10])

## Create data of training
# Number of room
rooms_train = DataFrame(boston_df["RM"])
# Target is price
T_train = boston.target
# Create model of linear regression
model = linear_model.LinearRegression()
# Training
model.fit(rooms_train, T_train)

# Create test data for number of room
rooms_test = DataFrame(np.arange(rooms_train.values.min(), rooms_train.values.max(), 0.1))
# Predict price from test data by model
prices_test = model.predict(rooms_test)

## Draw graph
# Trained data
plt.scatter(rooms_train.values.ravel(), T_train, c = "b", alpha = 0.5)
# Regression line
plt.plot(rooms_test.values.ravel(), prices_test, c = "r")
plt.title("House Prices dataset")
plt.xlabel("rooms")
plt.ylabel("price $1000's")
plt.show()

