import csv
from models import Player

def load_players(path: str = 'players.csv') -> list:
    """
    Always loads the fixed Premier League roster from 'players.csv'.
    CSV columns: name, team, value, cost.
    """
    players = []
    with open(path, newline='') as f:
        """Opens the CSV file to separate the columns into variables
        in our program."""
        reader = csv.DictReader(f)
        for row in reader:
            players.append(Player(
                name=row['name'],
                team=row['team'],
                value=float(row['value']),
                cost=float(row['cost'])
            ))
    return players
