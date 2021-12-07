class Board:
    
    def __init__(self) -> None:
        self.field = []
        self.removed = False

    def getSum(self):
        sum_false = 0
        for line in self.field:
            for part in line:
                if not part[1]:
                    sum_false += part[0]

        return sum_false

    def setNumber(self, number):
        for line in self.field:
            for part in line:
                if part[0] == number:
                    part[1] = True

    def _checkHorizontal(self, field):
        for line in field:
            count = 0
            for part in line:
                if part[1]:
                    count += 1
            if count == 5:
                return True
        return False

    def checkForBingo(self):
        return self._checkHorizontal(self.field) or self._checkHorizontal(list(zip(*self.field)))


with open("input.txt", "r") as f:
    lines = f.readlines()
    bingo_numbers = []
    boards = []
    for number in lines[0].split(","):
        bingo_numbers.append(int(number))
    
    for i, n in enumerate(lines[2:]):
        if i % 6 == 0:
            boards.append(Board())
        n = n.replace("\n", "")
        n = n.replace("  ", " ")
        if n == "":
            continue
        if n[0] == " ":
            n = n[1:]
        boards[-1].field.append(list(map(lambda e: [int(e), False], n.split(" "))))
    winner = None
    for number in bingo_numbers:
        for board in boards:
            board.setNumber(number)
            if board.checkForBingo():
                board.removed = True
        last_board = boards[0]
        boards = list(filter(lambda e: not e.removed, boards))
        if len(boards) == 0:
            print(last_board.getSum() * number)
            break
    