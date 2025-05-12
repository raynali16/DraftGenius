from models import Team

def optimize_team(players: list, budget: float, position_needs: dict, max_per_team: int = 3) -> Team:
    """
    Picks a team matching exact positional needs (e.g., 4 DEF, 3 MID, 3 FWD, 1 GK),
    respecting budget and team limit constraints.
    """
    sorted_players = sorted(players, key=lambda p: p.value / p.cost, reverse=True)
    team = Team()
    count_by_position = {pos: 0 for pos in position_needs}
    count_by_team = {}

    for p in sorted_players:
        if team.total_cost() + p.cost > budget:
            continue
        if count_by_position.get(p.position, 0) >= position_needs.get(p.position, 0):
            continue
        if count_by_team.get(p.team, 0) >= max_per_team:
            continue

        team.add_player(p)
        count_by_position[p.position] += 1
        count_by_team[p.team] = count_by_team.get(p.team, 0) + 1

        if all(count_by_position[pos] == position_needs[pos] for pos in position_needs):
            break

    return team