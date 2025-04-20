from models import Team

def greedy_team(players: list,
                budget: float,
                team_size: int = 11,
                max_per_team: int = 3) -> Team:
    """
    Builds an 11‑player squad (default) under `budget`,
    never picking more than 3 from any one Premier‑League team.
    """
    sorted_players = sorted(players, key=lambda p: p.value/p.cost, reverse=True)
    squad = Team()
    count_by_team = {}

    for p in sorted_players:
        """A for loop which is our main function, building an 11-player squad un
        -der budget, and keeping the 3-per-team rule."""
        if len(squad.players) >= team_size:
            break
        if squad.total_cost() + p.cost > budget:
            continue
        if count_by_team.get(p.team, 0) >= max_per_team:
            continue

        squad.add_player(p)
        count_by_team[p.team] = count_by_team.get(p.team, 0) + 1

    return squad
