import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras

# Prompt the user for input
current_gw = input("Please enter the current gameweek: ")

# Convert the input string to an integer
try:
    current_gw = int(current_gw)
    print(f"Current gameweek set to: {current_gw}")
except ValueError:
    print("Invalid input! Please enter a valid gameweek number.")


def train_and_predict(data_train, data_predict, position):
    # Split the data into X and y
    X_train = data_train.drop(columns=["name", "element", "GW", "total_points"])
    y_train = data_train["total_points"]
    
    X_predict = data_predict.drop(columns=["name", "element", "GW", "total_points"])
    
    # Normalize the data
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_predict = scaler.transform(X_predict)
    
    # Define the neural network model
    model = keras.Sequential([
        keras.layers.Dense(64, activation="relu", input_shape=(X_train.shape[1],)),
        keras.layers.Dropout(0.3),
        keras.layers.Dense(32, activation="relu"),
        keras.layers.Dropout(0.3),
        keras.layers.Dense(1)
    ])
    
    model.compile(optimizer="adam", loss="mse")
    
    # Train the model
    model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.1, verbose=0)
    
    # Make predictions
    predicted_points = model.predict(X_predict)
    
    # Create the predictions dataframe
    predictions_df = data_predict[["name"]].copy()
    predictions_df["predicted_points"] = predicted_points
    
    # Sort by predicted_points and take top 10
    predictions_df = predictions_df.sort_values(by="predicted_points", ascending=False).head(10)
    
    return predictions_df


num_runs = 3
positions = ['GK', 'DEF', 'MID', 'FWD']
predictions_all_runs = {position: [] for position in positions}

for run in range(num_runs):
    for position in positions:
        data_train = pd.read_csv(f"{position}_master.csv")
        data_predict = pd.read_csv(f"{position}_data.csv")
        predictions = train_and_predict(data_train, data_predict, position)
        predictions_all_runs[position].append(predictions)

# Save to a CSV file
next_gw = current_gw + 1
filename = f"Gameweek_{next_gw}_predictions.csv"

# Create a new empty DataFrame for each position
for position in positions:
    df_predictions = pd.DataFrame(columns=['Name', 'Run 1', 'Name', 'Run 2', 'Name', 'Run 3'])
    
    for i in range(len(predictions_all_runs[position][0])):  # Assuming same number of players in each run
        player_name_1 = predictions_all_runs[position][0].iloc[i]['name']
        points_run_1 = predictions_all_runs[position][0].iloc[i]['predicted_points']
        
        player_name_2 = predictions_all_runs[position][1].iloc[i]['name']
        points_run_2 = predictions_all_runs[position][1].iloc[i]['predicted_points']
        
        player_name_3 = predictions_all_runs[position][2].iloc[i]['name']
        points_run_3 = predictions_all_runs[position][2].iloc[i]['predicted_points']
        
        df_predictions.loc[i] = [player_name_1, points_run_1, player_name_2, points_run_2, player_name_3, points_run_3]
    
    # Append the DataFrame to the CSV file
    with open(filename, 'a') as f:
        f.write(position + ' prediction\n')
        df_predictions.to_csv(f, index=False)
        f.write("\n")
