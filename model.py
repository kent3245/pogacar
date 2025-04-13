import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Load the dataset; file should have columns: 'race_name' and 'race_speed'
df = pd.read_csv('race_data_output.csv')

# Display the first few rows and column names to inspect the data
print("Columns in the dataset:", df.columns)
print(df.head())

# Since our CSV only contains data for 2024, we are going to assume
# that the speeds recorded are for that year and we want to predict for next year.
# In a more complete dataset, you might have a column for the year.
# Here, we add a column 'year' for clarity.
df['year'] = 2024

# We will use the race name as our main feature.
# Since race names are categorical, we use OneHotEncoder to convert these to numeric features.
encoder = OneHotEncoder(sparse=False)
race_encoded = encoder.fit_transform(df[['race_name']])

# Create a DataFrame with the encoded race names and keep track of the feature names
race_feature_names = encoder.get_feature_names_out(['race_name'])
df_encoded = pd.DataFrame(race_encoded, columns=race_feature_names)

# Combine the encoded features with the original dataframe (if you plan to use additional numerical features later)
df_model = pd.concat([df[['race_speed']], df_encoded], axis=1)

# In this simple example, our feature matrix X consists solely of the encoded race name.
X = df_model.drop('race_speed', axis=1)
y = df_model['race_speed']

# Since we only have one year of data, splitting into training and test sets may not be very informative,
# but we include a split to mimic a standard modeling workflow.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model on the training data
model.fit(X_train, y_train)

# Evaluate performance on the test set
y_pred_test = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred_test)
print("Mean Absolute Error on test data:", mae)

# ------------------------------------------------------------------------------
# Prediction for 2025:
# Suppose you want to predict the race speed for a specific race this year (e.g., the same race as in 2024).
# Create a new input DataFrame for the race of interest with the same structure.
#
# Example: Predicting for a race named "Grand Prix A"

race_to_predict = "Grand Prix A"

# We need to encode this race name using the same OneHotEncoder.  
# Note: If the race name is new (never seen during training), the encoder will raise an error.
# For production use, you'll need to handle unknown categories appropriately.
race_input_encoded = encoder.transform([[race_to_predict]])
X_new = pd.DataFrame(race_input_encoded, columns=race_feature_names)

predicted_speed = model.predict(X_new)
print(f"Predicted Race Speed for '{race_to_predict}' in 2025: {predicted_speed[0]:.2f}")

# ------------------------------------------------------------------------------
# Note:
# This model will effectively be memorizing the 2024 speeds tied to each race name.
# For a more robust forecast, consider incorporating data from multiple years or additional features.
