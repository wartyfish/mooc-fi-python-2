from datetime import timedelta

class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

        self.time = timedelta(minutes=self.minutes, seconds=self.seconds)

    def __str__(self):
        total_seconds = int(self.time.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        min, sec = divmod(remainder, 60)
        return f"{min:02}:{sec:02}"
    
    def tick(self):
        self.time += timedelta(seconds=1)

    
if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()