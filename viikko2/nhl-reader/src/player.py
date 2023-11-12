class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.games = dict['games']
        self.goals = dict['goals']
        self.assists = dict['assists']
    def points(self):
        return self.goals + self.assists
        

    def __str__(self):
        return f"{self.name:20} {self.team:4} {self.games:3} {self.goals:2} + {self.assists:2} {self.assists+self.goals:4}"
