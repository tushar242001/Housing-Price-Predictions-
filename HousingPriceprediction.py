import pandas as pd
from sklearn.linear_model import LinearRegression

# read in the training and test data sets
housing_train = pd.read_csv("housing_train.csv")
housing_test = pd.read_csv("housing_test.csv")

# one-hot encode the categorical columns
housing_train = pd.get_dummies(housing_train, columns=["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea", "furnishingstatus"])
housing_test = pd.get_dummies(housing_test, columns=["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea", "furnishingstatus"])

# select the relevant columns for the model
train_x = housing_train[["area", "bedrooms", "bathrooms", "stories", "parking", "mainroad_no", "mainroad_yes", "guestroom_no", "guestroom_yes", "basement_no", "basement_yes", "hotwaterheating_no", "hotwaterheating_yes", "airconditioning_no", "airconditioning_yes", "prefarea_no", "prefarea_yes", "furnishingstatus_furnished", "furnishingstatus_semi-furnished", "furnishingstatus_unfurnished"]]
train_y = housing_train["price"]

# create a Linear Regression model
model = LinearRegression()

# train the model using the training data
model.fit(train_x, train_y)

# select the relevant columns from the test data set
test_x = housing_test[["area", "bedrooms", "bathrooms", "stories", "parking", "mainroad_no", "mainroad_yes", "guestroom_no", "guestroom_yes", "basement_no", "basement_yes", "hotwaterheating_no", "hotwaterheating_yes", "airconditioning_no", "airconditioning_yes", "prefarea_no", "prefarea_yes", "furnishingstatus_furnished", "furnishingstatus_semi-furnished", "furnishingstatus_unfurnished"]]


# make predictions using the test data
test_y_pred = model.predict(test_x)

# combine the predictions with the house IDs
test_y_pred = pd.DataFrame(test_y_pred, columns=["predicted"])
test_y_pred["houseID"] = housing_test["houseID"]

# save the predictions to a new file
test_y_pred.to_csv("predictions.csv", index=False)
