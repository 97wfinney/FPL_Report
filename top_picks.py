import pandas as pd

def extract_consistent_players_from_csv():
    # Prompt user for the gameweek
    gw = input("Please enter the gameweek you want to analyze: ")

    # Load the CSV
    file_path = f"Gameweek_{gw}_predictions.csv"
    predictions = pd.read_csv(file_path)

    # Consider only the first 60 rows
    subset = predictions.head(60)

    # Find players that appear three times
    consistent_players = subset['Name'].value_counts()
    consistent_players = consistent_players[consistent_players == 3]

    print("\nConsistent players across all runs:")
    for player in consistent_players.index:
        print(player)

if __name__ == "__main__":
    extract_consistent_players_from_csv()
