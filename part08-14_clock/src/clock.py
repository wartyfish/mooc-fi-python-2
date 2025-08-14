from datetime import timedelta

class Clock:
    def __init__(self, hr: int, min: int, sec: int):
        self.seconds = sec
        self.minutes = min
        self.hours = hr

        self.time = timedelta(hours = self.hours, minutes=self.minutes, seconds=self.seconds)

    def __str__(self):
        total_seconds = int(self.time.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        hours = hours % 24
        min, sec = divmod(remainder, 60)
        return f"{hours:02}:{min:02}:{sec:02}"
    
    def tick(self):
        self.time += timedelta(seconds=1)

    def set(self, hr: int, min: int):
        self.seconds = 0
        self.minutes = min
        self.hours = hr

        self.time = timedelta(hours = self.hours, minutes=self.minutes, seconds=self.seconds)

    
if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)