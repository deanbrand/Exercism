class Clock:
    def __init__(self, hour, minute):
        self.hour = (hour + minute // 60) % 24
        self.minute = minute % 60

    def __repr__(self):
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self):
        return f'{self.hour:02}:{self.minute:02}'

    def __eq__(self, other):
        return self.minute == other.minute and self.hour == other.hour

    def __add__(self, minutes):
        self.minute += minutes
        self.hour += self.minute // 60
        self.hour = self.hour % 24
        self.minute = self.minute % 60
        return self

    def __sub__(self, minutes):
        self.minute -= minutes
        self.hour += self.minute // 60
        self.hour = self.hour % 24
        self.minute = self.minute % 60
        return self
