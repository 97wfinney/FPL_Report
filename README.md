# EPL Fantasy Football Neural Network Predictor

## Overview

The EPL Fantasy Football Neural Network Predictor is a sophisticated machine learning project aimed at predicting the performance of English Premier League (EPL) football players in fantasy leagues. The project consists of two main components:

1. **Data Preparation (Player Data.ipynb)**: This notebook contains the code for collecting, processing, and preparing the data required for training and making predictions. It leverages the official FPL API to gather gameweek statistics for players in different positions (GK, DEF, MID, FWD) and organizes them into a structured format suitable for machine learning.


2. **Prediction Script (prediction.py)**: This Python script is the primary tool for running the neural network model, which predicts the next gameweek's total points for players based on their historical performance. After processing the data, the script utilizes the trained neural network model to output predictions to a CSV file, providing an efficient and streamlined approach to generating fantasy player forecasts.

3. **Legacy Prediction Model (Legacy/Prediction Model.ipynb)**: Previously the main tool for predictions, this notebook encapsulates the original neural network model used for player point predictions. While it's no longer the primary prediction tool, it remains valuable as it offers a detailed step-by-step walkthrough of the neural network architecture and its training process, serving as a comprehensive guide for those interested in the underlying methodology.

## Technical Details

### Data Preparation

The data preparation process involves several key steps:

- **Data Collection**: Utilises the FPL API to gather gameweek statistics.
- **Data Transformation**: Organises the data into specific positions and calculates additional features, such as mean reversion.
- **Data Saving**: Saves the data into CSV files, including current season data and master files containing historical data.

### Master Files

The master files include comprehensive FPL data for the 19/20, 20/21, and 21/22 seasons. They are essential for training the model and are available in the GitHub repository.

### Prediction Model

The prediction model is built using the following approach:

- **Data Loading**: Reads the historical data from the master CSV files.
- **Feature Engineering**: Creates a target variable representing the next week's total points.
- **Data Splitting**: Splits the data into training and test sets.
- **Normalization**: Applies MinMax scaling to normalize the feature data.
- **Model Architecture**: Defines a neural network with two hidden layers.
- **Training**: Trains the model using mean squared error loss and the Adam optimiser.

## Usage

To utilise this project, follow these steps:

1. **Run Player Data.ipynb**: Execute this notebook to prepare the data for the current gameweek.
2. **Run Prediction Model.ipynb**: Execute this notebook to train the neural network and make predictions for the next gameweek.
3. **Repeat After Each Gameweek**: After each gameweek, re-run the scripts to update the data and predictions.

## Dependencies

- Python 3.x
- Pandas
- NumPy
- TensorFlow
- scikit-learn

## Features by Position

The "Features by Position" section outlines the specific attributes and statistics that are used to model the performance of players in various positions within the English Premier League (EPL). These features encompass a range of performance metrics, including scoring, assists, defensive contributions, playtime, and more. By categorizing these features according to the player's position (Goalkeepers, Defenders, Midfielders, Forwards), the model can better understand the unique roles and responsibilities of players on the field. This detailed breakdown allows for more precise predictions and insights into the factors that contribute to a player's fantasy league performance.

### Goalkeepers (GK)

- Name
- Element
- Gameweek (GW)
- Bonus
- Assists
- Clean Sheets
- Goals Conceded
- Minutes
- Own Goals
- Penalties Saved
- Saves
- Yellow Cards
- Value
- Total Points
- Mean Reversion

### Defenders (DEF)

- Name
- Element
- Gameweek (GW)
- Bonus
- Assists
- Clean Sheets
- Goals Conceded
- Goals Scored
- Minutes
- Own Goals
- Yellow Cards
- Red Cards
- Value
- Total Points
- Mean Reversion

### Midfielders (MID)

- Name
- Element
- Gameweek (GW)
- Bonus
- Assists
- Clean Sheets
- Goals Conceded
- Goals Scored
- Minutes
- Own Goals
- Yellow Cards
- Red Cards
- Value
- Total Points
- Mean Reversion

### Forwards (FWD)

- Name
- Element
- Gameweek (GW)
- Bonus
- Assists
- Goals Scored
- Minutes
- Own Goals
- Yellow Cards
- Red Cards
- Value
- Total Points
- Mean Reversion


## Contributions and Support

This project has been developed with the intention of providing insights into EPL fantasy football performance. Contributions, bug reports, and enhancement suggestions are welcome. Please open an issue or submit a pull request on GitHub.
