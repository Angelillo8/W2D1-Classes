
class Team:
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player):
        if player in self.players:
            return True
        else:
            return False
        # return player in self.players
        # return self.players.count(player) > 0
    
    def play_game(self, has_won):
        if has_won == True:
            self.points += 3
        elif has_won == False:
            self.points += 0
        # if game_won:
        #     self.points += 3
