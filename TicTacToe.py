class TicTacToe():

    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.possible_moves = [(a,b) for a in range(3) for b in range(3)]
        self.turn = 'X'

    def make_move(self, move):
        self.possible_moves.remove(move)
        'O' if self.turn == 'X' else self.turn == 'X'
    
    def game_over(self) -> bool:
        True if self.possible_moves == [] else False
    
if __name__ == "__main__":
    game = TicTacToe()
    while (not game.game_over()):
        move = input("What move are you going to make?")
        game.make_move(move)