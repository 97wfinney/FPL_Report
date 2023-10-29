import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Prompt the user for input
current_gw = input("Please enter the current gameweek: ")

# Convert the input string to an integer
try:
    current_gw = int(current_gw)
    print(f"Current gameweek set to: {current_gw}")
except ValueError:
    print("Invalid input! Please enter a valid gameweek number.")


# Load the combined CSV file into a DataFrame
df = pd.read_csv('GK_master.csv')

# Create a new column for next week's total points
df['next_week_total_points'] = df.groupby('name')['total_points'].shift(-1)

# Drop rows with NaNs caused by the shift operation
df.dropna(subset=['next_week_total_points'], inplace=True)

# Split the DataFrame into features (X) and target (y)
X = df.drop(['name', 'element', 'next_week_total_points'], axis=1)
y = df['next_week_total_points']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the feature data
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the neural network architecture
model = Sequential()
model.add(Dense(32, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, batch_size=32)


# Load the data for previous gameweek
df_24 = pd.read_csv('GK_data.csv')

# Prepare the feature data. Drop the columns that were dropped during training.
X_24 = df_24.drop(['name', 'element'], axis=1)

# Scale the features using the same scaler used in training.
X_24_scaled = scaler.transform(X_24)

# Make predictions using the trained model.
predictions = model.predict(X_24_scaled)

# Add the predictions to the DataFrame.
df_24['predicted_points'] = predictions

# Sort the DataFrame by the predicted points in descending order and take the top 10 players.
top_players = df_24.sort_values('predicted_points', ascending=False).head(10)

# Save the top players DataFrame.
top_players[['name', 'predicted_points']].to_csv('GK_prediction.csv', index=False)

# Print the top players DataFrame.
print(top_players[['name', 'predicted_points']])


# Load the combined CSV file into a DataFrame
df = pd.read_csv('DEF_master.csv')


# Create a new column for next week's total points
df['next_week_total_points'] = df.groupby('name')['total_points'].shift(-1)

# Drop rows with NaNs caused by the shift operation
df.dropna(subset=['next_week_total_points'], inplace=True)

# Split the DataFrame into features (X) and target (y)
X = df.drop(['name', 'element', 'next_week_total_points'], axis=1)
y = df['next_week_total_points']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the feature data
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the neural network architecture
model = Sequential()
model.add(Dense(32, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, batch_size=32)


# Load the data for previous gameweek
df_24 = pd.read_csv('DEF_data.csv')

# Prepare the feature data. Drop the columns that were dropped during training.
X_24 = df_24.drop(['name', 'element'], axis=1)

# Scale the features using the same scaler used in training.
X_24_scaled = scaler.transform(X_24)

# Make predictions using the trained model.
predictions = model.predict(X_24_scaled)

# Add the predictions to the DataFrame.
df_24['predicted_points'] = predictions

# Sort the DataFrame by the predicted points in descending order and take the top 10 players.
top_players = df_24.sort_values('predicted_points', ascending=False).head(10)

# Save the top players DataFrame.
top_players[['name', 'predicted_points']].to_csv('DEF_prediction.csv', index=False)

# Print the top players DataFrame.
print(top_players[['name', 'predicted_points']])


# Load the combined CSV file into a DataFrame
df = pd.read_csv('MID_master.csv')


# Create a new column for next week's total points
df['next_week_total_points'] = df.groupby('name')['total_points'].shift(-1)

# Drop rows with NaNs caused by the shift operation
df.dropna(subset=['next_week_total_points'], inplace=True)

# Split the DataFrame into features (X) and target (y)
X = df.drop(['name', 'element', 'next_week_total_points'], axis=1)
y = df['next_week_total_points']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the feature data
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the neural network architecture
model = Sequential()
model.add(Dense(32, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, batch_size=32)



# Load the data for previous gameweek
df_24 = pd.read_csv('MID_data.csv')

# Prepare the feature data. Drop the columns that were dropped during training.
X_24 = df_24.drop(['name', 'element'], axis=1)

# Scale the features using the same scaler used in training.
X_24_scaled = scaler.transform(X_24)

# Make predictions using the trained model.
predictions = model.predict(X_24_scaled)

# Add the predictions to the DataFrame.
df_24['predicted_points'] = predictions

# Sort the DataFrame by the predicted points in descending order and take the top 10 players.
top_players = df_24.sort_values('predicted_points', ascending=False).head(10)

# Save the top players DataFrame.
top_players[['name', 'predicted_points']].to_csv('MID_prediction.csv', index=False)

# Print the top players DataFrame.
print(top_players[['name', 'predicted_points']])



# Load the combined CSV file into a DataFrame
df = pd.read_csv('FWD_master.csv')


# Create a new column for next week's total points
df['next_week_total_points'] = df.groupby('name')['total_points'].shift(-1)

# Drop rows with NaNs caused by the shift operation
df.dropna(subset=['next_week_total_points'], inplace=True)

# Split the DataFrame into features (X) and target (y)
X = df.drop(['name', 'element', 'next_week_total_points'], axis=1)
y = df['next_week_total_points']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the feature data
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the neural network architecture
model = Sequential()
model.add(Dense(32, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, batch_size=32)

# Load the data for previous gameweek
df_24 = pd.read_csv('FWD_data.csv')

# Prepare the feature data. Drop the columns that were dropped during training.
X_24 = df_24.drop(['name', 'element'], axis=1)

# Scale the features using the same scaler used in training.
X_24_scaled = scaler.transform(X_24)

# Make predictions using the trained model.
predictions = model.predict(X_24_scaled)

# Add the predictions to the DataFrame.
df_24['predicted_points'] = predictions

# Sort the DataFrame by the predicted points in descending order and take the top 10 players.
top_players = df_24.sort_values('predicted_points', ascending=False).head(10)

# Save the top players DataFrame.
top_players[['name', 'predicted_points']].to_csv('FWD_prediction.csv', index=False)

# Print the top players DataFrame.
print(top_players[['name', 'predicted_points']])


# Define the positions and corresponding prediction files
positions = ['GK', 'DEF', 'MID', 'FWD']
prediction_files = {'GK': 'GK_prediction.csv', 'DEF': 'DEF_prediction.csv', 'MID': 'MID_prediction.csv', 'FWD': 'FWD_prediction.csv'}

# Create a DataFrame to store the top 10 players for each position
top_players_df = pd.DataFrame()

# Iterate over the positions and read the corresponding prediction file
for position in positions:
    prediction_df = pd.read_csv(prediction_files[position])
    top_players = prediction_df['name'].head(10).tolist()  # Assuming the 'name' column contains player names
    top_players_df[position] = top_players

# Save the DataFrame to a TXT file with the game week in the title
game_week = current_gw + 1  
filename = f'Gameweek_{game_week}_predictions.txt'
top_players_df.to_csv(filename, index=False, sep='\t')

print(f"Top players for Gameweek {game_week} saved to {filename}")










































