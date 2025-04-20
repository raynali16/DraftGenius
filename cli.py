import argparse
from parser import load_players
from optimizer import greedy_team

def main():
    """This function returns the best possible combination for the squad based on the budget."""
    p = argparse.ArgumentParser("DraftGenius: Premier League Draft Assistant")
    p.add_argument('--budget', type=float, required=True, help="Total salary cap for your 11‑player squad")
    p.add_argument('--size',  type=int, default=11, help="Squad size (default: 11)")
    p.add_argument('--max',   type=int, default=3, help="Max players per real‑world team (default: 3)")
    args = p.parse_args()

    players = load_players()  # always reads 'players.csv'
    team = greedy_team(players, args.budget, args.size, args.max)

    print("\nRecommended Squad:")
    for pl in team.players:
        """This for loop returns the best possible squad combination for the user."""
        print(" -", pl)
        print(f"\nTotal Cost: {team.total_cost():.2f}, Total Value: {team.total_value():.2f}")

if __name__ == "__main__":
    """The main function."""
    main()
