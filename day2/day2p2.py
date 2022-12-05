class PSR:
    """
    Defined by A = ROCK, B = PAPER, C = SCISSORS
    X = LOSE, Y = TIE, Z = WIN
    """
    win = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }

    tie = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }

    points = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    def __init__(self, opponent, outcome) -> None:
        self.opponent = opponent
        self.outcome = outcome
        if self.outcome == 
        self.won = self.win[opponent] == you
        self.tie = self.tie[opponent] == you
        self.score = self.points[you] + (6 if self.won else 3 if self.tie else 0)
        # print(self.won, self.tie, self.score)

def solveP1():
    score = 0
    with open('input.txt') as f:
        for line in f:
            input_split = line.strip('\n').split(' ')
            print(input_split)
            score += PSR(input_split[0], input_split[1]).score
    return score

print(solveP1())
