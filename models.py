class Player:
    def __init__(self, name: str, team: str, value: float, cost: float):
        """The 'player' class, it contains values relating to the player's name,
        team, value, and cost."""
        self.name = name
        self.team = team
        self.value = value
        self.cost = cost

    def __repr__(self):
        """Returns a string representation of the player class."""
        return f"{self.name} ({self.team}) - Val: {self.value}, Cost: {self.cost}"


class Team:
    def __init__(self):
        """The 'team' class, initialized thru a players list."""
        self.players = []

    def add_player(self, player: Player):
        """This method adds a player thru an instance of the player class to
        the players list."""
        self.players.append(player)

    def total_cost(self) -> float:
        """This method returns the total cost of every player in the players list."""
        return sum(p.cost for p in self.players)

    def total_value(self) -> float:
        """This method returns the total value of every player in the players list."""
        return sum(p.value for p in self.players)
