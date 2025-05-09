import argparse
from parser import load_players
from optimizer import optimize_team

def parse_formation(formation: str) -> dict:
    """
    Convert formation string like '4-3-3' into position requirement dict.
    Assumes 1 GK by default.
    """
    parts = formation.strip().split('-')
    if len(parts) != 3:
        raise ValueError("Formation must be in the format DEF-MID-FWD (e.g., 4-3-3)")

    def_num, mid_num, fwd_num = map(int, parts)
    return {'GK': 1, 'DEF': def_num, 'MID': mid_num, 'FWD': fwd_num}

def main():
    parser = argparse.ArgumentParser("DraftGenius: Formation-Based Fantasy Draft Assistant")
    parser.add_argument('--budget', type=float, required=True, help="Total salary cap")
    parser.add_argument('--formation', type=str, required=True, help="Formation (e.g., 4-3-3)")
    parser.add_argument('--max', type=int, default=3, help="Max players per real-world team (default: 3)")
    args = parser.parse_args()

    try:
        position_needs = parse_formation(args.formation)
    except ValueError as e:
        print(f"Error: {e}")
        return

    players = load_players()
    team = optimize_team(players, args.budget, position_needs, args.max)

    print("\nRecommended Squad:")
    for p in team.players:
        print(" -", p)
    print(f"\nTotal Cost: {team.total_cost():.2f}, Total Value: {team.total_value():.2f}")

if __name__ == "__main__":
    main()