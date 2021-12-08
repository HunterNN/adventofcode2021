class Fish:
    def __init__(self, timer) -> None:
        self.timer = timer

    def passDay(self, container):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            container.append(Fish(8))

with open("input.txt", "r") as f:
    container = []
    line = f.readlines()
    numbers = list(map(lambda e: int(e), line[0].split(",")))
    for number in numbers:
        container.append(Fish(number))
    for i in range(80):
        tmp_container = container.copy()
        for fish in tmp_container:
            fish.passDay(container)
    print(len(container))