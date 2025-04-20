class Player:
    def __init__(self, name: str, team: str, value: float, cost: float):
        self.name = name
        self.team = team
        self.value = value
        self.cost = cost

    def __repr__(self):
        return f"{self.name} ({self.team}) - Val: {self.value}, Cost: {self.cost}"


class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player: Player):
        self.players.append(player)

    def total_cost(self) -> float:
        return sum(p.cost for p in self.players)

    def total_value(self) -> float:
        return sum(p.value for p in self.players)
