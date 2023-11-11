class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.games = dict['games']
        self.goals = dict['goals']
    
    def __str__(self):
        return f"{self.name} team {self.team} games {self.games} goals {self.goals}"
