class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name is self.player1_name:
            self.player1_score +=  1
        else:
            self.player2_score +=  1

    def get_draw(self, score):
        if score == 0: 
            return "Love-All"
        if score == 1: 
            return "Fifteen-All"
        if score == 2:
            return "Thirty-All"
        else: 
            return "Deuce"
    
    def get_tiebreak(self, player1_score, player2_score):
        if player1_score == player2_score +1:
            return "Advantage player1"
        elif player1_score >= player2_score +2:
            return "Win for player1"
        elif player2_score == player1_score +1:
            return "Advantage player2"
        elif player2_score >= player1_score +2:
            return "Win for player2"
            

    def get_score(self):

        scores = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty", 
            3: "Forty"
            }
        

        if self.player1_score  == self.player2_score:
            return self.get_draw(self.player1_score)
        if self.player1_score >= 4 or self.player2_score >= 4:
            return self.get_tiebreak(self.player1_score, self.player2_score)
        else:
            return scores[self.player1_score] + "-" + scores[self.player2_score] 
