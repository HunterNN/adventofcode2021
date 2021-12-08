from rich.progress import track

def compressFish(container):
    tmp_container = []
    container.sort(key=lambda e: e.timer)
    last_timer = -1
    for fish in container:
        if fish.timer == last_timer:
            tmp_container[-1].weight += fish.weight
        else:
            last_timer = fish.timer
            tmp_container.append(Fish(last_timer, 0))
            tmp_container[-1].weight += fish.weight
    return tmp_container

class Fish:
    def __init__(self, timer, weight) -> None:
        self.timer = timer
        self.weight = weight

    def passDay(self, container):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            container.append(Fish(8, self.weight))

with open("input.txt", "r") as f:
    container = []
    line = f.readlines()
    numbers = list(map(lambda e: int(e), line[0].split(",")))
    numbers.sort()
    for number in numbers:
        container.append(Fish(number, 1))
    container = compressFish(container)
    for i in track(range(256)):
        tmp_container = container.copy()
        for fish in tmp_container:
            fish.passDay(container)
        container = compressFish(container)
    sum = 0
    for fish in container:
        sum += fish.weight
    print(sum)